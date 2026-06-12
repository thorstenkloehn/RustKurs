import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch15_1_intro": (
        "Willkommen zum fünfzehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion besprechen wir "
        "Kontrollstrukturen – also Bedingungen, Musterabgleich und Schleifen. Kontrollstrukturen steuern den Ablauf "
        "deines Programms und sorgen dafür, dass dein Code auf unterschiedliche Situationen reagiert. In der Praxis "
        "nutzen wir sie, um Benutzereingaben zu prüfen, Zustandsmaschinen zu steuern, Spiele-Schleifen am Laufen "
        "zu halten oder Datenmengen zu verarbeiten."
    ),
    "ch15_2_expressions": (
        "Ein wichtiges Grundlagenkonzept in Rust ist der Unterschied zwischen Ausdrücken und Anweisungen. Anweisungen "
        "führen eine Aktion aus, geben aber keinen Wert zurück und enden fast immer mit einem Semikolon. Ausdrücke "
        "dagegen berechnen ein Ergebnis und geben einen Wert zurück – sie enden ohne Semikolon. Da in Rust fast alle "
        "Kontrollstrukturen Ausdrücke sind, können wir ihre Ergebnisse direkt einer Variablen zuweisen."
    ),
    "ch15_3_if_else": (
        "Mit if und else treffen wir einfache Ja-Nein-Entscheidungen. Anders als in vielen Sprachen benötigen wir "
        "in Rust keine runden Klammern um die Bedingung. Da if ein Ausdruck ist, können wir den ermittelten Wert "
        "direkt zurückgeben. Wichtig ist dabei nur, dass alle Zweige der if-Bedingung denselben Datentyp zurückgeben, "
        "andernfalls beschwert sich der Compiler."
    ),
    "ch15_4_match": (
        "Für komplexere Fallunterscheidungen besitzt Rust eine besondere Superkraft: match. Man kann sich match wie "
        "eine viel sicherere und mächtigere Variante von switch vorstellen. Die wichtigste Regel hierbei ist die "
        "Vollständigkeit: Der Compiler zwingt uns dazu, jeden einzelnen möglichen Fall abzudecken. Mit dem Platzhalter "
        "Unterstrich können wir einen Auffang-Fall für alle übrigen Werte definieren."
    ),
    "ch15_5_loop_while": (
        "Kommen wir zu den Schleifen. Die einfachste Schleife ist loop. Sie läuft unendlich weiter, bis wir sie mit "
        "break stoppen. Mit continue können wir den restlichen Code überspringen und direkt zum nächsten Durchlauf springen. "
        "Eine Besonderheit in Rust ist, dass loop einen Wert zurückgeben kann, den wir einfach hinter das break schreiben. "
        "Die while-Schleife hingegen prüft vor jedem Durchlauf eine Bedingung. Solange diese Bedingung wahr ist, "
        "wird der Codeblock wiederholt."
    ),
    "ch15_6_for_labels": (
        "Die for-Schleife ist die sicherste und am häufigsten genutzte Schleife in Rust. Mit ihr können wir über Bereiche "
        "wie eins bis fünf laufen oder über Arrays iterieren. Da for-Schleifen die Länge von Arrays automatisch kennen, "
        "verhindern sie Indexüberschreitungen und sind extrem performant. Wenn wir Schleifen ineinander verschachteln, "
        "können wir sie mit Labels benennen. So können wir aus einer inneren Schleife direkt die äußere Schleife abbrechen."
    ),
    "ch15_7_outro": (
        "Damit sind wir am Ende von Kapitel fünfzehn. Du kennst nun alle Kontrollstrukturen, um deinen Rust-Code dynamisch "
        "zu steuern. Viel Erfolg beim Ausprobieren, vielen Dank fürs Zuschauen und bis zum nächsten Mal!"
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
        
    with open("audio/durations_ch15.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch15.json")

if __name__ == "__main__":
    main()
