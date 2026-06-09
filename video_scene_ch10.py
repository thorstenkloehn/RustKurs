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

class RustFunctionsVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Load durations
        try:
            with open("audio/durations_ch10.json", "r") as f:
                durations = json.load(f)
        except Exception:
            durations = {
                "ch10_1_intro": 18.0,
                "ch10_2_main_and_custom": 20.0,
                "ch10_3_parameters_arguments": 22.0,
                "ch10_4_return_values": 24.0,
                "ch10_5_outro": 18.0
            }

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        dur_1 = durations["ch10_1_intro"]
        self.add_sound("audio/ch10_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 10: Funktionen", font_size=32, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)

        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)

        title_small = Text("Kapitel 10: Funktionen", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        intro_badge = RoundedRectangle(corner_radius=0.15, width=9.0, height=2.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.5)
        intro_badge_text = Text(
            "• Wiederverwendbare Code-Blöcke\n"
            "• Vermeidung von redundantem Code\n"
            "• Strukturierung und Ordnung im Programm", 
            font_size=14, color=WHITE, line_spacing=0.6
        ).move_to(intro_badge.get_center())
        intro_badge_group = VGroup(intro_badge, intro_badge_text)

        self.play(FadeIn(intro_badge_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_1 - 6.5 - 1.0))
        self.play(FadeOut(intro_badge_group), FadeOut(title_group), run_time=1.0)

        # ==========================================
        # SECTION 2: MAIN & CUSTOM FUNCTIONS
        # ==========================================
        dur_2 = durations["ch10_2_main_and_custom"]
        self.add_sound("audio/ch10_2_main_and_custom.wav")

        sec2_title = Text("1. Die main-Funktion & eigene Funktionen", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        editor2 = create_terminal_window(11.0, 3.8, "src/main.rs").move_to([0, 0.2, 0])
        code_text2 = Paragraph(
            "fn main() {",
            "    gruss_schreiben(); // Aufruf der Funktion",
            "}",
            "",
            "fn gruss_schreiben() { // Definition mit 'fn'",
            "    println!(\"Hallo Welt!\");",
            "}",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(editor2.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor2), FadeIn(code_text2), run_time=1.5)
        self.wait(6.0)

        # Highlight function call and definition
        highlight_call = RoundedRectangle(corner_radius=0.05, width=4.8, height=0.4, color=CYAN, fill_opacity=0.15, stroke_width=1.5).move_to(code_text2[1].get_center())
        highlight_def = RoundedRectangle(corner_radius=0.05, width=6.8, height=0.4, color=GREEN, fill_opacity=0.15, stroke_width=1.5).move_to(code_text2[4].get_center())
        
        self.play(Create(highlight_call), Create(highlight_def), run_time=1.5)
        self.wait(2.0)

        info_badge2 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.5, 0])
        ib2_text = Text("Reihenfolge ist egal: Eigene Funktionen können überall stehen.\nSie werden erst ausgeführt, wenn sie in main() aufgerufen werden.", font_size=11, color=WHITE).move_to(info_badge2.get_center())
        ib2_group = VGroup(info_badge2, ib2_text)

        self.play(FadeIn(ib2_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_2 - 14.5 - 1.0))
        self.play(FadeOut(editor2), FadeOut(code_text2), FadeOut(highlight_call), FadeOut(highlight_def), FadeOut(ib2_group), FadeOut(sec2_title), run_time=1.0)

        # ==========================================
        # SECTION 3: PARAMETERS & ARGUMENTS
        # ==========================================
        dur_3 = durations["ch10_3_parameters_arguments"]
        self.add_sound("audio/ch10_3_parameters_arguments.wav")

        sec3_title = Text("2. Parameter und Argumente (Eingaben)", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # Cards for Parameter vs Argument
        card_param = RoundedRectangle(corner_radius=0.12, width=5.6, height=2.4, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([-3.0, 1.4, 0])
        cp_title = Text("Parameter (Definition)", font_size=13, color=PURPLE, weight=BOLD).next_to(card_param.get_top(), DOWN, buff=0.2)
        cp_desc = Paragraph(
            "• Platzhalter für Werte\n"
            "• Typangabe zwingend erforderlich\n"
            "  z.B. name: &str",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(cp_title, DOWN, buff=0.2).align_to(cp_title, LEFT).shift(LEFT * 0.4)
        cp_group = VGroup(card_param, cp_title, cp_desc)

        card_arg = RoundedRectangle(corner_radius=0.12, width=5.6, height=2.4, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.0).move_to([3.0, 1.4, 0])
        ca_title = Text("Argument (Aufruf)", font_size=13, color=CYAN, weight=BOLD).next_to(card_arg.get_top(), DOWN, buff=0.2)
        ca_desc = Paragraph(
            "• Der konkrete übergebene Wert\n"
            "• Muss exakt zum Typ passen\n"
            "  z.B. \"Anna\"",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(ca_title, DOWN, buff=0.2).align_to(ca_title, LEFT).shift(LEFT * 0.4)
        ca_group = VGroup(card_arg, ca_title, ca_desc)

        self.play(FadeIn(cp_group, shift=RIGHT), FadeIn(ca_group, shift=LEFT), run_time=1.5)
        self.wait(3.5)

        # Editor showing code with param & arg
        editor3 = create_terminal_window(11.0, 2.6, "src/main.rs").move_to([0, -1.6, 0])
        code_text3 = Paragraph(
            "let name = \"Anna\"; // Argument",
            "alter_anzeigen(name, 25); // Aufruf",
            "fn alter_anzeigen(name: &str, alter: i32) { ... }",
            font_size=11, line_spacing=0.5, color=WHITE
        ).move_to(editor3.get_center()).shift(LEFT * 1.5 + UP * 0.1)

        self.play(FadeIn(editor3), FadeIn(code_text3), run_time=1.5)
        self.wait(max(0.1, dur_3 - 8.5 - 1.0))
        self.play(FadeOut(cp_group), FadeOut(ca_group), FadeOut(editor3), FadeOut(code_text3), FadeOut(sec3_title), run_time=1.0)

        # ==========================================
        # SECTION 4: RETURN VALUES
        # ==========================================
        dur_4 = durations["ch10_4_return_values"]
        self.add_sound("audio/ch10_4_return_values.wav")

        sec4_title = Text("3. Rückgabewerte (Ausgaben)", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        # Two code boxes comparing explicit and implicit return
        box_w, box_h = 5.6, 3.2
        card_ret_a = RoundedRectangle(corner_radius=0.12, width=box_w, height=box_h, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.0).move_to([-3.0, 0.0, 0])
        cra_title = Text("Weg A: Mit return", font_size=12, color=YELLOW, weight=BOLD).next_to(card_ret_a.get_top(), DOWN, buff=0.2)
        cra_code = Paragraph(
            "fn addieren(a: i32, b: i32) -> i32 {",
            "    return a + b;",
            "}",
            font_size=10, line_spacing=0.6, color=WHITE
        ).next_to(cra_title, DOWN, buff=0.3).align_to(cra_title, LEFT).shift(LEFT * 0.8)
        cra_group = VGroup(card_ret_a, cra_title, cra_code)

        card_ret_b = RoundedRectangle(corner_radius=0.12, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.0).move_to([3.0, 0.0, 0])
        crb_title = Text("Weg B: Ausdruck (Rust-Standard)", font_size=12, color=GREEN, weight=BOLD).next_to(card_ret_b.get_top(), DOWN, buff=0.2)
        crb_code = Paragraph(
            "fn addieren(a: i32, b: i32) -> i32 {",
            "    a + b  // kein Semikolon!",
            "}",
            font_size=10, line_spacing=0.6, color=WHITE
        ).next_to(crb_title, DOWN, buff=0.3).align_to(crb_title, LEFT).shift(LEFT * 0.8)
        crb_group = VGroup(card_ret_b, crb_title, crb_code)

        self.play(FadeIn(cra_group, shift=RIGHT), FadeIn(crb_group, shift=LEFT), run_time=1.5)
        self.wait(5.0)

        # Accentuate the arrow -> and missing semicolon
        arrow_highlight_a = Circle(radius=0.25, color=CYAN, stroke_width=1.5).move_to(cra_code[0].get_right() + LEFT * 0.4)
        arrow_highlight_b = Circle(radius=0.25, color=CYAN, stroke_width=1.5).move_to(crb_code[0].get_right() + LEFT * 0.4)
        semicolon_cross = Line(start=[-0.1, -0.1, 0], end=[0.1, 0.1, 0], color=RED, stroke_width=3).move_to(crb_code[1].get_right() + RIGHT * 0.1)

        self.play(Create(arrow_highlight_a), Create(arrow_highlight_b), run_time=1.0)
        self.play(Create(semicolon_cross), run_time=1.0)
        self.wait(3.0)

        info_badge4 = RoundedRectangle(corner_radius=0.1, width=11.0, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.0).move_to([0, -2.4, 0])
        ib4_text = Text("Der Typ nach -> legt fest, was zurückgegeben werden muss.\nAusdruck ohne Semikolon gibt den Wert automatisch zurück.", font_size=11, color=WHITE).move_to(info_badge4.get_center())
        ib4_group = VGroup(info_badge4, ib4_text)

        self.play(FadeIn(ib4_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_4 - 13.0 - 1.0))
        self.play(FadeOut(cra_group), FadeOut(crb_group), FadeOut(arrow_highlight_a), FadeOut(arrow_highlight_b), FadeOut(semicolon_cross), FadeOut(ib4_group), FadeOut(sec4_title), run_time=1.0)

        # ==========================================
        # SECTION 5: OUTRO
        # ==========================================
        dur_5 = durations["ch10_5_outro"]
        self.add_sound("audio/ch10_5_outro.wav")

        sec5_title = Text("Zusammenfassung: Funktionen", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0)
        self.wait(1.0)

        summary_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0, 0])
        sc_title = Text("💡 Wichtigste Erkenntnisse:", font_size=15, color=CYAN, weight=BOLD).next_to(summary_card.get_top(), DOWN, buff=0.25)
        sc_desc = Paragraph(
            "• fn name() umschließt wiederverwendbare Logik.\n"
            "• Parameter haben strengen Typzwang (name: Typ).\n"
            "• Rückgaben erfolgen mit -> Typ und return ODER als Ausdruck.\n"
            "• Der Compiler blockiert falschen Typen- oder Parameter-Gebrauch.",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(sc_title, DOWN, buff=0.2).align_to(sc_title, LEFT).shift(LEFT * 0.4)
        sc_group = VGroup(summary_card, sc_title, sc_desc)

        self.play(FadeIn(sc_group, shift=UP), run_time=1.5)
        self.wait(6.5)

        outro_card = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.6, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).move_to([0, 0, 0])
        outro_text = Text("Kapitel 10 fertig!\nGut gemacht!", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        outro_group = VGroup(outro_card, outro_text)

        self.play(
            FadeOut(sc_group),
            FadeIn(outro_group, scale=0.8),
            run_time=2.0
        )

        self.wait(max(0.1, dur_5 - 12.0 - 1.0))
        self.play(FadeOut(outro_group), FadeOut(sec5_title), run_time=1.0)
