import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch10_1_intro": (
        "Willkommen zum zehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion beschäftigen wir uns mit "
        "Funktionen. Eine Funktion ist ein wiederverwendbarer Code-Block, der eine bestimmte Aufgabe erledigt. Du "
        "deklarierst sie einmal und kannst sie danach im Programm beliebig oft aufrufen. Das spart doppelten Code "
        "und hält das Programm übersichtlich."
    ),
    "ch10_2_main_and_custom": (
        "Jedes Rust-Programm startet automatisch in der main-Funktion. Eigene Funktionen werden mit dem Schlüsselwort "
        "fn definiert. Dabei ist die Reihenfolge in der Datei völlig egal: Eigene Funktionen können vor oder nach der "
        "main-Funktion stehen. Beachte aber: Das Aufschreiben einer Funktion führt sie noch nicht aus. Erst durch den "
        "Aufruf mit runden Klammern wird der Code tatsächlich gestartet."
    ),
    "ch10_3_parameters_arguments": (
        "Um Funktionen flexibel zu machen, übergeben wir ihnen Werte. Hierbei unterscheiden wir Parameter und Argumente. "
        "Der Parameter ist der Platzhalter in der Definition, für den wir in Rust zwingend einen Datentyp angeben müssen, "
        "zum Beispiel name Doppelpunkt und &str. Das Argument ist der konkrete Wert beim Aufruf, wie zum Beispiel "
        "der Name Anna. Der Compiler prüft streng, ob Typ und Anzahl der Argumente exakt übereinstimmen."
    ),
    "ch10_4_return_values": (
        "Neben Eingaben können Funktionen auch Ergebnisse zurückgeben. Den Rückgabetyp definieren wir mit einem Pfeil "
        "hinter der Parameterliste. In Rust haben wir zwei Möglichkeiten für die Rückgabe: Entweder nutzen wir das "
        "Schlüsselwort return, was die Funktion sofort beendet, oder wir schreiben den Wert als Ausdruck in die letzte "
        "Zeile – ganz ohne das Wort return und ohne Semikolon. Das ist der typische Rust-Stil!"
    ),
    "ch10_5_outro": (
        "Zusammenfassend: Funktionen strukturieren unseren Code und machen ihn wiederverwendbar. Durch die strenge "
        "Typprüfung des Compilers und die flexiblen Rückgabemöglichkeiten schreiben wir sicheren und sauberen Code. "
        "Damit hast du ein weiteres wichtiges Werkzeug in Rust gelernt! Bis zum nächsten Mal."
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
        
    with open("audio/durations_ch10.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch10.json")

if __name__ == "__main__":
    main()
