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

class RustGoogleAIVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Load durations if they exist, otherwise use sensible defaults
        durations = {
            "ch16_1_intro": 25.0,
            "ch16_2_antigravity": 31.0,
            "ch16_3_gemini_code_assist": 29.0,
            "ch16_4_ai_studio": 25.0,
            "ch16_5_practical": 22.0,
            "ch16_6_best_practices": 22.0,
            "ch16_7_outro": 20.0
        }
        
        durations_path = "audio/durations_ch16.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        self.add_sound("audio/ch16_1_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 16: Google KI zum Programmieren", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # Move Title to Top
        title_small = Text("Kapitel 16: Beste Google KI nutzen", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s
        self.wait(0.5)  # total 5.0s

        # Diagram: Google AI Services
        center_node = RoundedRectangle(corner_radius=0.1, width=3.5, height=0.8, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.2, 0])
        center_text = Text("Google KI-Tools", font_size=12, color=PURPLE, weight=BOLD).move_to(center_node.get_center())
        center_group = VGroup(center_node, center_text)

        node_left = RoundedRectangle(corner_radius=0.1, width=3.2, height=0.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.5, -0.6, 0])
        node_left_text = Text("Antigravity\n(Agentisch & CLI)", font_size=10, color=CYAN, weight=BOLD).move_to(node_left.get_center())
        node_left_group = VGroup(node_left, node_left_text)

        node_right = RoundedRectangle(corner_radius=0.1, width=3.2, height=0.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.5, -0.6, 0])
        node_right_text = Text("Gemini Code Assist\n(IDE Integration)", font_size=10, color=GREEN, weight=BOLD).move_to(node_right.get_center())
        node_right_group = VGroup(node_right, node_right_text)

        node_mid = RoundedRectangle(corner_radius=0.1, width=3.2, height=0.8, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -0.6, 0])
        node_mid_text = Text("Google AI Studio\n(Experimente & API)", font_size=10, color=YELLOW, weight=BOLD).move_to(node_mid.get_center())
        node_mid_group = VGroup(node_mid, node_mid_text)

        arrow_left = Arrow(start=[0, 0.8, 0], end=[-3.5, -0.2, 0], stroke_width=3, color=GRAY)
        arrow_mid = Arrow(start=[0, 0.8, 0], end=[0, -0.2, 0], stroke_width=3, color=GRAY)
        arrow_right = Arrow(start=[0, 0.8, 0], end=[3.5, -0.2, 0], stroke_width=3, color=GRAY)

        dia_group = VGroup(center_group, node_left_group, node_mid_group, node_right_group, arrow_left, arrow_mid, arrow_right)
        self.play(
            FadeIn(center_group, shift=DOWN),
            Create(arrow_left),
            Create(arrow_mid),
            Create(arrow_right),
            FadeIn(node_left_group, shift=RIGHT),
            FadeIn(node_mid_group, shift=UP),
            FadeIn(node_right_group, shift=LEFT),
            run_time=2.0
        )  # total 7.0s
        self.wait(1.0)  # total 8.0s

        intro_bullets = VGroup(
            Text("• Unterstützt dich beim Programmieren lernen", font_size=13, color=WHITE),
            Text("• Findet Compiler-Fehler & erklärt Konzepte", font_size=13, color=WHITE),
            Text("• Schreibt Code und erstellt Testfälle", font_size=13, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -2.0, 0])

        for bullet in intro_bullets:
            self.play(FadeIn(bullet, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 13.0s

        # Wait for the audio segment to complete
        self.wait(max(1.0, durations["ch16_1_intro"] - 13.0 - 1.0))
        self.play(
            FadeOut(dia_group),
            FadeOut(intro_bullets),
            run_time=1.0
        )


        # ==========================================
        # SECTION 2: GOOGLE ANTIGRAVITY
        # ==========================================
        self.add_sound("audio/ch16_2_antigravity.wav")

        title_anti = Text("16. Google Antigravity (Agent)", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_anti), run_time=1.0)
        self.wait(1.0)

        # Card showing Antigravity details
        anti_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        anti_title = Text("Das agentische Assistenzsystem", font_size=14, color=PURPLE, weight=BOLD).next_to(anti_rect.get_top(), DOWN, buff=0.3)
        
        anti_content = VGroup(
            Text("• Antigravity 2.0: Optimiert auf logisches Denken & Code-Verständnis", font_size=12, color=WHITE),
            Text("• Antigravity CLI (agy): Autonome Ausführung in sicherer Sandbox", font_size=12, color=WHITE),
            Text("• Antigravity IDE: Direkte Integration & Code-Vorschläge beim Tippen", font_size=12, color=WHITE),
            Text("Beispiel: agy \"Schreibe eine Rust-Funktion zur Primzahlprüfung\"", font_size=11, color=CYAN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(anti_title, DOWN, buff=0.4)
        
        anti_group = VGroup(anti_rect, anti_title, anti_content)

        self.play(FadeIn(anti_group, scale=0.9), run_time=1.5)
        self.wait(5.0)

        # Highlight CLI command
        cli_highlight = SurroundingRectangle(anti_content[3], color=YELLOW, buff=0.1, stroke_width=2)
        self.play(Create(cli_highlight), run_time=1.0)
        self.wait(6.0)

        # Wait for audio to finish
        self.wait(max(1.0, durations["ch16_2_antigravity"] - 1.0 - 1.0 - 1.5 - 5.0 - 1.0 - 6.0 - 1.0))
        self.play(
            FadeOut(anti_group),
            FadeOut(cli_highlight),
            run_time=1.0
        )


        # ==========================================
        # SECTION 3: GEMINI CODE ASSIST
        # ==========================================
        self.add_sound("audio/ch16_3_gemini_code_assist.wav")

        title_code_assist = Text("16. Gemini Code Assist (IDE-Begleiter)", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_code_assist), run_time=1.0)
        self.wait(1.0)

        # Three versions cards
        v_width = 3.6
        v_height = 4.0
        
        v1_rect = RoundedRectangle(corner_radius=0.1, width=v_width, height=v_height, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-4.1, -0.6, 0])
        v1_title = Text("Für Einzelpersonen", font_size=11, color=GREEN, weight=BOLD).next_to(v1_rect.get_top(), DOWN, buff=0.25)
        v1_desc = VGroup(
            Text("• Komplett kostenlos!", font_size=9, color=WHITE),
            Text("• Perfekt für Einsteiger", font_size=9, color=WHITE),
            Text("• VS Code Erweiterung", font_size=9, color=WHITE),
            Text("• Chat & Vervollständigung", font_size=9, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(v1_title, DOWN, buff=0.3)
        v1_group = VGroup(v1_rect, v1_title, v1_desc)

        v2_rect = RoundedRectangle(corner_radius=0.1, width=v_width, height=v_height, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, -0.6, 0])
        v2_title = Text("Standard", font_size=11, color=CYAN, weight=BOLD).next_to(v2_rect.get_top(), DOWN, buff=0.25)
        v2_desc = VGroup(
            Text("• Für Cloud-Entwickler", font_size=9, color=WHITE),
            Text("• Professionelle Teams", font_size=9, color=WHITE),
            Text("• Google Cloud Portfolio", font_size=9, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(v2_title, DOWN, buff=0.3)
        v2_group = VGroup(v2_rect, v2_title, v2_desc)

        v3_rect = RoundedRectangle(corner_radius=0.1, width=v_width, height=v_height, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([4.1, -0.6, 0])
        v3_title = Text("Enterprise", font_size=11, color=PURPLE, weight=BOLD).next_to(v3_rect.get_top(), DOWN, buff=0.25)
        v3_desc = VGroup(
            Text("• Für Großunternehmen", font_size=9, color=WHITE),
            Text("• Code-Customization", font_size=9, color=WHITE),
            Text("• Höchste Sicherheit", font_size=9, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(v3_title, DOWN, buff=0.3)
        v3_group = VGroup(v3_rect, v3_title, v3_desc)

        self.play(
            FadeIn(v1_group, shift=RIGHT),
            FadeIn(v2_group, shift=UP),
            FadeIn(v3_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(5.0)

        # Highlight Free Individual Version
        free_highlight = SurroundingRectangle(v1_rect, color=YELLOW, buff=0.08, stroke_width=2.5)
        free_label = Text("Kostenlos für dich!", font_size=11, color=YELLOW, weight=BOLD).next_to(v1_rect, DOWN, buff=0.15)
        
        self.play(
            Create(free_highlight),
            FadeIn(free_label, shift=UP),
            run_time=1.0
        )
        self.wait(8.0)

        # Wait for audio to finish
        self.wait(max(1.0, durations["ch16_3_gemini_code_assist"] - 1.0 - 1.0 - 2.0 - 5.0 - 1.0 - 8.0 - 1.0))
        self.play(
            FadeOut(v1_group),
            FadeOut(v2_group),
            FadeOut(v3_group),
            FadeOut(free_highlight),
            FadeOut(free_label),
            run_time=1.0
        )


        # ==========================================
        # SECTION 4: GOOGLE AI STUDIO
        # ==========================================
        self.add_sound("audio/ch16_4_ai_studio.wav")

        title_studio = Text("16. Google AI Studio (Prototyping)", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_studio), run_time=1.0)
        self.wait(1.0)

        # Code Studio box
        studio_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        studio_title = Text("Plattform für Experimente & APIs", font_size=14, color=YELLOW, weight=BOLD).next_to(studio_rect.get_top(), DOWN, buff=0.3)
        
        studio_content = VGroup(
            Text("• Riesiges Kontextfenster: Bis zu 2 Millionen Token", font_size=12, color=WHITE),
            Text("  -> Lade deine komplette Codebasis oder Dokumentation hoch!", font_size=11, color=GRAY),
            Text("• Kostenlose API-Schlüssel für deine eigenen Projekte", font_size=12, color=WHITE),
            Text("• Interaktives Prompt-Design und Feineinstellung im Browser", font_size=12, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(studio_title, DOWN, buff=0.4)
        
        studio_group = VGroup(studio_rect, studio_title, studio_content)

        self.play(FadeIn(studio_group, scale=0.9), run_time=1.5)
        self.wait(5.0)

        # Highlight context window
        context_highlight = SurroundingRectangle(studio_content[0], color=CYAN, buff=0.1, stroke_width=2)
        self.play(Create(context_highlight), run_time=1.0)
        self.wait(6.0)

        # Wait for audio to finish
        self.wait(max(1.0, durations["ch16_4_ai_studio"] - 1.0 - 1.0 - 1.5 - 5.0 - 1.0 - 6.0 - 1.0))
        self.play(
            FadeOut(studio_group),
            FadeOut(context_highlight),
            run_time=1.0
        )


        # ==========================================
        # SECTION 5: GEMINI PRACTICAL BEDIENUNG
        # ==========================================
        self.add_sound("audio/ch16_5_practical.wav")

        title_prac = Text("16. Gemini Code Assist: Bedienung", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_prac), run_time=1.0)
        self.wait(1.0)

        # Card showing shortcuts
        prac_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        prac_title = Text("Tastenkombinationen & Chat-Befehle", font_size=14, color=GREEN, weight=BOLD).next_to(prac_rect.get_top(), DOWN, buff=0.3)
        
        prac_content = VGroup(
            Text("• Strg + I (Cmd + I): Inline-Chat öffnen (generieren & beheben)", font_size=11, color=WHITE),
            Text("• Tab-Taste: Graue Inline-Vorschläge übernehmen", font_size=11, color=WHITE),
            Text("• /generate: Neue Datenstrukturen & Funktionen erstellen", font_size=11, color=CYAN, font="Monospace"),
            Text("• /fix: Fehler gezielt analysieren und korrigieren lassen", font_size=11, color=CYAN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(prac_title, DOWN, buff=0.4)
        
        prac_group = VGroup(prac_rect, prac_title, prac_content)

        self.play(FadeIn(prac_group, scale=0.9), run_time=1.5)
        self.wait(6.0)

        # Highlight Strg+I shortcut
        prac_highlight = SurroundingRectangle(prac_content[0], color=YELLOW, buff=0.08, stroke_width=1.5)
        self.play(Create(prac_highlight), run_time=1.0)
        self.wait(6.0)

        # Wait for audio to finish
        self.wait(max(1.0, durations["ch16_5_practical"] - 1.0 - 1.0 - 1.5 - 6.0 - 1.0 - 6.0 - 1.0))
        self.play(
            FadeOut(prac_group),
            FadeOut(prac_highlight),
            run_time=1.0
        )


        # ==========================================
        # SECTION 6: BEST PRACTICES
        # ==========================================
        self.add_sound("audio/ch16_6_best_practices.wav")

        title_practices = Text("16. Best Practices für Anfänger", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_practices), run_time=1.0)
        self.wait(1.0)

        # Best Practices Box
        practice_rect = RoundedRectangle(corner_radius=0.15, width=9.5, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        practice_title = Text("So nutzt du KI als echten Mentor", font_size=14, color=CYAN, weight=BOLD).next_to(practice_rect.get_top(), DOWN, buff=0.3)
        
        practice_content = VGroup(
            Text("1. Code erklären lassen:", font_size=12, color=CYAN, weight=BOLD),
            Text("   Kopiere nicht nur, frage nach einer Zeile-für-Zeile-Erklärung.", font_size=11, color=WHITE),
            Text("2. Sparringspartner für Compiler-Fehler:", font_size=12, color=CYAN, weight=BOLD),
            Text("   Füttere die KI mit Rust-Fehlermeldungen zur Ursachenanalyse.", font_size=11, color=WHITE),
            Text("3. Präzise Prompts formulieren:", font_size=12, color=CYAN, weight=BOLD),
            Text("   Je genauer die Vorgaben, desto besser und lehrreicher der Code.", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(practice_title, DOWN, buff=0.3)
        
        practice_group = VGroup(practice_rect, practice_title, practice_content)

        self.play(FadeIn(practice_group, scale=0.9), run_time=1.5)
        self.wait(8.0)

        # Highlight explanation point
        exp_highlight = SurroundingRectangle(practice_content[0:2], color=YELLOW, buff=0.08, stroke_width=1.5)
        self.play(Create(exp_highlight), run_time=1.0)
        self.wait(6.0)

        # Wait for audio to finish
        self.wait(max(1.0, durations["ch16_6_best_practices"] - 1.0 - 1.0 - 1.5 - 8.0 - 1.0 - 6.0 - 1.0))
        self.play(
            FadeOut(practice_group),
            FadeOut(exp_highlight),
            run_time=1.0
        )


        # ==========================================
        # SECTION 7: OUTRO
        # ==========================================
        self.add_sound("audio/ch16_7_outro.wav")

        # Outro Title
        outro_title = Text("Vielen Dank fürs Zuschauen!", font_size=32, color=RUST_ORANGE, weight=BOLD)
        outro_subtitle = Text("Beschleunige dein Lernen mit Google KI!", font_size=18, color=CYAN).next_to(outro_title, DOWN, buff=0.4)
        outro_group = VGroup(outro_title, outro_subtitle).move_to([0, -0.2, 0])

        # Spin Gear (Visualizing Rust)
        gear_center = Circle(radius=0.6, color=RUST_ORANGE, stroke_width=4).next_to(outro_group, UP, buff=0.6)
        teeth = VGroup()
        num_teeth = 12
        for i in range(num_teeth):
            angle = i * (360 / num_teeth) * DEGREES
            tooth = Rectangle(width=0.18, height=0.25, color=RUST_ORANGE, fill_opacity=1, stroke_width=0)
            tooth.move_to(gear_center.get_center())
            tooth.shift(0.65 * np.array([np.cos(angle), np.sin(angle), 0]))
            tooth.rotate(angle)
            teeth.add(tooth)
        inner_circle = Circle(radius=0.25, color=BG_COLOR, stroke_width=0, fill_opacity=1).move_to(gear_center.get_center())
        gear = VGroup(gear_center, teeth, inner_circle)

        self.play(
            FadeOut(title_group),
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )

        spin_time = max(1.0, durations["ch16_7_outro"] - 2.0 - 1.0)
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )
