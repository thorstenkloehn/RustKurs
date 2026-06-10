import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch12_1_intro": (
        "Willkommen zum zwölften Kapitel unseres Rust-Kurses für Anfänger. Heute befassen wir uns ausführlich mit den Operatoren in Rust. "
        "Operatoren sind spezielle Symbole, mit denen wir dem Compiler mitteilen, arithmetische, logische oder speicherbezogene Aktionen auszuführen. "
        "Da Rust eine extrem sichere und performante Programmiersprache ist, verhalten sich manche Operatoren hier anders, als du es vielleicht von "
        "C, C++ oder Java gewohnt bist. Der Compiler achtet streng darauf, dass Operatoren nur mit kompatiblen Typen verwendet werden. "
        "In diesem Video werden wir uns Schritt für Schritt durch alle Kategorien arbeiten und genau zeigen, was im Speicher passiert."
    ),
    "ch12_2_arithmetic_comparison": (
        "Schauen wir uns zuerst die arithmetischen Operatoren an. Dazu gehören Plus für die Addition, Minus für die Subtraktion, das Sternchen für die "
        "Multiplikation, der Schrägstrich für die Division und das Prozentzeichen für den Modulo-Operator. Modulo berechnet den verbleibenden Rest "
        "einer Ganzzahldivision. Bei der Division gibt es eine wichtige Besonderheit: Wenn du zwei Ganzzahlen teilst, wie zum Beispiel zehn geteilt durch drei, "
        "schneidet Rust alle Nachkommastellen ab und liefert das Ergebnis drei. Um eine Fließkommadivision mit Nachkommastellen durchzuführen, müssen beide Zahlen "
        "als Fließkommazahlen deklariert sein, also zehn Komma null geteilt durch drei Komma null. "
        "Als nächstes kommen die Vergleichsoperatoren. Mit zwei Gleichheitszeichen prüfen wir auf Gleichheit, mit Ausrufezeichen und Gleichheitszeichen auf Ungleichheit. "
        "Zudem haben wir kleiner als, größer als, kleiner gleich und größer gleich. Das Ergebnis eines Vergleichs ist immer ein boolescher Wert, also entweder "
        "true oder false. Ganz wichtig in Rust: Du kannst nur Werte vergleichen, die den exakt gleichen Datentyp besitzen. Ein Vergleich zwischen einer "
        "Ganzzahl und einer Fließkommazahl führt sofort zu einem Compilerfehler."
    ),
    "ch12_3_logical_bitwise": (
        "Als nächstes betrachten wir die logischen Operatoren. Das doppelte Kaufmanns-Und steht für das logische UND, bei dem beide Bedingungen wahr sein müssen. "
        "Die zwei senkrechten Striche stehen für das logische ODER, bei dem mindestens eine Bedingung wahr sein muss. Das Ausrufezeichen invertiert einen Wahrheitswert. "
        "Rust verwendet hierbei die sogenannte Kurzschluss-Auswertung, auch bekannt als Short-Circuit-Evaluation. Wenn das Gesamtergebnis bereits durch die linke "
        "Bedingung feststeht, wertet Rust die rechte Seite gar nicht erst aus. Das spart Rechenzeit und verhindert Fehler, beispielsweise wenn die rechte Seite "
        "auf eine ungültige Speicheradresse zugreifen würde. "
        "Bitweise Operatoren arbeiten direkt auf den einzelnen Bits einer Ganzzahl. Hier nutzen wir das einfache Kaufmanns-Und für das bitweise UND, den einzelnen "
        "senkrechten Strich für das bitweise ODER und das Zirkumflex für das bitweise Exklusiv-Oder. Das Ausrufezeichen invertiert alle Bits einer Zahl. "
        "Mit den doppelten Pfeilen verschieben wir Bits. Ein Links-Shift um eins verschiebt alle Bits nach links, was mathematisch einer Multiplikation mit zwei entspricht. "
        "Ein Rechts-Shift verschiebt die Bits nach rechts und entspricht einer Division durch zwei."
    ),
    "ch12_4_assignment_references": (
        "Zuweisungsoperatoren schreiben Werte in Variablen. Neben dem einfachen Gleichheitszeichen gibt es zusammengesetzte Zuweisungen wie plus-gleich, "
        "minus-gleich oder mal-gleich. Sie führen die mathematische Operation aus und weisen das Ergebnis direkt der Variablen zu. Eine wichtige Besonderheit "
        "in Rust ist, dass es keine Post- oder Prä-Inkrement-Operatoren wie plus-plus oder minus-minus gibt. Du musst stattdessen immer plus-gleich eins schreiben. "
        "Das verhindert uneindeutigen Code. "
        "Da Rust ein striktes Ownership-System besitzt, sind die Referenz-Operatoren von zentraler Bedeutung. Mit dem einfachen Kaufmanns-Und deklarieren wir "
        "eine unveränderliche Referenz, die es uns erlaubt, einen Wert sicher auszuleihen, ohne ihn zu kopieren. Mit Und-Mut erstellen wir eine veränderliche "
        "Referenz, über die wir den ausgeliehenen Wert verändern können. Der Stern dient als Dereferenzierungs-Operator. Er ermöglicht es uns, dem Zeiger im "
        "Speicher zu folgen, um den echten Wert hinter der Referenz zu lesen oder zu überschreiben. Das zeigt unser Speichermodell gleich deutlich."
    ),
    "ch12_5_casting_error_ranges": (
        "Kommen wir nun zu den Spezialoperatoren für Typumwandlung und Fehlerbehandlung. Da Rust keine automatische Typkonvertierung durchführt, müssen wir "
        "den Operator as verwenden, um beispielsweise eine Ganzzahl explizit in eine Fließkommazahl umzuwandeln. "
        "Ein extrem mächtiges Werkzeug in Rust ist der Fragezeichen-Operator für die Fehlerweiterleitung. Er wird an Funktionen angehängt, die ein Result "
        "oder Option zurückgeben. Wenn die Operation erfolgreich ist, entpackt das Fragezeichen den darin enthaltenen Erfolgswert. Tritt jedoch ein Fehler auf, "
        "bricht die Funktion sofort ab und gibt den Fehler direkt an den Aufrufer zurück. Das spart uns lange Match-Anweisungen im Code. "
        "Zuletzt gibt es die Range-Operatoren. Punkt-Punkt definiert einen exklusiven Bereich, bei dem der Endwert nicht mitgezählt wird. Punkt-Punkt-Gleich "
        "definiert einen inklusiven Bereich. Diese Bereiche sind besonders in For-Schleifen oder beim Erzeugen von Array-Slices nützlich."
    ),
    "ch12_6_outro": (
        "Zusammenfassend haben wir in diesem Kapitel das gesamte Spektrum der Rust-Operatoren kennengelernt. Wir haben arithmetische Berechnungen durchgeführt, "
        "logische Ausdrücke ausgewertet, Bits manipuliert, Referenzen verfolgt, Typen explizit konvertiert und Fehler elegant weitergeleitet. Dieses tiefe "
        "Verständnis ist essenziell für die sichere Programmierung in Rust. Vielen Dank fürs Zuschauen, arbeite die Beispiele in Ruhe durch und bis zum nächsten Kapitel!"
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
        
    with open("audio/durations_ch12.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch12.json")

if __name__ == "__main__":
    main()
