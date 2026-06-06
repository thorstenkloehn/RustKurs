import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch2_intro": (
        "Willkommen zum zweiten Kapitel unseres Rust-Kurses für Anfänger. In diesem Kapitel bereiten "
        "wir dein System vor und installieren alle Werkzeuge, die du für die Softwareentwicklung mit "
        "Rust brauchst. Wir konzentrieren uns dabei Schritt für Schritt auf das Betriebssystem Ubuntu Linux. "
        "Lass uns direkt mit den Voraussetzungen starten."
    ),
    "ch2_build_essential": (
        "Als Erstes installieren wir das Paket build-essential. Doch was ist das genau? Rust ist "
        "zwar eine eigenständige Programmiersprache, benötigt jedoch für das finale Linken und Übersetzen "
        "von Programmen die standardmäßigen C-Bibliotheken sowie einen C-Linker. Das Paket build-essential "
        "bündelt diese wichtigen Compiler-Werkzeuge wie den G-C-C Compiler und das Tool Make. Du kannst "
        "es ganz einfach in deinem Ubuntu-Terminal installieren. Führe dazu den Befehl sudo apt update "
        "aus, gefolgt von sudo apt install build-essential."
    ),
    "ch2_vscode": (
        "Als Editor nutzen wir Visual Studio Code, eine leistungsstarke und erweiterbare Entwicklungsumgebung. "
        "Auf Ubuntu kannst du VS Code ganz einfach über das Terminal mit dem Snap-Befehl "
        "sudo snap install --classic code installieren. Um das Schreiben von Rust-Code extrem komfortabel "
        "zu machen, installieren wir darin die offizielle Erweiterung namens rust-analyzer. Sie fungiert als "
        "Sprachserver und bietet dir intelligente Code-Vervollständigung, Syntaxhervorhebung, Formatierung "
        "und sofortige Fehlermeldungen direkt beim Tippen."
    ),
    "ch2_rustup": (
        "Jetzt installieren wir Rust selbst! Der offizielle und empfohlene Weg unter Linux ist rustup. "
        "rustup ist das Tool zur Verwaltung der Rust-Versionen. Es lädt den Compiler rustc, den Paketmanager "
        "Cargo und alle wichtigen Hilfswerkzeuge herunter und hält sie aktuell. Kopiere dazu einfach den "
        "offiziellen Installations-Befehl von der Website rustup.rs in dein Terminal und drücke Enter. "
        "Folge danach den Standard-Anweisungen auf dem Bildschirm. Starte anschließend dein Terminal neu und "
        "überprüfe die Installation mit dem Befehl rustc --version. Herzlichen Glückwunsch, dein System ist "
        "jetzt komplett bereit!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.0, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        # Calculate duration in seconds
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations_ch2.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch2.json")

if __name__ == "__main__":
    main()
