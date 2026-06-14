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

class RustSummaryVideo(Scene):
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
            "ch21_1_intro": 35.0,
            "ch21_2_holy_trinity": 35.0,
            "ch21_3_ownership": 35.0,
            "ch21_4_borrowing": 35.0,
            "ch21_5_lifetimes": 35.0,
            "ch21_6_string_str": 35.0,
            "ch21_7_expressions": 35.0,
            "ch21_8_outro": 35.0
        }
        
        durations_path = "audio/durations_ch21.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # Compute total audio duration and required padding per section to hit exactly 300.0 seconds
        total_audio = sum(durations.values())
        padding_per_section = (300.0 - total_audio) / 8.0
        print(f"Total audio: {total_audio}s. Padding per section: {padding_per_section}s.")

        def get_wait_time(key, anim_time):
            d_i = durations[key]
            # wait_time + anim_time + 1.0 (transition) = d_i + padding_per_section
            wait_val = d_i + padding_per_section - anim_time - 1.0
            return max(0.1, wait_val)

        # ==========================================
        # SECTION 1: INTRO & BASICS RÜCKBLICK
        # ==========================================
        self.add_sound("audio/ch21_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 21: Grundlagen-Zusammenfassung & Das Dreigestirn", font_size=18, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 21: Zusammenfassung & Dreigestirn", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Grid of basic concepts
        box_w, box_h = 5.2, 1.4
        
        box1 = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.0, 0.8, 0])
        txt1 = Paragraph("1. Scopes & Gültigkeiten", "let mut x = 5; // Scopes per {}", font_size=9, color=WHITE).move_to(box1.get_center())
        
        box2 = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.0, 0.8, 0])
        txt2 = Paragraph("2. Datentypen", "Skalar (i32, f64...) & Compound (Arrays, Tupel)", font_size=9, color=WHITE).move_to(box2.get_center())
        
        box3 = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.0, -1.0, 0])
        txt3 = Paragraph("3. Kontrollstrukturen", "if-else Schleifen, match-Muster", font_size=9, color=WHITE).move_to(box3.get_center())
        
        box4 = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.0, -1.0, 0])
        txt4 = Paragraph("4. Funktionen & Operatoren", "fn name(x: i32) -> i32", font_size=9, color=WHITE).move_to(box4.get_center())

        grid = VGroup(box1, txt1, box2, txt2, box3, txt3, box4, txt4)
        self.play(FadeIn(grid, shift=UP), run_time=2.0)

        # Animations: 1.5 + 2.5 + 1.5 + 1.0 + 2.0 = 8.5 seconds
        self.wait(get_wait_time("ch21_1_intro", 8.5))

        self.play(FadeOut(grid), run_time=1.0)

        # ==========================================
        # SECTION 2: DAS HEILIGE DREIGESTIRN
        # ==========================================
        self.add_sound("audio/ch21_2_holy_trinity.wav")

        title_trinity = Text("21. Das Heilige Dreigestirn von Rust", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_trinity), run_time=1.0)
        self.wait(1.0)

        # Three pillar cards arranged in a row
        card_w, card_h = 3.6, 3.2
        
        c1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=RUST_ORANGE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-4.0, -0.4, 0])
        c1_title = Text("Säule 1\nOwnership (Besitz)", font_size=12, color=RUST_ORANGE, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.25)
        c1_desc = Paragraph(
            "- Wer besitzt die Daten?\n- Ein Besitzer pro Wert\n- drop am Scope-Ende",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c1_title, DOWN, buff=0.3)
        c1_group = VGroup(c1, c1_title, c1_desc)

        c2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        c2_title = Text("Säule 2\nBorrowing (Ausleihen)", font_size=12, color=CYAN, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.25)
        c2_desc = Paragraph(
            "- Daten sicher teilen\n- &T (viele Leser)\n- &mut T (ein Schreiber)",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c2_title, DOWN, buff=0.3)
        c2_group = VGroup(c2, c2_title, c2_desc)

        c3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([4.0, -0.4, 0])
        c3_title = Text("Säule 3\nLifetimes (Lebensdauern)", font_size=12, color=PURPLE, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.25)
        c3_desc = Paragraph(
            "- Wie lange sind Zeiger gültig?\n- Verhindert Dangling Refs\n- Statische Prüfung",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c3_title, DOWN, buff=0.3)
        c3_group = VGroup(c3, c3_title, c3_desc)

        self.play(
            FadeIn(c1_group, shift=UP),
            FadeIn(c2_group, shift=UP),
            FadeIn(c3_group, shift=UP),
            run_time=2.0
        )
        self.wait(3.0)

        # Speichersicherheit banner at the bottom
        sec_banner = RoundedRectangle(corner_radius=0.08, width=11.6, height=0.6, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -2.4, 0])
        sec_txt = Text("Ergebnis: Speichersicherheit zur Laufzeit ohne Garbage Collector! 🟢", font_size=10, color=GREEN)
        sec_group = VGroup(sec_banner, sec_txt)
        
        self.play(FadeIn(sec_group, shift=DOWN), run_time=1.0)

        # Animations: 1.0 + 1.0 + 2.0 + 3.0 + 1.0 = 8.0 seconds
        self.wait(get_wait_time("ch21_2_holy_trinity", 8.0))

        self.play(
            FadeOut(c1_group), FadeOut(c2_group), FadeOut(c3_group), FadeOut(sec_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: SÄULE 1 - OWNERSHIP (MOVE VS COPY)
        # ==========================================
        self.add_sound("audio/ch21_3_ownership.wav")

        title_own = Text("21. Säule 1: Ownership (Move vs. Copy)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_own), run_time=1.0)
        self.wait(1.0)

        # Compare Move vs Copy visually
        box_w, box_h = 5.2, 3.2
        
        # Left: Move (Heap)
        move_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=RUST_ORANGE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.2, -0.4, 0])
        move_title = Text("Heap-Daten: MOVE", font_size=11, color=RUST_ORANGE, weight=BOLD).next_to(move_box.get_top(), DOWN, buff=0.2)
        move_flow = Paragraph(
            "let s1 = String::from(\"Hallo\");",
            "let s2 = s1; // MOVE von s1 zu s2",
            "",
            "s1 ist danach UNGÜLTIG! ❌",
            "Speicherbesitzer hat gewechselt.",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(move_title, DOWN, buff=0.3).align_to(move_box, LEFT).shift(RIGHT * 0.4)
        move_group = VGroup(move_box, move_title, move_flow)

        # Right: Copy (Stack)
        copy_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.2, -0.4, 0])
        copy_title = Text("Stack-Daten: COPY", font_size=11, color=GREEN, weight=BOLD).next_to(copy_box.get_top(), DOWN, buff=0.2)
        copy_flow = Paragraph(
            "let x = 42;",
            "let y = x; // COPY",
            "",
            "Beide sind WEITERHIN GÜLTIG! 🟢",
            "Stack-Werte kopieren sich automatisch.",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(copy_title, DOWN, buff=0.3).align_to(copy_box, LEFT).shift(RIGHT * 0.4)
        copy_group = VGroup(copy_box, copy_title, copy_flow)

        self.play(
            FadeIn(move_group, shift=RIGHT),
            FadeIn(copy_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(4.0)

        # Animations: 1.0 + 1.0 + 2.0 + 4.0 = 8.0 seconds
        self.wait(get_wait_time("ch21_3_ownership", 8.0))

        self.play(FadeOut(move_group), FadeOut(copy_group), run_time=1.0)

        # ==========================================
        # SECTION 4: SÄULE 2 - BORROWING (RULES)
        # ==========================================
        self.add_sound("audio/ch21_4_borrowing.wav")

        title_borrow = Text("21. Säule 2: Borrowing (Die Ausleihregeln)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_borrow), run_time=1.0)
        self.wait(1.0)

        # Visualizing Leser vs Schreiber
        res_card = RoundedRectangle(corner_radius=0.1, width=3.2, height=1.6, color=GRAY, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.0, 0])
        res_title = Text("Ressource im Speicher", font_size=10, color=WHITE, weight=BOLD).next_to(res_card.get_top(), DOWN, buff=0.2)
        res_val = Text("\"Rust Daten\"", font_size=12, color=WHITE).next_to(res_title, DOWN, buff=0.25)
        res_group = VGroup(res_card, res_title, res_val)

        # Scenario 1: Beliebig viele Leser
        leser1 = RoundedRectangle(corner_radius=0.05, width=2.2, height=0.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([-3.2, -1.2, 0])
        leser1_txt = Paragraph("Leser 1 (&T)", "liest Daten", font_size=8, color=CYAN).move_to(leser1.get_center())
        arrow_l1 = Arrow(start=leser1.get_top(), end=res_card.get_left(), color=CYAN, buff=0.1)

        leser2 = RoundedRectangle(corner_radius=0.05, width=2.2, height=0.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([3.2, -1.2, 0])
        leser2_txt = Paragraph("Leser 2 (&T)", "liest Daten", font_size=8, color=CYAN).move_to(leser2.get_center())
        arrow_l2 = Arrow(start=leser2.get_top(), end=res_card.get_right(), color=CYAN, buff=0.1)

        self.play(FadeIn(res_group, shift=DOWN), run_time=1.5)
        self.play(
            FadeIn(leser1), FadeIn(leser1_txt), Create(arrow_l1),
            FadeIn(leser2), FadeIn(leser2_txt), Create(arrow_l2),
            run_time=1.5
        )
        self.wait(3.0)

        # Transition to Scenario 2: Exklusiv ein Schreiber (Leser verschwinden)
        schreiber = RoundedRectangle(corner_radius=0.05, width=3.2, height=0.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([0, -1.2, 0])
        schreiber_txt = Paragraph("Schreiber (&mut T)", "exklusiver Schreib-/Lesezugriff", font_size=8, color=GREEN).move_to(schreiber.get_center())
        arrow_sch = Arrow(start=schreiber.get_top(), end=res_card.get_bottom(), color=GREEN, buff=0.1)

        self.play(
            FadeOut(leser1), FadeOut(leser1_txt), FadeOut(arrow_l1),
            FadeOut(leser2), FadeOut(leser2_txt), FadeOut(arrow_l2),
            run_time=1.0
        )
        self.play(FadeIn(schreiber), FadeIn(schreiber_txt), Create(arrow_sch), run_time=1.0)
        self.wait(3.0)

        # Banner for Rules
        rule_banner = RoundedRectangle(corner_radius=0.08, width=11.6, height=0.6, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, 2.2, 0])
        rule_txt = Text("Entweder viele Leser (&T) ODER ein Schreiber (&mut T) - Niemals beides! ⚠️", font_size=9, color=YELLOW, weight=BOLD)
        rule_group = VGroup(rule_banner, rule_txt)
        self.play(FadeIn(rule_group, shift=DOWN), run_time=1.0)

        # Animations: 1.0 + 1.0 + 1.5 + 1.5 + 3.0 + 1.0 + 1.0 + 3.0 + 1.0 = 14.0 seconds
        self.wait(get_wait_time("ch21_4_borrowing", 14.0))

        self.play(
            FadeOut(res_group), FadeOut(schreiber), FadeOut(schreiber_txt), FadeOut(arrow_sch), FadeOut(rule_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: SÄULE 3 - LIFETIMES (DANGLING)
        # ==========================================
        self.add_sound("audio/ch21_5_lifetimes.wav")

        title_life = Text("21. Säule 3: Lifetimes (Lebensdauern)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_life), run_time=1.0)
        self.wait(1.0)

        # Visualizing Lifetime Lines
        owner_bar = RoundedRectangle(corner_radius=0.05, width=8.0, height=0.4, color=GREEN, fill_color=GREEN, fill_opacity=0.4).move_to([0, 0.6, 0])
        owner_lbl = Text("Besitzer (lebt lang)", font_size=10, color=WHITE).next_to(owner_bar, LEFT, buff=0.3)
        
        ref_bar = RoundedRectangle(corner_radius=0.05, width=5.0, height=0.4, color=CYAN, fill_color=CYAN, fill_opacity=0.4).move_to([-1.5, -0.4, 0])
        ref_lbl = Text("Referenz (lebt kürzer)", font_size=10, color=WHITE).next_to(ref_bar, LEFT, buff=0.3)

        self.play(FadeIn(owner_bar), FadeIn(owner_lbl), run_time=1.5)
        self.play(FadeIn(ref_bar), FadeIn(ref_lbl), run_time=1.5)
        self.wait(3.0)

        # Dangling Reference illustration
        bad_ref_bar = RoundedRectangle(corner_radius=0.05, width=9.0, height=0.4, color=RED, fill_color=RED, fill_opacity=0.4).move_to([0.5, -1.4, 0])
        bad_ref_lbl = Text("Referenz lebt länger! ❌", font_size=10, color=RED).next_to(bad_ref_bar, LEFT, buff=0.3)
        
        cross = Cross(bad_ref_bar, stroke_color=RED, stroke_width=4)

        self.play(FadeIn(bad_ref_bar), FadeIn(bad_ref_lbl), run_time=1.5)
        self.play(Create(cross), run_time=1.0)
        self.wait(3.0)

        # Animations: 1.0 + 1.0 + 1.5 + 1.5 + 3.0 + 1.5 + 1.0 + 3.0 = 13.5 seconds
        self.wait(get_wait_time("ch21_5_lifetimes", 13.5))

        self.play(
            FadeOut(owner_bar), FadeOut(owner_lbl), FadeOut(ref_bar), FadeOut(ref_lbl),
            FadeOut(bad_ref_bar), FadeOut(bad_ref_lbl), FadeOut(cross),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: STRING VS &str (MEMORY)
        # ==========================================
        self.add_sound("audio/ch21_6_string_str.wav")

        title_str = Text("21. String vs. &str (Besitzer vs. Gast)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_str), run_time=1.0)
        self.wait(1.0)

        # String vs &str visual representations
        box_w, box_h = 5.2, 3.2
        
        # Left: String
        string_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.2, -0.4, 0])
        string_title = Text("String (Heap)", font_size=11, color=GREEN, weight=BOLD).next_to(string_box.get_top(), DOWN, buff=0.2)
        string_desc = Paragraph(
            "- Eigener Speicherbesitz\n- Dynamisch veränderbar\n- Liegt auf dem Heap\n- Let mut s = String::new();\n- Belegt Speicher variabel",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(string_title, DOWN, buff=0.3).align_to(string_box, LEFT).shift(RIGHT * 0.4)
        string_group = VGroup(string_box, string_title, string_desc)

        # Right: &str
        str_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.2, -0.4, 0])
        str_title = Text("&str (String-Slice)", font_size=11, color=CYAN, weight=BOLD).next_to(str_box.get_top(), DOWN, buff=0.2)
        str_desc = Paragraph(
            "- Ein reiner Gast / Zeiger\n- Unveränderliche Sicht\n- Zeigt auf Textbereich\n- Let s: &str = \"Hallo\";\n- Belegt exakt 16 Byte (Stack)",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(str_title, DOWN, buff=0.3).align_to(str_box, LEFT).shift(RIGHT * 0.4)
        str_group = VGroup(str_box, str_title, str_desc)

        self.play(
            FadeIn(string_group, shift=RIGHT),
            FadeIn(str_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(4.0)

        # Animations: 1.0 + 1.0 + 2.0 + 4.0 = 8.0 seconds
        self.wait(get_wait_time("ch21_6_string_str", 8.0))

        self.play(FadeOut(string_group), FadeOut(str_group), run_time=1.0)

        # ==========================================
        # SECTION 7: KONTROLLSTRUKTUREN ALS AUSDRÜCKE
        # ==========================================
        self.add_sound("audio/ch21_7_expressions.wav")

        title_expr = Text("21. Kontrollstrukturen als Ausdrücke", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_expr), run_time=1.0)
        self.wait(1.0)

        # Code showing expressions in if/else and match
        expr_box = RoundedRectangle(corner_radius=0.1, width=11.2, height=3.6, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        expr_title = Text("if-else und match liefern Werte zurück", font_size=11, color=PURPLE, weight=BOLD).next_to(expr_box.get_top(), DOWN, buff=0.2)
        
        expr_lines = Paragraph(
            "let status = if alter >= 18 {",
            "    \"Volljährig\" // Kein Semikolon!",
            "} else {",
            "    \"Minderjährig\"",
            "};",
            "",
            "let bewertung = match note {",
            "    1..=3 => \"Bestanden\",",
            "    _     => \"Nicht bestanden\", // Fallback",
            "};",
            font="Monospace", font_size=8.5, color=WHITE, line_spacing=0.45
        ).next_to(expr_title, DOWN, buff=0.25).align_to(expr_box, LEFT).shift(RIGHT * 1.5)

        self.play(FadeIn(expr_box, shift=UP), FadeIn(expr_title), run_time=1.5)
        self.play(FadeIn(expr_lines, shift=DOWN), run_time=2.0)
        self.wait(4.0)

        # Highlight match fallback
        fb_highlight = SurroundingRectangle(expr_lines[8], color=YELLOW, stroke_width=1.5)
        fb_lbl = Text("Unterstrich deckt alles ab!", font_size=8, color=YELLOW).next_to(fb_highlight, RIGHT, buff=0.3)
        self.play(Create(fb_highlight), FadeIn(fb_lbl, shift=LEFT), run_time=1.0)
        self.wait(1.0)

        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 4.0 + 1.0 + 1.0 = 11.5 seconds
        self.wait(get_wait_time("ch21_7_expressions", 11.5))

        self.play(
            FadeOut(expr_box), FadeOut(expr_title), FadeOut(expr_lines), FadeOut(fb_highlight), FadeOut(fb_lbl),
            run_time=1.0
        )

        # ==========================================
        # SECTION 8: OUTRO & AUSBLICK
        # ==========================================
        self.add_sound("audio/ch21_8_outro.wav")

        title_outro = Text("21. Zusammenfassung: Wie geht es weiter?", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Outro Board with next steps
        board = RoundedRectangle(corner_radius=0.15, width=11.6, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.5).move_to([0, -0.4, 0])
        
        step_title = Text("Nächste Ausbildungs-Themen:", font_size=12, color=CYAN, weight=BOLD)
        steps = Paragraph(
            "1. Strukturen (Structs) & Methoden (eigene komplexe Datentypen)\n"
            "2. Vektoren (Vec) - dynamisch wachsende Listen auf dem Heap\n"
            "3. Enums & Fortgeschrittenes Pattern Matching\n"
            "4. Traits & Generics (wiederverwendbare Schnittstellen)",
            font_size=9, color=WHITE, line_spacing=0.4
        )
        steps_v = VGroup(step_title, steps).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(board.get_center())

        self.play(Create(board), run_time=1.5)
        self.play(FadeIn(steps_v, shift=UP), run_time=2.0)
        self.wait(4.0)

        outro_text = Text("Vielen Dank fürs Zuschauen! Viel Erfolg bei den Challenges.", font_size=14, color=YELLOW).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(outro_text, shift=DOWN), run_time=1.5)

        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 4.0 + 1.5 = 11.0 seconds
        self.wait(get_wait_time("ch21_8_outro", 11.0))

        self.play(
            FadeOut(board), FadeOut(steps_v), FadeOut(outro_text), FadeOut(title_group),
            run_time=1.0
        )
        self.wait(0.1)
