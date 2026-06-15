import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch25_1_intro": (
        "Willkommen zum fünfundzwanzigsten Kapitel unseres Rust-Videokurses. Heute besprechen wir den Slice-Typ. "
        "Slices sind eines der mächtigsten Werkzeuge in Rust, um sicher, effizient und ohne zusätzliche Allokationen "
        "auf Teilausschnitte von Kollektionen zuzugreifen."
    ),
    "ch25_2_definition": (
        "Ein Slice ist ein Ausschnitt einer Kollektion, der durch einen Fat Pointer repräsentiert wird. "
        "Dieser Zeiger liegt auf dem Stack und speichert zwei Werte: die Speicheradresse des ersten Elements "
        "und die Länge des Ausschnitts. Slices besitzen den Speicher nicht, sondern leihen ihn aus."
    ),
    "ch25_3_problem": (
        "Das Problem ohne Slices: Wenn wir Teilausschnitte über separate Index-Variablen verwalten, "
        "können diese Indizes und die Datenquelle asynchron werden. Wird die Kollektion verändert, "
        "verweist der Index auf eine veraltete Position, was zu Abstürzen oder Fehlern führt."
    ),
    "ch25_4_naive": (
        "Im naiven Versuch schreiben wir eine Funktion, die das Ende des ersten Wortes als Zahl zurückgibt. "
        "Nach dem Aufruf leeren wir den String mit clear. Die Index-Zahl bleibt unverändert bestehen. "
        "Beim Zugriff stürzt das Programm ab."
    ),
    "ch25_5_anatomy": (
        "Die Anatomie des Fehlers: Das Programm kompiliert fehlerfrei, da die Zahl unabhängig vom String ist. "
        "Zur Laufzeit jedoch ist der String leer, und der Zugriff auf den alten Index provoziert eine kontrollierte "
        "Panik wegen einer Grenzüberschreitung."
    ),
    "ch25_6_solution": (
        "Die Lösung liegt in String-Slices. Wenn wir eine Referenz auf einen String-Ausschnitt zurückgeben, "
        "koppelt Rust die Lebensdauer an die Datenquelle. Der Borrow Checker verhindert das Leeren des Strings, "
        "solange der Ausschnitt noch verwendet wird."
    ),
    "ch25_7_tutorial": (
        "In unserem Tutorial bauen wir einen einfachen Log-Parser. Die Funktion extrahiert das Log-Level "
        "und die Nachricht als Slices. Da beide Slices auf den Log-Eintrag verweisen, verhindert der Compiler "
        "jede Mutation des Eintrags während der Verarbeitung."
    ),
    "ch25_8_outro": (
        "Zusammenfassend bieten Slices eine sichere, kostenfreie Abstraktion zur Speicherreferenzierung. "
        "Dank Deref Coercion machen sie Funktionsparameter flexibel. Nutzen Sie Slices, um Ihre Programme "
        "sicher und performant zu machen. Vielen Dank fürs Zuschauen!"
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
    
    with open("audio/durations_ch25.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch25.json")

if __name__ == "__main__":
    main()
