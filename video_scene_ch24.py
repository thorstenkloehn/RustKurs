from manim import *
import numpy as np
import json
import os

# Harmonious design palette
BG_COLOR = "#0f172a"      # Sleek slate-900 background
RUST_ORANGE = "#ea580c"   # Vibrant Rust Orange
CYAN = "#06b6d4"          # Accent Cyan
PURPLE = "#8b5cf6"        # Accent Purple/Violet
WHITE = "#f1f5f9"         # Off-white text
GRAY = "#64748b"          # Slate-500 for secondary elements and borders
GREEN = "#10b981"         # Emerald-500 for positives
RED = "#ef4444"           # Red-500 for challenges
YELLOW = "#f59e0b"        # Yellow-500 for warnings/info
LIGHT_BG = "#1e293b"      # slate-800 for card backgrounds
TERM_BG = "#090d16"       # Dark deep blue for terminal windows

class RustProfessionalizationVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Continuous watermark footer
        watermark = Text(
            "Auszüge aus 'The Rust Programming Language' (MIT/Apache 2.0) | Lizenz: CC-BY-SA 4.0 | Autoren: Steve Klabnik, Carol Nichols & Rust-Community",
            font_size=8.0,
            color=GRAY,
            fill_opacity=0.65
        ).to_edge(DOWN, buff=0.15)
        self.add(watermark)

        # Default durations (will be updated by JSON)
        durations = {
            "ch24_1_intro": 35.0,
            "ch24_2_governance": 35.0,
            "ch24_3_rules_glossary": 35.0,
            "ch24_4_agy_cli": 35.0,
            "ch24_5_tui_commands": 35.0,
            "ch24_6_feedback_loop": 35.0,
            "ch24_7_tutorial_dir": 35.0,
            "ch24_8_outro": 35.0
        }
        
        durations_path = "audio/durations_ch24.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # Compute total audio duration and required padding per section to hit exactly 300.0 seconds
        total_audio = sum(durations.values())
        target_video_duration = 300.0
        padding_per_section = (target_video_duration - total_audio) / 8.0
        print(f"Total audio: {total_audio}s. Padding per section: {padding_per_section}s.")

        def get_wait_time(key, anim_time):
            d_i = durations[key]
            # wait_time + anim_time + 1.0 (transition) = d_i + padding_per_section
            wait_val = d_i + padding_per_section - anim_time - 1.0
            return max(0.1, wait_val)

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        self.add_sound("audio/ch24_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 24: Projekt-Professionalisierung & das Antigravity CLI", font_size=18, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 24: Projekt-Professionalisierung & das Antigravity CLI", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Visual folder structure showcase
        root_dir = RoundedRectangle(corner_radius=0.1, width=11.0, height=3.0, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -0.6, 0])
        root_lbl = Text("Projekt-Root (Workspace)", font_size=12, color=CYAN, weight=BOLD).next_to(root_dir.get_top(), DOWN, buff=0.25)
        
        files_list = VGroup()
        files = ["AGENTS.md", "skills.md", ".agentrules", "glossary.md"]
        for i, f_name in enumerate(files):
            box = RoundedRectangle(corner_radius=0.08, width=2.2, height=1.0, color=WHITE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5)
            lbl = Text(f_name, font_size=10, color=WHITE, weight=BOLD).move_to(box.get_center())
            f_group = VGroup(box, lbl).move_to([-3.45 + i * 2.3, -0.8, 0])
            files_list.add(f_group)

        self.play(FadeIn(root_dir, shift=UP), FadeIn(root_lbl), run_time=1.5)
        self.play(LaggedStart(*(FadeIn(f, shift=RIGHT) for f in files_list), lag_ratio=0.25), run_time=1.5)
        self.wait(1.0)

        # Total anim time = 1.5 + 2.5 + 1.5 + 1.0 + 1.5 + 1.5 + 1.0 = 10.5 seconds
        self.wait(get_wait_time("ch24_1_intro", 10.5))

        self.play(FadeOut(root_dir), FadeOut(root_lbl), FadeOut(files_list), run_time=1.0)

        # ==========================================
        # SECTION 2: GOVERNANCE SÄULEN 1 & 2
        # ==========================================
        self.add_sound("audio/ch24_2_governance.wav")

        title_gov = Text("24. Workspace-Governance (Teil 1)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_gov), run_time=1.0)
        self.wait(1.0)

        # Two main columns: AGENTS.md vs skills.md
        card_w, card_h = 5.2, 3.6
        c1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.0, -0.6, 0])
        c1_t = Text("AGENTS.md", font_size=14, color=CYAN, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.3)
        c1_desc = Paragraph(
            "- Wer macht was?\n- Aktueller Projektstatus\n- Rollen & Zuständigkeiten\n- Schützt vor redundanten\n  Aufgaben",
            font_size=9, color=WHITE, line_spacing=0.5
        ).next_to(c1_t, DOWN, buff=0.3)
        g_c1 = VGroup(c1, c1_t, c1_desc)

        c2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, -0.6, 0])
        c2_t = Text("skills.md", font_size=14, color=PURPLE, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.3)
        c2_desc = Paragraph(
            "- Prozedurales Spezialwissen\n- Manim: video_scene.py\n- Blender: Python & Nodes\n- Kokoro-onnx: TTS\n- Verhindert Fehler",
            font_size=9, color=WHITE, line_spacing=0.5
        ).next_to(c2_t, DOWN, buff=0.3)
        g_c2 = VGroup(c2, c2_t, c2_desc)

        self.play(FadeIn(g_c1, shift=LEFT), FadeIn(g_c2, shift=RIGHT), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch24_2_governance", 7.0))

        self.play(FadeOut(g_c1), FadeOut(g_c2), run_time=1.0)

        # ==========================================
        # SECTION 3: GOVERNANCE SÄULEN 3 & 4
        # ==========================================
        self.add_sound("audio/ch24_3_rules_glossary.wav")

        title_rules = Text("24. Workspace-Governance (Teil 2)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_rules), run_time=1.0)
        self.wait(1.0)

        # Two columns: .agentrules vs glossary.md
        c3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.0, -0.6, 0])
        c3_t = Text(".agentrules", font_size=14, color=GREEN, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.3)
        c3_desc = Paragraph(
            "- Allgemeine Verhaltensregeln\n- Sprach- & Tonspezifikation\n- Code-Editiermethode\n- Linter- & Clippy-Vorgaben\n- Markdown-Regeln (GFM)",
            font_size=9, color=WHITE, line_spacing=0.5
        ).next_to(c3_t, DOWN, buff=0.3)
        g_c3 = VGroup(c3, c3_t, c3_desc)

        c4 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, -0.6, 0])
        c4_t = Text("glossary.md", font_size=14, color=YELLOW, weight=BOLD).next_to(c4.get_top(), DOWN, buff=0.3)
        c4_desc = Paragraph(
            "- Exakte Begriffsdefinitionen\n- Bsp: Ownership, Borrowing\n- Sichert einheitliche\n  Lehrbuch-Texte\n- Verhindert Widersprüche",
            font_size=9, color=WHITE, line_spacing=0.5
        ).next_to(c4_t, DOWN, buff=0.3)
        g_c4 = VGroup(c4, c4_t, c4_desc)

        self.play(FadeIn(g_c3, shift=UP), FadeIn(g_c4, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch24_3_rules_glossary", 7.0))

        self.play(FadeOut(g_c3), FadeOut(g_c4), run_time=1.0)

        # ==========================================
        # SECTION 4: ANTIMATTER/ANTIGRAVITY CLI
        # ==========================================
        self.add_sound("audio/ch24_4_agy_cli.wav")

        title_cli = Text("24. Das Antigravity CLI (agy)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_cli), run_time=1.0)
        self.wait(1.0)

        # Draw a Terminal
        term_box = RoundedRectangle(corner_radius=0.1, width=8.5, height=3.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.5, 0])
        term_top = Line(term_box.get_left() + UP*1.2, term_box.get_right() + UP*1.2, color=GRAY, stroke_width=2)
        dot_r = Dot(color=RED, radius=0.08).move_to(term_box.get_left() + UP*1.4 + RIGHT*0.25)
        dot_y = Dot(color=YELLOW, radius=0.08).move_to(term_box.get_left() + UP*1.4 + RIGHT*0.5)
        dot_g = Dot(color=GREEN, radius=0.08).move_to(term_box.get_left() + UP*1.4 + RIGHT*0.75)
        term_lbl = Text("Terminal - Sandbox Environment", font_size=8, color=GRAY).move_to(term_box.get_top() - DOWN*0.2)
        
        term_text = Paragraph(
            "$ cd /home/thorsten/RustKurs\n$ agy\nInitializing secure nsjail Sandbox...\nRules loaded: .agentrules, AGENTS.md\nAgy active: Prompt me!",
            font_size=10, color=WHITE, line_spacing=0.5
        ).next_to(term_top, DOWN, buff=0.35).align_to(term_box, LEFT).shift(RIGHT*0.5)

        term_group = VGroup(term_box, term_top, dot_r, dot_y, dot_g, term_lbl, term_text)

        self.play(FadeIn(term_group, shift=DOWN), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch24_4_agy_cli", 7.0))

        self.play(FadeOut(term_group), run_time=1.0)

        # ==========================================
        # SECTION 5: TUI SLASH COMMANDS
        # ==========================================
        self.add_sound("audio/ch24_5_tui_commands.wav")

        title_cmd = Text("24. TUI Slash-Befehle", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_cmd), run_time=1.0)
        self.wait(1.0)

        # Show commands in two columns
        cmd_g1 = VGroup()
        cmds1 = [
            ("/settings / /config", "Konfiguration & API-Keys", CYAN),
            ("/permissions", "Lese- und Schreibrechte prüfen", CYAN),
            ("/skills", "Geladene Skills auflisten", CYAN),
            ("/clear", "Agenten-Gedächtnis löschen", CYAN)
        ]
        for i, (name, desc, col) in enumerate(cmds1):
            lbl = Text(name, font_size=10, color=col, weight=BOLD).move_to([-3.5, 0.8 - i * 0.8, 0])
            txt = Text(desc, font_size=9, color=WHITE).next_to(lbl, DOWN, buff=0.15)
            cmd_g1.add(VGroup(lbl, txt))

        cmd_g2 = VGroup()
        cmds2 = [
            ("/rewind", "Zurückspringen im Kontext", PURPLE),
            ("/resume", "Letzte Sitzung wiederaufnehmen", PURPLE),
            ("/fork", "Entwicklungszweig abspalten", PURPLE),
            ("!", "Kommando direkt ausführen (z. B. !cargo run)", RUST_ORANGE)
        ]
        for i, (name, desc, col) in enumerate(cmds2):
            lbl = Text(name, font_size=10, color=col, weight=BOLD).move_to([3.5, 0.8 - i * 0.8, 0])
            txt = Text(desc, font_size=9, color=WHITE).next_to(lbl, DOWN, buff=0.15)
            cmd_g2.add(VGroup(lbl, txt))

        self.play(FadeIn(cmd_g1, shift=LEFT), FadeIn(cmd_g2, shift=RIGHT), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch24_5_tui_commands", 7.0))

        self.play(FadeOut(cmd_g1), FadeOut(cmd_g2), run_time=1.0)

        # ==========================================
        # SECTION 6: INTERACTIVE FEEDBACK LOOP
        # ==========================================
        self.add_sound("audio/ch24_6_feedback_loop.wav")

        title_loop = Text("24. Interaktive Feedbackschleife", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_loop), run_time=1.0)
        self.wait(1.0)

        # Draw 4 flowchart steps
        steps = VGroup()
        step_data = [
            ("1. Vorschlag", "Agent schlägt Code vor", CYAN, [-4.5, -0.6, 0]),
            ("2. Review (ctrl+r)", "Benutzer prüft Code", YELLOW, [-1.5, -0.6, 0]),
            ("3. Kommentar", "Kritik & Feedback", PURPLE, [1.5, -0.6, 0]),
            ("4. Anpassung", "Agent korrigiert Code", GREEN, [4.5, -0.6, 0])
        ]
        
        for name, desc, col, pos in step_data:
            box = RoundedRectangle(corner_radius=0.1, width=2.4, height=1.6, color=col, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2.0).move_to(pos)
            lbl = Text(name, font_size=10, color=col, weight=BOLD).next_to(box.get_top(), DOWN, buff=0.2)
            txt = Paragraph(desc, font_size=7, color=WHITE, alignment="center").next_to(lbl, DOWN, buff=0.15)
            steps.add(VGroup(box, lbl, txt))

        # Draw arrows between steps
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(start=steps[i].get_right(), end=steps[i+1].get_left(), buff=0.1, color=GRAY, max_stroke_width_to_length_ratio=8, stroke_width=2)
            arrows.add(arrow)

        # Loop-back arrow from step 4 to 1
        loop_arrow = DoubleArrow(start=steps[3].get_top() + UP*0.2, end=steps[0].get_top() + UP*0.2, color=RUST_ORANGE, stroke_width=2)

        self.play(FadeIn(steps[0], shift=UP), run_time=1.0)
        for i in range(3):
            self.play(GrowArrow(arrows[i]), FadeIn(steps[i+1], shift=UP), run_time=1.0)
        self.play(FadeIn(loop_arrow), run_time=1.0)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 2.0 = 8.0 seconds
        self.wait(get_wait_time("ch24_6_feedback_loop", 8.0))

        self.play(FadeOut(steps), FadeOut(arrows), FadeOut(loop_arrow), run_time=1.0)

        # ==========================================
        # SECTION 7: TUTORIAL DIRECTORY & zahlenraten
        # ==========================================
        self.add_sound("audio/ch24_7_tutorial_dir.wav")

        title_tut = Text("24. Praxistutorial: zahlenraten", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_tut), run_time=1.0)
        self.wait(1.0)

        # Show prompt on top and generated folders below
        prompt_box = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, 1.2, 0])
        prompt_lbl = Text("Prompt für agy:", font_size=8, color=GRAY).next_to(prompt_box.get_top(), DOWN, buff=0.15).align_to(prompt_box, LEFT).shift(RIGHT*0.3)
        prompt_txt = Text('"Erstelle das Unterverzeichnis Tutorial mit dem Cargo-Projekt zahlenraten..."', font_size=9, color=WHITE).next_to(prompt_lbl, DOWN, buff=0.1).align_to(prompt_box, LEFT).shift(RIGHT*0.3)
        prompt_g = VGroup(prompt_box, prompt_lbl, prompt_txt)

        # Tree layout below
        tree_box = RoundedRectangle(corner_radius=0.1, width=8.0, height=2.4, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -1.0, 0])
        tree_text = Paragraph(
            "Tutorial/\n├── README.md              # Build-Anleitung\n└── zahlenraten/\n    ├── Cargo.toml         # Deklariert rand Crate\n    └── src/main.rs        # Zahlenratespiel-Code",
            font_size=10, color=WHITE, line_spacing=0.5
        ).next_to(tree_box.get_top(), DOWN, buff=0.35).align_to(tree_box, LEFT).shift(RIGHT*0.6)
        tree_g = VGroup(tree_box, tree_text)

        self.play(FadeIn(prompt_g, shift=DOWN), run_time=1.5)
        self.play(FadeIn(tree_g, shift=UP), run_time=1.5)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 1.5 + 1.5 + 2.0 = 7.0 seconds
        self.wait(get_wait_time("ch24_7_tutorial_dir", 7.0))

        self.play(FadeOut(prompt_g), FadeOut(tree_g), run_time=1.0)

        # ==========================================
        # SECTION 8: OUTRO
        # ==========================================
        self.add_sound("audio/ch24_8_outro.wav")

        title_outro = Text("Zusammenfassung & Ausblick", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to([0, 1.2, 0])
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Key Takeaways
        takeaways = VGroup()
        items = [
            ("1. Professionalisierung", "Verwende AGENTS.md, .agentrules, skills.md, glossary.md", CYAN),
            ("2. Antigravity CLI", "Nutze agy in der Sandbox für sichere, agentische Codierung", PURPLE),
            ("3. Feedback-Schleife", "Prüfe Änderungen mit ctrl+r und gib Korrekturkommentare", GREEN),
            ("4. Tutorial-Bereich", "Kapsle Übungsverzeichnisse sauber vom Hauptprojekt ab", YELLOW)
        ]

        for i, (heading, body, col) in enumerate(items):
            h_lbl = Text(heading, font_size=11, color=col, weight=BOLD).move_to([-4.5, -0.2 - i * 0.75, 0])
            b_lbl = Text(body, font_size=9, color=WHITE).next_to(h_lbl, DOWN, buff=0.1).align_to(h_lbl, LEFT)
            takeaways.add(VGroup(h_lbl, b_lbl))

        self.play(LaggedStart(*(FadeIn(t, shift=RIGHT) for t in takeaways), lag_ratio=0.25), run_time=2.5)
        self.wait(4.0)

        # Total anim time = 1.0 + 1.0 + 2.5 + 4.0 = 8.5 seconds
        self.wait(get_wait_time("ch24_8_outro", 8.5))

        # Final fade out
        self.play(FadeOut(title_group), FadeOut(takeaways), run_time=1.5)
        self.wait(1.0)
