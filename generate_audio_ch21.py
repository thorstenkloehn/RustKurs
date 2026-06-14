import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch21_1_intro": (
        "Willkommen zum einundzwanzigsten Kapitel unseres Rust-Videokurses. Heute ziehen wir ein Fazit über die bisher gelernten Grundlagen und widmen uns dem Herzen von Rust, dem sogenannten Heiligen Dreigestirn. Bisher haben wir alle wichtigen Werkzeuge kennengelernt: Variablen und ihre Gültigkeitsbereiche, skalare und zusammengesetzte Datentypen, Kontrollstrukturen für Entscheidungen und Schleifen, sowie Funktionen und Operatoren. Mit diesen Bausteinen können wir bereits vielseitige Konsolenprogramme entwickeln. Doch um Rust wirklich zu beherrschen, müssen wir verstehen, wie diese Elemente im Speicher zusammenarbeiten."
    ),
    "ch21_2_holy_trinity": (
        "Rust unterscheidet sich von fast allen anderen Programmiersprachen durch seine einzigartige Speicherverwaltung. Anstatt auf einen langsamen Garbage Collector oder risikoreiches manuelles Freigeben zu setzen, ruht Rust auf drei untrennbaren Säulen: Ownership, Borrowing und Lifetimes. Zusammen bilden sie das Heilige Dreigestirn von Rust. Diese statischen Spielregeln werden bereits während des Kompilierens strengstens überprüft. Dadurch garantiert Rust absolute Speichersicherheit zur Laufzeit, ohne die Performance des Programms zu beeinträchtigen. Gehen wir diese drei Säulen nun im Detail durch."
    ),
    "ch21_3_ownership": (
        "Die erste Säule ist das Ownership-System. Jedes Datenelement im Speicher besitzt genau eine Variable als Eigentümer. Es kann niemals zwei Besitzer gleichzeitig geben. Verlässt der Besitzer seinen Gültigkeitsbereich, den Scope, wird der Speicher automatisch freigegeben. Übergeben wir eine Heap-Variable wie einen String an eine Funktion, verschiebt Rust das Eigentum. Dies nennen wir einen Move. Die ursprüngliche Variable wird dadurch ungültig. Liegen Daten stattdessen komplett auf dem Stack, wie einfache Zahlen, kopiert Rust sie automatisch per Copy, und beide Variablen bleiben gültig."
    ),
    "ch21_4_borrowing": (
        "Um Daten flexibel zu teilen, ohne ständig das Eigentum zu verschieben, nutzen wir die zweite Säule: das Ausleihen oder Borrowing. Über Referenzen, gekennzeichnet durch das kaufmännische Und-Symbol, leiht sich eine Funktion nur die Speicheradresse aus. Hierbei gelten strikte Regeln. Du darfst entweder beliebig viele unveränderliche Lese-Referenzen gleichzeitig aktiv haben – oder aber genau eine einzige veränderliche Schreib-Referenz. Diese Exklusivität verhindert Datenkonflikte, sogenannte Data Races, bei denen zwei Zeiger gleichzeitig versuchen, denselben Speicher zu manipulieren."
    ),
    "ch21_5_lifetimes": (
        "Die dritte Säule sind die Lifetimes, also die Lebensdauern von Referenzen. Der Rust-Compiler garantiert statisch, dass kein Verweis jemals ins Leere zeigt. Eine Referenz darf niemals länger leben als das eigentliche Datenelement, auf das sie verweist. Versucht eine Funktion zum Beispiel, eine Referenz auf eine lokale Variable zurückzugeben, scheitert das, da die lokale Variable am Funktionsende gelöscht wird. Es entsteht eine ungültige, hängende Referenz. Rust verhindert solche Dangling References zur Kompilierzeit, indem der Compiler das Eigentum am Rückgabewert erzwingt."
    ),
    "ch21_6_string_str": (
        "Ein häufiger Stolperstein für Anfänger ist der Unterschied zwischen dem Datentyp String und dem String-Slice und-str. Ein String ist eine dynamisch wachsende Zeichenkette auf dem Heap, die den Text besitzt und verändert werden kann. Ein und-str ist dagegen ein reiner Verweis, also ein Zeiger auf ein bestehendes Stück Text. Er besitzt keine Daten selbst und belegt auf dem Stack immer nur eine feste Größe. Dieses Prinzip zieht sich durch Rust: Wir entscheiden stets bewusst zwischen Besitzern und Gästen im Speicher, um maximale Performance zu erzielen."
    ),
    "ch21_7_expressions": (
        "Ein weiteres wichtiges Konzept in Rust ist, dass fast alle Kontrollstrukturen Ausdrücke, also Expressions, sind. Das bedeutet, dass if-else-Blöcke und match-Statements einen Wert direkt zurückgeben können. Dies ermöglicht es uns, Variablen elegant zu initialisieren, ohne sie vorab veränderlich deklarieren zu müssen. Beim Pattern Matching mit match fordert Rust zudem absolute Vollständigkeit. Alle möglichen Fälle müssen abgedeckt sein. Der Unterstrich dient dabei als praktischer Fallback, damit unser Programm auch bei unerwarteten Werten stabil bleibt."
    ),
    "ch21_8_outro": (
        "Um diese Grundlagen zu festigen, bietet dir dieses Kapitel vierzig vielseitige Projektvorschläge – von Notenrechnern über Spiele bis zu CLI-Tools. Alle kommen komplett ohne komplexe Structs und Vektoren aus. Nutze interaktive Tools wie Rustlings oder Exercism, und integriere kleine Übungen in deinen Alltag. Der Compiler ist dabei kein Feind, sondern dein bester Verbündeter auf dem Weg zu sicherem Code. Im nächsten Kapitel lernen wir fortgeschrittene Datenstrukturen wie Structs kennen. Vielen Dank fürs Zuschauen, viel Erfolg und bis zum nächsten Mal!"
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
    
    with open("audio/durations_ch21.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch21.json")

if __name__ == "__main__":
    main()
