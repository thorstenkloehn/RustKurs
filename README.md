# 🎬 Media- & Grafik-Tools Installationsanleitung (Linux/Ubuntu)

Dieses Dokument beschreibt die Installation und Konfiguration von **VLC Media Player**, **OBS Studio**, **Kdenlive**, **Inkscape**, **GIMP**, **Gromit-MPX**, **Flameshot**, **Glaxnimate**, **OpenBoard**, **Xournal++**, **Audacity**, **mdBook**, **Blender 3D** und dem **Model Context Protocol (MCP) VS Code Command Server** auf einem Ubuntu- bzw. Linux-System. Diese Tools bilden die Grundlage für die Wiedergabe, Aufnahme, den Schnitt, die grafische Gestaltung, 3D-Modellierung, die Live-Präsentation, handschriftliche Erklärungen, das Audio-Mastering, das Hosten und die KI-gestützte Steuerung Ihres Rust-Videokurses.

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
> Um sicherzustellen, dass alle gängigen Audio- und Videocodecs vorhanden sind, installieren Sie die Restricted Extras mit:
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
* Unter Ubuntu/Linux benötigen Sie dafür das Kernel-Modul `v4l2loopback`:
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

Um 2D-Vektor-Animationen (wie wandernde Pfeile, Einkreisungen oder Hervorhebungen) direkt über Ihre Videos in Kdenlive zu zeichnen, können Sie **Glaxnimate** als Erweiterung nutzen.

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

Für die Erstellung von visuellen Assets, Diagrammen und Vorschaubildern (Thumbnails) für Ihren Videokurs sind folgende Grafikprogramme sehr zu empfehlen:

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

Wenn Sie Ihren Bildschirm mit OBS Studio aufnehmen und live Code erklären, ist es extrem hilfreich, direkt auf dem Bildschirm zeichnen zu können, um wichtige Zeilen hervorzuheben.

### 📊 Gromit-MPX Übersicht
* **Was es ist:** Ein Desktop-Annotationstool, mit dem Sie per Tastendruck auf dem gesamten Bildschirm (über allen Fenstern wie VS Code oder dem Browser) zeichnen können.
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
1. Starten Sie Gromit-MPX über das Anwendungsmenü oder das Terminal (`gromit-mpx`).
2. **Zeichnen aktivieren/deaktivieren:** Drücken Sie die Taste **`F9`** (der Cursor verwandelt sich in ein Fadenkreuz).
3. **Zeichnen:** Halten Sie die linke Maustaste gedrückt und zeichnen Sie.
4. **Radieren:** Halten Sie die rechte Maustaste gedrückt oder nutzen Sie `Umschalt` + linke Maustaste.
5. **Alles löschen:** Drücken Sie **`Mittelklick`** oder **`Strg + F9`** (je nach Konfiguration), um alle Zeichnungen zu leeren.

---

## 📸 6. Screenshot-Tools (Flameshot)

Für die Erstellung von Dokumentationen, Kursunterlagen oder Präsentationen ist ein gutes Screenshot-Tool unerlässlich.

### 📊 Flameshot Übersicht
* **Was es ist:** Ein hochentwickeltes Open-Source-Screenshot-Tool, mit dem Sie direkt beim Aufnehmen Markierungen vornehmen können.
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
1. Starten Sie Flameshot über das Terminal: `flameshot gui`.
2. **Tastenkombination einrichten (Empfohlen):**
   Um Flameshot auf die Taste `Druck` (PrintScreen) zu legen, gehen Sie unter Ubuntu auf:
   * **Einstellungen** > **Tastatur** > **Tastaturkürzel anzeigen und anpassen** > **Eigene Kürzel**.
   * Fügen Sie ein neues Kürzel hinzu:
     - **Name:** Flameshot
     - **Befehl:** `flameshot gui`
     - **Tastenkombination:** `Druck` (PrintScreen) festlegen.

---

## 📝 7. Whiteboard- & Notizen-Software (OpenBoard & Xournal++)

Für handschriftliche Erklärungen, Zeichnungen mit einem Grafiktablett oder interaktive Tafelbilder während Ihres Videokurses eignen sich OpenBoard und Xournal++ perfekt.

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
* **OpenBoard:** Bietet eine integrierte "Podcast"-Funktion, mit der Sie Ihre Whiteboard-Aktivitäten direkt aufzeichnen können. Für die beste Videoqualität empfiehlt es sich jedoch, OpenBoard als Fensterquelle in **OBS Studio** aufzunehmen.
* **Xournal++:** Unterstützt den Export Ihrer handschriftlichen Notizen als **SVG-Vektorgrafik**. Diese SVGs können Sie anschließend direkt in **Manim** als `SVGMobject` importieren und programmgesteuert animieren!

---

## 🎧 8. Audio-Nachbearbeitung (Audacity)

Für das Mastering und die Feinabstimmung Ihrer mit Kokoro TTS generierten Sprachspuren ist Audacity das Standardwerkzeug.

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

Um Ihre Markdown-Kurskapitel (`1.md`, `2.md`...) in eine ansprechende, durchsuchbare Weboberfläche zu verwandeln, wird das Rust-native Tool **mdBook** verwendet.

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

Blender ist eine freie, quelloffene 3D-Grafiksoftware. Sie eignet sich hervorragend für 3D-Animationen, Modellierung, Rendering und visuelle Effekte. Im Rahmen Ihres Videokurses kann Blender für 3D-Intros, komplexe grafische Veranschaulichungen oder erweiterte visuelle Elemente verwendet werden.

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
Falls Sie die Umgebung auf einem anderen Rechner neu erstellen möchten, können Sie folgende Befehle nutzen:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Ausführung der Skripte

#### 1. Virtuelle Umgebung aktivieren:
Vor jeder Ausführung im Terminal müssen Sie die virtuelle Umgebung aktivieren:
```bash
source .venv/bin/activate
```
*(Ihr Terminal-Prompt zeigt danach `(.venv)` als Präfix an).*

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
Rendern Sie Ihre Animations-Skripte und verbinden Sie sie mit der Tonspur bzw. mischen Sie externe Videos ab.

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
* **Kapitel 10 (Funktionen):**
  ```bash
  python generate_audio_ch10.py
  manim -pqm video_scene_ch10.py RustFunctionsVideo
  cp media/videos/video_scene_ch10/720p30/RustFunctionsVideo.mp4 10.mp4
  ```
* **Kapitel 11 (Funktionen - Details):**
  ```bash
  python generate_audio_ch11.py
  manim -pqm video_scene_ch11.py RustFunctionsDetailsVideo
  cp media/videos/video_scene_ch11/720p30/RustFunctionsDetailsVideo.mp4 11.mp4
  ```
* **Kapitel 12 (Operatoren):**
  ```bash
  python generate_audio_ch12.py
  manim -pqm video_scene_ch12.py RustOperatorsVideo
  cp media/videos/video_scene_ch12/720p30/RustOperatorsVideo.mp4 12.mp4
  ```
* **Kapitel 13 (Übungen zu Operatoren):**
  ```bash
  python generate_audio_ch13.py
  manim -pqm video_scene_ch13.py RustExercisesVideo
  cp media/videos/video_scene_ch13/720p30/RustExercisesVideo.mp4 13.mp4
  ```
* **Kapitel 14 (Antigravity CLI):**
  ```bash
  python generate_audio_ch14.py
  manim -pqm video_scene_ch14.py RustAntigravityCLIVideo
  cp media/videos/video_scene_ch14/720p30/RustAntigravityCLIVideo.mp4 14.mp4
  ```
* **Kapitel 15 (Kontrollstrukturen):**
  ```bash
  python generate_audio_ch15.py
  manim -pqm video_scene_ch15.py RustControlStructuresVideo
  cp media/videos/video_scene_ch15/720p30/RustControlStructuresVideo.mp4 15.mp4
  ```
* **Kapitel 16 (Beste Google KI zum Programmieren nutzen):**
  ```bash
  python generate_audio_ch16.py
  manim -pqm video_scene_ch16.py RustGoogleAIVideo
  cp media/videos/video_scene_ch16/720p30/RustGoogleAIVideo.mp4 16.mp4
  ```
* **Kapitel 17 (Speicherverwaltung & Rust Ownership):**
  ```bash
  python generate_audio_ch17.py
  manim -pqm video_scene_ch17.py RustOwnershipVideo
  cp media/videos/video_scene_ch17/720p30/RustOwnershipVideo.mp4 17.mp4
  ```
* **Kapitel 18 (Was ist Ownership?):**
  ```bash
  python generate_audio_ch18.py
  manim -pqm video_scene_ch18.py RustOwnershipDetailedVideo
  cp media/videos/video_scene_ch18/720p30/RustOwnershipDetailedVideo.mp4 18.mp4
  ```
* **Kapitel 19 (Referenzen & Borrowing):**
  ```bash
  python generate_audio_ch19.py
  manim -pqm video_scene_ch19.py RustBorrowingVideo
  cp media/videos/video_scene_ch19/720p30/RustBorrowingVideo.mp4 19.mp4
  ```

Ab Kapitel 20 wird ein dreistufiger Build-Prozess mit einem FFmpeg-Mischskript (`build_chX_audio.py`) verwendet, um die Audiospuren mit exakt 1.5s Lücke zu synchronisieren und nach EBU R128 zu normalisieren:

* **Kapitel 20 bis 26 (Dreistufiger Build-Prozess):**
  Führen Sie für das jeweilige Kapitel (z. B. Kapitel 26) nacheinander folgende Befehle aus:
  ```bash
  # 1. Audiospuren generieren
  python generate_audio_ch26.py
  
  # 2. Manim-Szenen rendern (High Quality -qh)
  manim -qh video_scene_ch26.py RustAgentsVideo
  
  # 3. Audio & Video mischen & normalisieren
  python build_ch26_audio.py
  ```
  *(Ersetzen Sie 'ch26', 'RustAgentsVideo' und 'build_ch26_audio.py' durch die entsprechenden Dateinamen und Klassennamen des jeweiligen Kapitels. Die Klassennamen lauten: Ch20: RustReferencesVideo, Ch21: RustSummaryVideo, Ch22: RustPlanningVideo, Ch23: RustLearningStrategyVideo, Ch24: RustProfessionalizationVideo, Ch25: RustSlicesVideo, Ch26: RustAgentsVideo)*

> [!TIP]
> Der Schalter `-pql` rendert das Video schnell in niedriger Vorschauqualität (480p/15fps oder 720p/30fps, je nach Konfiguration). Benutzen Sie `-pqh` für Full-HD-Produktionsqualität (1080p/60fps).

#### 4. Virtuelle Umgebung wieder deaktivieren:
Wenn Sie fertig sind, können Sie die Umgebung wieder verlassen:
```bash
deactivate
```

---

## 🌐 12. Model Context Protocol (MCP) VS Code Command Server

Der **Model Context Protocol (MCP) VS Code Command Server** ermöglicht es KI-Assistenten, Befehle direkt innerhalb Ihrer laufenden VS Code-Instanz auszuführen. Dies verbessert die Integration von KI-Tools in Ihren Entwicklungs- und Aufnahmeworkflow erheblich.

### 🛠️ Global installieren
Der Server wird global über Node.js (NPM) auf deinem Linux-System installiert:
```bash
npm install -g @modelcontextprotocol/server-vscode-command
```

### 🚀 Konfiguration & Einbindung
Fügen Sie den Server in die globale Konfigurationsdatei Ihres MCP-Clients (z. B. Claude Desktop unter `~/.config/Claude/claude_desktop_config.json` oder in den Einstellungen Ihres jeweiligen Agenten) ein:

```json
{
  "mcpServers": {
    "vscode-command": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-vscode-command"
      ]
    }
  }
}
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
* 🎥 **Kapitel 10:** [10.mp4](file:///home/thorsten/RustKurs/10.mp4) (Funktionen)
* 🎥 **Kapitel 11:** [11.mp4](file:///home/thorsten/RustKurs/11.mp4) (Funktionen - Details)
* 🎥 **Kapitel 12:** [12.mp4](file:///home/thorsten/RustKurs/12.mp4) (Operatoren)
* 🎥 **Kapitel 13:** [13.mp4](file:///home/thorsten/RustKurs/13.mp4) (Übungen zu Operatoren)
* 🎥 **Kapitel 14:** [14.mp4](file:///home/thorsten/RustKurs/14.mp4) (Antigravity CLI)
* 🎥 **Kapitel 15:** [15.mp4](file:///home/thorsten/RustKurs/15.mp4) (Kontrollstrukturen)
* 🎥 **Kapitel 16:** [16.mp4](file:///home/thorsten/RustKurs/16.mp4) (Beste Google KI zum Programmieren nutzen)
* 🎥 **Kapitel 17:** [17.mp4](file:///home/thorsten/RustKurs/17.mp4) (Speicherverwaltung & Rust Ownership)
* 🎥 **Kapitel 18:** [18.mp4](file:///home/thorsten/RustKurs/18.mp4) (Was ist Ownership?)
* 🎥 **Kapitel 19:** [19.mp4](file:///home/thorsten/RustKurs/19.mp4) (Referenzen & Borrowing)
* 🎥 **Kapitel 20:** [20.mp4](file:///home/thorsten/RustKurs/20.mp4) (Referenzen & Borrowing Grundlagen)
* 🎥 **Kapitel 21:** [21.mp4](file:///home/thorsten/RustKurs/21.mp4) (Zusammenfassung & Ausblick)
* 🎥 **Kapitel 22:** [22.mp4](file:///home/thorsten/RustKurs/22.mp4) (Der VS Code Planungs-Workflow)
* 🎥 **Kapitel 23:** [23.mp4](file:///home/thorsten/RustKurs/23.mp4) (Lernstrategie, Lernportale & KI-Prompts)
* 🎥 **Kapitel 24:** [24.mp4](file:///home/thorsten/RustKurs/24.mp4) (Projekt-Professionalisierung & das Antigravity CLI)
* 🎥 **Kapitel 25:** [25.mp4](file:///home/thorsten/RustKurs/25.mp4) (Der Slice-Typ (Slices))
* 🎥 **Kapitel 26:** [26.mp4](file:///home/thorsten/RustKurs/26.mp4) (KI-Agenten & autonome Software-Ingenieure)

