## EVA-Prinzip
### Eingabe(Input)

* StartWert = 1
* EndWert = 10

Das Ziel ist also ein starres Raster von 10 Zeilen mal 10 Spalten.
### Verarbeitung

Die äußere Schleife (Zeilen-Zähler): Wir stellen uns virtuell in die Zeile 1.
Die innere Schleife (Spalten-Zähler): Während wir in Zeile 1 stehen bleiben, wandert ein zweiter Zeiger von Spalte 1 bis Spalte 10 durch.
Die Berechnung: Bei jedem einzelnen Schritt der inneren Schleife wird gerechnet:$$\text{Aktuelle Zeile} \times \text{Aktuelle Spalte} = \text{Ergebnis}$$(In Zeile 1 wäre das: $1 \times 1$, dann $1 \times 2$, dann $1 \times 3$, bis $1 \times 10$)

Der Wechsel: Erst wenn die innere Schleife bei 10 angekommen ist, springt die äußere Schleife weiter in Zeile 2. Das Spiel beginnt von vorn ($2 \times 1, 2 \times 2 \dots$).

3. A (Ausgabe / Output)
* Die Ausgabe passiert direkt während der Verarbeitung, Zeile für Zeile, und nutzt zwei wichtige Formatierungs-Regeln:

* Das "Nebeneinander-Drucken" (print!): Jedes berechnete Ergebnis einer Reihe wird ohne Zeilenumbruch direkt rechts neben das vorherige Ergebnis geschrieben.

* Der Platzhalter-Trick: Damit die Zahlen nicht als ein langer Brei kleben (12345678910), sagen wir der Konsole: "Egal wie lang die Zahl ist, reserviere für sie immer genau 4 Zeichen Platz!" Dadurch rutschen einstellige Zahlen (wie 4) und dreistellige Zahlen (wie 100) perfekt bündig untereinander.

* Der Zeilenumbruch: Sobald die innere Schleife die Spalte 10 gedruckt hat, befehlen wir der Konsole einen harten Zeilenumbruch. Erst dadurch springt der Cursor in die nächste Zeile, und die Tabelle wird quadratisch.

:::Mermaid
graph TD
    Start([Start]) --> InitAussen[Aussen = 1]
    
    %% Äußere Schleife
    InitAussen --> BedAussen{Aussen <= 10?}
    
    %% Innere Schleife Initialisierung (wird bei jedem äußeren Durchlauf zurückgesetzt)
    BedAussen -- Ja --> InitInnen[Innen = 1* Aussen]
    InitInnen --> BedInnen{Innen <= 10?}
    
    %% Inhalt der inneren Schleife
    BedInnen -- Ja --> Aktion[Aktion ausführen <br> z.B. Aussen * Innen]
    Aktion --> IncInnen[Innen = Innen * Aussen]
    IncInnen --> BedInnen
    
    %% Innere Schleife fertig -> Äußeren Zähler erhöhen
    BedInnen -- Nein --> IncAussen[Aussen = Aussen  1]
    IncAussen --> BedAussen
    
    %% Äußere Schleife fertig -> Ende
    BedAussen -- Nein --> Ende([Ende])
:::
```
 [ START ]
    │
    ▼
[EINGABE]: Setze Rastergröße auf 10
    │
    ▼
[ÄUßERE SCHLEIFE]: Starte bei Zeile 1 (bis 10)
    │
    ├──► [INNERE SCHLEIFE]: Starte bei Spalte 1 (bis 10)
    │        │
    │        ▼
    │    [VERARBEITUNG]: Berechne (Zeile * Spalte)
    │        │
    │        ▼
    │    [AUSGABE]: Drucke Ergebnis mit 4 Zeichen Abstand (bleibe in der Zeile)
    │        │
    │        └─ (Nächste Spalte, bis 10 erreicht ist)
    │
    ▼
[AUSGABE]: Mache einen Zeilenumbruch!
    │
    └─ (Nächste Zeile, bis Zeile 10 erreicht ist)
    │
    ▼
 [ ENDE ]
