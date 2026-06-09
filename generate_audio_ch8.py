import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch8_1_intro": (
        "Willkommen zum achten Kapitel unseres Rust-Kurses für Anfänger. Nachdem wir im letzten Kapitel unser erstes "
        "Übungsprojekt abgeschlossen und die skalaren Datentypen vertieft haben, kommen wir nun zu den zusammengesetzten "
        "Datentypen. In Rust gibt es zwei primäre zusammengesetzte Datentypen: Arrays und Tupel. Sie erlauben es uns, "
        "mehrere Werte in einer einzigen Variable zu bündeln."
    ),
    "ch8_2_array_intro": (
        "Beginnen wir mit dem Array. Ein Array kannst du dir wie eine Schachtel mit festen Fächern vorstellen. Es zeichnet "
        "sich durch drei wichtige Eigenschaften aus. Erstens, es ist homogen. Das bedeutet, alle Elemente müssen vom selben "
        "Datentyp sein. Zweitens, es hat eine feste Größe. Ein Array kann im Nachhinein weder wachsen noch schrumpfen. "
        "Und drittens, es ist geordnet. Die Elemente liegen in einer festen Reihenfolge vor."
    ),
    "ch8_3_array_syntax": (
        "Schauen wir uns die Syntax in Rust an. Wenn du ein Array deklarierst, kann Rust den Typ automatisch über die Typinferenz "
        "bestimmen, zum Beispiel bei einer Liste von sechs Ganzzahlen in eckigen Klammern. Alternativ kannst du den Typ auch "
        "explizit angeben. Die Schreibweise dafür lautet: eckige Klammer auf, der Datentyp, ein Semikolon, die Anzahl der Elemente, "
        "und eckige Klammer zu. Wichtig dabei ist: Wenn du eine feste Anzahl vorgibst, musst du auch exakt so viele Elemente in "
        "die Klammer schreiben, sonst bricht der Compiler mit einem Fehler ab."
    ),
    "ch8_4_array_functions": (
        "Rust bietet uns nützliche Hilfsfunktionen für Arrays. Mit der Methode punkt len können wir jederzeit die Länge abfragen, "
        "also die Anzahl der Elemente im Array ermitteln. Auch leere Arrays sind in Rust erlaubt. Das geht allerdings nur, wenn "
        "wir den Datentyp und die Länge Null ausdrücklich dazuschreiben, da der Compiler sonst nicht weiß, welche Werte später "
        "darin gespeichert werden sollen."
    ),
    "ch8_5_array_indexing": (
        "Wie greifen wir auf Elemente zu? In der Programmierung beginnen wir immer bei Index Null zu zählen. Das erste Element "
        "liegt also bei Index Null, das zweite bei Index Eins, und das letzte bei der Länge minus Eins. Zwar hat ein Array eine "
        "feste Größe, wir können aber bestehende Werte überschreiben. Dazu müssen wir das Array lediglich mit dem Schlüsselwort "
        "let mut deklarieren. Und als kleine Vorschau: Wenn du später ein Array brauchst, das dynamisch wachsen oder schrumpfen kann, "
        "nutzen wir in Rust einen sogenannten Vektor."
    ),
    "ch8_6_tuple_intro": (
        "Kommen wir zum zweiten zusammengesetzten Typen: dem Tupel. Ein Tupel ist der flexible Mix-Container in Rust. Genau wie "
        "ein Array speichert es mehrere Werte in einer festen Reihenfolge. Der riesige Unterschied ist jedoch: Ein Tupel darf "
        "verschiedene Datentypen mischen! Du kannst darin gleichzeitig Text, ganze Zahlen und Wahrheitswerte speichern. Das macht "
        "es perfekt, um zusammengehörige Informationen zu bündeln. Erstellt wird ein Tupel mit normalen, runden Klammern."
    ),
    "ch8_7_tuple_access": (
        "Der Zugriff auf die Werte eines Tupels unterscheidet sich ebenfalls vom Array. Auch hier startet der Index bei Null. "
        "Doch anstatt eckiger Klammern nutzen wir beim Tupel die Punkt-Notation. Wir schreiben also einfach den Variablennamen, "
        "gefolgt von einem Punkt und dem jeweiligen Index, um an die einzelnen Daten heranzukommen."
    ),
    "ch8_8_tuple_destructuring": (
        "Ein besonders eleganter Profi-Trick in Rust ist das Destrukturieren, also der Musterabgleich. Weil das manuelle Auslesen "
        "über Punkt-Null oder Punkt-Eins mühsam sein kann, können wir ein Tupel in einer einzigen Zeile komplett entpacken und "
        "in einzelne Variablen zerlegen. Rust weist die Werte dabei automatisch von links nach rechts den neuen Variablen zu, "
        "die wir danach direkt verwenden können."
    ),
    "ch8_9_tuple_debug_outro": (
        "Zum Abschluss gibt es noch ein wichtiges Detail beim Drucken im Terminal. Ein Tupel kann nicht direkt mit dem Standard-Platzhalter "
        "geschweifte Klammern ausgegeben werden. Du musst dafür den Debug-Modus verwenden, indem du einen Doppelpunkt und ein "
        "Fragezeichen in die geschweiften Klammern schreibst. Schauen wir uns den vollständigen Beispielcode an: Wir erstellen eine "
        "Person als Tupel aus Name, Alter und Aktivitätsstatus, lesen das Alter aus, entpacken das Tupel komplett und geben es "
        "schließlich im Debug-Format aus. Damit haben wir die zusammengesetzten Datentypen erfolgreich gemeistert! Bis zum nächsten Kapitel."
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
        
    with open("audio/durations_ch8.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch8.json")

if __name__ == "__main__":
    main()
