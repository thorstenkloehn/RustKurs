import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch19_1_intro": (
        "Willkommen zum neunzehnten Kapitel unseres Rust-Kurses. Heute beschäftigen wir uns mit Referenzen und "
        "dem Konzept des Ausleihens, auch bekannt als Borrowing. Wie wir im letzten Kapitel gesehen haben, "
        "überträgt Rust beim Zuweisen oder Übergeben von Heap-Variablen standardmäßig das Eigentum, also die "
        "Ownership. Das zwingt uns, Werte mühsam per Return zurückzugeben. Um dies zu vermeiden, nutzen wir Referenzen, "
        "die mit dem kaufmännischen Und-Symbol deklariert werden. Sie speichern lediglich Speicheradressen auf dem Stack, "
        "ohne das Eigentum zu verändern."
    ),
    "ch19_2_borrowing_types": (
        "In Rust unterscheiden wir vier Übergabe-Arten. Übergeben wir Werte wie String, übernimmt die Funktion "
        "den Besitz und kann die Daten je nach mut-Deklaration verändern. Bei einer unveränderlichen Referenz wie "
        "und-String erhält die Funktion nur eine Leseadresse. Das ist der Standard für Leseoperationen. "
        "Eine veränderliche Referenz wie und-mut-String erlaubt es dagegen, die Originaldaten auf dem Heap direkt zu "
        "modifizieren, ohne das Eigentum zu übernehmen. Rust dereferenziert diese Adressen bei Methodenaufrufen automatisch."
    ),
    "ch19_3_borrow_checker_rules": (
        "Der Borrow Checker ist der strenge Wächter unseres Codes. Um Datenkonflikte zur Laufzeit zu verhindern, setzt "
        "er zwei goldene Regeln durch. Erstens: Du darfst beliebig viele unveränderliche Lese-Referenzen gleichzeitig haben. "
        "Zweitens: Du darfst maximal eine veränderliche Schreib-Referenz zur selben Zeit besitzen. Wenn jemand schreibt, "
        "darf niemand sonst lesen oder schreiben. Stell dir vor, Klaus fährt das Auto und erwartet ein rotes Auto, während "
        "Sabine es gleichzeitig blau lackiert. Das führt zu Fehlern. Rust blockiert solche Überschneidungen bereits zur Kompilierzeit."
    ),
    "ch19_4_lifetimes": (
        "Um diese Regeln zu prüfen, misst der Compiler die Lebensdauer, also die Lifetimes, von Referenzen. Durch "
        "Non-Lexical Lifetimes erfolgt dies zeilenbasiert und nicht mehr starr an geschweiften Klammern. Eine Referenz "
        "gilt im Speicher als beendet, sobald sie das letzte Mal im Code benutzt wird. Nacheinander stattfindende Ausleihen "
        "sind daher völlig legal. Überschneiden sich die Lebensdauern jedoch, da ein Schreiber aktiv ist während ein Leser "
        "zugreift, verweigert der Compiler den Build mit einem Fehler."
    ),
    "ch19_5_copy_vs_move": (
        "Das Zuweisen von Referenzen folgt unterschiedlichen Regeln. Unveränderliche Referenzen implementieren das Copy-Trait. "
        "Da sie Daten nur lesen, wird die Adresse einfach dupliziert und beide Zeiger bleiben gültig. Veränderliche Referenzen "
        "dagegen implementieren Copy nicht, sondern verwenden die Move-Semantik. Beim Zuweisen wandert das Schreibrecht komplett "
        "zur neuen Variable, und der alte Zeiger stirbt. Das garantiert, dass es immer nur einen aktiven Schreiber gibt. "
        "Es ist wie ein Stift: Den Stift zum Schreiben gibt es nur einmal, er muss weitergereicht werden."
    ),
    "ch19_6_dangling_references_outro": (
        "Ein weiterer schwerer Programmierfehler sind Dangling References, also hängende Zeiger auf bereits gelöschten Speicher. "
        "Rust verbietet dies vollständig. Wenn du eine Variable in einer Funktion erstellst, darfst du niemals eine Referenz "
        "darauf zurückgeben, da der Speicher am Funktionsende abgeräumt wird. Gib stattdessen immer das Eigentum selbst zurück. "
        "Damit haben wir die Grundlagen des Ausleihens gemeistert. Im nächsten Kapitel vertiefen wir unser Wissen über Slices. "
        "Vielen Dank fürs Zuschauen, und bis zum nächsten Mal!"
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
        
    with open("audio/durations_ch19.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch19.json")

if __name__ == "__main__":
    main()
