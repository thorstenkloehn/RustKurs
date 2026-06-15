import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch27_1_intro": (
        "Willkommen zum siebenundzwanzigsten Kapitel unseres Rust-Videokurses. Heute beschäftigen wir uns "
        "mit dem Fundament der Datenmodellierung in Rust: den Strukturen oder kurz Structs. Sie lernen, wie Sie eigene "
        "Datentypen erstellen, Daten logisch kapseln und mit Methoden ausstatten."
    ),
    "ch27_2_definition": (
        "Ein Struct ist ein benutzerdefinierter Typ, der verschiedene Werte gruppiert. Rust bietet drei Arten: "
        "Erstens: klassische Structs mit benannten Feldern. Zweitens: Tuple-Structs mit namenlosen, durchnummerierten "
        "Feldern. Und drittens: Unit-Like-Structs ohne Felder, die für Trait-Implementierungen genutzt werden."
    ),
    "ch27_3_problem": (
        "Warum reichen lose Variablen oder Tupel nicht aus? Lose Variablen haben keinen logischen Bezug zueinander "
        "und blähen Signaturen auf. Tupel bieten keine Benennung der Felder und keine Typsicherheit. Der Compiler kann "
        "logisch falsche Zuordnungen nicht verhindern. Structs lösen diese Probleme."
    ),
    "ch27_4_naive": (
        "In unserem naiven Versuch versuchen wir, String-Slices, also Referenzen, in einem Struct zu speichern, um Heap-Allokationen "
        "zu vermeiden. Außerdem versuchen wir fälschlicherweise, einzelne Felder direkt in der Struct-Definition als veränderbar zu markieren."
    ),
    "ch27_5_anatomy": (
        "Die Anatomie des Fehlers zeigt uns, dass der Compiler den Build blockiert. Er fordert Lebensdauer-Annotationen für Referenzen, "
        "um Dangling Pointer zu verhindern. Zudem führt das mut-Schlüsselwort im Struct-Körper zu einem Syntaxfehler. "
        "Mutabilität betrifft in Rust stets die gesamte Instanz."
    ),
    "ch27_6_solution": (
        "Die Lösung ist einfach: Wir verwenden besitzende Typen wie String im Struct. Dadurch besitzt die Struktur ihre Daten selbst. "
        "Die Mutabilität steuern wir flexibel bei der Instanziierung im Stack-Frame über let mut."
    ),
    "ch27_7_tutorial": (
        "In unserem Tutorial bauen wir eine Rechteck-Engine. Wir verlagern die Flächenberechnung in einen impl-Block für das Struct "
        "Rectangle. Mit dem Parameter self definieren wir Methoden und mit assoziierten Funktionen ohne self erstellen wir praktische Konstruktoren."
    ),
    "ch27_8_deepdive": (
        "Im Deep Dive betrachten wir das Speicherlayout. Der Compiler fügt unsichtbare Füllbytes, das Padding, ein, um Daten an geraden "
        "Speicheradressen auszurichten. Zudem lernen wir das mächtige Type-State-Pattern kennen, das Zustände zur Kompilierzeit absichert."
    ),
    "ch27_9_exercises": (
        "Es folgen drei praktische Übungen zur Vertiefung: Formatieren Sie Buchdaten mit manuellen Default-Implementierungen. "
        "Verwalten Sie ein Bankkonto mit Transaktionshistorie. Und entwickeln Sie eine typsichere mathematische 3D-Vektor-Bibliothek."
    ),
    "ch27_10_learning": (
        "Unsere Lernstrategie setzt auf aktives Erinnern und gezielte Fehlerprovokation. Versuchen Sie bewusst, unmutablen Speicher zu beschreiben "
        "oder Ownership-Moves zu provozieren, um die hilfreichen Fehlermeldungen des Compilers zu verstehen."
    ),
    "ch27_11_outro": (
        "Zusammenfassend sind Structs das Herzstück von Rusts Datendesign. Sie trennen Daten und Verhalten sauber und bieten "
        "maximale Performance bei absoluter Speichersicherheit. Den Code finden Sie im Repository. Viel Erfolg beim Ausprobieren!"
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
    
    with open("audio/durations_ch27.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch27.json")

if __name__ == "__main__":
    main()
