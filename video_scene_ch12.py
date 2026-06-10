from manim import *
import json
import numpy as np

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

class RustOperatorsVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Load durations
        try:
            with open("audio/durations_ch12.json", "r") as f:
                durations = json.load(f)
        except Exception:
            durations = {
                "ch12_1_intro": 35.90,
                "ch12_2_arithmetic_comparison": 64.43,
                "ch12_3_logical_bitwise": 63.21,
                "ch12_4_assignment_references": 56.51,
                "ch12_5_casting_error_ranges": 51.14,
                "ch12_6_outro": 24.81
            }

        # ==========================================
        # SECTION 1: INTRO (35.90 seconds)
        # ==========================================
        dur_1 = durations["ch12_1_intro"]
        self.add_sound("audio/ch12_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 12: Operatoren", font_size=30, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4).shift(UP * 0.5)

        self.play(FadeIn(title_group, shift=UP), run_time=1.2)
        self.wait(2.0)

        title_small = Text("Kapitel 12: Operatoren", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        # Overview badge
        intro_badge = RoundedRectangle(corner_radius=0.15, width=9.5, height=2.4, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.5).shift(UP * 0.1)
        intro_badge_text = Text(
            "• Arithmetische & Vergleichsoperatoren\n"
            "• Logische & Bitweise Operationen\n"
            "• Zuweisungen, Referenzen und Borrowing\n"
            "• Typumwandlung (as), Ranges (..) und Fehlerbehandlung (?)", 
            font_size=12, color=WHITE, line_spacing=0.6
        ).move_to(intro_badge.get_center())
        intro_badge_group = VGroup(intro_badge, intro_badge_text)

        self.play(FadeIn(intro_badge_group, shift=UP), run_time=1.5)
        self.wait(5.0)

        # Let's animate some introductory bullets below or replace the badge to keep active animation
        bullets_intro = VGroup(
            Text("• Strikte Typprüfung zur Kompilierzeit", font_size=15, color=WHITE),
            Text("• Fokus auf Speichersicherheit & Ownership", font_size=15, color=WHITE),
            Text("• Keine implizite Typkonvertierung", font_size=15, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 2.0)

        self.play(FadeIn(bullets_intro[0], shift=RIGHT), run_time=1.2)
        self.wait(5.0)
        self.play(FadeIn(bullets_intro[1], shift=RIGHT), run_time=1.2)
        self.wait(5.0)
        self.play(FadeIn(bullets_intro[2], shift=RIGHT), run_time=1.2)

        self.wait(max(0.1, dur_1 - 1.2 - 2.0 - 1.5 - 0.5 - 1.5 - 5.0 - 1.2 - 5.0 - 1.2 - 5.0 - 1.0))
        self.play(FadeOut(intro_badge_group), FadeOut(bullets_intro), FadeOut(title_group), run_time=1.0)

        # ==========================================
        # SECTION 2: ARITHMETIC & COMPARISON (64.43 seconds)
        # ==========================================
        dur_2 = durations["ch12_2_arithmetic_comparison"]
        self.add_sound("audio/ch12_2_arithmetic_comparison.wav")

        sec2_title = Text("1. Arithmetische & Vergleichsoperatoren", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # --- PART A: Arithmetic Operators (0s - 32s) ---
        editor2_a = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text2_a = Paragraph(
            "fn main() {",
            "    let a = 10;",
            "    let b = 3;",
            "    let summe = a + b;     // Addition: 13",
            "    let quotient = a / b;  // Ganzzahldivision: 3",
            "    let rest = a % b;      // Modulo (Restwert): 1",
            "}",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(editor2_a.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor2_a), FadeIn(code_text2_a), run_time=1.5)
        self.wait(8.0)

        # Highlight quotient (integer division)
        int_div_highlight = RoundedRectangle(corner_radius=0.05, width=9.2, height=0.35, color=CYAN, fill_opacity=0.15, stroke_width=1.5).move_to(code_text2_a[4].get_center())
        int_div_label = Text("Ganzzahldivision schneidet den Nachkommateil ab!", font_size=11, color=CYAN).next_to(editor2_a, DOWN, buff=0.3)
        self.play(Create(int_div_highlight), FadeIn(int_div_label, shift=UP), run_time=1.2)
        self.wait(8.0)

        # Let's show float division as alternative
        editor2_b = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text2_b = Paragraph(
            "fn main() {",
            "    let x = 10.0;",
            "    let y = 3.0;",
            "    let exakt = x / y;     // Fließkommadivision: 3.3333333333333335",
            "    // Beides müssen Fließkommazahlen sein!",
            "}",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(editor2_b.get_center()).shift(LEFT * 1.2 + UP * 0.1)

        self.play(
            FadeOut(code_text2_a), FadeOut(int_div_highlight), FadeOut(int_div_label),
            FadeIn(code_text2_b),
            run_time=1.5
        )
        self.wait(10.0)

        # --- PART B: Comparison Operators (32s - 62s) ---
        editor2_c = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text2_c = Paragraph(
            "fn main() {",
            "    let alter = 18;",
            "    let mindestalter = 18;",
            "    let ist_volljaehrig = alter >= mindestalter; // true",
            "    let ist_identisch = alter == mindestalter;   // true",
            "    // let fehler = alter == 18.0; // ✘ COMPILERFEHLER!",
            "}",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(editor2_c.get_center()).shift(LEFT * 1.0 + UP * 0.1)

        error_label = Text("Typzwang: Kein impliziter Vergleich zwischen i32 und f64!", font_size=11, color=RED).next_to(editor2_c, DOWN, buff=0.3)
        error_highlight = RoundedRectangle(corner_radius=0.05, width=9.2, height=0.35, color=RED, fill_opacity=0.15, stroke_width=1.5).move_to(code_text2_c[5].get_center())

        self.play(
            FadeOut(editor2_b), FadeOut(code_text2_b),
            FadeIn(editor2_c), FadeIn(code_text2_c),
            run_time=1.5
        )
        self.wait(12.0)

        self.play(Create(error_highlight), FadeIn(error_label, shift=UP), run_time=1.2)
        self.wait(12.0)

        self.wait(max(0.1, dur_2 - 1.0 - 1.0 - 1.5 - 8.0 - 1.2 - 8.0 - 1.5 - 10.0 - 1.5 - 12.0 - 1.2 - 12.0 - 1.0))
        self.play(FadeOut(editor2_c), FadeOut(code_text2_c), FadeOut(error_highlight), FadeOut(error_label), FadeOut(sec2_title), run_time=1.0)

        # ==========================================
        # SECTION 3: LOGICAL & BITWISE (63.21 seconds)
        # ==========================================
        dur_3 = durations["ch12_3_logical_bitwise"]
        self.add_sound("audio/ch12_3_logical_bitwise.wav")

        sec3_title = Text("2. Logische & Bitweise Operatoren", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # --- PART A: Logical Operators & Short-Circuit (0s - 30s) ---
        left_card = RoundedRectangle(corner_radius=0.12, width=5.8, height=3.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.2, 0.1, 0])
        lc_title = Text("Logisch & Short-Circuit", font_size=13, color=CYAN, weight=BOLD).next_to(left_card.get_top(), DOWN, buff=0.2)
        lc_body = Paragraph(
            "&&  (UND)  - Beide wahr\n"
            "||  (ODER) - Mindestens einer wahr\n"
            "!   (NICHT)- Invertiert Wert\n\n"
            "Short-Circuit-Evaluierung:\n"
            "false && teure_funktion()\n"
            "true  || teure_funktion()",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(lc_title, DOWN, buff=0.2).shift(LEFT * 0.1)
        lc_group = VGroup(left_card, lc_title, lc_body)

        self.play(FadeIn(lc_group, shift=RIGHT), run_time=1.5)
        self.wait(8.0)

        # Show red cross over teure_funktion() for UND and ODER short-circuit
        cross_und = Line(start=[-2.8, -0.6, 0], end=[-0.4, -0.6, 0], color=RED, stroke_width=3)
        cross_oder = Line(start=[-2.8, -1.0, 0], end=[-0.4, -1.0, 0], color=RED, stroke_width=3)
        cross_label = Text("Wird nie ausgewertet!", font_size=10, color=RED).move_to([-1.6, -1.5, 0])

        self.play(Create(cross_und), Create(cross_oder), FadeIn(cross_label, shift=UP), run_time=1.2)
        self.wait(12.0)

        # --- PART B: Bitwise Operators (30s - 60s) ---
        right_card = RoundedRectangle(corner_radius=0.12, width=5.8, height=3.8, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.2, 0.1, 0])
        rc_title = Text("Bitweise Operatoren", font_size=13, color=PURPLE, weight=BOLD).next_to(right_card.get_top(), DOWN, buff=0.2)
        rc_body = Paragraph(
            "a:  1100  (12)\n"
            "b:  1010  (10)\n"
            "---------------\n"
            "& : 1000  (8)   [UND]\n"
            "| : 1110  (14)  [ODER]\n"
            "^ : 0110  (6)   [XOR]\n"
            "a << 1 = 11000  (24)\n"
            "a >> 1 = 0110   (6)",
            font_size=10, line_spacing=0.45, color=WHITE
        ).next_to(rc_title, DOWN, buff=0.2).shift(LEFT * 0.2)
        rc_group = VGroup(right_card, rc_title, rc_body)

        self.play(FadeIn(rc_group, shift=LEFT), run_time=1.5)
        self.wait(10.0)

        # Animate highlights over shifts
        shift_highlight = RoundedRectangle(corner_radius=0.03, width=4.8, height=0.5, color=YELLOW, fill_opacity=0.15, stroke_width=1.5).move_to(rc_body[6].get_center() - DOWN * 0.15)
        shift_label = Text("Shift links (<<) = * 2  |  Shift rechts (>>) = / 2", font_size=11, color=YELLOW).next_to(right_card, DOWN, buff=0.3)

        self.play(Create(shift_highlight), FadeIn(shift_label, shift=UP), run_time=1.2)
        self.wait(18.0)

        self.wait(max(0.1, dur_3 - 1.0 - 1.0 - 1.5 - 8.0 - 1.2 - 12.0 - 1.5 - 10.0 - 1.2 - 18.0 - 1.0))
        self.play(FadeOut(lc_group), FadeOut(rc_group), FadeOut(cross_und), FadeOut(cross_oder), FadeOut(cross_label), FadeOut(shift_highlight), FadeOut(shift_label), FadeOut(sec3_title), run_time=1.0)

        # ==========================================
        # SECTION 4: ASSIGNMENT & REFERENCES (56.51 seconds)
        # ==========================================
        dur_4 = durations["ch12_4_assignment_references"]
        self.add_sound("audio/ch12_4_assignment_references.wav")

        sec4_title = Text("3. Zuweisungs- & Referenzoperatoren", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # --- PART A: Assignment and lack of ++/-- (0s - 25s) ---
        editor4 = create_terminal_window(5.8, 3.8, "src/main.rs").move_to([-3.2, 0.1, 0])
        code_text4 = Paragraph(
            "let mut x = 5;",
            "x += 10; // x = 15",
            "x *= 2;  // x = 30",
            "",
            "// ✘ KEIN x++ !",
            "// ✘ KEIN x-- !",
            "// Nutze stattdessen:",
            "x += 1;",
            font_size=10, line_spacing=0.5, color=WHITE
        ).move_to(editor4.get_center()).shift(LEFT * 0.4 + UP * 0.1)
        editor_group = VGroup(editor4, code_text4)

        self.play(FadeIn(editor_group, shift=RIGHT), run_time=1.5)
        self.wait(5.0)

        # Show red warning mark over NO x++
        no_inc_highlight = RoundedRectangle(corner_radius=0.05, width=4.5, height=0.6, color=RED, fill_opacity=0.15, stroke_width=2).move_to(code_text4[4].get_center() - DOWN * 0.18)
        no_inc_text = Text("Keine Inkremente in Rust!", font_size=10, color=RED, weight=BOLD).next_to(editor4, DOWN, buff=0.3)
        self.play(Create(no_inc_highlight), FadeIn(no_inc_text, shift=UP), run_time=1.2)
        self.wait(12.0)

        # --- PART B: References & Pointer-Operators (25s - 52s) ---
        mem_card = RoundedRectangle(corner_radius=0.12, width=5.8, height=3.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.2, 0.1, 0])
        mc_title = Text("Borrowing & Dereferenzieren", font_size=13, color=CYAN, weight=BOLD).next_to(mem_card.get_top(), DOWN, buff=0.2)
        
        # Memory boxes
        box_zahl_label = Text("zahl", font_size=11, color=WHITE).move_to([1.8, 0.4, 0])
        box_zahl = Square(side_length=0.7, color=RUST_ORANGE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, 0.4, 0])
        val_zahl = Text("42", font_size=12, color=WHITE).move_to(box_zahl.get_center())
        
        box_ref_label = Text("ref_mut", font_size=11, color=WHITE).move_to([1.8, -0.6, 0])
        box_ref = RoundedRectangle(corner_radius=0.08, width=1.1, height=0.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.4, -0.6, 0])
        val_ref = Text("&mut zahl", font_size=9, color=CYAN).move_to(box_ref.get_center())

        arrow = Arrow(start=box_ref.get_top(), end=box_zahl.get_bottom(), color=CYAN, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        mem_group = VGroup(mem_card, mc_title, box_zahl_label, box_zahl, val_zahl, box_ref_label, box_ref, val_ref, arrow)

        self.play(FadeIn(mem_group, shift=LEFT), run_time=1.5)
        self.wait(10.0)

        # Show modification through dereferencing *ref_mut += 8
        val_new_zahl = Text("50", font_size=12, color=GREEN).move_to(box_zahl.get_center())
        flash_circle = Circle(radius=0.5, color=GREEN, stroke_width=3).move_to(box_zahl.get_center())
        pointer_label = Text("*ref_mut greift direkt auf 'zahl' zu!", font_size=10, color=GREEN).next_to(mem_card, DOWN, buff=0.3)

        self.play(
            Transform(val_zahl, val_new_zahl),
            Create(flash_circle),
            FadeIn(pointer_label, shift=UP),
            run_time=1.5
        )
        self.play(FadeOut(flash_circle), run_time=0.5)
        self.wait(12.0)

        self.wait(max(0.1, dur_4 - 1.0 - 1.0 - 1.5 - 5.0 - 1.2 - 12.0 - 1.5 - 10.0 - 1.5 - 0.5 - 12.0 - 1.0))
        self.play(FadeOut(editor_group), FadeOut(no_inc_highlight), FadeOut(no_inc_text), FadeOut(mem_group), FadeOut(pointer_label), FadeOut(sec4_title), run_time=1.0)

        # ==========================================
        # SECTION 5: CASTING, ERROR & RANGES (51.14 seconds)
        # ==========================================
        dur_5 = durations["ch12_5_casting_error_ranges"]
        self.add_sound("audio/ch12_5_casting_error_ranges.wav")

        sec5_title = Text("4. Typumwandlung, Fehler & Bereiche", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        panel_width = 3.6
        panel_height = 3.3
        
        # Casting Panel
        p1 = RoundedRectangle(corner_radius=0.1, width=panel_width, height=panel_height, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-4.0, 0.2, 0])
        p1_title = Text("Typguss (as)", font_size=12, color=CYAN, weight=BOLD).next_to(p1.get_top(), DOWN, buff=0.15)
        p1_body = Paragraph(
            "let x: i32 = 100;\n"
            "let y: f64 = 5.5;\n\n"
            "// Typen müssen\n"
            "// explizit gegossen\n"
            "// werden:\n"
            "let z = (x as f64) + y;",
            font_size=9, line_spacing=0.5, color=WHITE
        ).next_to(p1_title, DOWN, buff=0.15)
        g1 = VGroup(p1, p1_title, p1_body)

        # Error Panel
        p2 = RoundedRectangle(corner_radius=0.1, width=panel_width, height=panel_height, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([0, 0.2, 0])
        p2_title = Text("Fehler ( ? )", font_size=12, color=PURPLE, weight=BOLD).next_to(p2.get_top(), DOWN, buff=0.15)
        p2_body = Paragraph(
            "// Fehler-Propagierung:\n"
            "let f = File::open(\n"
            "  \"info.txt\"\n"
            ")?;\n\n"
            "• Wenn Ok: entpackt Wert\n"
            "• Wenn Err: gibt Fehler\n"
            "  sofort per return zurück!",
            font_size=9, line_spacing=0.5, color=WHITE
        ).next_to(p2_title, DOWN, buff=0.15)
        g2 = VGroup(p2, p2_title, p2_body)

        # Range Panel
        p3 = RoundedRectangle(corner_radius=0.1, width=panel_width, height=panel_height, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([4.0, 0.2, 0])
        p3_title = Text("Bereiche (Ranges)", font_size=12, color=GREEN, weight=BOLD).next_to(p3.get_top(), DOWN, buff=0.15)
        p3_body = Paragraph(
            "Exklusiv (..):\n"
            "1..5  (1, 2, 3, 4)\n\n"
            "Inklusiv (..=):\n"
            "1..=5 (1, 2, 3, 4, 5)\n\n"
            "Nutze for i in 1..=5\n"
            "oder beim Array-Slicing.",
            font_size=9, line_spacing=0.5, color=WHITE
        ).next_to(p3_title, DOWN, buff=0.15)
        g3 = VGroup(p3, p3_title, p3_body)

        # Animate them in step-by-step to fill the time
        self.play(FadeIn(g1, shift=UP), run_time=1.5)
        self.wait(12.0)

        self.play(FadeIn(g2, shift=UP), run_time=1.5)
        self.wait(12.0)

        # Highlight ? operator in panel 2
        q_highlight = RoundedRectangle(corner_radius=0.03, width=0.4, height=0.35, color=YELLOW, fill_opacity=0.2, stroke_width=1.5).move_to(p2_body[3].get_right() - RIGHT * 0.2)
        self.play(Create(q_highlight), run_time=1.0)
        self.wait(5.0)

        self.play(FadeIn(g3, shift=UP), run_time=1.5)
        self.wait(12.0)

        self.wait(max(0.1, dur_5 - 1.0 - 1.0 - 1.5 - 12.0 - 1.5 - 12.0 - 1.0 - 5.0 - 1.5 - 12.0 - 1.0))
        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(q_highlight), FadeOut(sec5_title), run_time=1.0)

        # ==========================================
        # SECTION 6: OUTRO (24.81 seconds)
        # ==========================================
        dur_6 = durations["ch12_6_outro"]
        self.add_sound("audio/ch12_6_outro.wav")

        sec6_title = Text("Zusammenfassung: Operatoren", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec6_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        summary_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0.1, 0])
        sc_title = Text("💡 Wichtigste Erkenntnisse:", font_size=15, color=CYAN, weight=BOLD).next_to(summary_card.get_top(), DOWN, buff=0.25)
        sc_desc = Paragraph(
            "• Typstrenge: Operationen verlangen identische Datentypen.\n"
            "• Keine Post-/Prä-Inkremente (++ / --) wie in C oder Java.\n"
            "• Referenzen (&, &mut) sind Leihgaben; * greift auf den Wert zu.\n"
            "• as dient zum Gießen; ? leitet Fehler sofort an den Aufrufer weiter.\n"
            "• Ranges (.. und ..=) definieren exklusive oder inklusive Intervalle.",
            font_size=11, line_spacing=0.55, color=WHITE
        ).next_to(sc_title, DOWN, buff=0.2).align_to(sc_title, LEFT).shift(LEFT * 0.4)
        sc_group = VGroup(summary_card, sc_title, sc_desc)

        self.play(FadeIn(sc_group, shift=UP), run_time=1.5)
        self.wait(10.0)

        outro_card = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.6, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).move_to([0, 0.1, 0])
        outro_text = Text("Kapitel 12 fertig!\nGroßartige Arbeit!", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        outro_group = VGroup(outro_card, outro_text)

        self.play(
            FadeOut(sc_group),
            FadeIn(outro_group, scale=0.8),
            run_time=2.0
        )

        self.wait(max(0.1, dur_6 - 1.0 - 1.0 - 1.5 - 10.0 - 2.0 - 1.0))
        self.play(FadeOut(outro_group), FadeOut(sec6_title), run_time=1.0)
