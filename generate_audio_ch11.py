import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch11_1_intro": (
        "Willkommen zum elften Kapitel unseres Kurses. Heute schauen wir uns weitere Details zu Funktionen in Rust an. "
        "Funktionen sind im Rust-Code allgegenwärtig. Wir verwenden die Konvention snake_case für Funktions- und Variablennamen. "
        "Alle Buchstaben sind klein und Wörter werden durch Unterstriche getrennt."
    ),
    "ch11_2_parameters": (
        "Funktionen können Parameter deklarieren, die Teil ihrer Signatur sind. Bei jedem Parameter müssen wir den Datentyp "
        "zwingend angeben, wie zum Beispiel value Doppelpunkt i32. Der Compiler prüft beim Aufruf streng, ob die "
        "übergebenen Argumente genau zu den erwarteten Parametern passen."
    ),
    "ch11_3_statements_expressions": (
        "Der Körper einer Funktion besteht aus Anweisungen und optional einem abschließenden Ausdruck. Anweisungen "
        "führen eine Aktion aus und geben keinen Wert zurück. Ausdrücke dagegen werten zu einem Ergebniswert aus. "
        "In Rust ist diese Unterscheidung sehr wichtig, da Rust eine ausdrucksbasierte Sprache ist."
    ),
    "ch11_4_block_expressions": (
        "Eine Variablenzuweisung mit let ist eine Anweisung. Sie liefert keinen Wert. Ein geschweifter Scope-Block ist "
        "dagegen ein Ausdruck, der zum Wert seiner letzten Zeile auswertet. Beachte, dass Ausdrücke am Ende kein "
        "Semikolon besitzen. Mit einem Semikolon wird ein Ausdruck sofort zu einer Anweisung."
    ),
    "ch11_5_returns": (
        "Um Werte zurückzugeben, definieren wir den Rückgabetyp mit einem Pfeil. Die Funktion gibt standardmäßig das "
        "Ergebnis des letzten Ausdrucks im Funktionskörper zurück. Setzt man versehentlich ein Semikolon dahinter, "
        "wird es zu einer Anweisung ohne Rückgabewert, und der Compiler meldet einen Typkonflikt."
    ),
    "ch11_6_outro": (
        "Zusammenfassend haben wir die feine Unterscheidung zwischen Anweisungen und Ausdrücken kennengelernt und gesehen, "
        "wie Rückgaben und Parameter in Rust sicher deklariert werden. Das war es für dieses Kapitel über Funktionen-Details. "
        "Bis zum nächsten Mal!"
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
        
    with open("audio/durations_ch11.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch11.json")

if __name__ == "__main__":
    main()
