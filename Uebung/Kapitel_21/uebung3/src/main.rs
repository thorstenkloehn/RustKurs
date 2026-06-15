fn dezimal_zu_binaer(mut zahl: u32) -> String {
    // Spezialfall für die Null, da die Schleife sonst leer ausgehen würde
    if zahl == 0 {
        return String::from("0");
    }

    let mut binaer_string = String::new();

    // Wir loopen, bis die Zahl komplett heruntergeteilt wurde
    while zahl > 0 {
        // 1. Modulo-Operation: Bestimmt das aktuelle Bit (0 oder 1)
        let bit = zahl % 2;
        
        // Das Bit wird in einen String konvertiert und VORNE angehängt.
        // Da push_str() standardmäßig hinten anhängt, tricksen wir hier kurz,
        // indem wir das Bit und den bisherigen String zusammenfügen.
        let bit_str = bit.to_string();
        binaer_string = bit_str + &binaer_string;

        // 2. Ganzzahlige Division: Verschiebt die Zahl für den nächsten Durchlauf
        zahl /= 2;
    }

    binaer_string
}

fn main() {
    let test_zahl = 42;
    let ergebnis = dezimal_zu_binaer(test_zahl);
    
    println!("Die Dezimalzahl {} ist binär: {}", test_zahl, ergebnis);
    // Erwartete Ausgabe: 101010
}