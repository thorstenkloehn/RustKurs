import json
import os
import subprocess

def main():
    # Load durations
    durations_path = "audio/durations_ch22.json"
    if not os.path.exists(durations_path):
        print(f"Error: {durations_path} not found! Run generate_audio_ch22.py first.")
        return

    with open(durations_path, "r") as f:
        durations = json.load(f)

    keys = [
        "ch22_1_intro",
        "ch22_2_workflow",
        "ch22_3_mermaid",
        "ch22_4_pseudocode",
        "ch22_5_example",
        "ch22_6_ai",
        "ch22_7_exercise",
        "ch22_8_outro"
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
        + f' -filter_complex "{filter_complex}" -map "[ap]" -c:a pcm_s16le audio/ch22_full_voiceover.wav'
    )

    print("Generating full synchronized voiceover track...")
    subprocess.run(ffmpeg_cmd, shell=True, check=True)

    # Now, merge the synchronized audio track with the video track
    # and apply EBU R128 (-14 LUFS) loudness normalization
    merge_cmd = (
        "ffmpeg -y -i media/videos/video_scene_ch22/720p30/RustPlanningVideo.mp4 "
        "-i audio/ch22_full_voiceover.wav -map 0:v -map 1:a "
        '-filter:a "loudnorm=I=-14:TP=-1.0:LRA=11" -c:v copy -c:a aac -shortest 22.mp4'
    )
    print("Merging video and normalized audio stream...")
    subprocess.run(merge_cmd, shell=True, check=True)
    print("Success! Final video with exactly 5 minutes (300.0s) duration is saved as 22.mp4")

if __name__ == "__main__":
    main()
