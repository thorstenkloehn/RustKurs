import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch23_1_intro": (
        "Willkommen zum dreiundzwanzigsten Kapitel unseres Rust-Videokurses. Heute besprechen wir, wie du Rust langfristig und ohne Frustration meistern kannst. Die optimale Lernstrategie basiert auf drei Säulen: Active Recall, Spaced Repetition und dem Akzeptieren des Compilers als Mentor. Vermeide die passive Tutorial-Hölle und plane jedes Projekt vorab mit einer planung.md."
    ),
    "ch23_2_strategies": (
        "Zusätzlich helfen dir fortgeschrittene Lernmethoden. Während das Bottom-Up-Lernen ein solides Fundament baut, fokussiert sich das Top-Down-Lernen auf ein konkretes Ziel. Pair Programming im Team, Code-Katas, Refactoring und REPL-basiertes Experimentieren beschleunigen das Verständnis. Teile deine Fortschritte über das Learning-in-Public-Prinzip."
    ),
    "ch23_3_portals": (
        "Interaktive Plattformen bieten dir eine ideale Praxisumgebung. Rustlings führt dich über die Kommandozeile durch über hundert fehlerhafte Code-Dateien. Exercism bietet dir mentorbasierte Code-Reviews und vergleichende Lösungen. Unser eigens erstelltes mdBook dient dir dabei als praktisches, interaktives Nachschlagewerk."
    ),
    "ch23_4_self_hosting": (
        "Für Teams und Bildungseinrichtungen kannst du Programmierplattformen selbst hosten. Das Backend bildet eine Sandbox zur sicheren Code-Ausführung wie Judge0, DMOJ, der Jobe Server, INGInious oder die Piston Engine. Diese führen den Benutzer-Code isoliert in Docker-Containern aus und bewerten ihn automatisch."
    ),
    "ch23_5_editors_moodle": (
        "Das Frontend deines Portals benötigt einen Browser-Editor. Der Monaco Editor bietet die vertraute VS-Code-Oberfläche, während CodeMirror extrem leichtgewichtig und mobiloptimiert ist. In Lernplattformen wie Moodle integrierst du Aufgaben einfach über VPL oder das CodeRunner-Plugin."
    ),
    "ch23_6_aspnet": (
        "Möchtest du eine eigene, maßgeschneiderte Lerninfrastruktur aufbauen, empfiehlt sich ASP.NET Core MVC. Damit lassen sich Nachbauten von Exercism, Open edX oder Moodle-Funktionalitäten realisieren, die durch strikte Authentifizierung und gehärtete Serverumgebungen maximale Ausführungssicherheit bieten."
    ),
    "ch23_7_prompting": (
        "Künstliche Intelligenz kann dein stärkster Lernpartner sein, wenn du sie richtig einsetzt. Nutze gezielte Prompt-Templates: den Erklärungs-Prompt bei komplexen Compilerfehlern, den Review-Prompt zur Verbesserung deiner Code-Idiomatik und den Übungs-Generator für maßgeschneiderte Programmier-Katas."
    ),
    "ch23_8_outro": (
        "Richte dir als Übung eine eigene lernplan.md ein. Definiere deine Ziele, deine tägliche Micro-Learning-Routine und teste die besprochenen KI-Prompts. Vertraue dem Rust-Compiler, sieh Fehler als Lernchancen und bleibe kontinuierlich am Ball. Vielen Dank fürs Zuschauen und viel Erfolg beim Lernen!"
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
    
    with open("audio/durations_ch23.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch23.json")

if __name__ == "__main__":
    main()
