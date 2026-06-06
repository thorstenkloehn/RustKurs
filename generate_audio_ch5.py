import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch5_1_intro": (
        "Willkommen zum fünften Kapitel unseres Rust-Kurses für Anfänger. Heute dreht sich alles um Variablen. "
        "Eine Variable ist wie eine beschriftete Box im Computer, in der wir einen Wert, wie zum Beispiel eine Zahl, "
        "speichern, um ihn später wiederzuverwenden. In dieser Lektion lernen wir, wie man Variablen in Rust "
        "erstellt, und wie man mit Fehlern und Warnungen im Code umgeht."
    ),
    "ch5_2_warnings": (
        "Wie deklarieren wir eine Variable? Mit dem Schlüsselwort let gefolgt vom Variablennamen erstellen wir eine "
        "Variable in Rust. Aber Vorsicht: Wenn du eine Variable erstellst, sie aber nirgendwo im Code benutzt, meckert "
        "der Rust-Compiler mit einer Warnung, einer gelben Wellenlinie im Editor. Unter dem Begriff unused variable "
        "erhältst du einen freundlichen Hinweis: Das Programm läuft trotzdem. Ein Fehler hingegen, markiert mit einer "
        "roten Wellenlinie, ist fatal. Das Programm kann nicht gestartet werden, bis der Fehler behoben ist."
    ),
    "ch5_3_println": (
        "Um Text und Variablen auf dem Bildschirm auszugeben, nutzen wir das println-Makro. Es gibt zwei Wege, "
        "Variablenwerte in einen Text einzufügen. Methode A ist die Direkt-Interpolation, bei der wir ab Rust "
        "Version 1.58 den Variablennamen direkt in die geschweiften Klammern schreiben. Methode B ist die klassische "
        "Variante, bei der wir die geschweiften Klammern als leere Platzhalter verwenden und die Variablen als Argumente "
        "hinten anstellen."
    ),
    "ch5_4_positional": (
        "Das Prinzip der Positionsargumente ist einfach: Wenn du Argumente hinten anstellst, zählt Rust im "
        "Hintergrund ab Null. Wir können die genaue Positionsnummer in den geschweiften Klammern angeben. "
        "Beispielsweise fügt die geschweifte Klammer Null das erste Argument und die geschweifte Klammer Eins das "
        "zweite Argument ein. So können wir Argumente mehrfach oder in beliebiger Reihenfolge verwenden."
    ),
    "ch5_5_underscore": (
        "Wenn eine Variable absichtlich oder vorübergehend beim Testen ungenutzt bleiben soll, gibt uns Rust eine "
        "Warnung aus. Die Lösung hierfür ist der Unterstrich. Wenn du einfach einen Unterstrich vor den Variablennamen "
        "setzt, signalisierst du dem Compiler, dass diese Variable absichtlich unbenutzt bleibt. Die Warnung verschwindet."
    ),
    "ch5_6_mutability": (
        "In Rust ist jede normale Variable standardmäßig unveränderlich, also immutable. Einmal zugewiesen, darfst "
        "du den Wert nicht mehr ändern, er ist wie in Stein gemeißelt. Wenn sich ein Wert im Laufe des Programms "
        "ändern muss, musst du das Schlüsselwort mut voranstellen. Mini-Merkregel: Ohne mut ist die Variable gesperrt, "
        "mit mut ist sie veränderbar."
    ),
    "ch5_7_explain": (
        "Keine Panik bei Fehlermeldungen! Der Compiler rustc hilft uns aktiv als Mentor. Bei einem Fehler zeigt "
        "er uns einen Fehlercode. Wenn du im Terminal rustc --explain gefolgt vom Fehlercode eingibst, erhältst du "
        "eine detaillierte Erklärung und Codebeispiele zur Lösung. Du musst dafür nicht mal den Editor verlassen!"
    ),
    "ch5_8_shadowing": (
        "Ein spannendes Konzept ist das Variablen-Shadowing, also die Beschattung. Normalerweise darf eine Variable "
        "ihren Datentyp in Rust niemals ändern. Mit let dürfen wir dieselbe Variable jedoch überschatten und "
        "ihr einen neuen Typ geben. Das ist so, als ob wir ein altes Buch wegschmeißen und ein neues Buch mit demselben "
        "Titel, aber völlig anderem Inhalt ins Regal stellen."
    ),
    "ch5_9_scopes": (
        "Für Variablen gelten die drei goldenen Scope-Regeln: Erstens, von außen nach innen: Ein innerer Block "
        "kann alles sehen und nutzen, was im äußeren Block deklariert wurde. Zweitens, von innen nach außen: "
        "Ein äußerer Block kann Variablen des inneren Blocks nicht sehen. Und drittens, das Lebensende: Am Ende eines "
        "Blocks, markiert durch die geschweifte Klammer, stirbt die Variable und wird aus dem Speicher gelöscht. "
        "Namens-Doppelgänger im inneren Block überdecken die äußere Variable nur temporär."
    ),
    "ch5_10_constants": (
        "Zuletzt gibt es Konstanten, deklariert mit const. Eine Konstante ist ein Name für einen Wert, der sich "
        "niemals ändern kann und noch strenger ist als eine unveränderliche Variable. Während eine normale Variable "
        "mit let wie ein beschreibbares Whiteboard im Zimmer ist, gleicht eine Konstante einem in Stein gemeißelten "
        "Schild an der Hauswand. In der nächsten Lektion lernen wir die Datentypen in Rust kennen."
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
        
    with open("audio/durations_ch5.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch5.json")

if __name__ == "__main__":
    main()
