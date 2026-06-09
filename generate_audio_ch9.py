import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch9_1_intro": (
        "Willkommen zum neunten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion fassen wir die Grundlagen "
        "über Variablen und Datentypen zusammen, die wir in den letzten Kapiteln gelernt haben. Beginnen wir mit "
        "der Veränderlichkeit von Variablen."
    ),
    "ch9_2_mutability": (
        "Variablen in Rust sind standardmäßig unveränderlich, also immutable. Wenn wir versuchen, einer normalen Variable "
        "nachträglich einen neuen Wert zuzuweisen, bricht der Compiler mit einem Fehler ab. Um eine Variable veränderbar "
        "zu machen, müssen wir das Schlüsselwort mut vor den Variablennamen setzen."
    ),
    "ch9_3_constants": (
        "Konstanten werden mit dem Schlüsselwort const deklariert. Im Gegensatz zu normalen Variablen sind sie immer "
        "unveränderlich – ein mut ist hier nicht erlaubt. Zudem müssen wir bei Konstanten den Datentyp zwingend explizit "
        "angeben. Sie werden direkt zur Kompilierzeit berechnet und eignen sich hervorragend für feste Werte im gesamten Programm."
    ),
    "ch9_4_shadowing": (
        "Shadowing, also das Überschatten, ist ein mächtiges Konzept in Rust. Du kannst eine Variable mit let einfach "
        "neu deklarieren und dabei denselben Namen wiederverwenden. Die neue Variable überschattet die alte. Das erlaubt "
        "es uns, den Datentyp einer Variable im Verlauf des Codes zu ändern, ohne neue Variablennamen erfinden zu müssen."
    ),
    "ch9_5_scalar_types": (
        "Kommen wir zu den skalaren Datentypen. Diese repräsentieren einen einzelnen Wert. Dazu gehören Ganzzahlen mit "
        "oder ohne Vorzeichen, wobei i32 der Standard ist. Außerdem gibt es Fließkommazahlen mit dem Standard f64, "
        "Wahrheitswerte vom Typ bool mit den Zuständen true oder false sowie einzelne Unicode-Zeichen vom Typ char "
        "in einfachen Anführungszeichen."
    ),
    "ch9_6_tuples": (
        "Zusammengesetzte Typen können mehrere Werte gruppieren. Der erste davon ist das Tupel. Ein Tupel hat eine "
        "feste Länge und darf unterschiedliche Datentypen mischen. Der Zugriff auf die Elemente erfolgt über die "
        "Punkt-Notation, wie punkt null, oder durch das direkte Entpacken in einzelne Variablen."
    ),
    "ch9_7_arrays": (
        "Der zweite zusammengesetzte Typ ist das Array. Ein Array speichert Elemente desselben Typs in einer festen Größe. "
        "Der Zugriff erfolgt über eckige Klammern und den Index ab null. Greifen wir auf einen ungültigen Index außerhalb "
        "der Grenzen zu, bricht Rust das Programm aus Sicherheitsgründen sofort mit einem Panic ab. Das schützt uns "
        "vor kritischen Speicherfehlern."
    ),
    "ch9_8_outro": (
        "Zusammenfassend: Rust bietet uns durch Immutabilität, Typsicherheit und automatische Grenzensicherungen "
        "maximale Stabilität bei gleichzeitig hoher Performance. Damit haben wir den ersten großen Block über Variablen "
        "und Datentypen erfolgreich gemeistert! Bis zum nächsten Kapitel."
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
        
    with open("audio/durations_ch9.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch9.json")

if __name__ == "__main__":
    main()
