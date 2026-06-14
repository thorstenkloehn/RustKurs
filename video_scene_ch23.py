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
RED = "#ef4444"           # Red-500 for challenges or invalid items
YELLOW = "#f59e0b"        # Yellow-500 for warnings/info
LIGHT_BG = "#1e293b"      # slate-800 for card backgrounds
TERM_BG = "#090d16"       # Dark deep blue for terminal windows

class RustLearningStrategyVideo(Scene):
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
            "ch23_1_intro": 35.0,
            "ch23_2_strategies": 35.0,
            "ch23_3_portals": 35.0,
            "ch23_4_self_hosting": 35.0,
            "ch23_5_editors_moodle": 35.0,
            "ch23_6_aspnet": 35.0,
            "ch23_7_prompting": 35.0,
            "ch23_8_outro": 35.0
        }
        
        durations_path = "audio/durations_ch23.json"
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
        # SECTION 1: INTRO & DIE DREI SÄULEN
        # ==========================================
        self.add_sound("audio/ch23_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 23: Lernstrategie, Lernportale & KI-Prompts", font_size=18, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 23: Lernstrategie & Lernportale", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Visual representation: Three pillars of learning
        col_w, col_h = 3.6, 3.2
        pillar1 = RoundedRectangle(corner_radius=0.1, width=col_w, height=col_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.6, 0])
        p1_title = Text("1. Active Recall", font_size=12, color=CYAN, weight=BOLD).next_to(pillar1.get_top(), DOWN, buff=0.25)
        p1_text = Paragraph(
            "- Kein passives Lesen\n- Direkt Code tippen\n- Eigene Miniprojekte",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(p1_title, DOWN, buff=0.3)
        g1 = VGroup(pillar1, p1_title, p1_text)

        pillar2 = RoundedRectangle(corner_radius=0.1, width=col_w, height=col_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0.0, -0.6, 0])
        p2_title = Text("2. Spaced Repetition", font_size=12, color=PURPLE, weight=BOLD).next_to(pillar2.get_top(), DOWN, buff=0.25)
        p2_text = Paragraph(
            "- Täglich 15-20 Min.\n- Lerne im Schlaf\n- Kontinuität > Block",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(p2_title, DOWN, buff=0.3)
        g2 = VGroup(pillar2, p2_title, p2_text)

        pillar3 = RoundedRectangle(corner_radius=0.1, width=col_w, height=col_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([4.0, -0.6, 0])
        p3_title = Text("3. Compiler als Mentor", font_size=12, color=GREEN, weight=BOLD).next_to(pillar3.get_top(), DOWN, buff=0.25)
        p3_text = Paragraph(
            "- Fehler akzeptieren\n- Meldung ganz lesen\n- Lösung verstehen",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(p3_title, DOWN, buff=0.3)
        g3 = VGroup(pillar3, p3_title, p3_text)

        pillars = VGroup(g1, g2, g3)
        self.play(FadeIn(pillars, shift=UP), run_time=2.0)

        # Total anim time = 1.5 + 2.5 + 1.5 + 1.0 + 2.0 = 8.5 seconds
        self.wait(get_wait_time("ch23_1_intro", 8.5))

        self.play(FadeOut(pillars), run_time=1.0)

        # ==========================================
        # SECTION 2: ERWEITERTE LERNMETHODEN
        # ==========================================
        self.add_sound("audio/ch23_2_strategies.wav")

        title_strat = Text("23. Erweiterte Lernmethoden", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_strat), run_time=1.0)
        self.wait(1.0)

        # Draw two main blocks: Top-Down vs Bottom-Up
        box_w, box_h = 5.2, 1.4
        bu_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.0, 1.0, 0])
        bu_title = Text("Bottom-Up-Ansatz 🧱", font_size=11, color=CYAN, weight=BOLD).next_to(bu_box.get_top(), DOWN, buff=0.15)
        bu_desc = Text("Grundlagen lernen, dann komplexere Dinge bauen.", font_size=8, color=WHITE).next_to(bu_title, DOWN, buff=0.15)
        bu_g = VGroup(bu_box, bu_title, bu_desc)

        td_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, 1.0, 0])
        td_title = Text("Top-Down-Ansatz 🏗️", font_size=11, color=PURPLE, weight=BOLD).next_to(td_box.get_top(), DOWN, buff=0.15)
        td_desc = Text("Vom Ziel ausgehend nur benötigte Details lernen.", font_size=8, color=WHITE).next_to(td_title, DOWN, buff=0.15)
        td_g = VGroup(td_box, td_title, td_desc)

        # Four additional methods in a list
        methods_list = VGroup()
        methods = [
            ("Pair Programming", "Arbeit im Team zur Fehlervermeidung", GREEN),
            ("Code-Katas & Refactoring", "Kleine Übungen wiederholen und verbessern", YELLOW),
            ("REPL & Notebooks (evcxr)", "Sofortiges Code-Feedback im Terminal", CYAN),
            ("Learning in Public", "Lernfortschritte öffentlich auf GitHub teilen", RUST_ORANGE)
        ]

        for i, (m_title, m_desc, col) in enumerate(methods):
            bullet = Dot(color=col).move_to([-4.5, -0.2 - i * 0.55, 0])
            lbl = Text(f"{m_title}: ", font_size=9, color=col, weight=BOLD).next_to(bullet, RIGHT, buff=0.2)
            desc = Text(m_desc, font_size=9, color=WHITE).next_to(lbl, RIGHT, buff=0.1)
            methods_list.add(VGroup(bullet, lbl, desc))

        self.play(FadeIn(bu_g, shift=UP), FadeIn(td_g, shift=UP), run_time=1.5)
        self.play(LaggedStart(*(FadeIn(m, shift=RIGHT) for m in methods_list), lag_ratio=0.25), run_time=2.0)
        self.wait(1.5)

        # Total anim time = 1.0 + 1.0 + 1.5 + 2.0 + 1.5 = 7.0 seconds
        self.wait(get_wait_time("ch23_2_strategies", 7.0))

        self.play(FadeOut(bu_g), FadeOut(td_g), FadeOut(methods_list), run_time=1.0)

        # ==========================================
        # SECTION 3: INTERAKTIVE PLATTFORMEN
        # ==========================================
        self.add_sound("audio/ch23_3_portals.wav")

        title_portals = Text("23. Interaktive Plattformen für Rust", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_portals), run_time=1.0)
        self.wait(1.0)

        # Cards for platforms
        card_w, card_h = 3.6, 3.2
        c1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.6, 0])
        c1_t = Text("A) Rustlings", font_size=12, color=CYAN, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.25)
        c1_txt = Paragraph(
            "- Offizieller Kurs\n- Über 100 Aufgaben\n- Terminal-Watch-Modus\n- Befehl 'hint' für Tipps",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(c1_t, DOWN, buff=0.3)
        g_c1 = VGroup(c1, c1_t, c1_txt)

        c2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0.0, -0.6, 0])
        c2_t = Text("B) Exercism", font_size=12, color=PURPLE, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.25)
        c2_txt = Paragraph(
            "- 80+ freie Aufgaben\n- Echtes Code-Review\n- Vergleich mit anderen\n- Mentor-Feedback",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(c2_t, DOWN, buff=0.3)
        g_c2 = VGroup(c2, c2_t, c2_txt)

        c3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([4.0, -0.6, 0])
        c3_t = Text("C) Kurs-mdBook & Mehr", font_size=12, color=GREEN, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.25)
        c3_txt = Paragraph(
            "- Lokales Lehrbuch\n- Integrierte Suche\n- Spickzettel kopieren\n- Bonus: Rustfinity",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(c3_t, DOWN, buff=0.3)
        g_c3 = VGroup(c3, c3_t, c3_txt)

        cards_group = VGroup(g_c1, g_c2, g_c3)
        self.play(FadeIn(cards_group, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch23_3_portals", 7.0))

        self.play(FadeOut(cards_group), run_time=1.0)

        # ==========================================
        # SECTION 4: EIGENE PLATTFORMEN & BACKEND
        # ==========================================
        self.add_sound("audio/ch23_4_self_hosting.wav")

        title_backend = Text("23. Sandbox-Architektur (Backend)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_backend), run_time=1.0)
        self.wait(1.0)

        # Center Server Block
        server = RoundedRectangle(corner_radius=0.15, width=4.0, height=2.0, color=RUST_ORANGE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.5).move_to([0, 0.8, 0])
        server_lbl = Text("Sichere Sandbox-API", font_size=12, color=RUST_ORANGE, weight=BOLD).next_to(server.get_top(), DOWN, buff=0.3)
        server_sub = Text("Docker-isolierte Ausführung", font_size=9, color=WHITE).next_to(server_lbl, DOWN, buff=0.2)
        server_g = VGroup(server, server_lbl, server_sub)

        # Surrounding judge options
        j_boxes = VGroup()
        judges = [
            ("Judge0 (Empfohlen)", [-4.2, 1.2, 0], GREEN),
            ("DMOJ Judge", [-4.2, -0.6, 0], CYAN),
            ("Jobe Server", [-4.2, -2.4, 0], PURPLE),
            ("Piston Engine", [4.2, 1.2, 0], YELLOW),
            ("INGInious", [4.2, -0.6, 0], CYAN),
            ("Runner-Backends", [4.2, -2.4, 0], WHITE)
        ]

        for name, pos, col in judges:
            box = RoundedRectangle(corner_radius=0.1, width=3.4, height=1.0, color=col, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to(pos)
            lbl = Text(name, font_size=9, color=WHITE).move_to(box.get_center())
            j_boxes.add(VGroup(box, lbl))

        self.play(FadeIn(server_g, shift=DOWN), run_time=1.5)
        self.play(LaggedStart(*(FadeIn(jb, shift=UP) for jb in j_boxes), lag_ratio=0.2), run_time=2.0)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 1.5 + 2.0 + 2.0 = 7.5 seconds
        self.wait(get_wait_time("ch23_4_self_hosting", 7.5))

        self.play(FadeOut(server_g), FadeOut(j_boxes), run_time=1.0)

        # ==========================================
        # SECTION 5: FRONTEND-EDITOREN & MOODLE
        # ==========================================
        self.add_sound("audio/ch23_5_editors_moodle.wav")

        title_frontend = Text("23. Frontend-Editoren & Moodle", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_frontend), run_time=1.0)
        self.wait(1.0)

        # Left Column: Web Editors
        ed_box = RoundedRectangle(corner_radius=0.1, width=5.4, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.0, -0.6, 0])
        ed_title = Text("Web-Code-Editoren", font_size=12, color=CYAN, weight=BOLD).next_to(ed_box.get_top(), DOWN, buff=0.25)
        ed_text = Paragraph(
            "Monaco Editor:\n- VS Code Engine im Browser\n- Mächtig mit LSP-Support\n\nCodeMirror:\n- Extrem leichtgewichtig\n- Ideal für Mobilgeräte (v6)",
            font_size=9.5, color=WHITE, line_spacing=0.4
        ).next_to(ed_title, DOWN, buff=0.35).align_to(ed_box, LEFT).shift(RIGHT * 0.4)
        ed_g = VGroup(ed_box, ed_title, ed_text)

        # Right Column: Moodle Integration
        mood_box = RoundedRectangle(corner_radius=0.1, width=5.4, height=3.6, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, -0.6, 0])
        mood_title = Text("Moodle-Anbindung", font_size=12, color=PURPLE, weight=BOLD).next_to(mood_box.get_top(), DOWN, buff=0.25)
        mood_text = Paragraph(
            "VPL (Virtual Programming Lab):\n- Integrierte Auswertung\n- Eigener Bewertungs-Server\n\nCodeRunner:\n- Aufgaben direkt in Fragen\n- Nutzt Jobe Server im Backend",
            font_size=9.5, color=WHITE, line_spacing=0.4
        ).next_to(mood_title, DOWN, buff=0.35).align_to(mood_box, LEFT).shift(RIGHT * 0.4)
        mood_g = VGroup(mood_box, mood_title, mood_text)

        self.play(FadeIn(ed_g, shift=LEFT), FadeIn(mood_g, shift=RIGHT), run_time=2.0)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 2.0 = 6.0 seconds
        self.wait(get_wait_time("ch23_5_editors_moodle", 6.0))

        self.play(FadeOut(ed_g), FadeOut(mood_g), run_time=1.0)

        # ==========================================
        # SECTION 6: ASP.NET CORE MVC & SICHERHEIT
        # ==========================================
        self.add_sound("audio/ch23_6_aspnet.wav")

        title_aspnet = Text("23. Nachbau auf ASP.NET Core MVC", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_aspnet), run_time=1.0)
        self.wait(1.0)

        # Shield for security
        shield = Polygon(
            [-1.5, 1.8, 0], [1.5, 1.8, 0], [1.5, -0.4, 0], [0, -1.8, 0], [-1.5, -0.4, 0],
            color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.5
        ).move_to([0, -0.6, 0])
        shield_lbl = Text("Härterung", font_size=12, color=GREEN, weight=BOLD).next_to(shield.get_top(), DOWN, buff=0.4)
        shield_sub = Text("ASP.NET Core MVC", font_size=10, color=WHITE).next_to(shield_lbl, DOWN, buff=0.2)
        shield_g = VGroup(shield, shield_lbl, shield_sub)

        # Left / Right boxes for platforms to clone
        l_box = RoundedRectangle(corner_radius=0.1, width=4.2, height=2.4, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-4.4, -0.6, 0])
        l_title = Text("Exercism & Open edX", font_size=11, color=CYAN, weight=BOLD).next_to(l_box.get_top(), DOWN, buff=0.2)
        l_desc = Paragraph(
            "- Eigener Lernpfad\n- Sichere REST-API\n- Backend-Kopplung",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(l_title, DOWN, buff=0.2)
        l_g = VGroup(l_box, l_title, l_desc)

        r_box = RoundedRectangle(corner_radius=0.1, width=4.2, height=2.4, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([4.4, -0.6, 0])
        r_title = Text("Moodle-Funktionen", font_size=11, color=PURPLE, weight=BOLD).next_to(r_box.get_top(), DOWN, buff=0.2)
        r_desc = Paragraph(
            "- Datenbank-Sicherheit\n- Strikte CSP Policies\n- Rollensystem (EF Core)",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(r_title, DOWN, buff=0.2)
        r_g = VGroup(r_box, r_title, r_desc)

        self.play(FadeIn(shield_g, scale=0.8), run_time=1.5)
        self.play(FadeIn(l_g, shift=RIGHT), FadeIn(r_g, shift=LEFT), run_time=1.5)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 1.5 + 1.5 + 2.0 = 7.0 seconds
        self.wait(get_wait_time("ch23_6_aspnet", 7.0))

        self.play(FadeOut(shield_g), FadeOut(l_g), FadeOut(r_g), run_time=1.0)

        # ==========================================
        # SECTION 7: KI-PROMPTING
        # ==========================================
        self.add_sound("audio/ch23_7_prompting.wav")

        title_prompt = Text("23. Der KI-Tutor: Prompt-Templates", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_prompt), run_time=1.0)
        self.wait(1.0)

        # 3 Prompt Cards
        card_w, card_h = 3.6, 3.2
        pr1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.6, 0])
        pr1_t = Text("1. Der Erklärer", font_size=11, color=CYAN, weight=BOLD).next_to(pr1.get_top(), DOWN, buff=0.25)
        pr1_txt = Paragraph(
            "Frage bei Fehlermeldungen:\n\n* 'Welche Borrow- oder\n  Ownership-Regel habe\n  ich hier verletzt?'",
            font_size=8, color=WHITE, line_spacing=0.4
        ).next_to(pr1_t, DOWN, buff=0.3)
        g_pr1 = VGroup(pr1, pr1_t, pr1_txt)

        pr2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0.0, -0.6, 0])
        pr2_t = Text("2. Der Reviewer", font_size=11, color=PURPLE, weight=BOLD).next_to(pr2.get_top(), DOWN, buff=0.25)
        pr2_txt = Paragraph(
            "Frage nach dem Lösen:\n\n* 'Wie kann ich diesen\n  Code in Rust\n  idiomatischer schreiben?'",
            font_size=8, color=WHITE, line_spacing=0.4
        ).next_to(pr2_t, DOWN, buff=0.3)
        g_pr2 = VGroup(pr2, pr2_t, pr2_txt)

        pr3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([4.0, -0.6, 0])
        pr3_t = Text("3. Der Generator", font_size=11, color=GREEN, weight=BOLD).next_to(pr3.get_top(), DOWN, buff=0.25)
        pr3_txt = Paragraph(
            "Frage nach Übungen:\n\n* 'Erstelle eine Aufgabe\n  ohne Lösung auf\n  meinem Niveau.'",
            font_size=8, color=WHITE, line_spacing=0.4
        ).next_to(pr3_t, DOWN, buff=0.3)
        g_pr3 = VGroup(pr3, pr3_t, pr3_txt)

        prompts_group = VGroup(g_pr1, g_pr2, g_pr3)
        self.play(FadeIn(prompts_group, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch23_7_prompting", 7.0))

        self.play(FadeOut(prompts_group), run_time=1.0)

        # ==========================================
        # SECTION 8: OUTRO & ÜBUNG
        # ==========================================
        self.add_sound("audio/ch23_8_outro.wav")

        title_outro = Text("23. Deine Übung: Der Lernplan", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Bullet list for outro
        outro_list = VGroup()
        outro_items = [
            ("1. Erstelle deine lernplan.md", "Halte deine persönliche Routine fest.", CYAN),
            ("2. Setze dir klare Lernziele", "Konkrete Themen (z. B. Structs) wählen.", PURPLE),
            ("3. Etabliere Micro-Learning", "Lerne täglich 15 bis 20 Minuten.", YELLOW),
            ("4. Nutze den Compiler als Mentor", "Lies Fehlermeldungen vollständig durch.", GREEN),
            ("5. Nutze KI als Tutor", "Kein Copy-Paste, lass dir Logik erklären.", RUST_ORANGE)
        ]

        for i, (o_title, o_desc, col) in enumerate(outro_items):
            bullet = Dot(color=col).move_to([-4.5, 1.0 - i * 0.65, 0])
            lbl = Text(f"{o_title}: ", font_size=11, color=col, weight=BOLD).next_to(bullet, RIGHT, buff=0.2)
            desc = Text(o_desc, font_size=11, color=WHITE).next_to(lbl, RIGHT, buff=0.1)
            outro_list.add(VGroup(bullet, lbl, desc))

        self.play(LaggedStart(*(FadeIn(ot, shift=RIGHT) for ot in outro_list), lag_ratio=0.25), run_time=2.5)
        self.wait(3.5)

        # Total anim time = 1.0 + 1.0 + 2.5 + 3.5 = 8.0 seconds
        self.wait(get_wait_time("ch23_8_outro", 8.0))

        # Final fade out
        self.play(FadeOut(outro_list), FadeOut(title_group), run_time=1.0)
        
        # Ending credits
        logo = Text("Rust", font_size=64, color=RUST_ORANGE, weight=BOLD)
        logo_sub = Text("Videokurs für Anfänger", font_size=24, color=WHITE)
        logo_g = VGroup(logo, logo_sub).arrange(DOWN, buff=0.3)
        self.play(FadeIn(logo_g, scale=0.8), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(logo_g), run_time=1.0)
        self.wait(1.0)
