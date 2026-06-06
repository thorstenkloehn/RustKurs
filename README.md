# 🦀 Rust-Videokurs für Anfänger

Dieses Projekt ist eine automatisierte Pipeline zur Erstellung eines interaktiven, deutschsprachigen Videokurses über die Programmiersprache **Rust**. Mithilfe von moderner mathematischer Animation und Text-to-Speech (TTS) werden verständliche Video-Lektionen für Einsteiger generiert.

---

## 🛠️ Genutzte Software-Technologien

- **Video-Animation**: [Manim (Community Edition)](https://www.manim.community/) zur Erstellung dynamischer visueller Szenen und Folien.
- **Sprachsynthese (TTS)**: [Kokoro TTS](https://github.com/remsky/kokoro-onnx) (via `kokoro-onnx`) mit dem deutschen Sprechermodell `martin` für die Audiospuren.
- **Audio- & Datenverarbeitung**: `soundfile`, `numpy` und Standard-Python-Bibliotheken zur Generierung und Synchronisation von Audio- und Videodaten.

---

## 📚 Kurskapitel & Inhalte

Der Kurs ist derzeit in vier Kapitel unterteilt, deren detaillierte Skripte und Konzepte in folgenden Markdown-Dateien zu finden sind:

1. **[Kapitel 1: Was ist Rust?](file:///home/thorsten/RustKurs/1.md)**
   - Einführung in Rust als Systemprogrammiersprache.
   - Vergleich mit C/C++ und Python (Geschwindigkeit vs. Speichersicherheit).
   - Einsatzgebiete im IT-Sektor (z. B. Android, Windows-Kernel, AWS, WebAssembly).
   - Vor- und Nachteile für Anfänger (Compiler-Meldungen, Cargo vs. Lernkurve).
2. **[Kapitel 2: Installation & Einrichtung](file:///home/thorsten/RustKurs/2.md)**
   - Voraussetzungen für Ubuntu (`build-essential`).
   - Einrichtung von Visual Studio Code und der Extension `rust-analyzer`.
   - Installation der Rust-Toolchain via `rustup`.
3. **[Kapitel 3: KI-Assistenten in der Entwicklung](file:///home/thorsten/RustKurs/3.md)**
   - Rolle von KI-Tools im Entwickleralltag (Cline, Gemini Code Assist, GitHub Copilot).
   - Warum das eigenständige Erlernen der Sprache trotz KI-Unterstützung essenziell ist.
4. **[Kapitel 4: Audio-Nachbearbeitung & Szenenanalyse](file:///home/thorsten/RustKurs/4.md)**
   - Erklärung und Analyse eines Demovideos (`Video/4.mp4`).
   - Rauschfilterung der Tonspur und Vertonung durch den Sprecher.
5. **[Kapitel 5: Variablen & Konstanten](file:///home/thorsten/RustKurs/5.md)**
   - Variablen als Boxen-Metapher im Arbeitsspeicher.
   - Warnungen (unused variable) vs. kritische Fehler im Editor.
   - Das `println!` Makro (Direkt-Interpolation vs. Argumentplatzhalter) und Positionsargumente.
   - Stummschalten von Compiler-Warnungen mit dem Unterstrich `_`.
   - Mutability (Veränderlichkeit) mit `let mut` vs. standardmäßig unveränderlichen Variablen.
   - Fehleranalyse mit `rustc --explain`.
   - Variablen-Shadowing (Überschattung) und Scopes (Gültigkeitsbereiche) mit den 3 goldenen Scope-Regeln.
   - Konstanten (`const`) im Vergleich zu Variablen (`let`).

---

## 📁 Projektstruktur

```text
RustKurs/
├── 1.md, 2.md, ...        # Kapitel-Konzepte und Skript-Vorgaben
├── AGENTS.md              # Projektregeln und Kapitelübersicht
├── generate_audio_*.py    # Python-Skripte zur Generierung der TTS-Sprachspuren
├── video_scene_*.py       # Python-Skripte zur Erzeugung der Manim-Videoszenen
├── audio/                 # Generierte WAV-Audiodateien (Sprecher-Stimme)
│   ├── intro.wav
│   └── ...
├── Video/                 # Ordner für Rohmaterialien (z.B. Video/4.mp4)
├── 1.mp4, 2.mp4, ...      # Die fertig gerenderten Videodateien der Kapitel
└── README.md              # Dieses Dokument
```

---

## 🚀 Inbetriebnahme & Ausführung

### 1. Voraussetzungen installieren
Stelle sicher, dass du Python, Manim (sowie dessen Systemabhängigkeiten wie FFmpeg) und das Kokoro-Modell eingerichtet hast.

```bash
pip install manim kokoro-onnx soundfile numpy
```

> [!NOTE]
> Die TTS-Generierung erfordert die Pfade zu den ONNX-Modelldateien (`kokoro-martin.onnx` und `voices-martin.npz`). Diese sind standardmäßig in den Skripten auf den lokalen Pfad `/home/thorsten/kurs/checkpoints/kokoro-german/` konfiguriert.

### 2. Audio generieren
Führe die Audioskripte aus, um die Sprecherdateien zu erzeugen:
```bash
python generate_audio.py
python generate_audio_ch2.py
...
```

### 3. Videos rendern
Nutze Manim, um die Szenen zu rendern und mit dem Audio zu mergen:
```bash
manim -pql video_scene.py RustIntroVideo
```
*(Option `-pql` rendert das Video in niedriger Qualität für eine schnelle Vorschau).*
