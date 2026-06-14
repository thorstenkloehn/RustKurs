import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch22_1_intro": (
        "Willkommen zum zweiundzwanzigsten Kapitel unseres Rust-Videokurses. Heute widmen wir uns einem Thema, das dich zu einem weitaus produktiveren Entwickler machen wird: dem VS Code Planungs-Workflow. Viele Einsteiger machen den Fehler, sofort mit dem Tippen von Rust-Code zu beginnen, sobald sie eine Aufgabe erhalten. Das ist die sogenannte Code-First-Falle. Rust ist aufgrund seines strengen Compilers und des Borrow Checkers jedoch eine Sprache, die sorgfältige Planung belohnt. Wer plant, trennt die fachliche Problemlösung von der syntaktischen Umsetzung."
    ),
    "ch22_2_workflow": (
        "Unser Planungs-Workflow besteht aus fünf Schritten, die wir in einer einfachen planung.md-Datei direkt in VS Code festhalten. Zuerst analysieren wir die Anforderungen nach dem EVA-Prinzip: Eingabe, Verarbeitung und Ausgabe. Als zweites visualisieren wir die Programmlogik mit einem Flussdiagramm. Im dritten Schritt formulieren wir präzisen, sprachneutralen Pseudocode. Viertens erstellen wir eine detaillierte To-Do-Checkliste mit kleinen Schritten. Erst im fünften Schritt schreiben wir den echten Rust-Code und refaktorieren ihn anschließend."
    ),
    "ch22_3_mermaid": (
        "Für die visuelle Darstellung unserer Algorithmen nutzen wir Mermaid. Mermaid ist ein Tool, mit dem man Diagramme direkt als Text in Markdown definieren kann. Das macht sie leicht editierbar und versionierbar. Für unsere Flussdiagramme nutzen wir abgerundete Rechtecke für den Start und das Ende, klassische Rechtecke für Berechnungen oder Zuweisungen, Rauten für logische Bedingungen sowie Parallelogramme für die Interaktion mit der Außenwelt. Die logischen Wege verbinden wir mit Pfeilen."
    ),
    "ch22_4_pseudocode": (
        "Pseudocode schlägt die Brücke zwischen der menschlichen Sprache und echtem Programmcode. Er folgt klaren Strukturen wie Verzweigungen und Schleifen, verzichtet aber auf syntaktische Feinheiten. Wir nutzen deutsche Begriffe wie DEFINIERE, WIEDERHOLE und FALLS. Ein wichtiger Schritt vor der Codierung ist der Trockenlauf: Gehe deinen Pseudocode im Kopf mit Beispieldaten durch, um Logikfehler wie Endlosschleifen oder Bereichsüberschreitungen vorab aufzuspüren."
    ),
    "ch22_5_example": (
        "Als Praxisbeispiel planen wir die Berechnung eines Notendurchschnitts. Zuerst definieren wir das Noten-Array und initialisieren die Summe. Im Ablaufdiagramm und im Pseudocode sehen wir genau, wie wir in einer Schleife jede Note zur Summe addieren und am Ende durch die Anzahl teilen. In Rust übersetzt, müssen wir lediglich darauf achten, die Summe veränderbar zu deklarieren und die Typen für die Division korrekt in Fließkommazahlen umzuwandeln. Die Logik steht da bereits felsenfest."
    ),
    "ch22_6_ai": (
        "Künstliche Intelligenz kann uns bei der Planung hervorragend unterstützen. Nutze Tools wie Copilot oder Claude als Sparringspartner. Bitte die KI, deine Anforderungen nach Sonderfällen zu durchleuchten, Mermaid-Entwürfe zu generieren oder deinen Pseudocode auf logische Schwachstellen hin zu prüfen. Wichtig ist jedoch, die Vorschläge der KI kritisch zu hinterfragen und sie strukturiert in deiner planung.md zu dokumentieren, statt sie einfach blind zu kopieren."
    ),
    "ch22_7_exercise": (
        "Um diesen Workflow direkt auszuprobieren, wartet eine praktische Übung auf dich: der Warenkorb-Rabatt-Rechner. Du sollst ein Programm planen und implementieren, das ein Array von fünf Artikelpreisen aufsummiert, bei einem Bestellwert über fünfzig Euro einen Rabatt von zehn Prozent abzieht und darauf die neunzehn Prozent Mehrwertsteuer berechnet. Erstelle zuerst deine planung.md mit Diagramm, Pseudocode und To-Do-Liste, bevor du Rust schreibst."
    ),
    "ch22_8_outro": (
        "In der Musterlösung siehst du, wie elegant Rusts if-Bedingungen als Ausdrücke verwendet werden können, um den Rabatt direkt einer Variablen zuzuweisen. Nutze diesen Planungs-Workflow bei jedem deiner künftigen Projekte. Er wird dir unzählige Stunden der Fehlersuche ersparen und dich zu einem besseren Softwareentwickler machen. Vielen Dank fürs Zuschauen, viel Erfolg beim Planen und bis zum nächsten Kapitel!"
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
    
    with open("audio/durations_ch22.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch22.json")

if __name__ == "__main__":
    main()
