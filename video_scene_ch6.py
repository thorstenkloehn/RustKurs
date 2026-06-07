from manim import *
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
    # Header line separating title bar
    header_bar = Line(
        start=[-width/2, height/2 - 0.45, 0], 
        end=[width/2, height/2 - 0.45, 0], 
        color=GRAY, 
        stroke_width=2
    )
    # Window control dots (Red, Yellow, Green)
    red_dot = Circle(radius=0.07, color=RED, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.25, height/2 - 0.22, 0])
    yellow_dot = Circle(radius=0.07, color=YELLOW, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.45, height/2 - 0.22, 0])
    green_dot = Circle(radius=0.07, color=GREEN, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.65, height/2 - 0.22, 0])
    # Window Title
    title = Text(title_text, font_size=11, color=GRAY).move_to([0, height/2 - 0.22, 0])
    
    return VGroup(window, header_bar, red_dot, yellow_dot, green_dot, title)

def create_squiggly_line(start_pt, end_pt, color, amplitude=0.06, wavelengths=6):
    start_pt = np.array(start_pt)
    end_pt = np.array(end_pt)
    direction = end_pt - start_pt
    length = np.linalg.norm(direction)
    unit_dir = direction / length
    normal = np.array([-unit_dir[1], unit_dir[0], 0])
    
    points = []
    num_pts = 60
    for i in range(num_pts):
        t = i / (num_pts - 1)
        pt = start_pt + t * direction + amplitude * np.sin(t * wavelengths * 2 * np.pi) * normal
        points.append(pt)
    return VMobject(color=color, stroke_width=2.5).set_points_as_corners(points)

class RustDatatypesVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 20.71s)
        # ==========================================
        self.add_sound("audio/ch6_1_intro.wav")

        # 0s - 3s: Title
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 6: Datentypen", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0) # total 3.0s

        # 3s - 5s: Move Title to Top
        title_small = Text("Kapitel 6: Datentypen in Rust", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5) # total 4.5s
        self.wait(0.5) # total 5.0s

        # 5s - 12s: Show Cards
        card1 = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, 0.4, 0])
        card1_title = Text("Statische Typisierung", font_size=16, color=CYAN, weight=BOLD).next_to(card1.get_top(), DOWN, buff=0.3)
        card1_desc = Text("Rust muss jeden Typ vor\ndem Programmstart kennen.", font_size=12, color=WHITE).next_to(card1_title, DOWN, buff=0.2)
        card1_group = VGroup(card1, card1_title, card1_desc)

        card2 = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, 0.4, 0])
        card2_title = Text("Typinferenz", font_size=16, color=PURPLE, weight=BOLD).next_to(card2.get_top(), DOWN, buff=0.3)
        card2_desc = Text("Rust erkennt den Typ oft\nautomatisch am Wert.", font_size=12, color=WHITE).next_to(card2_title, DOWN, buff=0.2)
        card2_group = VGroup(card2, card2_title, card2_desc)

        self.play(FadeIn(card1_group, shift=RIGHT), FadeIn(card2_group, shift=LEFT), run_time=1.5) # total 6.5s
        self.wait(5.5) # total 12.0s

        # 12s - 19.71s: Show Code below
        code_exp = Paragraph(
            "let x: i32 = 42;  // Expliziter Typ",
            "let y = 42;       // Typinferenz (i32)",
            font_size=15, line_spacing=0.8, color=WHITE
        ).move_to([0, -1.8, 0])

        self.play(FadeIn(code_exp, shift=UP), run_time=1.5) # total 13.5s
        self.wait(20.71 - 13.5 - 1.0) # total 19.71s
        self.play(FadeOut(card1_group), FadeOut(card2_group), FadeOut(code_exp), FadeOut(title_group), run_time=1.0) # total 20.71s


        # ==========================================
        # SECTION 2: SCALAR TYPES (Duration: 27.26s)
        # ==========================================
        self.add_sound("audio/ch6_2_scalartypes.wav")

        sec2_title = Text("1. Skalare Typen: Ganzzahlen", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Scalar Type definition
        scalar_def = RoundedRectangle(corner_radius=0.15, width=8.0, height=1.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 1.2, 0])
        scalar_def_text = Text("Skalarer Typ = Repräsentiert einen einzigen Wert", font_size=15, color=WHITE).move_to(scalar_def.get_center())
        scalar_group = VGroup(scalar_def, scalar_def_text)

        self.play(FadeIn(scalar_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Comparison Cards i vs u
        card_i = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, -1.0, 0])
        card_i_title = Text("i (signed / mit Vorzeichen)", font_size=14, color=CYAN, weight=BOLD).next_to(card_i.get_top(), DOWN, buff=0.3)
        card_i_desc = Paragraph(
            "• Positiv & Negativ möglich",
            "• Beispiel: -5, 12",
            "• Standard-Ganzzahltyp in Rust",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(card_i_title, DOWN, buff=0.3).shift(LEFT * 0.2)
        card_i_group = VGroup(card_i, card_i_title, card_i_desc)

        card_u = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.6, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, -1.0, 0])
        card_u_title = Text("u (unsigned / ohne Vorzeichen)", font_size=14, color=PURPLE, weight=BOLD).next_to(card_u.get_top(), DOWN, buff=0.3)
        card_u_desc = Paragraph(
            "• Nur 0 oder Positiv möglich",
            "• Beispiel: 5, 200",
            "• Verdoppelt positive Reichweite",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(card_u_title, DOWN, buff=0.3).shift(LEFT * 0.2)
        card_u_group = VGroup(card_u, card_u_title, card_u_desc)

        self.play(FadeIn(card_i_group, shift=UP), FadeIn(card_u_group, shift=UP), run_time=1.5) # total 9.5s
        self.wait(6.5) # total 16.0s

        # Highlight standard i32
        std_badge = RoundedRectangle(corner_radius=0.1, width=4.5, height=0.6, color=RUST_ORANGE, fill_color=RUST_ORANGE, fill_opacity=0.15, stroke_width=2).move_to([0, -2.6, 0])
        std_text = Text("Standard: i32", font_size=13, color=RUST_ORANGE, weight=BOLD).move_to(std_badge.get_center())
        std_group = VGroup(std_badge, std_text)

        self.play(FadeIn(std_group, shift=UP), run_time=1.0) # total 17.0s
        self.wait(27.26 - 17.0 - 1.0) # total 26.26s
        self.play(FadeOut(scalar_group), FadeOut(card_i_group), FadeOut(card_u_group), FadeOut(std_group), FadeOut(sec2_title), run_time=1.0) # total 27.26s


        # ==========================================
        # SECTION 3: BOUNDS & SPEICHERPLATZ (Duration: 34.47s)
        # ==========================================
        self.add_sound("audio/ch6_3_bounds.wav")

        sec3_title = Text("2. Speichergrößen & Grenzen", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Table showing bounds
        table_border = RoundedRectangle(corner_radius=0.12, width=11.0, height=2.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.2, 0])
        col_headers = Paragraph(
            "Typ       Speichergröße        Gültiger Bereich (Grenzen)",
            font_size=13, line_spacing=0.5, color=CYAN, weight=BOLD
        ).move_to(table_border.get_center()).shift(UP * 0.6)
        
        row1 = Text("i8          1 Byte (8 Bit)          -128 bis 127", font_size=12, color=WHITE).move_to(table_border.get_center()).shift(UP * 0.1)
        row2 = Text("u8          1 Byte (8 Bit)          0 bis 255", font_size=12, color=WHITE).move_to(table_border.get_center()).shift(DOWN * 0.3)
        row3 = Text("i16         2 Bytes (16 Bit)        -32.768 bis 32.767", font_size=12, color=WHITE).move_to(table_border.get_center()).shift(DOWN * 0.7)

        table_group = VGroup(table_border, col_headers, row1, row2, row3)
        self.play(FadeIn(table_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(8.5) # total 12.0s

        # Editor showing error
        editor = create_terminal_window(11.0, 3.4, "VS Code - Fehlerfall").move_to([0, -1.8, 0])
        code_err = Paragraph(
            "fn main() {",
            "    let x: u8 = -15;",
            "}",
            font_size=14, line_spacing=0.5, color=WHITE
        ).move_to(editor.get_center()).shift(LEFT * 3.5 + UP * 0.2)
        
        squiggly = create_squiggly_line([-2.4, -1.9, 0], [-1.9, -1.9, 0], RED)
        
        err_msg_rect = RoundedRectangle(corner_radius=0.08, width=5.5, height=0.8, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([2.0, -1.8, 0])
        err_msg = Paragraph(
            "error: cannot apply unary operator `-` to type `u8`",
            "error: could not compile `hello_world` due to previous error",
            font_size=9, line_spacing=0.4, color=RED
        ).move_to(err_msg_rect.get_center())
        
        fail_badge = RoundedRectangle(corner_radius=0.1, width=4.5, height=0.5, color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=2).move_to([2.0, -2.6, 0])
        fail_text = Text("✘ Fataler Fehler! Kompiliert nicht.", font_size=11, color=RED, weight=BOLD).move_to(fail_badge.get_center())
        
        error_group = VGroup(editor, code_err, squiggly, err_msg_rect, err_msg, fail_badge, fail_text)
        self.play(FadeIn(error_group), run_time=1.5) # total 13.5s
        self.wait(10.5) # total 24.0s

        # Replace error with Practical Guidance
        best_practice_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.4, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=2.5).move_to([0, -1.8, 0])
        bp_title = Text("💡 Praxis-Regel: Keine Mikro-Optimierung!", font_size=15, color=GREEN, weight=BOLD).next_to(best_practice_card.get_top(), DOWN, buff=0.3)
        bp_desc1 = Text("• Ganzzahlen: Nimm einfach standardmäßig i32", font_size=13, color=WHITE).next_to(bp_title, DOWN, buff=0.3).align_to(bp_title, LEFT).shift(LEFT * 1.0)
        bp_desc2 = Text("• Kommazahlen: Nimm einfach standardmäßig f64", font_size=13, color=WHITE).next_to(bp_desc1, DOWN, buff=0.2).align_to(bp_desc1, LEFT)
        bp_desc3 = Text("• Heutige Computer haben mehr als genug Arbeitsspeicher.", font_size=12, color=GRAY).next_to(bp_desc2, DOWN, buff=0.4).align_to(bp_desc2, LEFT)
        bp_group = VGroup(best_practice_card, bp_title, bp_desc1, bp_desc2, bp_desc3)

        self.play(FadeOut(error_group), FadeIn(bp_group), run_time=1.5) # total 25.5s
        self.wait(34.47 - 25.5 - 1.0) # total 33.47s
        self.play(FadeOut(table_group), FadeOut(bp_group), FadeOut(sec3_title), run_time=1.0) # total 34.47s


        # ==========================================
        # SECTION 4: UNDERSCORES (Duration: 19.43s)
        # ==========================================
        self.add_sound("audio/ch6_4_underscores.wav")

        sec4_title = Text("3. Tausendertrennzeichen (_)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Card comparison
        card_bad = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=RED, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, 0.4, 0])
        bad_title = Text("Schwer lesbar (viele Nullen):", font_size=13, color=RED, weight=BOLD).next_to(card_bad.get_top(), DOWN, buff=0.3)
        bad_code = Text("let a = 6000000;", font_size=15, color=WHITE).next_to(bad_title, DOWN, buff=0.4)
        bad_group = VGroup(card_bad, bad_title, bad_code)

        card_good = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, 0.4, 0])
        good_title = Text("Sehr gut lesbar (mit Unterstrich):", font_size=13, color=GREEN, weight=BOLD).next_to(card_good.get_top(), DOWN, buff=0.3)
        good_code = Text("let a = 6_000_000;", font_size=15, color=WHITE).next_to(good_title, DOWN, buff=0.4)
        good_group = VGroup(card_good, good_title, good_code)

        self.play(FadeIn(bad_group, shift=RIGHT), FadeIn(good_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Compiler ignores it (Unified compilation output)
        comp_rect = RoundedRectangle(corner_radius=0.15, width=6.0, height=1.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.8, 0])
        comp_text = Text("Für den Rust-Compiler identisch:\n      Wert im Speicher: 6000000", font_size=14, color=CYAN).move_to(comp_rect.get_center())
        comp_group = VGroup(comp_rect, comp_text)

        arrow_l = Arrow(start=[-3.0, -0.8, 0], end=[-1.0, -1.5, 0], color=GRAY)
        arrow_r = Arrow(start=[3.0, -0.8, 0], end=[1.0, -1.5, 0], color=GRAY)

        self.play(FadeIn(comp_group, shift=UP), Create(arrow_l), Create(arrow_r), run_time=1.5) # total 9.5s
        self.wait(19.43 - 9.5 - 1.0) # total 18.43s
        self.play(FadeOut(bad_group), FadeOut(good_group), FadeOut(comp_group), FadeOut(arrow_l), FadeOut(arrow_r), FadeOut(sec4_title), run_time=1.0) # total 19.43s


        # ==========================================
        # SECTION 5: ISIZE & USIZE (Duration: 22.38s)
        # ==========================================
        self.add_sound("audio/ch6_5_isize_usize.wav")

        sec5_title = Text("4. Systemabhängige Typen: isize & usize", font_size=28, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Architecture boxes
        arch64 = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, 0.4, 0])
        a64_title = Text("Auf einem 64-Bit System:", font_size=14, color=CYAN, weight=BOLD).next_to(arch64.get_top(), DOWN, buff=0.3)
        a64_desc = Paragraph(
            "• isize -> wird zu i64",
            "• usize -> wird zu u64",
            "• Belegt 8 Bytes im Speicher",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(a64_title, DOWN, buff=0.2).shift(LEFT * 0.2)
        a64_group = VGroup(arch64, a64_title, a64_desc)

        arch32 = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.4, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, 0.4, 0])
        a32_title = Text("Auf einem 32-Bit System:", font_size=14, color=PURPLE, weight=BOLD).next_to(arch32.get_top(), DOWN, buff=0.3)
        a32_desc = Paragraph(
            "• isize -> wird zu i32",
            "• usize -> wird zu u32",
            "• Belegt 4 Bytes im Speicher",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(a32_title, DOWN, buff=0.2).shift(LEFT * 0.2)
        a32_group = VGroup(arch32, a32_title, a32_desc)

        self.play(FadeIn(a64_group, shift=RIGHT), FadeIn(a32_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(8.5) # total 12.0s

        # Purpose description
        purpose = RoundedRectangle(corner_radius=0.12, width=11.0, height=1.6, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.8, 0])
        purpose_title = Text("Wofür braucht man usize?", font_size=14, color=RUST_ORANGE, weight=BOLD).next_to(purpose.get_top(), DOWN, buff=0.2)
        purpose_desc = Paragraph(
            "Hauptsächlich für Längenangaben von Listen (Arrays/Vektoren)\noder um Elemente über einen Index anzusprechen: let index: usize = 0;",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(purpose_title, DOWN, buff=0.2)
        purpose_group = VGroup(purpose, purpose_title, purpose_desc)

        self.play(FadeIn(purpose_group, shift=UP), run_time=1.5) # total 13.5s
        self.wait(22.38 - 13.5 - 1.0) # total 21.38s
        self.play(FadeOut(a64_group), FadeOut(a32_group), FadeOut(purpose_group), FadeOut(sec5_title), run_time=1.0) # total 22.38s


        # ==========================================
        # SECTION 6: STRINGS & ESCAPING (Duration: 21.06s)
        # ==========================================
        self.add_sound("audio/ch6_6_strings_escaping.wav")

        sec6_title = Text("5. String-Literale & Escaping", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec6_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Code string
        code_str = RoundedRectangle(corner_radius=0.12, width=11.0, height=1.0, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 1.2, 0])
        code_str_text = Text('let text = "Zeile 1\\nZeile 2\\t\\"Rust\\"";', font_size=16, color=WHITE).move_to(code_str.get_center())
        code_group = VGroup(code_str, code_str_text)

        self.play(FadeIn(code_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(6.5) # total 10.0s

        # Escape explanations
        esc_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=3.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.2, 0])
        esc_title = Text("Maskierung (Escaping) von Sonderzeichen:", font_size=14, color=CYAN, weight=BOLD).next_to(esc_card.get_top(), DOWN, buff=0.2)
        
        tbl_items = Paragraph(
            "\\n  ->  Erzeugt eine neue Zeile (New Line)\n"
            "\\t  ->  Erzeugt einen Tabulator-Abstand\n"
            "\\\"  ->  Druckt ein echtes Anführungszeichen\n"
            "\\\\  ->  Druckt einen einzelnen wörtlichen Backslash",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(esc_title, DOWN, buff=0.3).align_to(esc_title, LEFT).shift(LEFT * 0.5)
        
        esc_group = VGroup(esc_card, esc_title, tbl_items)

        self.play(FadeIn(esc_group, shift=UP), run_time=1.5) # total 11.5s
        self.wait(21.06 - 11.5 - 1.0) # total 20.06s
        self.play(FadeOut(code_group), FadeOut(esc_group), FadeOut(sec6_title), run_time=1.0) # total 21.06s


        # ==========================================
        # SECTION 7: RAW STRINGS (Duration: 17.41s)
        # ==========================================
        self.add_sound("audio/ch6_7_raw_strings.wav")

        sec7_title = Text("6. Die Rettung: Raw Strings", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec7_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Comparison cards
        card_normal = RoundedRectangle(corner_radius=0.12, width=5.4, height=3.2, color=RED, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, -0.6, 0])
        normal_t = Text("Klassischer String (doppelte Backslashes):", font_size=11, color=RED, weight=BOLD).next_to(card_normal.get_top(), DOWN, buff=0.3)
        normal_c = Paragraph(
            "let path = ",
            "  \"C:\\\\Programme\\\\Rust\\\\bin\";",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(normal_t, DOWN, buff=0.4).shift(LEFT * 0.2)
        normal_group = VGroup(card_normal, normal_t, normal_c)

        card_raw = RoundedRectangle(corner_radius=0.12, width=5.4, height=3.2, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, -0.6, 0])
        raw_t = Text("Raw String (Präfix r - kein Escaping nötig):", font_size=11, color=GREEN, weight=BOLD).next_to(card_raw.get_top(), DOWN, buff=0.3)
        raw_c = Paragraph(
            "let path = ",
            "  r\"C:\\Programme\\Rust\\bin\";",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(raw_t, DOWN, buff=0.4).shift(LEFT * 0.2)
        raw_group = VGroup(card_raw, raw_t, raw_c)

        self.play(FadeIn(normal_group, shift=RIGHT), FadeIn(raw_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Info badge
        info_badge = RoundedRectangle(corner_radius=0.1, width=11.0, height=0.6, color=CYAN, fill_color=CYAN, fill_opacity=0.15, stroke_width=2).move_to([0, -2.7, 0])
        info_text = Text("✔ Der Compiler ignoriert im Raw String jegliche Escaping-Sonderfunktionen!", font_size=12, color=CYAN, weight=BOLD).move_to(info_badge.get_center())
        info_group = VGroup(info_badge, info_text)

        self.play(FadeIn(info_group, shift=UP), run_time=1.5) # total 9.5s
        self.wait(17.41 - 9.5 - 1.0) # total 16.41s
        self.play(FadeOut(normal_group), FadeOut(raw_group), FadeOut(info_group), FadeOut(sec7_title), run_time=1.0) # total 17.41s


        # ==========================================
        # SECTION 8: METHODS (Duration: 20.76s)
        # ==========================================
        self.add_sound("audio/ch6_8_methods.wav")

        sec8_title = Text("7. Funktionen vs. Methoden", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec8_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Concept difference
        card_fn = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, 1.0, 0])
        fn_title = Text("Normale Funktion", font_size=13, color=CYAN, weight=BOLD).next_to(card_fn.get_top(), DOWN, buff=0.3)
        fn_desc = Text("Steht alleine:\nprintln!(...)", font_size=12, color=WHITE).next_to(fn_title, DOWN, buff=0.2)
        fn_group = VGroup(card_fn, fn_title, fn_desc)

        card_meth = RoundedRectangle(corner_radius=0.12, width=5.4, height=2.0, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, 1.0, 0])
        meth_title = Text("Methode", font_size=13, color=PURPLE, weight=BOLD).next_to(card_meth.get_top(), DOWN, buff=0.3)
        meth_desc = Text("Klebt mit Punkt an Variable:\ntext.trim()", font_size=12, color=WHITE).next_to(meth_title, DOWN, buff=0.2)
        meth_group = VGroup(card_meth, meth_title, meth_desc)

        self.play(FadeIn(fn_group, shift=RIGHT), FadeIn(meth_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(5.5) # total 9.0s

        # Code example showing math operations on floats
        meth_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.4, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -1.6, 0])
        meth_code = Paragraph(
            "let pi = 3.14159;",
            "pi.floor() -> 3.0  // Abrunden zum Boden (floor)",
            "pi.ceil()  -> 4.0  // Aufrunden zur Decke (ceiling)",
            "pi.round() -> 3.0  // Kaufmännisch runden zur nächsten Ganzzahl",
            font_size=12, line_spacing=0.5, color=WHITE
        ).move_to(meth_card.get_center()).shift(LEFT * 1.0)
        meth_code_group = VGroup(meth_card, meth_code)

        self.play(FadeIn(meth_code_group, shift=UP), run_time=1.5) # total 10.5s
        self.wait(20.76 - 10.5 - 1.0) # total 19.76s
        self.play(FadeOut(fn_group), FadeOut(meth_group), FadeOut(meth_code_group), FadeOut(sec8_title), run_time=1.0) # total 20.76s


        # ==========================================
        # SECTION 9: FLOAT FORMATTING (Duration: 20.54s)
        # ==========================================
        self.add_sound("audio/ch6_9_float_formatting.wav")

        sec9_title = Text("8. Formatierung bei Dezimalzahlen", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec9_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Code examples card
        code_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.8, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 0.8, 0])
        code_lines = Paragraph(
            "let pi = 3.14159265;",
            "println!(\"Pi auf 2 Stellen: {pi:.2}\"); // Ausgabe: 3.14",
            "println!(\"Pi auf 4 Stellen: {pi:.4}\"); // Ausgabe: 3.1416 (aufgerundet)",
            "println!(\"Klassisch: {:.3}\", pi);      // Ausgabe: 3.142",
            font_size=13, line_spacing=0.6, color=WHITE
        ).move_to(code_card.get_center()).shift(LEFT * 0.8)
        code_card_group = VGroup(code_card, code_lines)

        self.play(FadeIn(code_card_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(8.5) # total 12.0s

        # Eselsbrücke mnemonic visualization
        mnemonic_card = RoundedRectangle(corner_radius=0.12, width=11.0, height=1.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, -1.8, 0])
        m_title = Text("💡 Eselsbrücke für die Praxis:  {pi:.2}", font_size=15, color=CYAN, weight=BOLD).next_to(mnemonic_card.get_top(), DOWN, buff=0.2)
        m_desc = Text("Der Doppelpunkt : startet, der Punkt . trennt ab, und die 2 gibt die Anzahl Stellen an.", font_size=11, color=WHITE).next_to(m_title, DOWN, buff=0.2)
        m_group = VGroup(mnemonic_card, m_title, m_desc)

        self.play(FadeIn(m_group, shift=UP), run_time=1.5) # total 13.5s
        self.wait(20.54 - 13.5 - 1.0) # total 19.54s
        self.play(FadeOut(code_card_group), FadeOut(m_group), FadeOut(sec9_title), run_time=1.0) # total 20.54s


        # ==========================================
        # SECTION 10: CASTING WITH AS (Duration: 23.23s)
        # ==========================================
        self.add_sound("audio/ch6_10_casting.wav")

        sec10_title = Text("9. Casting (Typumwandlung) mit as", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec10_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Code casting representation
        cast_editor = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.4, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 1.0, 0])
        cast_code = Paragraph(
            "let strecke_float = 99.99;",
            "let strecke_int = strecke_float as i32;",
            "println!(\"{}\", strecke_int); // Ausgabe: 99",
            font_size=14, line_spacing=0.6, color=WHITE
        ).move_to(cast_editor.get_center()).shift(LEFT * 1.5)
        cast_group = VGroup(cast_editor, cast_code)

        self.play(FadeIn(cast_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(7.5) # total 11.0s

        # Critical Warning Card
        warning_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.0, color=RED, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=2.5).move_to([0, -1.6, 0])
        w_title = Text("⚠ WICHTIG: Rust schneidet beim Casting nur ab!", font_size=14, color=RED, weight=BOLD).next_to(warning_card.get_top(), DOWN, buff=0.2)
        w_desc = Paragraph(
            "Es wird niemals kaufmännisch aufgerundet! Aus 99.99 as i32 wird die Ganzzahl 99.\n"
            "Wenn du echtes Runden möchtest, wende vorher die Methode .round() an.",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(w_title, DOWN, buff=0.2)
        w_group = VGroup(warning_card, w_title, w_desc)

        self.play(FadeIn(w_group, shift=UP), run_time=1.5) # total 12.5s
        self.wait(23.23 - 12.5 - 1.0) # total 22.23s
        self.play(FadeOut(cast_group), FadeOut(w_group), FadeOut(sec10_title), run_time=1.0) # total 23.23s


        # ==========================================
        # SECTION 11: BOOLEANS (Duration: 21.95s)
        # ==========================================
        self.add_sound("audio/ch6_11_booleans.wav")

        sec11_title = Text("10. Wahrheitswerte (Booleans)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec11_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # States visualization
        card_t = RoundedRectangle(corner_radius=0.12, width=5.4, height=1.6, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([-3.0, 1.2, 0])
        t_title = Text("true (wahr)", font_size=15, color=GREEN, weight=BOLD).move_to(card_t.get_center())
        t_group = VGroup(card_t, t_title)

        card_f = RoundedRectangle(corner_radius=0.12, width=5.4, height=1.6, color=RED, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2).move_to([3.0, 1.2, 0])
        f_title = Text("false (falsch)", font_size=15, color=RED, weight=BOLD).move_to(card_f.get_center())
        f_group = VGroup(card_f, f_title)

        self.play(FadeIn(t_group, shift=RIGHT), FadeIn(f_group, shift=LEFT), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Storage info card
        storage_card = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.2, 0])
        s_title = Text("Speicher & Performance-Trick:", font_size=14, color=CYAN, weight=BOLD).next_to(storage_card.get_top(), DOWN, buff=0.2)
        s_desc = Paragraph(
            "• Typname: bool\n"
            "• Belegt 1 Byte (8 Bits) im Speicher, obwohl 1 Bit mathematisch reichen würde.\n"
            "• Grund: CPUs greifen auf ganze Bytes deutlich schneller zu als auf einzelne Bits.\n"
            "• Entstehung: Direkte Zuweisung, mathematische Vergleiche (z.B. 5 > 3) oder Methoden.",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(s_title, DOWN, buff=0.2).align_to(s_title, LEFT).shift(LEFT * 0.5)
        s_group = VGroup(storage_card, s_title, s_desc)

        self.play(FadeIn(s_group, shift=UP), run_time=1.5) # total 9.5s
        self.wait(21.95 - 9.5 - 1.0) # total 20.95s
        self.play(FadeOut(t_group), FadeOut(f_group), FadeOut(s_group), FadeOut(sec11_title), run_time=1.0) # total 21.95s


        # ==========================================
        # SECTION 12: CHAR & OUTRO (Duration: 22.44s)
        # ==========================================
        self.add_sound("audio/ch6_12_char_outro.wav")

        sec12_title = Text("11. Zeichen & Eselsbrücke", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec12_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Char comparison editor
        char_editor = RoundedRectangle(corner_radius=0.15, width=11.0, height=2.4, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 1.0, 0])
        char_code = Paragraph(
            "let buchstabe: char = 'B'; // Gültig (Einfache Anführungszeichen)",
            "let emoji: char = '🎧';    // Gültig (Ein Emoji ist ein Unicode-Zeichen)",
            "let text: &str = \"B\";     // String (Doppelte Anführungszeichen)",
            font_size=13, line_spacing=0.5, color=WHITE
        ).move_to(char_editor.get_center()).shift(LEFT * 0.8)
        char_code_group = VGroup(char_editor, char_code)

        self.play(FadeIn(char_code_group, shift=DOWN), run_time=1.5) # total 3.5s
        self.wait(6.5) # total 10.0s

        # Mnemonic card
        mnemonic_card2 = RoundedRectangle(corner_radius=0.12, width=11.0, height=1.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, -1.8, 0])
        m2_title = Text("💡 Eselsbrücke für Anfänger:", font_size=15, color=CYAN, weight=BOLD).next_to(mnemonic_card2.get_top(), DOWN, buff=0.2)
        m2_desc = Paragraph(
            "• Einfache Striche (')  = Einsames Zeichen (char)\n"
            "• Doppelte Striche (\") = Doppelt so viele Zeichen wie du willst (String)",
            font_size=12, line_spacing=0.5, color=WHITE
        ).next_to(m2_title, DOWN, buff=0.2).align_to(m2_title, LEFT).shift(LEFT * 0.5)
        m2_group = VGroup(mnemonic_card2, m2_title, m2_desc)

        self.play(FadeIn(m2_group, shift=UP), run_time=1.5) # total 11.5s
        self.wait(15.0 - 11.5) # total 15.0s

        # Fade out comparison, show outro
        outro_text = Text("Nächste Lektion:\nProjekt für Variablen &\nDatentypen (Übungen)", font_size=32, color=CYAN, weight=BOLD).move_to([0, -0.2, 0])
        self.play(
            FadeOut(char_code_group),
            FadeOut(m2_group),
            FadeIn(outro_text, shift=UP),
            run_time=1.5
        ) # total 16.5s

        self.wait(24.51 - 16.5 - 1.0) # total 23.51s
        self.play(FadeOut(outro_text), FadeOut(sec12_title), run_time=1.0) # total 24.51s
