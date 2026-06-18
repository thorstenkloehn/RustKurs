# Agent Skills – Playbooks

## 1. @generate-manim
* **Basis**: Erbe von `video_scene.py`.
* **Syntax**: `Pygments` nutzen (Default: `monokai`).
* **Render**: 
  * Test: `manim -ql s.py Scene`
  * Prod: `manim -qh s.py Scene`
* **Fehler**: Keine `ThreeDScene` für 2D. LaTeX in `Tex`/`MathTex` validieren.
* **Dauer**: Dynamisch (Audiozeit + 1.0–1.5s Pause/Abschnitt). Kein 300s-Padding.

## 2. @generate-blender
* **bpy**: Existenz prüfen: `if "Cube" in bpy.data.objects: bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)`
* **Grease Pencil**: Neue Struktur initialisieren, Layer explizit benennen.
* **Nodes**: Instanziierung via Python mit offizieller Nomenklatur (`GeometryNodeMeshToCurve`).
* **Headless**: `blender -b p.blend -P s.py -a`

## 3. @generate-audio (Kokoro-onnx)
* **Split**: Max. 150–200 Zeichen pro Segment.
* **Params**: `generate_audio.py`, Voice: `af_bella`, Speed: `1.0`, Ziel: `audio/`.
* **CLI**: `python3 generate_audio.py --text "..." --output audio/o.wav --speed 1.0`
* **Mix**: Feste Lücke (1.0–1.5s) zwischen Abschnitten. Gesamtdauer = Summe(Audios + Pausen). Kein 300s-Padding.