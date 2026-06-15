import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch26_1_intro": (
        "Willkommen zum sechsundzwanzigsten Kapitel unseres Rust-Videokurses. Heute beschäftigen wir uns mit KI-Agenten "
        "und autonomen Software-Ingenieuren. Sie lernen, wie diese intelligenten Systeme arbeiten und wie Sie sie in Ihrem "
        "Entwicklungsalltag einsetzen können."
    ),
    "ch26_2_definition": (
        "Ein KI-Agent ist ein System, das selbstständig planen, Werkzeuge nutzen und auf Umgebungs-Feedback reagieren kann. "
        "Im Vergleich zu einfachen Chatbots agieren sie wie ein Autopilot, der nicht nur Ratschläge gibt, sondern das Steuer selbst übernimmt."
    ),
    "ch26_3_problem": (
        "Das Problem klassischer Chatbots ist der fehlende Repository-Kontext und die fehlende Verbindung zum Terminal. "
        "Manuelles Kopieren von Code führt zu ständigen Reibungsverlusten und leicht vermeidbaren Fehlern."
    ),
    "ch26_4_naive": (
        "In unserem naiven Versuch kopieren wir eine Funktion zum Schreiben in eine Datei aus einem einfachen Chatbot. "
        "Wir fügen sie in unser Projekt ein, doch beim Kompilieren scheitert das Programm."
    ),
    "ch26_5_anatomy": (
        "Die Anatomie des Fehlers zeigt uns den Compilerfehler E0599. Der Compiler meldet, dass die Methode write_all für "
        "File nicht gefunden wurde, da der benötigte Trait std::io::Write nicht im aktuellen Scope importiert ist."
    ),
    "ch26_6_solution": (
        "Die Lösung besteht darin, den Trait korrekt zu importieren. Ein KI-Agent löst diesen Fehler automatisch: Er schreibt "
        "den Code, führt cargo check aus, fängt die Fehlermeldung ab, fügt den Import hinzu und verifiziert die Lösung selbstständig."
    ),
    "ch26_7_tutorial": (
        "In unserem Praxistutorial nutzen wir einen CLI-Agenten im Terminal. Wir weisen ihn an, eine Funktion zum Lesen "
        "der letzten Zeile einer Datei zu implementieren und diese per Unit-Test abzusichern."
    ),
    "ch26_8_security": (
        "Sicherheitsaspekte sind bei lokalen Agenten kritisch. Da sie Shell-Befehle ausführen können, sollten Sie sie in "
        "Docker-Containern oder virtuellen Maschinen ausführen, manuelle Bestätigungen fordern und ein sauberes Git-Repository "
        "als Sicherheitsnetz pflegen."
    ),
    "ch26_9_outro": (
        "Zusammenfassend verändern autonome Agenten die Art, wie wir Software entwickeln, grundlegend. Sie nutzen den "
        "Rust-Compiler als Mentor für fehlerfreien Code. Probieren Sie die praktischen Übungen aus! Vielen Dank fürs Zuschauen."
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
    
    with open("audio/durations_ch26.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch26.json")

if __name__ == "__main__":
    main()
