import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch13_1_intro": (
        "Willkommen zum dreizehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion festigen wir unser Wissen über "
        "Operatoren durch fünf praktische Übungen. Wir schauen uns die Grundrechenarten, die Ganzzahl-Falle bei Divisionen, "
        "Typumwandlungen mit dem as-Operator, Potenzierung und Wurzelziehen sowie eine praxisnahe Zinseszinsberechnung an. "
        "Bereite deine Entwicklungsumgebung vor, denn wir gehen direkt in Visual Studio Code, um den Code Zeile für Zeile zu schreiben "
        "und im Detail zu analysieren."
    ),
    "ch13_2_ex1": (
        "In der ersten Übung deklarieren wir zwei Variablen, a gleich fünfzehn und b gleich vier, als Ganzzahlen. "
        "Wir berechnen die Summe, Differenz, das Produkt, den Quotienten und den Modulo-Rest. "
        "Beachte hierbei: Da a und b Ganzzahlen sind, führt Rust eine Ganzzahldivision durch. Das Ergebnis von fünfzehn geteilt durch vier "
        "ist demnach drei. Die Nachkommastellen fallen komplett weg. Der Modulo-Operator berechnet den verbleibenden Rest der Division, "
        "welcher ebenfalls drei beträgt, da vier mal drei gleich zwölf ist und drei als Rest übrig bleibt."
    ),
    "ch13_3_ex2": (
        "In Übung zwei betrachten wir die Ganzzahl-Falle bei der Division im Detail. Wenn wir sieben geteilt durch zwei rechnen, "
        "erwarten wir mathematisch drei Komma fünf. Rust gibt uns jedoch drei zurück, da beide Variablen Ganzzahlen sind. "
        "Rust führt keine automatischen Typumwandlungen durch, um unvorhersehbare Rundungsfehler zu vermeiden. Die Lösung besteht darin, "
        "beide Zahlen mit dem Schlüsselwort as explizit in den Fließkommatyp f64 zu konvertieren. Dadurch führt Rust eine echte "
        "Gleitkommadivision aus und liefert das korrekte Ergebnis drei Komma fünf."
    ),
    "ch13_4_ex3": (
        "Die dritte Übung befasst sich mit dem Mischen unterschiedlicher Datentypen. Versuchen wir, eine Ganzzahl vom Typ i32 direkt mit "
        "einer Fließkommazahl vom Typ f64 zu addieren, verweigert der Compiler den Dienst. Um dieses Problem zu lösen, müssen wir die Ganzzahl "
        "explizit mit as f64 in eine Fließkommazahl umwandeln. Dies ist verlustfrei. Konvertieren wir jedoch umgekehrt eine Fließkommazahl wie "
        "drei Komma eins vier in eine Ganzzahl mittels as i32, schneidet Rust alle Nachkommastellen rigoros ab. Das Ergebnis ist drei, "
        "und wir erleiden einen Datenverlust."
    ),
    "ch13_5_ex4": (
        "In Übung vier lernen wir Potenzierung und Wurzelziehen. Für diese mathematischen Operationen stellt Rust nützliche Methoden direkt "
        "auf Fließkommazahlen zur Verfügung. Mit Punkt powf können wir eine Basis mit einem beliebigen Fließkomma-Exponenten potenzieren, "
        "zum Beispiel zwei Komma null hoch drei Komma null. Für Quadratwurzeln nutzen wir die Methode Punkt sqrt. Beide Methoden greifen "
        "direkt auf optimierte CPU-Befehle zu, sodass wir hierfür keine externen Bibliotheken einbinden müssen."
    ),
    "ch13_6_ex5": (
        "In der fünften Übung führen wir alles in einem praktischen Beispiel zusammen: der Zinseszinsberechnung. Wir berechnen das Endkapital "
        "eines Startkapitals von tausend Euro bei fünf Prozent Zinsen über eine Laufzeit von zehn Jahren. In der Formel müssen wir das "
        "Wachstum mit den Jahren potenzieren. Da die Jahre als positive Ganzzahl u32 definiert sind, konvertieren wir sie mittels as f64 "
        "für die powf-Methode. Das Ergebnis runden wir in der Ausgabe mit der Formatierung Doppelpunkt Punkt zwei auf genau zwei Nachkommastellen."
    ),
    "ch13_7_outro": (
        "Das waren die fünf Übungen zur Festigung der Rust-Operatoren! Du weißt nun, wie man arithmetische Operationen sicher steuert, "
        "Typen fehlerfrei konvertiert und Stolperfallen bei Ganzzahlberechnungen umgeht. Experimentiere ruhig mit eigenen Werten in deinem "
        "Editor. Im nächsten Kapitel machen wir den nächsten großen Schritt. Vielen Dank fürs Zuschauen und bis zum nächsten Mal!"
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
        
    with open("audio/durations_ch13.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch13.json")

if __name__ == "__main__":
    main()
