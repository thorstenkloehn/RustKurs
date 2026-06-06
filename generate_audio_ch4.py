import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf
from pydub import AudioSegment

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

# Concised texts to avoid overlapping and fit the video timeline perfectly
segments = {
    "ch4_1_intro": (
        "Willkommen zu Kapitel vier. Hier erstellen wir unser erstes Rust-Projekt. Im Ubuntu-Terminal nutzen "
        "wir das Tool Cargo, den offiziellen Paketmanager. Mit dem Befehl cargo new hallowelt legen wir ein "
        "neues Verzeichnis mit allen benötigten Projektdateien an."
    ),
    "ch4_2_code": (
        "Um den Quellcode zu bearbeiten, öffnen wir das Verzeichnis anschließend in Visual Studio Code mit "
        "dem Befehl code hallowelt."
    ),
    "ch4_3_vscode": (
        "Visual Studio Code öffnet sich nun. Auf der linken Seite im Explorer sehen wir die Struktur "
        "unseres Rust-Projekts. Neben der Konfigurationsdatei Cargo.toml finden wir den Quellcode-Ordner "
        "src, in dem sich unsere Programme befinden."
    ),
    "ch4_4_edit": (
        "Wir öffnen die Quellcodedatei main.rs im src-Ordner. Standardmäßig hat Cargo hier bereits "
        "ein einfaches Hallo-Welt-Programm in englischer Sprache generiert. Wir ändern den Text "
        "in Hallo Welt ab, um unser Programm zu personalisieren, und speichern die Datei."
    ),
    "ch4_5_run": (
        "Um das Programm auszuführen, klicken wir auf die kleine Run-Schaltfläche direkt über der "
        "Hauptfunktion. Visual Studio Code öffnet daraufhin am unteren Bildschirmrand ein Terminal "
        "und startet den Compiler."
    ),
    "ch4_6_outro": (
        "Der Compiler übersetzt unseren Code in kürzester Zeit und führt das Programm aus. "
        "Im Terminal sehen wir die Ausgabe Hallo Welt. Herzlichen Glückwunsch, du hast dein erstes "
        "Rust-Programm erfolgreich gestartet! Im nächsten Kapitel beschäftigen wir uns mit Variablen."
    )
}

# The target timestamps where each segment should start in milliseconds
start_times_ms = {
    "ch4_1_intro": 1000,     # Starts at 1s. Length ~13-14s. Ends at 14-15s.
    "ch4_2_code": 16500,     # Starts at 16.5s. Length ~6-7s. Ends at 23.5s.
    "ch4_3_vscode": 30000,   # Starts at 30s. Length ~11s. Ends at 41s.
    "ch4_4_edit": 46000,     # Starts at 46s. Length ~13s. Ends at 59s.
    "ch4_5_run": 67000,      # Starts at 67s. Length ~10s. Ends at 77s.
    "ch4_6_outro": 82000     # Starts at 82s. Length ~13s. Ends at 95s.
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    # 1. Generate individual WAV files with speed=1.05 to sound modern and fit timings
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.05, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations_ch4.json", "w") as f:
        json.dump(durations, f, indent=4)
        
    # 2. Assemble them using pydub
    print("\nAssembling full audio track...")
    video_duration_ms = 103381 # 103.38 seconds
    full_audio = AudioSegment.silent(duration=video_duration_ms, frame_rate=48000)
    
    for name in segments.keys():
        wav_path = f"audio/{name}.wav"
        segment_audio = AudioSegment.from_wav(wav_path)
        start_ms = start_times_ms[name]
        
        print(f"Overlaying {name} at {start_ms/1000:.2f}s...")
        full_audio = full_audio.overlay(segment_audio, position=start_ms)
        
    # Export final audio track
    output_audio_path = "audio/ch4_voiceover.wav"
    full_audio.export(output_audio_path, format="wav")
    print(f"Saved completed audio track to {output_audio_path}")

if __name__ == "__main__":
    main()
