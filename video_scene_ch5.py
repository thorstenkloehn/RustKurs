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
RED = "#ef4444"           # Red-500 for challenges
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

def create_lock(closed=True, color=WHITE):
    body = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.1, color=color, fill_color=color, fill_opacity=0.2, stroke_width=2.5)
    shackle_arc = Arc(radius=0.3, start_angle=0, angle=PI, color=color, stroke_width=2.5)
    
    if closed:
        shackle_left = Line(start=[-0.3, 0, 0], end=[-0.3, 0.3, 0], color=color, stroke_width=2.5)
        shackle_right = Line(start=[0.3, 0, 0], end=[0.3, 0.3, 0], color=color, stroke_width=2.5)
        shackle = VGroup(shackle_arc, shackle_left, shackle_right).move_to([0, 0.45, 0])
    else:
        shackle_left = Line(start=[-0.3, 0.1, 0], end=[-0.3, 0.4, 0], color=color, stroke_width=2.5)
        shackle_right = Line(start=[0.3, 0.1, 0], end=[0.3, 0.4, 0], color=color, stroke_width=2.5)
        shackle = VGroup(shackle_arc, shackle_left, shackle_right).move_to([0, 0.55, 0]).rotate(0.4)
    
    keyhole_top = Circle(radius=0.08, color=color, fill_opacity=1, stroke_width=0).move_to([0, 0.05, 0])
    keyhole_bot = Polygon([-0.05, -0.15, 0], [0.05, -0.15, 0], [0.03, 0.05, 0], [-0.03, 0.05, 0], color=color, fill_opacity=1, stroke_width=0)
    keyhole = VGroup(keyhole_top, keyhole_bot)
    
    return VGroup(body, shackle, keyhole)

def create_book(title, value, color):
    cover = RoundedRectangle(width=2.0, height=2.6, corner_radius=0.1, color=color, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=3)
    spine = Line(start=[-0.8, -1.3, 0], end=[-0.8, 1.3, 0], color=color, stroke_width=4)
    title_text = Text(title, font_size=20, color=color, weight=BOLD).move_to([0, 0.4, 0])
    val_text = Text(value, font_size=16, color=WHITE).move_to([0, -0.4, 0])
    return VGroup(cover, spine, title_text, val_text)

class RustVariablesVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 19.71s)
        # ==========================================
        self.add_sound("audio/ch5_1_intro.wav")

        # 0s - 3s: Title
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 5: Variablen & Konstanten", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0) # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 5: Variablen in Rust", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5) # total 4.5s
        self.wait(0.5) # total 5.0s

        # 5s - 10s: Draw Box representation
        box_outline = RoundedRectangle(corner_radius=0.15, width=3.0, height=2.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=3).move_to([-3.0, -0.5, 0])
        box_label = Text("x", font_size=32, color=CYAN, weight=BOLD).next_to(box_outline.get_top(), DOWN, buff=0.3)
        box_value = Text("42", font_size=28, color=WHITE).move_to(box_outline.get_center()).shift(DOWN * 0.2)
        box_desc = Text("Variable = Beschriftete Box", font_size=16, color=WHITE).next_to(box_outline, DOWN, buff=0.4)
        box_group = VGroup(box_outline, box_label, box_value, box_desc)

        self.play(FadeIn(box_group, shift=RIGHT), run_time=1.5) # total 6.5s
        self.wait(3.5) # total 10.0s

        # 10s - 18.71s: Show Overview of Content on the Right
        bullet1 = Text("• Deklaration & Warnungen", font_size=18, color=WHITE)
        bullet2 = Text("• Das println! Makro", font_size=18, color=WHITE)
        bullet3 = Text("• Mutability (Veränderlichkeit)", font_size=18, color=WHITE)
        bullet4 = Text("• Scopes & Shadowing", font_size=18, color=WHITE)
        bullet5 = Text("• Konstanten (const)", font_size=18, color=WHITE)
        bullets = VGroup(bullet1, bullet2, bullet3, bullet4, bullet5).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([2.8, -0.5, 0])

        self.play(FadeIn(bullets, shift=LEFT), run_time=1.5) # total 11.5s
        self.wait(19.71 - 11.5 - 1.0) # total 18.71s
        self.play(FadeOut(box_group), FadeOut(bullets), FadeOut(title_group), run_time=1.0) # total 19.71s


        # ==========================================
        # SECTION 2: WARNINGS & ERRORS (Duration: 28.33s)
        # ==========================================
        self.add_sound("audio/ch5_2_warnings.wav")

        sec2_title = Text("1. Warnungen vs. Fehler", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec2_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.5) # total 2.5s

        # Draw Editor Window
        editor = create_terminal_window(11.0, 5.0, "VS Code - main.rs").move_to([0, -0.6, 0])
        self.play(FadeIn(editor, shift=DOWN), run_time=1.5) # total 4.0s

        # Code with Warning
        code_warn = Paragraph(
            "fn main() {",
            "    let apples = 5;",
            "}",
            font_size=16, line_spacing=0.6, color=WHITE
        ).move_to(editor.get_center()).shift(LEFT * 3.5 + UP * 0.5)
        
        # Yellow squiggly under "apples" (relative coordinates to editor)
        squiggly_yellow = create_squiggly_line([-2.4, -0.4, 0], [-1.2, -0.4, 0], YELLOW)
        warn_msg_rect = RoundedRectangle(corner_radius=0.08, width=5.8, height=1.0, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([2.0, 0.4, 0])
        warn_msg = Paragraph(
            "warning: unused variable: `apples`",
            "help: if this is intentional, prefix it with an underscore: `_apples`",
            font_size=10, line_spacing=0.5, color=YELLOW
        ).move_to(warn_msg_rect.get_center())
        warn_box = VGroup(warn_msg_rect, warn_msg)

        ok_badge = RoundedRectangle(corner_radius=0.1, width=4.0, height=0.6, color=GREEN, fill_color=GREEN, fill_opacity=0.15, stroke_width=2.5).move_to([2.0, -1.0, 0])
        ok_text = Text("✔ Programm läuft trotzdem!", font_size=12, color=GREEN, weight=BOLD).move_to(ok_badge.get_center())
        ok_group = VGroup(ok_badge, ok_text)

        warn_scene = VGroup(code_warn, squiggly_yellow, warn_box, ok_group)
        self.play(FadeIn(warn_scene), run_time=1.5) # total 5.5s
        self.wait(7.5) # total 13.0s

        # Now replace with Error Code
        code_err = Paragraph(
            "fn main() {",
            "    let apples =",
            "}",
            font_size=16, line_spacing=0.6, color=WHITE
        ).move_to(editor.get_center()).shift(LEFT * 3.5 + UP * 0.5)

        squiggly_red = create_squiggly_line([-1.2, -0.4, 0], [-0.5, -0.4, 0], RED)
        err_msg_rect = RoundedRectangle(corner_radius=0.08, width=5.8, height=1.0, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([2.0, 0.4, 0])
        err_msg = Paragraph(
            "error: expected expression, found `}`",
            "error: could not compile `hello_world` due to previous error",
            font_size=10, line_spacing=0.5, color=RED
        ).move_to(err_msg_rect.get_center())
        err_box = VGroup(err_msg_rect, err_msg)

        fail_badge = RoundedRectangle(corner_radius=0.1, width=4.5, height=0.6, color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=2.5).move_to([2.0, -1.0, 0])
        fail_text = Text("✘ Fataler Fehler! Kompiliert nicht.", font_size=12, color=RED, weight=BOLD).move_to(fail_badge.get_center())
        fail_group = VGroup(fail_badge, fail_text)

        err_scene = VGroup(code_err, squiggly_red, err_box, fail_group)
        
        self.play(FadeOut(warn_scene), FadeIn(err_scene), run_time=1.5) # total 14.5s
        self.wait(28.33 - 14.5 - 1.0) # total 27.33s
        self.play(FadeOut(editor), FadeOut(err_scene), FadeOut(sec2_title), run_time=1.0) # total 28.33s


        # ==========================================
        # SECTION 3: PRINTLN! (Duration: 24.47s)
        # ==========================================
        self.add_sound("audio/ch5_3_println.wav")

        sec3_title = Text("2. Text ausgeben: println!", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec3_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Card A (Left)
        card_a_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.0, -0.6, 0])
        card_a_title = Text("Methode A: Direkt-Interpolation", font_size=14, color=CYAN, weight=BOLD).next_to(card_a_rect.get_top(), DOWN, buff=0.3)
        card_a_vers = Text("(ab Rust Version 1.58)", font_size=11, color=GRAY).next_to(card_a_title, DOWN, buff=0.1)
        card_a_code = Paragraph(
            "let name = \"Thorsten\";",
            "println!(\"Hallo {name}!\");",
            font_size=14, line_spacing=0.8, color=WHITE
        ).next_to(card_a_vers, DOWN, buff=0.6).shift(LEFT * 0.4)
        card_a = VGroup(card_a_rect, card_a_title, card_a_vers, card_a_code)

        self.play(FadeIn(card_a, shift=UP), run_time=1.5) # total 3.5s
        self.wait(6.5) # total 10.0s

        # Card B (Right)
        card_b_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, -0.6, 0])
        card_b_title = Text("Methode B: Argumente anhängen", font_size=14, color=PURPLE, weight=BOLD).next_to(card_b_rect.get_top(), DOWN, buff=0.3)
        card_b_vers = Text("(Klassische Variante)", font_size=11, color=GRAY).next_to(card_b_title, DOWN, buff=0.1)
        card_b_code = Paragraph(
            "let name = \"Thorsten\";",
            "println!(\"Hallo {}!\", name);",
            font_size=14, line_spacing=0.8, color=WHITE
        ).next_to(card_b_vers, DOWN, buff=0.6).shift(LEFT * 0.4)
        card_b = VGroup(card_b_rect, card_b_title, card_b_vers, card_b_code)

        self.play(FadeIn(card_b, shift=UP), run_time=1.5) # total 11.5s
        self.wait(24.47 - 11.5 - 1.0) # total 23.47s
        self.play(FadeOut(card_a), FadeOut(card_b), FadeOut(sec3_title), run_time=1.0) # total 24.47s


        # ==========================================
        # SECTION 4: POSITIONAL ARGUMENTS (Duration: 21.61s)
        # ==========================================
        self.add_sound("audio/ch5_4_positional.wav")

        sec4_title = Text("3. Positionsargumente in println!", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec4_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Code display
        code_pos = Text(
            'println!("Ich mag {0} und {1}. Ja, wirklich {0}!", äpfel, orangen);',
            font_size=16, color=WHITE
        ).move_to([0, 0.8, 0])
        self.play(Write(code_pos), run_time=2.0) # total 4.0s
        self.wait(1.0) # total 5.0s

        # Highlight positions
        arrow0_1 = CurvedArrow(start_point=[-1.7, 0.5, 0], end_point=[1.9, 0.5, 0], color=CYAN, angle=-TAU/4)
        arrow1 = CurvedArrow(start_point=[-0.6, 0.5, 0], end_point=[2.9, 0.5, 0], color=GREEN, angle=-TAU/3)
        arrow0_2 = CurvedArrow(start_point=[0.8, 0.5, 0], end_point=[1.9, 0.5, 0], color=CYAN, angle=-TAU/5)
        
        lbl_0 = Text("Position 0", font_size=10, color=CYAN).move_to([-1.7, 1.2, 0])
        lbl_1 = Text("Position 1", font_size=10, color=GREEN).move_to([-0.6, 1.2, 0])
        arg_0 = Text("Argument 0", font_size=10, color=CYAN).move_to([1.9, 1.2, 0])
        arg_1 = Text("Argument 1", font_size=10, color=GREEN).move_to([2.9, 1.2, 0])

        highlights = VGroup(arrow0_1, arrow1, arrow0_2, lbl_0, lbl_1, arg_0, arg_1)
        self.play(FadeIn(highlights), run_time=2.0) # total 7.0s
        self.wait(5.0) # total 12.0s

        # Output box
        out_rect = RoundedRectangle(corner_radius=0.12, width=10.0, height=0.8, color=GRAY, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.8, 0])
        out_text = Text('Ausgabe: "Ich mag äpfel und orangen. Ja, wirklich äpfel!"', font_size=14, color=WHITE).move_to(out_rect.get_center())
        out_group = VGroup(out_rect, out_text)

        self.play(FadeIn(out_group, shift=UP), run_time=1.5) # total 13.5s
        self.wait(21.61 - 13.5 - 1.0) # total 20.61s
        self.play(FadeOut(code_pos), FadeOut(highlights), FadeOut(out_group), FadeOut(sec4_title), run_time=1.0) # total 21.61s


        # ==========================================
        # SECTION 5: THE UNDERSCORE (Duration: 17.17s)
        # ==========================================
        self.add_sound("audio/ch5_5_underscore.wav")

        sec5_title = Text("4. Die Lösung: Der Unterstrich (_)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec5_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Show old warning code
        editor_under = create_terminal_window(9.0, 4.0, "VS Code").move_to([0, -0.6, 0])
        code_under1 = Paragraph(
            "fn main() {",
            "    let apples = 5;",
            "}",
            font_size=15, line_spacing=0.6, color=WHITE
        ).move_to(editor_under.get_center()).shift(LEFT * 2.5 + UP * 0.4)
        squiggly_u1 = create_squiggly_line([-1.5, -0.4, 0], [-0.5, -0.4, 0], YELLOW)
        warn_lbl = Text("⚠ warning: unused variable: `apples`", font_size=11, color=YELLOW).move_to([2.0, -0.4, 0])

        under_w1 = VGroup(editor_under, code_under1, squiggly_u1, warn_lbl)
        self.play(FadeIn(under_w1), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Transform to underscore code
        code_under2 = Paragraph(
            "fn main() {",
            "    let _apples = 5;",
            "}",
            font_size=15, line_spacing=0.6, color=WHITE
        ).move_to(editor_under.get_center()).shift(LEFT * 2.5 + UP * 0.4)
        
        ok_lbl = Text("✔ Warnung verschwindet!", font_size=12, color=GREEN, weight=BOLD).move_to([2.0, -0.4, 0])
        
        self.play(
            Transform(code_under1, code_under2),
            FadeOut(squiggly_u1),
            Transform(warn_lbl, ok_lbl),
            run_time=1.5
        ) # total 9.5s

        self.wait(17.17 - 9.5 - 1.0) # total 16.17s
        self.play(FadeOut(under_w1), FadeOut(sec5_title), run_time=1.0) # total 17.17s


        # ==========================================
        # SECTION 6: MUTABILITY (Duration: 18.88s)
        # ==========================================
        self.add_sound("audio/ch5_6_mutability.wav")

        sec6_title = Text("5. Unveränderlich vs. Veränderbar", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec6_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.5) # total 2.5s

        # Card Left: Immutable
        card_imm_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=RED, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([-3.0, -0.6, 0])
        card_imm_title = Text("Standard: let (Immutable)", font_size=14, color=RED, weight=BOLD).next_to(card_imm_rect.get_top(), DOWN, buff=0.3)
        card_imm_code = Paragraph(
            "let x = 5;",
            "x = 6; // ✘ FEHLER!",
            font_size=14, line_spacing=0.8, color=WHITE
        ).next_to(card_imm_title, DOWN, buff=0.4).shift(LEFT * 0.6)
        lock_closed = create_lock(closed=True, color=RED).scale(0.8).move_to([-3.0, -1.8, 0])
        card_imm = VGroup(card_imm_rect, card_imm_title, card_imm_code, lock_closed)

        self.play(FadeIn(card_imm, shift=UP), run_time=1.5) # total 4.0s
        self.wait(4.0) # total 8.0s

        # Card Right: Mutable
        card_mut_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([3.0, -0.6, 0])
        card_mut_title = Text("Veränderbar: let mut (Mutable)", font_size=14, color=GREEN, weight=BOLD).next_to(card_mut_rect.get_top(), DOWN, buff=0.3)
        card_mut_code = Paragraph(
            "let mut x = 5;",
            "x = 6; // ✔ Erlaubt!",
            font_size=14, line_spacing=0.8, color=WHITE
        ).next_to(card_mut_title, DOWN, buff=0.4).shift(LEFT * 0.6)
        lock_open = create_lock(closed=False, color=GREEN).scale(0.8).move_to([3.0, -1.8, 0])
        card_mut = VGroup(card_mut_rect, card_mut_title, card_mut_code, lock_open)

        self.play(FadeIn(card_mut, shift=UP), run_time=1.5) # total 9.5s
        self.wait(18.88 - 9.5 - 1.0) # total 17.88s
        self.play(FadeOut(card_imm), FadeOut(card_mut), FadeOut(sec6_title), run_time=1.0) # total 18.88s


        # ==========================================
        # SECTION 7: COMPILER HELP (Duration: 17.88s)
        # ==========================================
        self.add_sound("audio/ch5_7_explain.wav")

        sec7_title = Text("6. Fehler erklären mit rustc", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec7_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Draw Terminal Window
        terminal_help = create_terminal_window(11.0, 4.6, "Terminal - Hilfe anfordern").move_to([0, -0.6, 0])
        self.play(FadeIn(terminal_help, shift=DOWN), run_time=1.5) # total 3.5s

        # Type command
        cmd_text = Text("$ rustc --explain E0384", font_size=15, color=WHITE).move_to(terminal_help.get_center()).shift(LEFT * 3.2 + UP * 1.2)
        self.play(Write(cmd_text), run_time=1.5) # total 5.0s
        self.wait(3.0) # total 8.0s

        # Display explanation output
        explain_output = Paragraph(
            "An immutable variable was reassigned.",
            "Example of erroneous code:",
            "  let x = 3;",
            "  x = 5; // error: cannot assign twice to immutable variable",
            "To fix this, make the variable mutable: `let mut x = 3;`",
            font_size=11, line_spacing=0.5, color=GRAY
        ).move_to(terminal_help.get_center()).shift(LEFT * 1.5 + DOWN * 0.4)
        
        self.play(FadeIn(explain_output), run_time=1.5) # total 9.5s
        self.wait(17.88 - 9.5 - 1.0) # total 16.88s
        self.play(FadeOut(terminal_help), FadeOut(cmd_text), FadeOut(explain_output), FadeOut(sec7_title), run_time=1.0) # total 17.88s


        # ==========================================
        # SECTION 8: VARIABLE SHADOWING (Duration: 19.99s)
        # ==========================================
        self.add_sound("audio/ch5_8_shadowing.wav")

        sec8_title = Text("7. Variablen-Shadowing", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec8_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Show code
        code_shadow = Paragraph(
            "let x = \"fünf\"; // Typ: &str",
            "let x = 5;      // Typ: i32 (Shadowing)",
            font_size=16, line_spacing=0.8, color=WHITE
        ).move_to([-3.0, 0.2, 0])
        self.play(FadeIn(code_shadow, shift=RIGHT), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Analogy: Book stacks
        book1 = create_book('let x', '"fünf"', CYAN).move_to([3.0, -1.0, 0])
        book2 = create_book('let x', '5', PURPLE).move_to([3.0, 1.2, 0])

        self.play(FadeIn(book1, shift=UP), run_time=1.0) # total 9.0s
        self.wait(1.0) # total 10.0s
        
        # Drop book2 on top of book1
        self.play(
            book2.animate.move_to([3.0, -0.6, 0]),
            book1.animate.scale(0.95).set_opacity(0.4).move_to([3.0, -1.2, 0]),
            run_time=2.0
        ) # total 12.0s
        
        shadow_lbl = Text("Alte Variable überschattet!", font_size=12, color=PURPLE, weight=BOLD).move_to([3.0, -2.2, 0])
        self.play(FadeIn(shadow_lbl), run_time=1.0) # total 13.0s

        self.wait(19.99 - 13.0 - 1.0) # total 18.99s
        self.play(FadeOut(code_shadow), FadeOut(book1), FadeOut(book2), FadeOut(shadow_lbl), FadeOut(sec8_title), run_time=1.0) # total 19.99s


        # ==========================================
        # SECTION 9: SCOPE RULES (Duration: 25.94s)
        # ==========================================
        self.add_sound("audio/ch5_9_scopes.wav")

        sec9_title = Text("8. Gültigkeitsbereiche (Scopes)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec9_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Scopes nesting visualization
        outer_bg = RoundedRectangle(corner_radius=0.15, width=6.5, height=4.2, fill_color=LIGHT_BG, fill_opacity=0.4, stroke_width=0).move_to([-3.2, -0.8, 0])
        outer_border = RoundedRectangle(corner_radius=0.15, width=6.5, height=4.2, color=CYAN, stroke_width=2).move_to([-3.2, -0.8, 0])
        outer_scope_border = DashedVMobject(outer_border, num_dashes=30)
        outer_scope = VGroup(outer_bg, outer_scope_border)
        outer_lbl = Text("Äußerer Block", font_size=10, color=CYAN).next_to(outer_bg.get_top(), DOWN, buff=0.2).align_to(outer_bg.get_left(), LEFT).shift(RIGHT * 0.3)
        outer_var = Text("let a = 1;", font_size=14, color=WHITE).next_to(outer_lbl, DOWN, buff=0.4).align_to(outer_lbl, LEFT)
        
        inner_bg = RoundedRectangle(corner_radius=0.15, width=4.5, height=2.2, fill_color=LIGHT_BG, fill_opacity=0.7, stroke_width=0).move_to([-3.2, -1.5, 0])
        inner_border = RoundedRectangle(corner_radius=0.15, width=4.5, height=2.2, color=PURPLE, stroke_width=2).move_to([-3.2, -1.5, 0])
        inner_scope_border = DashedVMobject(inner_border, num_dashes=20)
        inner_scope = VGroup(inner_bg, inner_scope_border)
        inner_lbl = Text("Innerer Block", font_size=10, color=PURPLE).next_to(inner_bg.get_top(), DOWN, buff=0.2).align_to(inner_bg.get_left(), LEFT).shift(RIGHT * 0.3)
        inner_var = Text("let b = 2;", font_size=14, color=WHITE).next_to(inner_lbl, DOWN, buff=0.4).align_to(inner_lbl, LEFT)

        self.play(FadeIn(outer_scope), FadeIn(outer_lbl), FadeIn(outer_var), run_time=1.5) # total 3.5s
        self.wait(3.5) # total 7.0s

        self.play(FadeIn(inner_scope), FadeIn(inner_lbl), FadeIn(inner_var), run_time=1.5) # total 8.5s
        self.wait(1.5) # total 10.0s

        # Rule 1: Inner sees Outer
        arrow_in_to_out = DoubleArrow(start=[-3.2, -1.8, 0], end=[-5.0, -0.5, 0], color=GREEN, stroke_width=2.5, buff=0.1)
        ok_lbl_rule1 = Text("✔ Sichtbar (innen nach außen)", font_size=10, color=GREEN).move_to([-3.2, -0.2, 0])
        self.play(Create(arrow_in_to_out), FadeIn(ok_lbl_rule1), run_time=1.5) # total 11.5s
        self.wait(1.5) # total 13.0s

        # Rule 2: Outer cannot see Inner (Draw cross)
        arrow_out_to_in = Arrow(start=[-1.0, -0.5, 0], end=[-2.0, -1.8, 0], color=RED, stroke_width=2.5, buff=0.1)
        cross_red = Cross(arrow_out_to_in, stroke_color=RED, stroke_width=4).scale(0.3).move_to(arrow_out_to_in.get_center())
        fail_lbl_rule2 = Text("✘ Gesperrt (außen nach innen)", font_size=10, color=RED).move_to([-1.0, -1.0, 0])
        self.play(Create(arrow_out_to_in), Create(cross_red), FadeIn(fail_lbl_rule2), run_time=1.5) # total 14.5s
        
        # House Analogy (Right side)
        house_wall = Rectangle(width=3.6, height=2.4, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2.5).move_to([3.4, -1.2, 0])
        house_roof = Polygon([1.3, 0.0, 0], [5.5, 0.0, 0], [3.4, 1.2, 0], color=GRAY, fill_color=GRAY, fill_opacity=0.9, stroke_width=2.5)
        house_window = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.8, color=CYAN, fill_color=CYAN, fill_opacity=0.3, stroke_width=2).move_to([3.4, -1.0, 0])
        house = VGroup(house_wall, house_roof, house_window)
        
        mirror_lbl = Paragraph(
            "Scope = Haus mit Einwegspiegeln:",
            "Wer drin steht (innerer Block) sieht raus.",
            "Wer draußen steht, sieht nicht rein.",
            font_size=11, line_spacing=0.6, color=WHITE
        ).move_to([3.4, 2.0, 0])

        self.play(FadeIn(house, shift=UP), FadeIn(mirror_lbl), run_time=2.0) # total 16.5s
        
        self.wait(25.94 - 16.5 - 1.0) # total 24.94s
        self.play(
            FadeOut(outer_scope), FadeOut(outer_lbl), FadeOut(outer_var),
            FadeOut(inner_scope), FadeOut(inner_lbl), FadeOut(inner_var),
            FadeOut(arrow_in_to_out), FadeOut(ok_lbl_rule1),
            FadeOut(arrow_out_to_in), FadeOut(cross_red), FadeOut(fail_lbl_rule2),
            FadeOut(house), FadeOut(mirror_lbl), FadeOut(sec9_title),
            run_time=1.0
        ) # total 25.94s


        # ==========================================
        # SECTION 10: CONSTANTS & OUTRO (Duration: 21.35s)
        # ==========================================
        self.add_sound("audio/ch5_10_constants.wav")

        sec10_title = Text("9. Konstanten (const)", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(sec10_title, shift=UP), run_time=1.0) # total 1.0s
        self.wait(1.0) # total 2.0s

        # Card Whiteboard (let)
        whiteboard = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=GRAY, fill_color=WHITE, fill_opacity=0.9, stroke_width=2).move_to([-3.0, -0.6, 0])
        wb_title = Text("Variable: let", font_size=15, color=TERM_BG, weight=BOLD).next_to(whiteboard.get_top(), DOWN, buff=0.3)
        wb_code = Paragraph(
            "let x = 5;",
            "• Beschreibbares Whiteboard",
            "• Kann abgewischt werden",
            "  (mit let mut)",
            font_size=13, line_spacing=0.6, color=TERM_BG
        ).next_to(wb_title, DOWN, buff=0.4).shift(LEFT * 0.2)
        wb_group = VGroup(whiteboard, wb_title, wb_code)

        self.play(FadeIn(wb_group, shift=UP), run_time=1.5) # total 3.5s
        self.wait(4.5) # total 8.0s

        # Card Stone (const)
        stone = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color=GRAY, fill_color=GRAY, fill_opacity=0.9, stroke_width=2).move_to([3.0, -0.6, 0])
        st_title = Text("Konstante: const", font_size=15, color=WHITE, weight=BOLD).next_to(stone.get_top(), DOWN, buff=0.3)
        st_code = Paragraph(
            "const MAX_PTS: u32 = 100_000;",
            "• In Stein gemeißelt",
            "• Datentyp zwingend nötig",
            "• Wert fest zur Kompilierzeit",
            font_size=13, line_spacing=0.6, color=WHITE
        ).next_to(st_title, DOWN, buff=0.4).shift(LEFT * 0.2)
        st_group = VGroup(stone, st_title, st_code)

        self.play(FadeIn(st_group, shift=UP), run_time=1.5) # total 9.5s
        self.wait(5.5) # total 15.0s

        # Fade out comparison cards, show outro
        outro_text = Text("Nächste Lektion:\nDatentypen in Rust", font_size=32, color=CYAN, weight=BOLD).move_to([0, -0.6, 0])
        self.play(
            FadeOut(wb_group),
            FadeOut(st_group),
            FadeIn(outro_text, shift=UP),
            run_time=1.5
        ) # total 16.5s

        self.wait(21.35 - 16.5 - 1.0) # total 20.35s
        self.play(FadeOut(outro_text), FadeOut(sec10_title), run_time=1.0) # total 21.35s
