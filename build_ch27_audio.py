import json
import os
import subprocess

def main():
    # Load durations
    durations_path = "audio/durations_ch27.json"
    if not os.path.exists(durations_path):
        print(f"Error: {durations_path} not found! Run generate_audio_ch27.py first.")
        return

    with open(durations_path, "r") as f:
        durations = json.load(f)

    keys = [
        "ch27_1_intro",
        "ch27_2_definition",
        "ch27_3_problem",
        "ch27_4_naive",
        "ch27_5_anatomy",
        "ch27_6_solution",
        "ch27_7_tutorial",
        "ch27_8_deepdive",
        "ch27_9_exercises",
        "ch27_10_learning",
        "ch27_11_outro"
    ]

    total_audio = sum(durations.values())
    gap_duration = 1.5
    print(f"Total audio duration: {total_audio:.4f}s")
    print(f"Gap between sections: {gap_duration:.4f}s")

    # Calculate start times (in milliseconds)
    start_times = []
    current_time = 0.0

    for key in keys:
        start_times.append(int(current_time * 1000))
        current_time += durations[key] + gap_duration

    # Build ffmpeg command to mix audios with delays
    inputs = []
    delays = []
    for i, key in enumerate(keys):
        inputs.append(f"-i audio/{key}.wav")
        delays.append(f"[{i}:a]adelay={start_times[i]}|{start_times[i]}[a{i}]")

    filter_complex = ";".join(delays)
    mix_inputs = "".join(f"[a{i}]" for i in range(len(keys)))
    filter_complex += f";{mix_inputs}amix=inputs={len(keys)}:duration=longest:dropout_transition=0[a]"

    ffmpeg_cmd = (
        f"ffmpeg -y "
        + " ".join(inputs)
        + f' -filter_complex "{filter_complex}" -map "[a]" -c:a pcm_s16le audio/ch27_full_voiceover.wav'
    )

    print("Generating full synchronized voiceover track...")
    subprocess.run(ffmpeg_cmd, shell=True, check=True)

    # Resolve video path (support both 720p30 and 1080p60)
    video_paths = [
        "media/videos/video_scene_ch27/720p30/RustStructsVideo.mp4",
        "media/videos/video_scene_ch27/1080p60/RustStructsVideo.mp4"
    ]
    
    video_path = None
    for vp in video_paths:
        if os.path.exists(vp):
            video_path = vp
            break
            
    if not video_path:
        # Check in whole media directory to be extremely robust
        found = False
        for root, dirs, files in os.walk("media"):
            if "RustStructsVideo.mp4" in files:
                video_path = os.path.join(root, "RustAgentsVideo.mp4") # Wait, actually RustStructsVideo.mp4
                video_path = os.path.join(root, "RustStructsVideo.mp4")
                found = True
                break
        if not found:
            print("Error: RustStructsVideo.mp4 not found in media/ directory! Render the Manim scene first.")
            return

    print(f"Found video at: {video_path}")
    
    # Merge the synchronized audio track with the video track
    # and apply EBU R128 (-14 LUFS) loudness normalization
    merge_cmd = (
        f'ffmpeg -y -i {video_path} '
        '-i audio/ch27_full_voiceover.wav -map 0:v -map 1:a '
        '-filter:a "loudnorm=I=-14:TP=-1.0:LRA=11" -c:v copy -c:a aac -shortest 27.mp4'
    )
    print("Merging video and normalized audio stream...")
    subprocess.run(merge_cmd, shell=True, check=True)
    print("Success! Final video is saved as 27.mp4")

if __name__ == "__main__":
    main()
