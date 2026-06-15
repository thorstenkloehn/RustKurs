# Glossar: Exakte Begriffsdefinitionen für das Rust-Lehrbuch

Dieses Glossar definiert die zentralen Begriffe und Konzepte der Programmiersprache Rust. Autoren und KI-Agenten müssen sich bei der Erklärung von Konzepten strikt an diese Terminologie halten.

---

## Kernkonzepte der Speicherverwaltung

### Ownership (Besitzrecht)
Das fundamentale Speicherverwaltungsmodell von Rust. 
*   **Regel 1**: Jeder Wert in Rust hat einen Besitzer (eine Variable).
*   **Regel 2**: Es kann immer nur einen Besitzer gleichzeitig geben.
*   **Regel 3**: Wenn der Besitzer den Gültigkeitsbereich (Scope) verlässt, wird der Wert und sein Speicher automatisch freigegeben (RAII/Drop).

### Borrowing (Ausleihen)
Der Vorgang, bei dem eine Variable Zugriff auf einen Wert erhält, ohne dessen Eigentümer (Owner) zu werden. Dies geschieht über Referenzen (`&` oder `&mut`).

### Borrow Checker
Eine Komponente des Rust-Compilers, die zur Kompilierzeit prüft, ob alle Referenzen und Ausleihen gültig sind. Der Borrow Checker stellt sicher, dass:
*   Referenzen niemals länger leben als der Wert, auf den sie zeigen (Verhinderung von Dangling Pointers).
*   Es entweder beliebig viele unveränderliche Referenzen (`&T`) ODER genau eine veränderliche Referenz (`&mut T`) auf einen Wert zur gleichen Zeit gibt (Verhinderung von Data Races).

### Lifetimes (Lebensdauern)
Vom Compiler überprüfte Parameter, die angeben, wie lange eine Referenz auf einen Wert gültig ist. Lifetimes werden meist implizit vom Compiler ermittelt (Lifetime Elision Rules), müssen jedoch bei komplexeren Strukturen oder Signaturen explizit deklariert werden (z. B. `'a`).

---

## Datentypen und Strukturen

### Shadowing (Variablen-Überschattung)
Das Deklarieren einer neuen Variable mit demselben Namen wie eine bereits existierende Variable im selben oder einem übergeordneten Scope. Die ursprüngliche Variable wird dadurch überschattet und ist im aktuellen Scope nicht mehr direkt ansprechbar. Dies erlaubt es auch, den Datentyp einer Variable unter Beibehaltung des Namens zu ändern.

### Slice
Eine Ansicht auf eine zusammenhängende Sequenz von Elementen in einer Kollektion (z. B. einem Array oder einem Vektor). Slices werden als Referenz übergeben (z. B. `&[T]` für Arrays/Vektoren oder `&str` für Zeichenketten) und besitzen eine zur Laufzeit bekannte Länge, aber kein Ownership über die Daten.

### Vector (`Vec<T>`)
Ein dynamisch wachsendes, auf dem Heap allokiertes Array. Im Gegensatz zu statischen Arrays (`[T; N]`) kann ein Vektor zur Laufzeit vergrößert oder verkleinert werden.

### Reference (Referenz)
Ein Zeiger auf einen Wert im Speicher, der den Zugriff auf diesen Wert erlaubt, ohne die Eigentumsrechte zu übertragen. Referenzen sind in Rust standardmäßig unveränderlich.
