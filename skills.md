# Agent Skills – Tool-Steuerung und Generierungs-Playbooks

Diese Datei enthält erprobtes und fehlerfreies Spezialwissen zur Steuerung von Manim, Blender und Kokoro-onnx. AI-Agenten müssen sich strikt an diese Playbooks halten, um Render- und Generierungsfehler zu vermeiden.

---

## 1. Skill: @generate-manim (Animationen mit Manim)
Verwende diesen Ablauf, um fehlerfreie Manim-Skripte (Python) zu schreiben:

*   **Basisklasse**: Verwende immer die Kurs-eigene Klasse `video_scene.py` (oder Unterklassen davon) als Basis.
*   **Syntax-Highlighting**: Für Code-Einblendungen muss die `Pygments`-Bibliothek verwendet werden. Standardmäßig ein dunkles Schema (z. B. `monokai`) wählen.
*   **Rendering-Modi**:
    *   *Testen*: Render Szenen immer zuerst mit niedriger Auflösung und niedriger Framerate:
        ```bash
        manim -ql scene.py SceneName
        ```
    *   *Produktion*: Erst nach erfolgreichem Test mit hoher Qualität rendern:
        ```bash
        manim -qh scene.py SceneName
        ```
*   **Fehlervermeidung**: Keine 3D-Kamera (`ThreeDScene`) verwenden, wenn nur 2D-Elemente gerendert werden. Alle Text-Objekte mit `Tex` oder `MathTex` strukturieren und LaTeX-Syntax vorher auf Gültigkeit prüfen.
*   **Dynamische Videolänge**: Das Video muss nicht auf genau 5 Minuten (300 Sekunden) gestreckt werden. Die Dauer des Videos soll sich stattdessen dynamisch nach der tatsächlichen Audiozeit der Voiceover-Spuren plus 1,0 bis 1,5 Sekunden Übergangszeit pro Abschnitt richten.

---

## 2. Skill: @generate-blender (3D & 2D-Vektor-Animationen)
Ablauf für Blender-Automatisierung mit Python, Grease Pencil und Geometry Nodes:

*   **Blender Python API (`bpy`)**:
    *   Vor dem Löschen oder Ändern von Objekten prüfen, ob diese existieren:
        ```python
        if "Cube" in bpy.data.objects:
            bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
        ```
*   **Grease Pencil**:
    *   Beim Zeichnen von 2D-Vektorlinien über Python immer eine neue Grease-Pencil-Datenstruktur initialisieren und die Layer explizit benennen.
*   **Geometry Nodes**:
    *   Zur Erstellung prozeduraler Formen müssen Nodes per Python-Skript instanziiert und verknüpft werden. Nutze ausschließlich die offizielle Node-Nomenklatur (z. B. `GeometryNodeMeshToCurve`).
*   **Headless Rendering**:
    *   Rendern auf Servern ohne Display (Headless-Modus):
        ```bash
        blender -b projekt.blend -P script.py -a
        ```

---

## 3. Skill: @generate-audio (Kokoro-onnx Voiceovers)
Ablauf zur Erstellung von Audio-Voiceovers mit dem Kokoro-onnx Text-to-Speech (TTS) System:

*   **Textaufteilung**:
    *   Lange Kapiteltexte müssen vor der Übergabe an das TTS-Modell in Sätze oder kurze Absätze aufgeteilt werden (maximal 150 bis 200 Zeichen pro Segment).
*   **Audio-Skript Parameter**:
    *   Nutze die Skripte `generate_audio.py` oder die kapitelspezifischen Skripte (`generate_audio_chX.py`).
    *   Standard-Stimme (Voice): `af_bella` (weiblich, klarer englisch/deutscher Akzent) oder das konfigurierte Standardmodell.
    *   Geschwindigkeit (Speed): `1.0` (Standard) oder leicht angepasst für bessere Verständlichkeit.
*   **Speicherorte**:
    *   Alle generierten `.wav`-Audiodateien gehören in das Verzeichnis `audio/`.
*   **Pipeline**:
    ```bash
    python3 generate_audio.py --text "Dein Skripttext" --output audio/output.wav --speed 1.0
    ```
*   **Dynamische Audio-Zusammenführung**: Mische und verzögere die Audiospuren mit einer festen Lücke von 1,0–1,5 Sekunden zwischen den Abschnitten. Die Gesamtspielzeit ergibt sich dynamisch aus der Summe aller Spuren und Pausen. Verwende keine künstliche Auffüllung (Padding) auf 300 Sekunden.
