import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch24_1_intro": (
        "Willkommen zum vierundzwanzigsten Kapitel unseres Rust-Videokurses. Heute besprechen wir die Professionalisierung deines Rust-Projekts und die Nutzung des Antigravity CLI. Eine professionelle Ordnerstruktur hilft dir, den Überblick zu behalten, und legt klare Verhaltensregeln für deine KI-Entwicklungspartner fest."
    ),
    "ch24_2_governance": (
        "Die Workspace-Governance ruht auf vier Säulen: Die Datei agents.md dokumentiert den aktuellen Projektstatus und die Aufgabenteilung. In skills.md legst du prozedurales Spezialwissen für Tools wie Manim, Blender und Kokoro-onnx fest. So vermeidet die KI Fehler bei komplexen Generierungen."
    ),
    "ch24_3_rules_glossary": (
        "Die Datei .agentrules definiert allgemeine Verhaltensregeln wie Programmierstil, Sprache und präzise Code-Editiermethoden. Im glossary.md wiederum legst du exakte Begriffsdefinitionen für deine Projektdokumentation fest. Das sorgt für maximale Konsistenz und klaren Fokus."
    ),
    "ch24_4_agy_cli": (
        "Das Antigravity CLI, aufgerufen mit agy, ist ein mächtiges, terminalbasiertes KI-Werkzeug. Es arbeitet direkt auf deinen lokalen Dateien, jedoch geschützt in einer sicheren Sandbox. Mit nützlichen Befehlen wie agy inspect kannst du deinen Workspace analysieren und Probleme diagnostizieren."
    ),
    "ch24_5_tui_commands": (
        "Die Benutzeroberfläche des CLI bietet dir praktische Slash-Befehle wie settings zur Konfiguration, permissions zur Prüfung deiner Rechte, clear zum Zurücksetzen des Gedächtnisses und rewind, resume oder fork, um deine Entwicklungsschritte flexibel zu steuern."
    ),
    "ch24_6_feedback_loop": (
        "Ein Highlight ist der interaktive Kommentar- und Feedback-Workflow. Wenn der Agent Codeänderungen vorschlägt, kannst du diese mit Control R prüfen und über Kommentare gezielt anpassen lassen. Der Agent passt die Dateien iterativ an, bis sie perfekt sind."
    ),
    "ch24_7_tutorial_dir": (
        "Lass uns praktisch ein Unterverzeichnis Tutorial anlegen. Mit dem Prompt zur Verzeichniserstellung initialisiert die KI ein neues Cargo-Projekt namens zahlenraten, schreibt ein fehlerfreies, interaktives Zahlenratespiel und legt eine informative README-Datei an."
    ),
    "ch24_8_outro": (
        "Damit hast du die Werkzeuge gelernt, um deine Projekte strukturiert zu skalieren und KI-Agenten sicher und effizient zu führen. Lade das Antigravity CLI herunter, richte deine Governance-Dateien ein und professionalisiere deinen Workflow. Vielen Dank fürs Zuschauen und viel Erfolg!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    speed = 1.12
    
    durations = {}
    for name, text in segments.items():
        print(f"Generating audio for: {name} (speed={speed})...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=speed, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    total_audio = sum(durations.values())
    print(f"Total audio duration: {total_audio:.2f} seconds")
    print(f"With transitions (1s each): {total_audio + 7:.2f} seconds")
    
    with open("audio/durations_ch24.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch24.json")

if __name__ == "__main__":
    main()
