import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch20_1_intro": (
        "Willkommen zum zwanzigsten Kapitel unseres Rust-Videokurses. Heute widmen wir uns den Referenzen und dem Konzept des Ausleihens, dem Borrowing. In den vorherigen Kapiteln haben wir gelernt, dass Rusts Speicherverwaltung auf dem Ownership-System beruht. Übergibt man jedoch eine Variable an eine Funktion, verliert man standardmäßig das Eigentum daran. Um den Wert danach weiterzuverwenden, müsste die Funktion ihn umständlich zurückgeben. Das führt schnell zu unleserlichem Code. Rust bietet die perfekte Lösung: Wir leihen uns die Daten nur aus. Dies geschieht mit Referenzen, gekennzeichnet durch das kaufmännische Und-Symbol. Sie erlauben den Zugriff auf Werte, ohne den Besitzer zu wechseln."
    ),
    "ch20_2_references_concept": (
        "Lass uns einen Blick auf die Hardware-Ebene werfen. Der Arbeitsspeicher ist eine Kette von nummerierten Zellen mit Speicheradressen. Eine Referenz in Rust ist eine Variable auf dem Stack, die genau so eine Speicheradresse speichert. Auf einer modernen 64-Bit-CPU belegt eine Referenz immer exakt acht Byte. Nutzen wir eine Referenz, springt der Prozessor über diese Adresse direkt zu den eigentlichen Daten. Da wir beim Ausleihen nur diese acht Byte kopieren, ist der Vorgang extrem schnell. Weder Heap-Daten noch Verwaltungsdaten müssen dupliziert werden. Deshalb erreicht Rust trotz maximaler Sicherheit die Performance von C und C-Plus-Plus."
    ),
    "ch20_3_immutable_borrowing": (
        "Wir unterscheiden in Rust zwei Arten von Ausleihen. Die erste ist die unveränderliche Referenz, deklariert mit einem einfachen kaufmännischen Und. Sie erlaubt das reine Lesen von Daten. Da Leseoperationen die Daten nicht verändern, gibt es keine Sicherheitsrisiken. Deshalb dürfen beliebig viele unveränderliche Referenzen auf denselben Wert gleichzeitig aktiv sein. Das ist wie bei einem Buch in einer Bibliothek: Beliebig viele Besucher dürfen gleichzeitig lesen, da niemand hineinschreiben darf. Versucht man jedoch, über eine unveränderliche Referenz Daten zu verändern, bricht der Compiler den Build sofort mit einer Fehlermeldung ab."
    ),
    "ch20_4_mutable_borrowing": (
        "Die zweite Art ist die veränderliche Referenz, gekennzeichnet durch die Syntax und-mut. Sie erlaubt es, Daten direkt an ihrer Speicheradresse zu verändern. Dafür muss die Variable mit let-mut deklariert sein. Hier gilt die strengste Regel von Rust: Du darfst zu jedem Zeitpunkt nur eine einzige aktive veränderliche Referenz auf ein Datenelement besitzen. Gibt es einen Schreiber, sind keine weiteren Leser oder Schreiber erlaubt. Wie bei einem exklusiven Handwerker darf nur eine Person am Werkstück arbeiten. Rust erzwingt diese Exklusivität absolut zuverlässig zur Kompilierzeit."
    ),
    "ch20_5_data_races": (
        "Warum ist diese Exklusivität so wichtig? Sie verhindert Datenkonflikte, sogenannte Data Races. Ein Datenkonflikt tritt auf, wenn zwei Zeiger gleichzeitig auf dieselbe Speicheradresse zugreifen, mindestens einer davon schreibt und es keine Synchronisation gibt. Solche Konflikte führen in C und C-Plus-Plus zu schwer auffindbaren Bugs, da Speicherbereiche korrumpiert werden. Der Borrow Checker von Rust analysiert alle Ausleihen statisch beim Kompilieren. Da garantiert nur ein Schreiber aktiv sein kann, sind Datenkonflikte zur Laufzeit unmöglich. Das ist Speichersicherheit ohne Performance-Verlust."
    ),
    "ch20_6_mixing_borrows": (
        "Ein wichtiger Aspekt ist das Mischen von Lese- und Schreibzugriffen. Rust verbietet eine veränderliche Referenz, solange noch aktive Lese-Referenzen existieren. Denn Leser erwarten, dass sich Daten nicht plötzlich im Hintergrund ändern. Dank Non-Lexical Lifetimes wird diese Regel sehr intelligent geprüft: Die Lebensdauer einer Referenz endet exakt nach ihrer letzten Verwendung im Code, nicht erst am Blockende. Sobald ein Leser das letzte Mal genutzt wurde, erlischt die Ausleihe. In der nächsten Zeile darfst du daher problemlos eine veränderliche Referenz erstellen."
    ),
    "ch20_7_dangling_references": (
        "Zusätzlich schützt uns Rust vor Dangling References – also hängenden Zeigern auf bereits freigegebenen Speicher. Gibt eine Funktion eine Referenz auf eine lokale Variable zurück, würde diese ins Leere zeigen, da lokale Variablen am Funktionsende gelöscht werden. Der Rust-Compiler erkennt dies sofort und gibt den Fehler E0515 aus. Um das zu lösen, musst du einfach das Eigentum selbst zurückgeben. Die Daten werden per Move sicher an den Aufrufer übergeben, und der Speicher bleibt vollständig gültig."
    ),
    "ch20_8_conclusion_rules": (
        "Fassen wir die zwei goldenen Regeln zusammen. Erstens: Zu jedem Zeitpunkt darfst du entweder beliebig viele unveränderliche Referenzen haben, oder genau eine veränderliche Referenz – niemals beides gleichzeitig. Zweitens: Eine Referenz muss immer auf gültigen Speicher verweisen und darf niemals länger leben als ihr Besitzer. Mit diesen Prinzipien hast du das Fundament von Rust verstanden. Der Compiler ist dein bester Verbündeter. Im nächsten Kapitel fassen wir die Grundlagen zusammen. Vielen Dank fürs Zuschauen, viel Erfolg bei den Challenges und bis zum nächsten Mal!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    # We want total audio duration + 1s transition padding between 8 segments (7 transitions)
    # to be very close to 290 seconds, so with natural pauses it's exactly 300 seconds (5:00).
    # Let's test generating at speed=1.12 first.
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
    
    with open("audio/durations_ch20.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch20.json")

if __name__ == "__main__":
    main()
