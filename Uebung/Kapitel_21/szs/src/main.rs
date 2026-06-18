fn main() {
    let mut zahl1ref = &42;
    // zahl1ref ist eine Variable, die eine Referenz auf zahl hält

    // Hier übergibst du eine veränderbare Referenz AUF die Variable zahl1ref
    testausgabe(&mut zahl1ref); 

    // Jetzt zeigt zahl1ref in main tatsächlich auf die 100!
    println!("zahl1ref in main zeigt jetzt auf: {}", zahl1ref); 
}

// Die Funktion erwartet nun eine veränderbare Referenz auf eine Referenz (&mut &i32)
fn testausgabe(thorsten: &mut &i32) {
    // Mit *thorsten (Dereferenzierung) greifst du auf die originale 
    // Variable zahl1ref in main zu und änderst, worauf sie zeigt.
    *thorsten = &100; 
    
}