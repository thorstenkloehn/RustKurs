import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch16_1_intro": (
        "Willkommen zum sechzehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion besprechen wir, "
        "wie du die besten KI-Werkzeuge von Google nutzt, um effizienter Programmieren zu lernen und Code zu schreiben. "
        "Künstliche Intelligenz kann wie ein persönlicher Mentor wirken, der dir Konzepte erklärt, Fehler im Code findet "
        "und dir hilft, schneller Fortschritte zu machen. Google bietet hierfür verschiedene maßgeschneiderte Lösungen an."
    ),
    "ch16_2_antigravity": (
        "Zuerst betrachten wir Google Antigravity – das agentische Assistenzsystem. Wie du bereits aus Kapitel 14 weißt, "
        "ist Antigravity weit mehr als ein einfacher Chatbot. Es basiert auf dem Modell Antigravity 2.0, das speziell "
        "auf logisches Denken und die Nutzung von Werkzeugen optimiert ist. Mit dem Antigravity CLI, aufrufbar über den Befehl agy, "
        "kann die KI selbstständig in einer sicheren Sandbox Dateien bearbeiten und Befehle ausführen. Zusätzlich sorgt die Antigravity IDE "
        "für eine nahtlose Integration direkt in deinem Editor."
    ),
    "ch16_3_gemini_code_assist": (
        "Als nächstes haben wir Gemini Code Assist. Das ist Googles offizielle Erweiterung für Entwicklungsumgebungen wie "
        "VS Code und die JetBrains-IDEs. Gemini Code Assist unterstützt dich direkt beim Tippen mit Auto-Vervollständigung und einem integrierten Chat. "
        "Für Einsteiger ist die Version für Einzelpersonen besonders attraktiv, da sie komplett kostenlos verfügbar ist. Für Teams gibt es "
        "die Standard-Version, und für große Konzerne die Enterprise-Version, die sich an den eigenen Code des Unternehmens anpassen lässt."
    ),
    "ch16_4_ai_studio": (
        "Für Experimente und Prototypen gibt es das Google AI Studio. Diese Plattform ist genial, wenn du direkt mit den Gemini-Modellen "
        "arbeiten möchtest. Ein riesiger Vorteil ist das gigantische Kontextfenster von bis zu zwei Millionen Token. Damit kannst du "
        "die Dokumentation einer kompletten Bibliothek oder deine gesamte Codebasis auf einmal hochladen. Außerdem kannst du hier "
        "kostenlos API-Schlüssel erstellen, um Gemini in deine eigenen Programme einzubinden."
    ),
    "ch16_5_practical": (
        "Wie bedienst du Gemini Code Assist für Einzelpersonen in der Praxis? Mit der Tastenkombination Steuerung und I öffnest du "
        "das Inline-Chatfenster, um neuen Code an der Cursorposition zu generieren oder markierte Fehler korrigieren zu lassen. "
        "Vorschläge der automatischen Code-Vervollständigung kannst du einfach mit der Tab-Taste annehmen. Im Chat stehen dir zudem "
        "Befehle wie slash generate für neue Strukturen und slash fix zur gezielten Fehlerbehebung bereit."
    ),
    "ch16_6_best_practices": (
        "Wie holst du als Anfänger das Beste aus diesen Tools heraus? Erstens: Lass dir Code immer erklären, anstatt ihn nur stumpf "
        "zu kopieren. Frage die KI nach einer Zeile-für-Zeile-Erklärung. Zweitens: Nutze die KI als Sparringspartner bei Compiler-Fehlern. "
        "Kopiere die Fehlermeldungen direkt in den Chat. Und drittens: Formuliere deine Prompts so präzise wie möglich, um exakte und "
        "lehrreiche Antworten zu erhalten."
    ),
    "ch16_7_outro": (
        "Zusammenfassend: Antigravity ist dein mächtiger, autonomer Helfer im Terminal. Gemini Code Assist begleitet dich direkt "
        "im Editor, und das Google AI Studio ist perfekt für tiefergehende Experimente und API-Projekte. Probiere diese Tools aus, "
        "um dein Lernen zu beschleunigen. Vielen Dank fürs Zuschauen, viel Erfolg beim Programmieren und bis zum nächsten Mal!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.05, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        # Calculate duration in seconds
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations_ch16.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch16.json")

if __name__ == "__main__":
    main()
