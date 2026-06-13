import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch18_1_intro": (
        "Willkommen zum achtzehnten Kapitel unseres Rust-Kurses. In dieser Lektion vertiefen wir unser Verständnis des "
        "Ownership-Systems. Wir werfen einen detaillierten Blick auf die Speicherverwaltung auf Hardware-Ebene. Während C "
        "und C++ uns die Verantwortung für Speicherlecks und Dangling Pointers zuschieben, und Sprachen wie Java oder "
        "Python durch Garbage Collection oder Referenzzählung Laufzeiteinbußen erleiden, bietet Rust absolute Speichersicherheit "
        "und maximale Performance zur Kompilierzeit."
    ),
    "ch18_2_stack_heap": (
        "Der Stack und der Heap sind die beiden Speicherbereiche im RAM. Der Stack arbeitet nach dem Last-In-First-Out-Prinzip "
        "und verwaltet Daten mit fester Größe, wie primitive Zahlen. Der Stack-Pointer verschiebt sich dabei in nur einem "
        "CPU-Taktzyklus. Der Heap hingegen ist unstrukturiert. Wenn wir dort Speicher anfordern, sucht der Allocator nach "
        "einem freien Platz, markiert ihn und gibt einen Zeiger zurück. Da der Zugriff über Zeiger langsamer ist und zu Cache-Misses "
        "führen kann, ist eine effiziente Verwaltung entscheidend."
    ),
    "ch18_3_rules_scopes": (
        "Das Fundament bilden drei Regeln: Erstens, jeder Wert hat einen Besitzer. Zweitens, es gibt nur einen Besitzer gleichzeitig. "
        "Drittens, verlässt der Besitzer seinen Gültigkeitsbereich, wird der Wert über die drop-Funktion sofort freigegeben. In "
        "verschachtelten Scopes werden lokale Variablen am Ende des Blocks automatisch abgebaut. Dieses deterministische Prinzip, "
        "bekannt als RAII, stellt sicher, dass Ressourcen wie Speicher oder Datei-Handles sicher und ohne Garbage Collector freigegeben werden."
    ),
    "ch18_4_move_copy": (
        "Wenn wir eine Heap-Variable wie einen String einer neuen Variablen zuweisen, kopiert Rust nur die Metadaten auf dem Stack. "
        "Um Double-Free-Fehler zu vermeiden, deklariert Rust die Quellvariable sofort für ungültig. Das Eigentum wird verschoben – "
        "ein Move findet statt. Bei Stack-Typen wie Ganzzahlen greift dagegen der Copy-Trait: Der Wert wird byteweise kopiert und beide "
        "Variablen bleiben gültig. Heap-Typen dürfen niemals Copy implementieren, da sie eine Drop-Bereinigung benötigen."
    ),
    "ch18_5_clone_structs": (
        "Um eine tiefe Kopie von Heap-Daten zu erzeugen, nutzen wir den Clone-Trait und rufen die clone-Methode auf. Dies dupliziert "
        "den Heap-Speicher, ist jedoch performancetechnisch teurer. Auch bei Strukturen und Enums greift das Ownership-System: Ein "
        "Struct besitzt seine Felder. Wenn wir ein Feld herausbewegen, findet ein teilweiser Move statt und das gesamte Struct wird ungültig. "
        "Vektoren besitzen ebenfalls ihre Elemente und geben sie beim eigenen Zerstören rekursiv frei."
    ),
    "ch18_6_errors_outro": (
        "Bei Fehlern wie dem berüchtigten 'use of moved value' hilft uns der Compiler mit klaren Erklärungen. Er zeigt genau, wo "
        "der Wert verschoben wurde und wo wir unerlaubt darauf zugreifen. Meistens lösen wir dies, indem wir die Daten mittels "
        "Referenzen ausleihen. Im nächsten Kapitel besprechen wir daher das Ausleihen im Detail. Vielen Dank fürs Zuschauen, "
        "und bis zum nächsten Kapitel!"
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
        
    with open("audio/durations_ch18.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch18.json")

if __name__ == "__main__":
    main()
