import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch28_1_intro": (
        "Willkommen zum achtundzwanzigsten Kapitel unseres Rust-Videokurses. Heute lernen wir Enums und "
        "Pattern Matching kennen. Sie erfahren, wie Sie exklusive Zustände und Alternativen typsicher "
        "ausdrücken und diese im Programm kontrolliert auswerten."
    ),
    "ch28_2_definition": (
        "Ein Aufzählungstyp oder kurz Enum beschreibt eine feste Menge exklusiver Varianten. Ein Wert "
        "repräsentiert zu jedem Zeitpunkt exakt eine Variante. Diese können Nutzdaten wie Tupel oder "
        "benannte Felder tragen. Pattern Matching prüft Werte und extrahiert diese Nutzdaten."
    ),
    "ch28_3_problem": (
        "Viele Programme nutzen lose Strings oder Booleans zur Zustandsmodellierung. Tippfehler bei Strings "
        "werden vom Compiler jedoch nicht erkannt, und ungültige Zustandskombinationen wie offene Zahlungen "
        "mit Tracking-Code bleiben möglich. Booleans sind oft mehrdeutig."
    ),
    "ch28_4_naive": (
        "In unserem naiven Versuch nutzen wir lose Strings für den Bestellstatus und eine leere Zeichenkette "
        "als Platzhalter für einen fehlenden Tracking-Code. Zudem greifen wir mit unwrap unsicher auf optionale "
        "Werte zu und vergessen eine Variante beim Matching."
    ),
    "ch28_5_anatomy": (
        "Die Anatomie des Fehlers zeigt uns, warum der naive Code fehlerhaft ist. Lose Strings bieten keine "
        "Typsicherheit zur Compilezeit, und unwrap führt bei abwesenden Werten zu Laufzeitabstürzen. "
        "Beim Match-Block bricht der Compiler ab, falls eine Variante nicht abgedeckt ist."
    ),
    "ch28_6_solution": (
        "Die Lösung ist ein BestellStatus-Enum mit den Varianten Offen, Bezahlt, Versendet mit Tracking-Code "
        "und Fehlgeschlagen mit Grund. Über match werten wir alle Varianten vollständig und typsicher aus. "
        "Abwesenheit modellieren wir sicher mit Option."
    ),
    "ch28_7_tutorial": (
        "Im Tutorial programmieren wir eine Bestelllogik. Wir nutzen match für komplexe Weichenstellungen, "
        "if let für den Zugriff auf einzelne interessante Varianten und let else für das frühe Aussteigen aus "
        "Funktionen, um den Kontrollfluss flach zu halten."
    ),
    "ch28_8_deepdive": (
        "Im Deep Dive betrachten wir Enums als mathematische Summentypen. Wir untersuchen das Speicherlayout "
        "mit Diskriminant, Alignment und Padding und sehen, wie die Nischen-Optimierung es erlaubt, Option "
        "ohne Speicher-Overhead zu repräsentieren. Zudem besprechen wir Option-Standardmethoden."
    ),
    "ch28_9_exercises": (
        "Vertiefen Sie Ihr Wissen in drei praktischen Übungen: Erstellen Sie eine Benutzer-Begrüßung basierend "
        "auf Rollen. Schreiben Sie einen Dateidownload-Statusprüfer mit matches. Und filtern Sie eine Liste von "
        "Rabatten typsicher mit Match Guards."
    ),
    "ch28_10_learning": (
        "Nutzen Sie Active Recall und provozieren Sie gezielt Compiler-Fehler: Versuchen Sie beispielsweise, "
        "Option direkt zu addieren, oder vergessen Sie absichtlich eine Variante beim Matching, um die "
        "aussagekräftigen Fehlerbilder des Compilers zu verstehen."
    ),
    "ch28_11_outro": (
        "Enums und Pattern Matching machen ungültige Zustände in Ihren Rust-Programmen schwerer darstellbar "
        "und sorgen für Robustheit und Typsicherheit. Den gesamten Code finden Sie im Repository. "
        "Viel Erfolg beim Ausprobieren!"
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
    
    with open("audio/durations_ch28.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch28.json")

if __name__ == "__main__":
    main()
