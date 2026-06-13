import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch17_1_intro": (
        "Willkommen zum siebzehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion besprechen wir "
        "eines der wichtigsten Konzepte in Rust: die Speicherverwaltung und das Ownership-System. Jedes Programm "
        "benötigt RAM, um temporäre Daten abzuspeichern. In C und C++ muss man diesen Speicher manuell verwalten – das "
        "ist extrem schnell, aber auch sehr fehleranfällig. In Java oder Go übernimmt ein Garbage Collector das Aufräumen – das "
        "ist sicher, kostet aber Performance. Rust geht einen dritten Weg: Ownership. Der Compiler prüft "
        "den Code vor dem Start anhand strenger Eigentumsregeln und fügt die Speicherfreigabe ohne Performance-Overhead direkt ein."
    ),
    "ch17_2_stack_heap": (
        "Um das zu verstehen, müssen wir Stack und Heap vergleichen. Der Stack ist wie ein Tellerstapel: LIFO, also Last "
        "In First Out. Er speichert Daten mit fester Größe, wie Integers oder Booleans, extrem schnell. Der Heap dagegen "
        "ist wie ein großes Lagerhaus für flexible Daten, wie wachsende Texte. Der Computer sucht einen freien Platz "
        "auf dem Heap und speichert die Adresse als Zeiger auf dem Stack. Da der Heap-Zugriff langsamer ist, "
        "müssen wir ihn sauber verwalten. Rusts Ownership sorgt dafür, dass Heap-Daten exakt dann gelöscht werden, wenn "
        "ihr Besitzer auf dem Stack ungültig wird."
    ),
    "ch17_3_scopes_copy": (
        "In Rust bestimmen geschweifte Klammern die Lebensdauer von Variablen. Sobald eine Variable ihren Scope verlässt, "
        "wird ihr Speicher automatisch über die drop-Funktion bereinigt. Wenn mehrere Variablen im selben Scope liegen, "
        "räumt Rust sie in umgekehrter Reihenfolge ihrer Erstellung auf. Einfache Typen auf dem Stack, wie i32 oder bool, "
        "besitzen zudem den Copy-Trait. Weist du einen solchen Wert einer neuen Variablen zu, wird er automatisch dupliziert – "
        "beide Variablen bleiben unabhängig voneinander nutzbar. Bei Heap-Daten ist das jedoch anders."
    ),
    "ch17_4_strings": (
        "Schauen wir uns das am Beispiel der zwei String-Typen an. Ein String-Literal, also und-str, ist starr und fest in die Programmdatei "
        "eingebrannt. Der Typ String dagegen liegt auf dem Heap und kann verändert werden. Ein Heap-String besitzt auf dem Stack drei Werte: "
        "einen Pointer auf den Heap, die aktuelle Länge und die Kapazität. Hängen wir mit push_str Text an, kann es sein, "
        "dass die Kapazität überschritten wird. In diesem Fall sucht Rust im Hintergrund vollautomatisch einen neuen, größeren "
        "Platz auf dem Heap und zieht mit den Daten um, ohne dass du dich darum kümmern musst."
    ),
    "ch17_5_move_clone": (
        "Was passiert nun bei einer Zuweisung eines Heap-Strings? Um einen teuren Kopiervorgang auf dem Heap und Speicherfehler wie double-free "
        "zu vermeiden, kopiert Rust nur den Stack-Eintrag und erklärt die alte Variable sofort für ungültig. Das Eigentum zieht um – "
        "wir nennen das einen Move. Willst du stattdessen eine echte, tiefe Kopie der Heap-Daten erzwingen, musst du die clone-Methode "
        "aufrufen. Am Anfang ist es völlig okay, clone zu nutzen, um den Compiler glücklich zu machen, während du den Code zum Laufen bringst."
    ),
    "ch17_6_references": (
        "Um Moves und teure Klone zu vermeiden, nutzen wir Referenzen. Mit dem Kaufmanns-Und erstellst du einen Verweis auf einen Wert. "
        "Das Gegenstück dazu ist der Stern, der Dereferenzierungsoperator. Er folgt der Adresse zum echten Wert. Stell dir die "
        "Referenz wie die Adresse auf einem Zettel vor und den Dereferenzierungsoperator wie den Postboten, der zum Haus geht. Weil "
        "eine Referenz auf dem Stack liegt und winzig ist, kopiert sie sich bei Zuweisungen selbst. Die ursprüngliche Variable "
        "bleibt dabei vollkommen gültig."
    ),
    "ch17_7_functions_outro": (
        "Für Funktionen gelten dieselben Regeln. Übergibst du Heap-Daten ohne Referenz, findet ein Move statt – die Funktion "
        "frisst die Variable auf und löscht sie am Ende. Du kannst das Eigentum zwar per return zurückgeben oder den Parameter mit "
        "mut veränderbar machen, aber bei vielen Schritten führt das zu unübersichtlichem Eigentums-Ping-Pong. Wie uns Rust aus "
        "diesem Ping-Pong rettet, lernen wir im nächsten Kapitel über das Ausleihen, dem Borrowing. Vielen Dank fürs Zuschauen "
        "und bis zum nächsten Mal!"
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
        
    with open("audio/durations_ch17.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch17.json")

if __name__ == "__main__":
    main()
