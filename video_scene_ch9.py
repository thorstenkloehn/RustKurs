from manim import *
import numpy as np
import json

# Harmonious design palette
BG_COLOR = "#0f172a"      # Sleek slate-900 background
RUST_ORANGE = "#ea580c"   # Vibrant Rust Orange
CYAN = "#06b6d4"          # Accent Cyan
PURPLE = "#8b5cf6"        # Accent Purple/Violet
WHITE = "#f1f5f9"         # Off-white text
GRAY = "#64748b"          # Slate-500 for secondary elements and borders
GREEN = "#10b981"         # Emerald-500 for positives
RED = "#ef4444"           # Red-500 for challenges/errors
YELLOW = "#f59e0b"        # Yellow-500 for warnings/info
LIGHT_BG = "#1e293b"      # slate-800 for card backgrounds
TERM_BG = "#090d16"       # Dark deep blue for terminal windows

def create_terminal_window(width, height, title_text):
    window = RoundedRectangle(corner_radius=0.15, width=width, height=height, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2)
    header_bar = Line(
        start=[-width/2, height/2 - 0.45, 0], 
        end=[width/2, height/2 - 0.45, 0], 
        color=GRAY, 
        stroke_width=2
    )
    red_dot = Circle(radius=0.07, color=RED, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.25, height/2 - 0.22, 0])
    yellow_dot = Circle(radius=0.07, color=YELLOW, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.45, height/2 - 0.22, 0])
    green_dot = Circle(radius=0.07, color=GREEN, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.65, height/2 - 0.22, 0])
    title = Text(title_text, font_size=11, color=GRAY).move_to([0, height/2 - 0.22, 0])
    return VGroup(window, header_bar, red_dot, yellow_dot, green_dot, title)

class RustSummaryVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Load durations
        try:
            with open("audio/durations_ch9.json", "r") as f:
                durations = json.load(f)
        except Exception:
            durations = {
                "ch9_1_intro": 13.0,
                "ch9_2_mutability": 20.0,
                "ch9_3_constants": 20.0,
                "ch9_4_shadowing": 20.0,
                "ch9_5_scalar_types": 25.0,
                "ch9_6_tuples": 22.0,
                "ch9_7_arrays": 22.0,
                "ch9_8_outro": 20.0
            }

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        dur_1 = durations["ch9_1_intro"]
        self.add_sound("audio/ch9_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 9: Zusammenfassung\nVariablen & Datentypen", font_size=28, color=CYAN).arrange(DOWN, buff=0.2)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)

        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0) # total 3.0s

        title_small = Text("Kapitel 9: Zusammenfassung", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5) # total 4.5s
        self.wait(0.5) # total 5.0s

        intro_badge = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.5).move_to([0, 0, 0])
        intro_badge_text = Text("Kompakter Überblick über Variablen, Konstanten,\nShadowing, Skalare & Zusammengesetzte Typen", font_size=13, color=WHITE).move_to(intro_badge.get_center())
        intro_badge_group = VGroup(intro_badge, intro_badge_text)

        self.play(FadeIn(intro_badge_group, shift=UP), run_time=1.5) # total 6.5s
        self.wait(max(0.1, dur_1 - 6.5 - 1.0))
        self.play(FadeOut(intro_badge_group), FadeOut(title_group), run_time=1.0)


        # ==========================================
        # SECTION 2: MUTABILITY
        # ==========================================
        dur_2 = durations["ch9_2_mutability"]
        self.add_sound("audio/ch9_2_mutability.wav")

        sec2_title = Text("1. Variablen & Veränderlichkeit (Mutability)", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Card Unveränderlich
        card_immut = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.8, color=RED, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.0, 0.2, 0])
        ci_title = Text("Unveränderlich (Standard)", font_size=14, color=RED, weight=BOLD).next_to(card_immut.get_top(), DOWN, buff=0.25)
        ci_desc = Paragraph(
            "let x = 5;",
            "// x = 6;  // ✘ FEHLER!",
            "Wert kann nachträglich\nnicht geändert werden.",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(ci_title, DOWN, buff=0.3).align_to(ci_title, LEFT).shift(LEFT * 0.4)
        ci_group = VGroup(card_immut, ci_title, ci_desc)

        # Card Veränderlich mit mut
        card_mut = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.0, 0.2, 0])
        cm_title = Text("Veränderlich mit mut", font_size=14, color=GREEN, weight=BOLD).next_to(card_mut.get_top(), DOWN, buff=0.25)
        cm_desc = Paragraph(
            "let mut x = 5;",
            "x = 6;  // ✔ ERLAUBT!",
            "Ermöglicht das",
            "Überschreiben des Werts.",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(cm_title, DOWN, buff=0.3).align_to(cm_title, LEFT).shift(LEFT * 0.4)
        cm_group = VGroup(card_mut, cm_title, cm_desc)

        self.play(FadeIn(ci_group, shift=RIGHT), FadeIn(cm_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(max(0.1, dur_2 - 3.5 - 1.0))
        self.play(FadeOut(ci_group), FadeOut(cm_group), FadeOut(sec2_title), run_time=1.0)


        # ==========================================
        # SECTION 3: CONSTANTS
        # ==========================================
        dur_3 = durations["ch9_3_constants"]
        self.add_sound("audio/ch9_3_constants.wav")

        sec3_title = Text("2. Konstanten (const)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Code editor window
        editor3 = create_terminal_window(11.0, 3.2, "src/main.rs").move_to([0, 0.3, 0])
        code_text3 = Paragraph(
            "// 1. Immer unveränderlich (kein mut erlaubt)",
            "// 2. Datentyp muss zwingend angegeben werden",
            "const DREI_STUNDEN_IN_SEKUNDEN: u32 = 60 * 60 * 3;",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor3.get_center()).shift(LEFT * 1.0 + UP * 0.1)

        self.play(FadeIn(editor3), FadeIn(code_text3), run_time=1.5) # total 3.5s
        self.wait(6.5) # total 10.0s

        # Details badge below
        info_badge3 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.4, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.4, 0])
        ib3_text = Text("Konstanten werden zur Kompilierzeit berechnet.\nSie sind ideal für globale, feststehende Werte im gesamten Code.", font_size=12, color=WHITE).move_to(info_badge3.get_center())
        ib3_group = VGroup(info_badge3, ib3_text)

        self.play(FadeIn(ib3_group, shift=UP), run_time=1.5) # total 11.5s
        self.wait(max(0.1, dur_3 - 11.5 - 1.0))
        self.play(FadeOut(editor3), FadeOut(code_text3), FadeOut(ib3_group), FadeOut(sec3_title), run_time=1.0)


        # ==========================================
        # SECTION 4: SHADOWING
        # ==========================================
        dur_4 = durations["ch9_4_shadowing"]
        self.add_sound("audio/ch9_4_shadowing.wav")

        sec4_title = Text("3. Shadowing (Überschatten)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        editor4 = create_terminal_window(11.0, 3.4, "src/main.rs").move_to([0, 0.4, 0])
        code_text4 = Paragraph(
            "let x = 5;",
            "let x = x + 1; // x wird überschattet zu 6",
            "",
            "let spaces = \"   \";        // Typ: &str",
            "let spaces = spaces.len(); // Typ: usize (Länge: 3)",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor4.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor4), FadeIn(code_text4), run_time=1.5) # total 3.5s
        self.wait(6.5) # total 10.0s

        # Shadowing summary card
        shadow_card = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.4, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, -2.4, 0])
        sc_text = Text("Mit let darfst du denselben Namen wiederverwenden.\nDas erlaubt Typänderungen, ohne neue Variablennamen zu erfinden.", font_size=11, color=WHITE).move_to(shadow_card.get_center())
        sc_group = VGroup(shadow_card, sc_text)

        self.play(FadeIn(sc_group, shift=UP), run_time=1.5) # total 11.5s
        self.wait(max(0.1, dur_4 - 11.5 - 1.0))
        self.play(FadeOut(editor4), FadeOut(code_text4), FadeOut(sc_group), FadeOut(sec4_title), run_time=1.0)


        # ==========================================
        # SECTION 5: SCALAR TYPES
        # ==========================================
        dur_5 = durations["ch9_5_scalar_types"]
        self.add_sound("audio/ch9_5_scalar_types.wav")

        sec5_title = Text("4. Skalare Datentypen", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # 4 cards representing integers, floats, booleans, char
        card_w5, card_h5 = 5.2, 1.8
        c1 = RoundedRectangle(corner_radius=0.1, width=card_w5, height=card_h5, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.0, 1.2, 0])
        c1_t = Text("Ganzzahlen (Integers)", font_size=13, color=CYAN, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.15)
        c1_d = Text("i8..i128 (mit Vorzeichen)\nu8..u128 (ohne), Standard: i32", font_size=10, color=WHITE).next_to(c1_t, DOWN, buff=0.1)
        g1 = VGroup(c1, c1_t, c1_d)

        c2 = RoundedRectangle(corner_radius=0.1, width=card_w5, height=card_h5, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.0, 1.2, 0])
        c2_t = Text("Fließkommazahlen (Floats)", font_size=13, color=PURPLE, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.15)
        c2_d = Text("f32 & f64\nStandard: f64 (doppelte Genauigkeit)", font_size=10, color=WHITE).next_to(c2_t, DOWN, buff=0.1)
        g2 = VGroup(c2, c2_t, c2_d)

        c3 = RoundedRectangle(corner_radius=0.1, width=card_w5, height=card_h5, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.0, -1.2, 0])
        c3_t = Text("Wahrheitswerte (Booleans)", font_size=13, color=GREEN, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.15)
        c3_d = Text("bool\nKann true oder false sein (1 Byte)", font_size=10, color=WHITE).next_to(c3_t, DOWN, buff=0.1)
        g3 = VGroup(c3, c3_t, c3_d)

        c4 = RoundedRectangle(corner_radius=0.1, width=card_w5, height=card_h5, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.0, -1.2, 0])
        c4_t = Text("Zeichen (Characters)", font_size=13, color=YELLOW, weight=BOLD).next_to(c4.get_top(), DOWN, buff=0.15)
        c4_d = Text("char (4 Bytes)\nUnicode-Zeichen, z.B. 'z' oder '😻'", font_size=10, color=WHITE).next_to(c4_t, DOWN, buff=0.1)
        g4 = VGroup(c4, c4_t, c4_d)

        self.play(FadeIn(g1, shift=RIGHT), FadeIn(g2, shift=LEFT), run_time=1.5) # total 3.5s
        self.play(FadeIn(g3, shift=RIGHT), FadeIn(g4, shift=LEFT), run_time=1.5) # total 5.0s

        self.wait(max(0.1, dur_5 - 5.0 - 1.0))
        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(g4), FadeOut(sec5_title), run_time=1.0)


        # ==========================================
        # SECTION 6: TUPLE
        # ==========================================
        dur_6 = durations["ch9_6_tuples"]
        self.add_sound("audio/ch9_6_tuples.wav")

        sec6_title = Text("5. Das Tupel (Tuple)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec6_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Visual Tuple
        tuple_container = RoundedRectangle(corner_radius=0.15, width=7.5, height=1.3, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 1.2, 0])
        bracket_l = Text("(", font_size=38, color=PURPLE, weight=BOLD).next_to(tuple_container, LEFT, buff=0.2)
        bracket_r = Text(")", font_size=38, color=PURPLE, weight=BOLD).next_to(tuple_container, RIGHT, buff=0.2)
        elem1 = Text('"Molly"', font_size=14, color=CYAN).move_to(tuple_container.get_center()).shift(LEFT * 2.2)
        elem2 = Text('32', font_size=14, color=GREEN).move_to(tuple_container.get_center())
        elem3 = Text('true', font_size=14, color=CYAN).move_to(tuple_container.get_center()).shift(RIGHT * 2.2)
        commas = VGroup(
            Text(",", font_size=14, color=WHITE).next_to(elem1, RIGHT, buff=0.7),
            Text(",", font_size=14, color=WHITE).next_to(elem2, RIGHT, buff=0.8)
        )
        tuple_visual = VGroup(tuple_container, bracket_l, bracket_r, elem1, elem2, elem3, commas)

        self.play(FadeIn(tuple_visual, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Code editor below
        editor6 = create_terminal_window(11.0, 2.6, "src/main.rs").move_to([0, -1.5, 0])
        code_text6 = Paragraph(
            "let tup: (&str, i32, bool) = (\"Molly\", 32, true);",
            "let name = tup.0; // Zugriff via Punkt-Notation",
            "let (n, a, active) = tup; // Entpacken (Destrukturierung)",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(editor6.get_center()).shift(LEFT * 1.2 + UP * 0.1)

        self.play(FadeIn(editor6), FadeIn(code_text6), run_time=1.5) # total 9.5s
        self.wait(max(0.1, dur_6 - 9.5 - 1.0))
        self.play(FadeOut(tuple_visual), FadeOut(editor6), FadeOut(code_text6), FadeOut(sec6_title), run_time=1.0)


        # ==========================================
        # SECTION 7: ARRAYS
        # ==========================================
        dur_7 = durations["ch9_7_arrays"]
        self.add_sound("audio/ch9_7_arrays.wav")

        sec7_title = Text("6. Das Array", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec7_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Grid box representing array
        array_boxes = VGroup(*[
            Square(side_length=0.9, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.15).move_to([0, 1.2, 0])
        
        vals = [1, 2, 3, 4, 5]
        array_texts = VGroup(*[
            Text(str(val), font_size=18, color=WHITE).move_to(box.get_center())
            for val, box in zip(vals, array_boxes)
        ])
        array_indices = VGroup(*[
            Text(f"[{i}]", font_size=11, color=GRAY).next_to(box, DOWN, buff=0.15)
            for i, box in enumerate(array_boxes)
        ])
        array_visual = VGroup(array_boxes, array_texts, array_indices)

        self.play(Create(array_boxes), Write(array_texts), FadeIn(array_indices), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Warning panel below showing Panic case
        editor7 = create_terminal_window(11.0, 2.6, "src/main.rs").move_to([0, -1.5, 0])
        code_text7 = Paragraph(
            "let a: [i32; 5] = [1, 2, 3, 4, 5];",
            "let first = a[0]; // Erster Wert",
            "let element = a[10]; // ✘ FEHLER! Program panic (Absturz)",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(editor7.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor7), FadeIn(code_text7), run_time=1.5) # total 9.5s
        self.wait(4.5) # total 14.0s

        # Draw red warning highlight
        warn_box = RoundedRectangle(corner_radius=0.1, width=6.8, height=0.6, color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=2.0).move_to([0, -2.8, 0])
        warn_text = Text("⚠ Sicherheit: Rust verhindert ungültigen Speicherzugriff!", font_size=11, color=RED, weight=BOLD).move_to(warn_box.get_center())
        warn_group = VGroup(warn_box, warn_text)

        self.play(FadeIn(warn_group, shift=UP), run_time=1.0) # total 15.0s
        self.wait(max(0.1, dur_7 - 15.0 - 1.0))
        self.play(FadeOut(array_visual), FadeOut(editor7), FadeOut(code_text7), FadeOut(warn_group), FadeOut(sec7_title), run_time=1.0)


        # ==========================================
        # SECTION 8: OUTRO
        # ==========================================
        dur_8 = durations["ch9_8_outro"]
        self.add_sound("audio/ch9_8_outro.wav")

        sec8_title = Text("Zusammenfassung Variablen & Datentypen", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec8_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Card summary
        summary_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0, 0])
        sc_title = Text("💡 Rust Grundlagen gemeistert:", font_size=15, color=CYAN, weight=BOLD).next_to(summary_card.get_top(), DOWN, buff=0.25)
        sc_desc = Paragraph(
            "• Immutabilität als Standard sorgt für vorhersagbaren Code.\n"
            "• Statische Typsicherheit verhindert Laufzeitfehler vorab.\n"
            "• Automatische Grenzenkontrollen schützen den Speicher vor Fehlern.\n"
            "• Hohe Performance ohne Ressourcenverschwendung.",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(sc_title, DOWN, buff=0.2).align_to(sc_title, LEFT).shift(LEFT * 0.4)
        sc_group = VGroup(summary_card, sc_title, sc_desc)

        self.play(FadeIn(sc_group, shift=UP), run_time=1.5) # total 3.5s
        self.wait(8.5) # total 12.0s

        # Outro text showing end of part 1
        outro_card = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.6, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).move_to([0, 0, 0])
        outro_text = Text("Ende von Teil 1:\nVariablen & Datentypen", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        outro_group = VGroup(outro_card, outro_text)

        self.play(
            FadeOut(sc_group),
            FadeIn(outro_group, scale=0.8),
            run_time=2.0
        ) # total 14.0s

        self.wait(max(0.1, dur_8 - 14.0 - 1.0))
        self.play(FadeOut(outro_group), FadeOut(sec8_title), run_time=1.0)
