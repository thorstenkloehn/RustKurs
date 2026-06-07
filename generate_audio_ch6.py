import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch6_1_intro": (
        "Willkommen zum sechsten Kapitel unseres Rust-Kurses. Heute beschäftigen wir uns mit den Datentypen in Rust. "
        "Rust ist eine statisch typisierte Sprache. Das bedeutet, dass der Compiler den Typ jeder Variable bereits vor "
        "dem Start des Programms genau kennen muss. Doch keine Sorge: Dank der sogenannten Typinferenz erkennt Rust "
        "den Typ oft ganz automatisch anhand des zugewiesenen Wertes."
    ),
    "ch6_2_scalartypes": (
        "Beginnen wir mit den skalaren Typen. Ein skalarer Typ repräsentiert einen einzigen Wert. Die wichtigsten davon "
        "sind Ganzzahlen, im Englischen Integers genannt. Rust unterscheidet Ganzzahlen mit Vorzeichen, gekennzeichnet durch "
        "ein kleines i für signed, und Ganzzahlen ohne Vorzeichen, gekennzeichnet durch ein kleines u für unsigned. "
        "Signed-Variablen können positiv und negativ sein. Unsigned-Variablen können nur null oder positiv sein. Der "
        "Standardtyp für Ganzzahlen in Rust ist i32."
    ),
    "ch6_3_bounds": (
        "Die Zahlen im Typnamen, wie acht, 16 oder 32, stehen für die Speichergröße in Bit. Ein i8 belegt zum Beispiel "
        "ein Byte und kann Werte von minus 128 bis plus 127 speichern. Ein u8 kann Werte von null bis 255 speichern. "
        "Wichtig für die Praxis: Sprengt eine Zahl diese Grenzen, bricht Rust den Kompiliervorgang sofort mit einer "
        "Fehlermeldung ab. Das schützt uns vor bösen Fehlern im fertigen Programm. Und als Anfänger gilt: Nutze einfach "
        "die Standards i32 und f64, anstatt Speicher vorzeitig zu optimieren."
    ),
    "ch6_4_underscores": (
        "Große Zahlen wie sechs Millionen sind im Quellcode oft schwer zu lesen. Rust bietet hier eine elegante Lösung: "
        "Du kannst Unterstriche als visuelle Trennzeichen verwenden, ähnlich dem Tausenderpunkt in der Mathematik. "
        "Dem Compiler ist das völlig egal – er ignoriert die Unterstriche beim Kompilieren komplett. So wird aus einer "
        "unübersichtlichen Zahl ein gut lesbares Konstrukt."
    ),
    "ch6_5_isize_usize": (
        "Neben den festen Typen gibt es die systemabhängigen Typen isize und usize. Ihre Größe passt sich automatisch "
        "an die Architektur des Computers an, auf dem das Programm läuft. Auf einem 64-Bit-System belegen sie 64 Bit, "
        "auf einem 32-Bit-System 32 Bit. In der Praxis nutzen wir vor allem usize, um die Länge von Listen zu bestimmen "
        "oder Elemente über einen Index anzusprechen."
    ),
    "ch6_6_strings_escaping": (
        "Kommen wir zu den Texten. Ein Text in doppelten Anführungszeichen ist in Rust ein String-Literal. Manchmal müssen "
        "wir Sonderzeichen verwenden. Mit einem Backslash können wir diese maskieren, also escapen. So erzeugt Backslash n "
        "eine neue Zeile, Backslash t einen Tabulator-Abstand, Backslash Anführungszeichen ein echtes Anführungszeichen "
        "und ein doppelter Backslash einen einzelnen Backslash."
    ),
    "ch6_7_raw_strings": (
        "Wenn du viele Backslashes oder Pfade in deinem Text hast, kann das ständige Maskieren den Code unleserlich machen. "
        "Hier kommen Raw Strings ins Spiel. Wenn du ein kleines r vor die Anführungszeichen setzt, ignoriert Rust alle "
        "Sonderfunktionen des Backslashs. Der Text wird exakt so gedruckt und interpretiert, wie er im Quellcode steht."
    ),
    "ch6_8_methods": (
        "Viele Datentypen in Rust besitzen Methoden. Eine Methode ist im Grunde eine Funktion, die fest an einen "
        "bestimmten Wert oder Datentyp gebunden ist. Während normale Funktionen eigenständig stehen, werden Methoden "
        "mit einem Punkt direkt an eine Variable gehängt. Ein Beispiel sind Methoden für Fließkommazahlen wie floor "
        "zum Abrunden, ceil zum Aufrunden und round zum kaufmännischen Runden."
    ),
    "ch6_9_float_formatting": (
        "Bei der Ausgabe von Fließkommazahlen mit dem println-Makro können wir die AN-Zahl der Nachkommastellen begrenzen. "
        "Die Syntax lautet: Doppelpunkt, Punkt und die gewünschte AN-Zahl an Stellen innerhalb der geschweiften Klammern – "
        "zum Beispiel Doppelpunkt Punkt zwei für zwei Nachkommastellen. Der Wert in der Variable ändert sich dabei nicht, "
        "Rust passt nur die optische Darstellung an und rundet dabei korrekt."
    ),
    "ch6_10_casting": (
        "Manchmal müssen wir einen Wert von einem Typ in einen anderen umwandeln – das nennt man Casting. In Rust nutzen "
        "wir dafür das Schlüsselwort as. Wenn wir zum Beispiel eine Fließkommazahl mit as in eine Ganzzahl umwandeln, wird "
        "der Nachkommateil abgeschnitten. Achtung: Rust rundet hierbei nicht auf! Aus 99,99 wird gnadenlos die Ganzzahl 99. "
        "Für echtes Runden müssen wir zuvor die Methode round nutzen."
    ),
    "ch6_11_booleans": (
        "Der Datentyp bool steht für Booleans und repräsentiert Wahrheitswerte. Er kennt nur zwei Zustände: true für wahr "
        "und false für falsch. Obwohl ein einziges Bit ausreichen würde, belegt ein bool im Speicher ein volles Byte, da "
        "moderne Computer auf ganze Bytes viel schneller zugreifen können. Booleans entstehen durch direkte Zuweisung, "
        "mathematische Vergleiche oder eingebaute Methoden."
    ),
    "ch6_12_char_outro": (
        "Zuletzt gibt es den Datentyp char für einzelne Zeichen wie Buchstaben oder Emojis. In Rust wird ein char immer in "
        "einfache Anführungszeichen gesetzt, während Strings doppelte Anführungszeichen nutzen. Merk dir die Eselsbrücke: "
        "Einfache Striche für ein einsames Zeichen, doppelte Striche für beliebig viele Zeichen. Damit haben wir die wichtigsten "
        "Datentypen gemeistert. In der nächsten Lektion programmieren wir ein Projekt mit praktischen Übungen zu Variablen und Datentypen."
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
        
    with open("audio/durations_ch6.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch6.json")

if __name__ == "__main__":
    main()
