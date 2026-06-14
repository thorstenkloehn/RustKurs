import json
import os
import subprocess

def main():
    # Load durations
    with open("audio/durations_ch20.json", "r") as f:
        durations = json.load(f)

    keys = [
        "ch20_1_intro",
        "ch20_2_references_concept",
        "ch20_3_immutable_borrowing",
        "ch20_4_mutable_borrowing",
        "ch20_5_data_races",
        "ch20_6_mixing_borrows",
        "ch20_7_dangling_references",
        "ch20_8_conclusion_rules"
    ]

    total_audio = sum(durations.values())
    padding_per_section = (300.0 - total_audio) / 8.0
    print(f"Total audio duration: {total_audio:.4f}s")
    print(f"Padding per section: {padding_per_section:.4f}s")

    # Calculate start times (in milliseconds)
    start_times = []
    current_time = 0.0

    for key in keys:
        start_times.append(int(current_time * 1000))
        current_time += durations[key] + padding_per_section

    # Build ffmpeg command to mix audios with delays
    inputs = []
    delays = []
    for i, key in enumerate(keys):
        inputs.append(f"-i audio/{key}.wav")
        # adelay filter requires delays for all channels (stereo: delay|delay)
        delays.append(f"[{i}:a]adelay={start_times[i]}|{start_times[i]}[a{i}]")

    filter_complex = ";".join(delays)
    mix_inputs = "".join(f"[a{i}]" for i in range(len(keys)))
    filter_complex += f";{mix_inputs}amix=inputs={len(keys)}:duration=longest:dropout_transition=0[a];[a]apad=whole_dur=300[ap]"

    ffmpeg_cmd = (
        f"ffmpeg -y "
        + " ".join(inputs)
        + f' -filter_complex "{filter_complex}" -map "[ap]" -c:a pcm_s16le audio/ch20_full_voiceover.wav'
    )

    print("Generating full synchronized voiceover track...")
    subprocess.run(ffmpeg_cmd, shell=True, check=True)

    # Now, merge the synchronized audio track with the video track
    # and apply EBU R128 (-14 LUFS) loudness normalization
    merge_cmd = (
        "ffmpeg -y -i media/videos/video_scene_ch20/720p30/RustReferencesVideo.mp4 "
        "-i audio/ch20_full_voiceover.wav -map 0:v -map 1:a "
        '-filter:a "loudnorm=I=-14:TP=-1.0:LRA=11" -c:v copy -c:a aac -shortest 20.mp4'
    )
    print("Merging video and normalized audio stream...")
    subprocess.run(merge_cmd, shell=True, check=True)
    print("Success! Final video with exactly 5 minutes (300.0s) duration is saved as 20.mp4")

if __name__ == "__main__":
    main()
