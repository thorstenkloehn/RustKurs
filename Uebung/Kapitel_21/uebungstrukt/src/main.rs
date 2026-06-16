struct Person {
    vorname : String,
    nachname : String,

}


fn main() {
    let person = Person {
        vorname: String::from("Thorsten"),
        nachname: String::from("Klöhn"),
    };
    println!("{} {}",person.vorname,person.nachname);
    let person1 = person;
    println!("{} {}",person1.vorname,person1.nachname);
}
