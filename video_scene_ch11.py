from manim import *
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

class RustFunctionsDetailsVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Load durations
        try:
            with open("audio/durations_ch11.json", "r") as f:
                durations = json.load(f)
        except Exception:
            durations = {
                "ch11_1_intro": 18.0,
                "ch11_2_parameters": 20.0,
                "ch11_3_statements_expressions": 22.0,
                "ch11_4_block_expressions": 22.0,
                "ch11_5_returns": 24.0,
                "ch11_6_outro": 18.0
            }

        # License Watermark (visible throughout the entire video)
        watermark_text = (
            "Dieser Inhalt basiert auf dem Buch „The Rust Programming Language“ von Steve Klabnik und Carol Nichols (Rust-Community),\n"
            "lizenziert unter MIT- und Apache-2.0-Lizenz. Der Text wurde für diesen Kurs übersetzt und modifiziert."
        )
        watermark = Text(watermark_text, font_size=8, color=GRAY, line_spacing=0.5).to_edge(DOWN, buff=0.15)
        self.add(watermark)

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        dur_1 = durations["ch11_1_intro"]
        self.add_sound("audio/ch11_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 11: Funktionen - Details", font_size=30, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4).shift(UP * 0.5)

        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)

        title_small = Text("Kapitel 11: Funktionen - Details", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        intro_badge = RoundedRectangle(corner_radius=0.15, width=9.0, height=2.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.5).shift(UP * 0.2)
        intro_badge_text = Text(
            "• Funktionsparameter & Typzwang\n"
            "• Anweisungen (Statements) vs. Ausdrücke (Expressions)\n"
            "• Scope-Blöcke & Rückgabewerte im Detail", 
            font_size=13, color=WHITE, line_spacing=0.6
        ).move_to(intro_badge.get_center())
        intro_badge_group = VGroup(intro_badge, intro_badge_text)

        self.play(FadeIn(intro_badge_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_1 - 6.5 - 1.0))
        self.play(FadeOut(intro_badge_group), FadeOut(title_group), run_time=1.0)

        # ==========================================
        # SECTION 2: PARAMETERS & TYPE CONSTRAINTS
        # ==========================================
        dur_2 = durations["ch11_2_parameters"]
        self.add_sound("audio/ch11_2_parameters.wav")

        sec2_title = Text("1. Parameter & Typzwang", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        editor2 = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text2 = Paragraph(
            "fn main() {",
            "    print_labeled_measurement(5, 'h');",
            "}",
            "",
            "fn print_labeled_measurement(value: i32, unit_label: char) {",
            "    println!(\"Die Messung ist: {value}{unit_label}\");",
            "}",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor2.get_center()).shift(LEFT * 1.0 + UP * 0.1)

        self.play(FadeIn(editor2), FadeIn(code_text2), run_time=1.5)
        self.wait(6.0)

        # Highlight value and unit_label types
        highlight_types = RoundedRectangle(corner_radius=0.05, width=4.8, height=0.45, color=CYAN, fill_opacity=0.15, stroke_width=1.5).move_to(code_text2[4].get_right() - RIGHT * 2.8)
        self.play(Create(highlight_types), run_time=1.5)
        self.wait(2.0)

        info_badge2 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.2, 0])
        ib2_text = Text("In Rust müssen alle Parametertypen in der Signatur deklariert werden.\nDas ermöglicht dem Compiler exzellente Typsicherheit und Fehlerprüfungen.", font_size=11, color=WHITE).move_to(info_badge2.get_center())
        ib2_group = VGroup(info_badge2, ib2_text)

        self.play(FadeIn(ib2_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_2 - 14.5 - 1.0))
        self.play(FadeOut(editor2), FadeOut(code_text2), FadeOut(highlight_types), FadeOut(ib2_group), FadeOut(sec2_title), run_time=1.0)

        # ==========================================
        # SECTION 3: STATEMENTS VS EXPRESSIONS
        # ==========================================
        dur_3 = durations["ch11_3_statements_expressions"]
        self.add_sound("audio/ch11_3_statements_expressions.wav")

        sec3_title = Text("2. Anweisungen vs. Ausdrücke", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # Comparison Cards
        card_stmt = RoundedRectangle(corner_radius=0.12, width=5.6, height=2.6, color=RED, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.0, 0.8, 0])
        cs_title = Text("Anweisung (Statement)", font_size=13, color=RED, weight=BOLD).next_to(card_stmt.get_top(), DOWN, buff=0.2)
        cs_desc = Paragraph(
            "• Führt eine Aktion aus\n"
            "• Liefert KEINEN Wert zurück\n"
            "  z.B. let y = 6;\n"
            "  oder Funktionsdefinitionen",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(cs_title, DOWN, buff=0.2).align_to(cs_title, LEFT).shift(LEFT * 0.4)
        cs_group = VGroup(card_stmt, cs_title, cs_desc)

        card_expr = RoundedRectangle(corner_radius=0.12, width=5.6, height=2.6, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.0, 0.8, 0])
        ce_title = Text("Ausdruck (Expression)", font_size=13, color=GREEN, weight=BOLD).next_to(card_expr.get_top(), DOWN, buff=0.2)
        ce_desc = Paragraph(
            "• Wertet zu einem Ergebnis aus\n"
            "• Liefert einen Wert zurück\n"
            "  z.B. 5 + 6  (liefert 11)\n"
            "  oder Funktionsaufrufe",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(ce_title, DOWN, buff=0.2).align_to(ce_title, LEFT).shift(LEFT * 0.4)
        ce_group = VGroup(card_expr, ce_title, ce_desc)

        self.play(FadeIn(cs_group, shift=RIGHT), FadeIn(ce_group, shift=LEFT), run_time=1.5)
        self.wait(5.0)

        # Editor showing incorrect statement assignment
        editor3 = create_terminal_window(11.0, 2.4, "src/main.rs").move_to([0, -1.8, 0])
        code_text3 = Paragraph(
            "fn main() {",
            "    let x = (let y = 6); // ✘ FEHLER! Anweisung liefert keinen Wert",
            "}",
            font_size=11, line_spacing=0.5, color=WHITE
        ).move_to(editor3.get_center()).shift(LEFT * 1.0 + UP * 0.1)

        self.play(FadeIn(editor3), FadeIn(code_text3), run_time=1.5)
        
        # Red highlight cross on let y = 6 in parenthesis
        cross_line = RoundedRectangle(corner_radius=0.05, width=3.2, height=0.35, color=RED, fill_opacity=0.2, stroke_width=1.5).move_to(code_text3[1].get_right() - RIGHT * 2.8)
        self.play(Create(cross_line), run_time=1.0)

        self.wait(max(0.1, dur_3 - 11.0 - 1.0))
        self.play(FadeOut(cs_group), FadeOut(ce_group), FadeOut(editor3), FadeOut(code_text3), FadeOut(cross_line), FadeOut(sec3_title), run_time=1.0)

        # ==========================================
        # SECTION 4: BLOCK EXPRESSIONS
        # ==========================================
        dur_4 = durations["ch11_4_block_expressions"]
        self.add_sound("audio/ch11_4_block_expressions.wav")

        sec4_title = Text("3. Scope-Blöcke als Ausdrücke", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        editor4 = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text4 = Paragraph(
            "fn main() {",
            "    let y = {",
            "        let x = 3;",
            "        x + 1 // Ausdruck ohne Semikolon!",
            "    };",
            "    println!(\"y ist {y}\");",
            "}",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor4.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor4), FadeIn(code_text4), run_time=1.5)
        self.wait(6.0)

        # Highlight x + 1 line
        block_highlight = RoundedRectangle(corner_radius=0.05, width=4.8, height=0.45, color=GREEN, fill_opacity=0.15, stroke_width=1.5).move_to(code_text4[3].get_center())
        self.play(Create(block_highlight), run_time=1.0)
        self.wait(3.0)

        info_badge4 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.2, 0])
        ib4_text = Text("Ein Block {} ist ein Ausdruck, der zum Wert seiner letzten Zeile auswertet.\nEin Semikolon am Ende würde den Wert verwerfen und () zurückgeben.", font_size=11, color=WHITE).move_to(info_badge4.get_center())
        ib4_group = VGroup(info_badge4, ib4_text)

        self.play(FadeIn(ib4_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_4 - 14.0 - 1.0))
        self.play(FadeOut(editor4), FadeOut(code_text4), FadeOut(block_highlight), FadeOut(ib4_group), FadeOut(sec4_title), run_time=1.0)

        # ==========================================
        # SECTION 5: RETURN VALUES & TYPE CONFLICTS
        # ==========================================
        dur_5 = durations["ch11_5_returns"]
        self.add_sound("audio/ch11_5_returns.wav")

        sec5_title = Text("4. Rückgabewerte & Typkonflikte", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        editor5 = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.4, 0])
        code_text5 = Paragraph(
            "fn main() {",
            "    let x = plus_one(5);",
            "}",
            "",
            "fn plus_one(x: i32) -> i32 {",
            "    x + 1; // ✘ FEHLER wegen Semikolon!",
            "}",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor5.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor5), FadeIn(code_text5), run_time=1.5)
        self.wait(6.0)

        # Error Highlight
        error_line = RoundedRectangle(corner_radius=0.05, width=4.8, height=0.45, color=RED, fill_opacity=0.15, stroke_width=1.5).move_to(code_text5[5].get_center())
        self.play(Create(error_line), run_time=1.0)
        self.wait(3.0)

        info_badge5 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.4, color=RED, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.3, 0])
        ib5_text = Text("Fehler: Typkonflikt (mismatched types). Erwartet wurde i32, erhalten wurde ().\nEntferne das Semikolon in der letzten Zeile, um den Wert zurückzugeben.", font_size=11, color=WHITE).move_to(info_badge5.get_center())
        ib5_group = VGroup(info_badge5, ib5_text)

        self.play(FadeIn(ib5_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_5 - 14.0 - 1.0))
        self.play(FadeOut(editor5), FadeOut(code_text5), FadeOut(error_line), FadeOut(ib5_group), FadeOut(sec5_title), run_time=1.0)

        # ==========================================
        # SECTION 6: OUTRO
        # ==========================================
        dur_6 = durations["ch11_6_outro"]
        self.add_sound("audio/ch11_6_outro.wav")

        sec6_title = Text("Zusammenfassung: Funktionen - Details", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec6_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        summary_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0.2, 0])
        sc_title = Text("💡 Wichtigste Erkenntnisse:", font_size=15, color=CYAN, weight=BOLD).next_to(summary_card.get_top(), DOWN, buff=0.25)
        sc_desc = Paragraph(
            "• Funktionsparameter verlangen feste Typangaben.\n"
            "• Anweisungen führen nur aus; Ausdrücke liefern Werte.\n"
            "• Ohne Semikolon am Ende liefert ein Block oder Körper einen Wert.\n"
            "• Semikolons bei Rückgaben führen zu Typkonflikten (mismatched types).",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(sc_title, DOWN, buff=0.2).align_to(sc_title, LEFT).shift(LEFT * 0.4)
        sc_group = VGroup(summary_card, sc_title, sc_desc)

        self.play(FadeIn(sc_group, shift=UP), run_time=1.5)
        self.wait(6.0)

        outro_card = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.6, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).move_to([0, 0.2, 0])
        outro_text = Text("Kapitel 11 fertig!\nGroßartige Arbeit!", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        outro_group = VGroup(outro_card, outro_text)

        self.play(
            FadeOut(sc_group),
            FadeIn(outro_group, scale=0.8),
            run_time=2.0
        )

        self.wait(max(0.1, dur_6 - 11.5 - 1.0))
        self.play(FadeOut(outro_group), FadeOut(sec6_title), run_time=1.0)
