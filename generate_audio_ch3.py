import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch3_intro": (
        "Willkommen zum dritten Kapitel unseres Kurses. In diesem Kapitel werfen wir einen Blick auf moderne "
        "KI-Assistenten, wie sie im Entwicklungsalltag genutzt werden und wie sie funktionieren. KI-Assistenten "
        "nutzen Tools, erledigen Aufgaben und können sogar im Internet nach weiteren Informationen suchen, um "
        "uns bei der Arbeit zu unterstützen. Lass uns direkt anschauen, wie diese Tools funktionieren."
    ),
    "ch3_tools": (
        "Es gibt verschiedene bekannte KI-Assistenten für Entwickler. Cline ist ein KI-Assistent, der Entwicklern "
        "hilft, Code schneller zu schreiben und zu verstehen. Gemini Code Assist ist ein KI-gestütztes Tool von "
        "Google, das uns bei der Code-Vervollständigung, der Fehlererkennung und beim Refactoring unterstützt. "
        "Und GitHub Copilot ist ein KI-Paarprogrammierer, der passenden Code direkt basierend auf Kommentaren "
        "und dem umgebenden Code vorschlägt."
    ),
    "ch3_favorites": (
        "Das sind meine persönlichen Favoriten: GitHub Copilot und Gemini Code Assist. Beide lassen sich "
        "nahtlos in moderne Editoren wie Visual Studio Code integrieren und steigern die Produktivität enorm."
    ),
    "ch3_learning": (
        "Aber warum sollte man eigentlich nicht alles von KI-Agenten erledigen lassen? Die Antwort ist simpel: "
        "Man lernt selbst nichts dabei. Wenn die künstliche Intelligenz jeden Code für dich schreibt, verstehst "
        "du die zugrunde liegenden Konzepte nicht und kannst bei Fehlern nicht selbstständig eingreifen. Nutze "
        "KI-Assistenten also als Unterstützung, aber lerne das Programmieren selbst!"
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
        
    with open("audio/durations_ch3.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch3.json")

if __name__ == "__main__":
    main()
