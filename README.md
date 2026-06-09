# 🎬 Media- & Grafik-Tools Installationsanleitung (Linux/Ubuntu)

Dieses Dokument beschreibt die Installation und Konfiguration von **VLC Media Player**, **OBS Studio**, **Kdenlive**, **Inkscape**, **GIMP**, **Gromit-MPX**, **Flameshot**, **Glaxnimate**, **OpenBoard**, **Xournal++**, **Audacity**, **mdBook** und **Blender 3D** auf einem Ubuntu- bzw. Linux-System. Diese Tools bilden die Grundlage für die Wiedergabe, Aufnahme, den Schnitt, die grafische Gestaltung, 3D-Modellierung, die Live-Präsentation, handschriftliche Erklärungen sowie das Audio-Mastering und das Hosten deines Rust-Videokurses.

---

## 🍊 1. VLC Media Player

VLC ist ein freier und quelloffener, plattformübergreifender Multimedia-Player, der fast alle Audio- und Videodateiformate abspielen kann.

### 📊 VLC Installationsmethoden im Vergleich

| Methode | Paketquelle | Update-Frequenz | Startzeit | Sandbox / Sicherheit |
| :--- | :--- | :--- | :--- | :--- |
| **APT** (Empfohlen) | Offizielle Ubuntu-Quellen | Stabil | Sehr schnell | Keine Sandbox (voller Systemzugriff) |
| **Snap** | Canonical Snap Store | Sehr aktuell | Mittel | Sandboxed (sicher, aber isoliert) |
| **Flatpak** | Flathub | Sehr aktuell | Mittel | Sandboxed (sicher, aber isoliert) |

### 🛠️ VLC Schritt-für-Schritt-Installation

#### Methode A: Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y vlc
```
> [!TIP]
> Um sicherzustellen, dass alle gängigen Audio- und Videocodecs vorhanden sind, installiere die Restricted Extras mit:
> `sudo apt install -y ubuntu-restricted-extras`

#### Methode B: Installation über Snap
```bash
sudo snap install vlc
```

#### Methode C: Installation über Flatpak
```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.videolan.VLC
```

---

## 🎥 2. OBS Studio

OBS (Open Broadcaster Software) Studio ist eine freie Software zur Videoaufnahme und Live-Streaming. Sie eignet sich hervorragend, um Bildschirmaufnahmen oder Vorlesungen aufzunehmen.

### 📊 OBS Installationsmethoden im Vergleich

| Methode | Paketquelle | Plugin-Kompatibilität | Leistung | Systemintegration |
| :--- | :--- | :--- | :--- | :--- |
| **APT (PPA)** (Empfohlen) | Offizielles OBS PPA | Sehr gut (einfach zu erweitern) | Optimal | Direkt im System (voller Zugriff) |
| **Flatpak** | Flathub | Eingeschränkt (via Flatpak-Addons) | Gut | Sandboxed (Sicherheitsvorteile) |
| **Snap** | Canonical Snap Store | Eingeschränkt | Gut | Sandboxed |

### 🛠️ OBS Schritt-für-Schritt-Installation

#### Methode A: Installation über APT (via offiziellem PPA - Empfohlen)
1. **Abhängigkeiten (FFmpeg) und PPA hinzufügen:**
   ```bash
   sudo apt update
   sudo apt install -y ffmpeg software-properties-common
   sudo add-apt-repository ppa:obsproject/obs-studio
   ```
2. **Paketquellen aktualisieren und OBS installieren:**
   ```bash
   sudo apt update
   sudo apt install -y obs-studio
   ```

#### Methode B: Installation über Flatpak
```bash
flatpak install flathub com.obsproject.Studio
```

#### Methode C: Installation über Snap
```bash
sudo snap install obs-studio
```

#### 📸 Virtuelle Kamera aktivieren (Virtual Camera)
* Unter Ubuntu/Linux benötigst du dafür das Kernel-Modul `v4l2loopback`:
  ```bash
  sudo apt install -y v4l2loopback-dkms
  ```

---

## 🎬 3. Kdenlive & Glaxnimate

Kdenlive ist ein leistungsstarker, freier Videoschnitt-Editor für Linux. Er eignet sich perfekt, um die mit Manim gerenderten Einzelszenen zusammenzuschneiden, Tonspuren anzupassen und Effekte oder Blenden einzufügen.

### 📊 Kdenlive Installationsmethoden im Vergleich

| Methode | Paketquelle | Rendertempo | Stabilität / Abhängigkeiten |
| :--- | :--- | :--- | :--- |
| **APT** (Empfohlen) | Offizielle Ubuntu-Quellen | Sehr schnell | Sehr gut integriert |
| **Flatpak** | Flathub | Schnell | Isoliert, bringt alle Bibliotheken mit |
| **Snap** | Canonical Snap Store | Schnell | Isoliert |

### 🛠️ Kdenlive Schritt-für-Schritt-Installation

#### Methode A: Installation über APT (Empfohlen)
```bash
sudo apt update
sudo apt install -y kdenlive
```

### 🎞️ Vektor-Animationen über Videos zeichnen (Glaxnimate)

Um 2D-Vektor-Animationen (wie wandernde Pfeile, Einkreisungen oder Hervorhebungen) direkt über deine Videos in Kdenlive zu zeichnen, kannst du **Glaxnimate** als Erweiterung nutzen.

#### 1. Glaxnimate via Snap installieren:
```bash
sudo snap install glaxnimate
```

#### 2. Kdenlive-Integration konfigurieren:
1. Öffne Kdenlive und gehe im Menü auf **Einstellungen** > **Kdenlive einrichten...** > **Umgebung**.
2. Scrolle ganz nach unten zum Eintrag **Pfad zu Glaxnimate**.
3. Trage dort den folgenden Pfad ein: `/snap/bin/glaxnimate`
4. Klicke auf **Anwenden** und **OK**.

---

## 🎨 4. Grafik-Software (Inkscape & GIMP)

Für die Erstellung von visuellen Assets, Diagrammen und Vorschaubildern (Thumbnails) für deinen Videokurs sind folgende Grafikprogramme sehr zu empfehlen:

### 📊 Grafik-Tools im Überblick

| Software | Typ | Verwendungszweck im Videokurs |
| :--- | :--- | :--- |
| **Inkscape** (Empfohlen) | Vektorgrafik (SVG) | Erstellung von Diagrammen und Logos, die in Manim direkt als Vektor-Objekt (`SVGMobject`) animiert werden können. |
| **GIMP** | Pixelgrafik (Raster) | Erstellung von YouTube- und Kurs-Thumbnails, Zuschneiden von Screenshots und Bearbeiten von PNG/JPG-Bilddateien. |

### 🛠️ Grafik-Software Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y inkscape gimp
```

---

## 🖌️ 5. Bildschirm-Präsentation & Annotation (Gromit-MPX)

Wenn du deinen Bildschirm mit OBS Studio aufnimmst und live Code erklärst, ist es extrem hilfreich, direkt auf dem Bildschirm zeichnen zu können, um wichtige Zeilen hervorzuheben.

### 📊 Gromit-MPX Übersicht
* **Was es ist:** Ein Desktop-Annotationstool, mit dem du per Tastendruck auf dem gesamten Bildschirm (über allen Fenstern wie VS Code oder dem Browser) zeichnen kannst.
* **Vorteile:** 
  - Funktioniert nahtlos während der OBS-Aufnahme.
  - Unterstützt verschiedene Farben (Rot, Blau, Gelb, Grün), Linienstärken und Radiergummis.
  - Kann per Hotkey (Standard: `F9`) ein- und ausgeschaltet werden.

### 🛠️ Gromit-MPX Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y gromit-mpx
```

### 🚀 Verwendung & Hotkeys
1. Starte Gromit-MPX über das Anwendungsmenü oder das Terminal (`gromit-mpx`).
2. **Zeichnen aktivieren/deaktivieren:** Drücke die Taste **`F9`** (der Cursor verwandelt sich in ein Fadenkreuz).
3. **Zeichnen:** Halte die linke Maustaste gedrückt und zeichne.
4. **Radieren:** Halte die rechte Maustaste gedrückt oder nutze `Umschalt` + linke Maustaste.
5. **Alles löschen:** Drücke **`Mittelklick`** oder **`Strg + F9`** (je nach Konfiguration), um alle Zeichnungen zu leeren.

---

## 📸 6. Screenshot-Tools (Flameshot)

Für die Erstellung von Dokumentationen, Kursunterlagen oder Präsentationen ist ein gutes Screenshot-Tool unerlässlich.

### 📊 Flameshot Übersicht
* **Was es ist:** Ein hochentwickeltes Open-Source-Screenshot-Tool, mit dem du direkt beim Aufnehmen Markierungen vornehmen kannst.
* **Vorteile:**
  - **Zeichenwerkzeuge:** Pfeile, Linien, Kreise, Rechtecke, Freihandzeichnen.
  - **Annotation:** Textwerkzeuge und Nummerierungen (Zähler) für Schritte.
  - **Sicherheit:** Unschärfe-Werkzeug (Blur) zum Verpixeln sensibler Bildbereiche (z. B. Passwörter).
  - **Ziele:** Direktes Kopieren in die Zwischenablage oder Speichern als Datei.

### 🛠️ Flameshot Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y flameshot
```

### 🚀 Verwendung & Shortcuts
1. Starte Flameshot über das Terminal: `flameshot gui`.
2. **Tastenkombination einrichten (Empfohlen):**
   Um Flameshot auf die Taste `Druck` (PrintScreen) zu legen, gehe unter Ubuntu auf:
   * **Einstellungen** > **Tastatur** > **Tastaturkürzel anzeigen und anpassen** > **Eigene Kürzel**.
   * Füge ein neues Kürzel hinzu:
     - **Name:** Flameshot
     - **Befehl:** `flameshot gui`
     - **Tastenkombination:** `Druck` (PrintScreen) festlegen.

---

## 📝 7. Whiteboard- & Notizen-Software (OpenBoard & Xournal++)

Für handschriftliche Erklärungen, Zeichnungen mit einem Grafiktablett oder interaktive Tafelbilder während deines Videokurses eignen sich OpenBoard und Xournal++ perfekt.

### 📊 Whiteboard-Tools im Überblick

| Software | Typ | Verwendungszweck |
| :--- | :--- | :--- |
| **OpenBoard** | Interaktives Whiteboard | Ideal für freies Zeichnen, Tafelbilder und Live-Erklärungen (lässt sich perfekt mit OBS aufnehmen). |
| **Xournal++** | Handschriften-Notizbuch | Perfekt für Notizen, mathematische Skizzen und PDF-Annotationen mit präziser Stift-Unterstützung. |

### 🛠️ Whiteboard-Software Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
Beide Programme können direkt über den Standard-Paketmanager von Ubuntu installiert werden:
```bash
sudo apt update
sudo apt install -y openboard xournalpp
```

### 🚀 Verwendungstipps
* **OpenBoard:** Bietet eine integrierte "Podcast"-Funktion, mit der du deine Whiteboard-Aktivitäten direkt aufzeichnen kannst. Für die beste Videoqualität empfiehlt es sich jedoch, OpenBoard als Fensterquelle in **OBS Studio** aufzunehmen.
* **Xournal++:** Unterstützt den Export deiner handschriftlichen Notizen als **SVG-Vektorgrafik**. Diese SVGs kannst du anschließend direkt in **Manim** als `SVGMobject` importieren und programmgesteuert animieren!

---

## 🎧 8. Audio-Nachbearbeitung (Audacity)

Für das Mastering und die Feinabstimmung deiner mit Kokoro TTS generierten Sprachspuren ist Audacity das Standardwerkzeug.

### 📊 Audacity Übersicht
* **Was es ist:** Ein freier, quelloffener Audio-Editor.
* **Vorteile:**
  - Einfaches Schneiden und Anpassen von Tonspuren.
  - Rauschminderung und Normalisierung der Lautstärke.
  - Kompressor-Effekte, um die Stimme präsenter und professioneller klingen zu lassen.

### 🛠️ Audacity Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y audacity
```

---

## 📖 9. Kursplattform-Generator (mdBook)

Um deine Markdown-Kurskapitel (`1.md`, `2.md`...) in eine ansprechende, durchsuchbare Weboberfläche zu verwandeln, wird das Rust-native Tool **mdBook** verwendet.

### 📊 mdBook Übersicht
* **Was es ist:** Ein in Rust geschriebenes Tool, das Markdown-Dateien in eine statische HTML-Website kompiliert (wie das offizielle Rust-Buch).
* **Vorteile:**
  - Volltextsuche und responsive Layouts.
  - Syntaxhervorhebung für Rust-Code.
  - Integrierter Webserver zur lokalen Vorschau.

### 🛠️ mdBook Schritt-für-Schritt-Installation

#### Installation über APT (Standard & Empfohlen)
```bash
sudo apt update
sudo apt install -y mdbook
```

### 🚀 Verwendung & Befehle
1. **mdBook-Projekt initialisieren:**
   ```bash
   mdbook init mein-kurs
   ```
2. **Lokalen Vorschau-Server starten:**
   ```bash
   mdbook serve --open
   ```
3. **Statische HTML-Seiten bauen:**
   ```bash
   mdbook build
   ```
---

## 🧡 10. Blender 3D

Blender ist eine freie, quelloffene 3D-Grafiksoftware. Sie eignet sich hervorragend für 3D-Animationen, Modellierung, Rendering und visuelle Effekte. Im Rahmen deines Videokurses kann Blender für 3D-Intros, komplexe grafische Veranschaulichungen oder erweiterte visuelle Elemente verwendet werden.

### 📊 Blender Installationsmethoden im Vergleich

| Methode | Paketquelle | Update-Frequenz / Version | Stabilität & Performance |
| :--- | :--- | :--- | :--- |
| **Snap** (Empfohlen) | Canonical Snap Store | Sehr aktuell (Neuere Features) | Hervorragend (klassische Sandbox) |
| **APT** | Offizielle Ubuntu-Quellen | Stabil (Ältere Version) | Optimal in das System integriert |
| **Flatpak** | Flathub | Sehr aktuell | Isoliert (Sandboxed) |

### 🛠️ Blender Schritt-für-Schritt-Installation

#### Methode A: Installation über Snap (Empfohlen für neueste Version)
```bash
sudo snap install blender --classic
```

#### Methode B: Installation über APT
```bash
sudo apt update
sudo apt install -y blender
```

#### Methode C: Installation über Flatpak
```bash
flatpak install flathub org.blender.Blender
```

---

## 🐍 11. Python-Umgebung & Ausführung (VIRTUAL ENV)

Um die Generierungsskripte für Video und Audio auszuführen, wurde eine isolierte virtuelle Umgebung (`.venv`) eingerichtet. Dies verhindert Konflikte mit dem restlichen System.

### 🛠️ Inbetriebnahme (Einmalig eingerichtet)
Falls du die Umgebung auf einem anderen Rechner neu erstellen möchtest, kannst du folgende Befehle nutzen:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Ausführung der Skripte

#### 1. Virtuelle Umgebung aktivieren:
Vor jeder Ausführung im Terminal musst du die virtuelle Umgebung aktivieren:
```bash
source .venv/bin/activate
```
*(Dein Terminal-Prompt zeigt danach `(.venv)` als Präfix an).*

#### 2. Audio-Sprachspuren generieren (Kokoro TTS):
Generiere die Audiodateien der Lektionen über Python. Diese Skripte nutzen das Kokoro-ONNX-Modell mit der deutschen Stimme "Martin", um hochqualitative, rauschfreie Audiodateien in dem Ordner `audio/` zu erstellen:
```bash
# Kapitel 1 bis 6 Sprachspuren generieren
python generate_audio.py
python generate_audio_ch2.py
python generate_audio_ch3.py
python generate_audio_ch4.py
python generate_audio_ch5.py
python generate_audio_ch6.py
```

#### 3. Videoszenen rendern (Manim & FFmpeg):
Rendere deine Animations-Skripte und verbinde sie mit der Tonspur bzw. mische externe Videos ab.

* **Kapitel 1 (Einführung):**
  ```bash
  manim -pql video_scene.py RustIntroVideo
  ```
* **Kapitel 2 (Installation):**
  ```bash
  manim -pql video_scene_ch2.py RustInstallVideo
  ```
* **Kapitel 3 (KI-Assistenten):**
  ```bash
  manim -pql video_scene_ch3.py RustToolsVideo
  ```
* **Kapitel 4 (Erstes Projekt):**
  *Dieses Video basiert auf einer Bildschirmaufnahme ([Video/4.mp4](file:///home/thorsten/RustKurs/Video/4.mp4)). Die Tonspur wurde per ffmpeg bereinigt und mit dem generierten Voiceover gemischt:*
  ```bash
  ffmpeg -y -i Video/4.mp4 -i audio/ch4_voiceover.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest 4.mp4
  ```
* **Kapitel 5 (Variablen):**
  ```bash
  manim -pql video_scene_ch5.py RustVariablesVideo
  ```
* **Kapitel 6 (Datentypen):**
  ```bash
  manim -pql video_scene_ch6.py RustDatatypesVideo
  ```
* **Kapitel 7 (Übungsprojekt):**
  *Dieses Video basiert auf einer Bildschirmaufnahme ([Video/7.mp4](file:///home/thorsten/RustKurs/Video/7.mp4)). Die verrauschte Tonspur wurde durch ein getimtes Kokoro-Voiceover ersetzt:*
  ```bash
  python generate_audio_ch7.py
  ffmpeg -y -i Video/7.mp4 -i audio/ch7_voiceover.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest 7.mp4
  ```
* **Kapitel 8 (Arrays & Tupel):**
  ```bash
  python generate_audio_ch8.py
  manim -pqm video_scene_ch8.py RustCompoundDatatypesVideo
  cp media/videos/video_scene_ch8/720p30/RustCompoundDatatypesVideo.mp4 8.mp4
  ```
* **Kapitel 9 (Zusammenfassung):**
  ```bash
  python generate_audio_ch9.py
  manim -pqm video_scene_ch9.py RustSummaryVideo
  cp media/videos/video_scene_ch9/720p30/RustSummaryVideo.mp4 9.mp4
  ```

> [!TIP]
> Der Schalter `-pql` rendert das Video schnell in niedriger Vorschauqualität (480p/15fps oder 720p/30fps, je nach Konfiguration). Benutze `-pqh` für Full-HD-Produktionsqualität (1080p/60fps).

#### 4. Virtuelle Umgebung wieder deaktivieren:
Wenn du fertig bist, kannst du die Umgebung wieder verlassen:
```bash
deactivate
```

---

## 🎬 Generierte Kurs-Videos Übersicht

Die fertigen Videodateien liegen im Hauptverzeichnis bereit zur Wiedergabe oder zum Upload:
* 🎥 **Kapitel 1:** [1.mp4](file:///home/thorsten/RustKurs/1.mp4) (Einführung)
* 🎥 **Kapitel 2:** [2.mp4](file:///home/thorsten/RustKurs/2.mp4) (Installation)
* 🎥 **Kapitel 3:** [3.mp4](file:///home/thorsten/RustKurs/3.mp4) (KI-Assistenten)
* 🎥 **Kapitel 4:** [4.mp4](file:///home/thorsten/RustKurs/4.mp4) (Erstes Cargo-Projekt & VS Code)
* 🎥 **Kapitel 5:** [5.mp4](file:///home/thorsten/RustKurs/5.mp4) (Variablen & Scopes)
* 🎥 **Kapitel 6:** [6.mp4](file:///home/thorsten/RustKurs/6.mp4) (Skalare & Zusammengesetzte Datentypen)
* 🎥 **Kapitel 7:** [7.mp4](file:///home/thorsten/RustKurs/7.mp4) (Übungsprojekt zu Variablen & Datentypen)
* 🎥 **Kapitel 8:** [8.mp4](file:///home/thorsten/RustKurs/8.mp4) (Arrays & Tupel)
* 🎥 **Kapitel 9:** [9.mp4](file:///home/thorsten/RustKurs/9.mp4) (Zusammenfassung Variablen & Datentypen)

