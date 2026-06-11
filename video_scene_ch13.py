from manim import *
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
RED = "#ef4444"           # Red-500 for challenges/errors
YELLOW = "#f59e0b"        # Yellow-500 for warnings/info
LIGHT_BG = "#1e293b"      # slate-800 for card backgrounds
TERM_BG = "#090d16"       # Dark deep blue for terminal windows

def create_vscode_window(width=13.0, height=6.8, file_name="src/main.rs"):
    # Main editor frame
    window = RoundedRectangle(corner_radius=0.15, width=width, height=height, color=GRAY, fill_color="#1e1e1e", fill_opacity=0.98, stroke_width=2)
    
    # Header bar
    header_h = 0.45
    header = Rectangle(width=width, height=header_h, stroke_width=0, fill_color="#2d2d2d", fill_opacity=1.0).move_to([0, height/2 - header_h/2, 0])
    
    # Red, yellow, green window controls
    red_dot = Circle(radius=0.06, color=RED, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.25, height/2 - header_h/2, 0])
    yellow_dot = Circle(radius=0.06, color=YELLOW, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.45, height/2 - header_h/2, 0])
    green_dot = Circle(radius=0.06, color=GREEN, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.65, height/2 - header_h/2, 0])
    
    # VS Code Title
    title = Text(f"{file_name} - RustKurs - Visual Studio Code", font_size=10, color=WHITE, weight=NORMAL).move_to([0, height/2 - header_h/2, 0])
    
    # Status bar at the bottom
    status_h = 0.35
    status_bar = Rectangle(width=width, height=status_h, stroke_width=0, fill_color="#007acc", fill_opacity=1.0).move_to([0, -height/2 + status_h/2, 0])
    status_text = Text("Ln 1, Col 1   UTF-8   Rust   rust-analyzer: ready", font_size=8, color=WHITE).move_to([width/2 - 2.5, -height/2 + status_h/2, 0])
    
    # Sidebar
    sidebar_w = 2.2
    sidebar_h = height - header_h - status_h
    sidebar_y = -0.05
    sidebar = Rectangle(width=sidebar_w, height=sidebar_h, stroke_width=0, fill_color="#252526", fill_opacity=1.0).move_to([-width/2 + sidebar_w/2, sidebar_y, 0])
    
    # Line separating sidebar and editor
    sidebar_line = Line(start=[-width/2 + sidebar_w, -height/2 + status_h, 0], end=[-width/2 + sidebar_w, height/2 - header_h, 0], color="#2d2d2d", stroke_width=1.5)
    
    # Activity bar (Icons bar on the far left)
    act_bar_w = 0.6
    act_bar = Rectangle(width=act_bar_w, height=sidebar_h, stroke_width=0, fill_color="#333333", fill_opacity=1.0).move_to([-width/2 + act_bar_w/2, sidebar_y, 0])
    
    # Editor Tabs
    tab_h = 0.45
    tab_bar = Rectangle(width=width - sidebar_w, height=tab_h, stroke_width=0, fill_color="#2d2d2d", fill_opacity=1.0).move_to([sidebar_w/2, height/2 - header_h - tab_h/2, 0])
    active_tab = Rectangle(width=1.5, height=tab_h, stroke_width=0, fill_color="#1e1e1e", fill_opacity=1.0).move_to([-width/2 + sidebar_w + 0.75, height/2 - header_h - tab_h/2, 0])
    tab_text = Text(file_name.split("/")[-1], font_size=9, color=WHITE).move_to(active_tab.get_center())
    
    # Explorer items in sidebar (folders & files)
    explorer_title = Text("EXPLORER: RUSTKURS", font_size=8, color=GRAY, weight=BOLD).move_to([-width/2 + act_bar_w + 0.8, height/2 - header_h - 0.3, 0])
    folder_src = Text("> src", font_size=9, color=WHITE).move_to([-width/2 + act_bar_w + 0.4, height/2 - header_h - 0.7, 0])
    file_main = Text("  main.rs", font_size=9, color=RUST_ORANGE).move_to([-width/2 + act_bar_w + 0.52, height/2 - header_h - 1.0, 0])
    file_cargo = Text("Cargo.toml", font_size=9, color=GRAY).move_to([-width/2 + act_bar_w + 0.5, height/2 - header_h - 1.3, 0])
    
    explorer_group = VGroup(explorer_title, folder_src, file_main, file_cargo)
    
    vscode_group = VGroup(
        window, header, red_dot, yellow_dot, green_dot, title,
        sidebar, sidebar_line, act_bar, status_bar, status_text,
        tab_bar, active_tab, tab_text, explorer_group
    )
    
    return vscode_group

def create_terminal_panel(width=10.8, height=1.6, center=[-1.1, -1.75, 0]):
    # Simulation of integrated terminal in VS Code
    term_bg = Rectangle(width=width, height=height, stroke_width=0, fill_color=TERM_BG, fill_opacity=0.98).move_to(center)
    term_line = Line(start=[center[0] - width/2, center[1] + height/2, 0], end=[center[0] + width/2, center[1] + height/2, 0], color="#2d2d2d", stroke_width=1.5)
    term_tab = Text("TERMINAL", font_size=8, color=WHITE, weight=BOLD).move_to([center[0] - width/2 + 0.6, center[1] + height/2 - 0.2, 0])
    return VGroup(term_bg, term_line, term_tab)

def create_squiggly_line(start_pt, end_pt, color=RED, amplitude=0.04, wavelengths=10):
    # Generates a squiggly line for compiler errors
    points = []
    dx = end_pt[0] - start_pt[0]
    dy = end_pt[1] - start_pt[1]
    length = np.sqrt(dx**2 + dy**2)
    ux = dx / length
    uy = dy / length
    nx = -uy
    ny = ux
    
    for i in range(101):
        t = i / 100.0
        x_pt = start_pt[0] + t * dx + amplitude * np.sin(t * wavelengths * 2 * np.pi) * nx
        y_pt = start_pt[1] + t * dy + amplitude * np.sin(t * wavelengths * 2 * np.pi) * ny
        points.append([x_pt, y_pt, 0])
        
    return VMobject(color=color, stroke_width=2).set_points_as_corners(points)

class RustExercisesVideo(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Load durations
        try:
            with open("audio/durations_ch13.json", "r") as f:
                durations = json.load(f)
        except Exception:
            durations = {
                "ch13_1_intro": 25.0,
                "ch13_2_ex1": 30.0,
                "ch13_3_ex2": 30.0,
                "ch13_4_ex3": 35.0,
                "ch13_5_ex4": 30.0,
                "ch13_6_ex5": 35.0,
                "ch13_7_outro": 20.0
            }

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        dur_1 = durations["ch13_1_intro"]
        self.add_sound("audio/ch13_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 13: Übungen zu Operatoren", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4).shift(UP * 0.5)

        self.play(FadeIn(title_group, shift=UP), run_time=1.2)
        self.wait(2.0)

        title_small = Text("Kapitel 13: Übungen zu Operatoren", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Transform(title_group, title_small), run_time=1.2)
        self.wait(0.5)

        # Overview badge
        intro_badge = RoundedRectangle(corner_radius=0.15, width=9.8, height=2.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=2.5).shift(DOWN * 0.5)
        intro_badge_text = Text(
            "• Übung 1: Grundrechenarten & Ganzzahldivision\n"
            "• Übung 2: Die Ganzzahl-Falle bei der Division\n"
            "• Übung 3: Typen mischen & explizite Konvertierung (as)\n"
            "• Übung 4: Potenzierung & Wurzelziehen (powf, sqrt)\n"
            "• Übung 5: Zinseszinsberechnung als Praxisbeispiel",
            font_size=12, color=WHITE, line_spacing=0.6
        ).move_to(intro_badge.get_center())
        intro_badge_group = VGroup(intro_badge, intro_badge_text)

        self.play(FadeIn(intro_badge_group, shift=UP), run_time=1.5)
        self.wait(max(0.1, dur_1 - 1.2 - 2.0 - 1.2 - 0.5 - 1.5 - 1.0))
        self.play(FadeOut(intro_badge_group), FadeOut(title_group), run_time=1.0)

        # Create VS Code Editor layout globally
        vscode = create_vscode_window(13.2, 6.8, "src/main.rs").move_to([0, 0, 0])
        # Editor center is approx X=1.1, Y=0.0 (excluding tab/header/status)
        editor_x_left = -3.8
        editor_y_top = 2.0

        # ==========================================
        # SECTION 2: ÜBUNG 1 (GRUNDRECHENARTEN)
        # ==========================================
        dur_2 = durations["ch13_2_ex1"]
        self.add_sound("audio/ch13_2_ex1.wav")

        sec2_title = Text("Übung 1: Grundrechenarten", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.3).shift(RIGHT * 1.1)
        self.play(FadeIn(vscode), run_time=1.2)
        self.play(FadeIn(sec2_title), run_time=0.8)

        # Code block 1 (Ganzzahlige Grundrechenarten)
        code_1 = Paragraph(
            "fn main() {",
            "    let a = 15;",
            "    let b = 4;",
            "    let summe = a + b;     // Addition: 19",
            "    let quotient = a / b;  // Division: 3",
            "    let rest = a % b;      // Modulo: 3",
            "}",
            font_size=11, line_spacing=0.55, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(code_1), run_time=1.5)
        self.wait(5.0)

        # Highlight division and modulo lines
        hl_div = RoundedRectangle(corner_radius=0.05, width=7.2, height=0.32, color=CYAN, fill_opacity=0.15, stroke_width=1.0).move_to(code_1[4].get_center())
        hl_mod = RoundedRectangle(corner_radius=0.05, width=7.2, height=0.32, color=CYAN, fill_opacity=0.15, stroke_width=1.0).move_to(code_1[5].get_center())
        self.play(Create(hl_div), Create(hl_mod), run_time=1.2)
        self.wait(3.0)

        # Integrated terminal output
        terminal_panel = create_terminal_panel(10.8, 1.6, [1.1, -1.75, 0])
        term_text_1 = Paragraph(
            "$ cargo run",
            "Summe: 19",
            "Quotient: 3",
            "Rest der Division (Modulo): 3",
            font_size=10, line_spacing=0.5, color=GREEN
        ).move_to([editor_x_left + 1.8, -1.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(terminal_panel), FadeIn(term_text_1), run_time=1.2)
        self.wait(max(0.1, dur_2 - 1.2 - 0.8 - 1.5 - 5.0 - 1.2 - 3.0 - 1.2 - 1.0))

        # Clear section 2
        self.play(
            FadeOut(code_1), FadeOut(hl_div), FadeOut(hl_mod),
            FadeOut(terminal_panel), FadeOut(term_text_1), FadeOut(sec2_title),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: ÜBUNG 2 (GANZZAHL-FALLE)
        # ==========================================
        dur_3 = durations["ch13_3_ex2"]
        self.add_sound("audio/ch13_3_ex2.wav")

        sec3_title = Text("Übung 2: Die Ganzzahl-Falle", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.3).shift(RIGHT * 1.1)
        self.play(FadeIn(sec3_title), run_time=0.8)

        code_2_a = Paragraph(
            "fn main() {",
            "    let x = 7;",
            "    let y = 2;",
            "    let ergebnis = x / y; // Ganzzahldivision: 3!",
            "}",
            font_size=11, line_spacing=0.55, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.6, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(code_2_a), run_time=1.5)
        self.wait(6.0)

        # Draw red warning box and squiggly line under x / y
        warning_box = RoundedRectangle(corner_radius=0.1, width=7.2, height=0.8, color=RED, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([1.1, 0.2, 0])
        warning_text = Text("Achtung: Division schneidet Nachkommastellen ab!", font_size=10, color=RED).move_to(warning_box.get_center())
        # Position squiggly line under "x / y" in code_2_a[3]
        squiggly = create_squiggly_line([1.0, 1.0, 0], [2.4, 1.0, 0], color=RED)
        
        self.play(Create(squiggly), FadeIn(warning_box), FadeIn(warning_text), run_time=1.2)
        self.wait(4.0)

        # Transition code to correct float casting
        code_2_b = Paragraph(
            "fn main() {",
            "    let x = 7;",
            "    let y = 2;",
            "    // Lösung: explizites Casting in f64",
            "    let ergebnis_exakt = (x as f64) / (y as f64); // 3.5",
            "}",
            font_size=11, line_spacing=0.55, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.6, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(
            FadeOut(code_2_a), FadeOut(squiggly), FadeOut(warning_box), FadeOut(warning_text),
            FadeIn(code_2_b),
            run_time=1.5
        )
        self.wait(3.0)

        # Terminal panel and output
        term_text_2 = Paragraph(
            "$ cargo run",
            "Ganzzahliges Ergebnis: 3",
            "Exaktes Ergebnis: 3.5",
            font_size=10, line_spacing=0.5, color=GREEN
        ).move_to([editor_x_left + 1.8, -1.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(terminal_panel), FadeIn(term_text_2), run_time=1.2)
        self.wait(max(0.1, dur_3 - 0.8 - 1.5 - 6.0 - 1.2 - 4.0 - 1.5 - 3.0 - 1.2 - 1.0))

        # Clear section 3
        self.play(
            FadeOut(code_2_b), FadeOut(terminal_panel), FadeOut(term_text_2), FadeOut(sec3_title),
            run_time=1.0
        )

        # ==========================================
        # SECTION 4: ÜBUNG 3 (TYPEN MISCHEN)
        # ==========================================
        dur_4 = durations["ch13_4_ex3"]
        self.add_sound("audio/ch13_4_ex3.wav")

        sec4_title = Text("Übung 3: Typen mischen & Casting", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.3).shift(RIGHT * 1.1)
        self.play(FadeIn(sec4_title), run_time=0.8)

        # Part 1: Mismatched types compiler error
        code_3_a = Paragraph(
            "fn main() {",
            "    let integer_wert: i32 = 10;",
            "    let float_wert: f64 = 3.14;",
            "    // Fehler: i32 + f64 ist verboten!",
            "    let summe = integer_wert + float_wert;",
            "}",
            font_size=11, line_spacing=0.55, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.7, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(code_3_a), run_time=1.5)
        self.wait(6.0)

        # Compiler error simulation
        err_squiggly = create_squiggly_line([-1.2, 0.65, 0], [1.8, 0.65, 0], color=RED)
        err_box = RoundedRectangle(corner_radius=0.1, width=8.2, height=1.0, color=RED, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([1.1, -0.4, 0])
        err_text = Paragraph(
            "error[E0308]: mismatched types",
            "expected `i32`, found `f64` (no implicit conversion)",
            font_size=9, line_spacing=0.5, color=RED
        ).move_to(err_box.get_center())

        self.play(Create(err_squiggly), FadeIn(err_box), FadeIn(err_text), run_time=1.2)
        self.wait(5.0)

        # Part 2: Correct code and float truncation
        code_3_b = Paragraph(
            "fn main() {",
            "    let integer_wert: i32 = 10;",
            "    let float_wert: f64 = 3.14;",
            "    // 1. Korrekte Addition (i32 as f64)",
            "    let summe = (integer_wert as f64) + float_wert;",
            "    // 2. Float as i32 (Datenverlust!)",
            "    let float_als_integer = float_wert as i32; // ergibt 3",
            "}",
            font_size=11, line_spacing=0.52, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.9, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(
            FadeOut(code_3_a), FadeOut(err_squiggly), FadeOut(err_box), FadeOut(err_text),
            FadeIn(code_3_b),
            run_time=1.5
        )
        self.wait(5.0)

        # Highlight truncation line
        hl_trunc = RoundedRectangle(corner_radius=0.05, width=8.5, height=0.32, color=YELLOW, fill_opacity=0.15, stroke_width=1.0).move_to(code_3_b[6].get_center())
        trunc_warn_box = RoundedRectangle(corner_radius=0.1, width=7.2, height=0.7, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([1.1, -0.3, 0])
        trunc_warn_text = Text("Datenverlust: Nachkommastellen (.14) werden abgeschnitten!", font_size=9, color=YELLOW).move_to(trunc_warn_box.get_center())
        
        self.play(Create(hl_trunc), FadeIn(trunc_warn_box), FadeIn(trunc_warn_text), run_time=1.2)
        self.wait(4.0)

        # Terminal output
        term_text_3 = Paragraph(
            "$ cargo run",
            "Korrekt berechnete Summe: 13.14",
            "Fließkommazahl als Ganzzahl: 3",
            font_size=10, line_spacing=0.5, color=GREEN
        ).move_to([editor_x_left + 1.8, -1.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(
            FadeOut(trunc_warn_box), FadeOut(trunc_warn_text),
            FadeIn(terminal_panel), FadeIn(term_text_3),
            run_time=1.2
        )
        self.wait(max(0.1, dur_4 - 0.8 - 1.5 - 6.0 - 1.2 - 5.0 - 1.5 - 5.0 - 1.2 - 4.0 - 1.2 - 1.0))

        # Clear section 4
        self.play(
            FadeOut(code_3_b), FadeOut(hl_trunc), FadeOut(terminal_panel), FadeOut(term_text_3), FadeOut(sec4_title),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: ÜBUNG 4 (POTENZ & WURZEL)
        # ==========================================
        dur_5 = durations["ch13_5_ex4"]
        self.add_sound("audio/ch13_5_ex4.wav")

        sec5_title = Text("Übung 4: Potenzen & Wurzelziehen", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.3).shift(RIGHT * 1.1)
        self.play(FadeIn(sec5_title), run_time=0.8)

        code_4 = Paragraph(
            "fn main() {",
            "    let base: f64 = 2.0;",
            "    let exp: f64 = 3.0;",
            "    // Potenzierung (2.0 hoch 3.0)",
            "    let ergebnis_potenz = base.powf(exp); // 8.0",
            "    // Wurzelziehen (Quadratwurzel)",
            "    let wurzel_zahl: f64 = 16.0;",
            "    let ergebnis_wurzel = wurzel_zahl.sqrt(); // 4.0",
            "}",
            font_size=11, line_spacing=0.52, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 1.0, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(code_4), run_time=1.5)
        self.wait(6.0)

        # Highlights
        hl_pow = RoundedRectangle(corner_radius=0.05, width=8.5, height=0.32, color=PURPLE, fill_opacity=0.15, stroke_width=1.0).move_to(code_4[4].get_center())
        hl_sqrt = RoundedRectangle(corner_radius=0.05, width=8.5, height=0.32, color=PURPLE, fill_opacity=0.15, stroke_width=1.0).move_to(code_4[7].get_center())
        self.play(Create(hl_pow), Create(hl_sqrt), run_time=1.2)
        self.wait(4.0)

        # Terminal output
        term_text_4 = Paragraph(
            "$ cargo run",
            "2.0 hoch 3.0 = 8.0",
            "Quadratwurzel von 16.0 = 4.0",
            font_size=10, line_spacing=0.5, color=GREEN
        ).move_to([editor_x_left + 1.8, -1.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(terminal_panel), FadeIn(term_text_4), run_time=1.2)
        self.wait(max(0.1, dur_5 - 0.8 - 1.5 - 6.0 - 1.2 - 4.0 - 1.2 - 1.0))

        # Clear section 5
        self.play(
            FadeOut(code_4), FadeOut(hl_pow), FadeOut(hl_sqrt),
            FadeOut(terminal_panel), FadeOut(term_text_4), FadeOut(sec5_title),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: ÜBUNG 5 (ZINSESZINS)
        # ==========================================
        dur_6 = durations["ch13_6_ex5"]
        self.add_sound("audio/ch13_6_ex5.wav")

        sec6_title = Text("Übung 5: Zinseszinsberechnung", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.3).shift(RIGHT * 1.1)
        self.play(FadeIn(sec6_title), run_time=0.8)

        code_5 = Paragraph(
            "fn main() {",
            "    let initial_capital: f64 = 1000.0;",
            "    let annual_rate: f64 = 0.05;",
            "    let years: u32 = 10;",
            "    // Berechnung: Startkapital * (1 + Zins)^Jahre",
            "    // 'years' muss von u32 in f64 casten!",
            "    let final_amount = initial_capital *",
            "        (1.0 + annual_rate).powf(years as f64);",
            "}",
            font_size=10, line_spacing=0.5, color=WHITE
        ).move_to([editor_x_left, editor_y_top - 0.9, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(code_5), run_time=1.5)
        self.wait(8.0)

        # Highlight formula
        hl_formula = RoundedRectangle(corner_radius=0.05, width=8.5, height=0.65, color=RUST_ORANGE, fill_opacity=0.15, stroke_width=1.0).move_to(VGroup(code_5[6], code_5[7]).get_center())
        self.play(Create(hl_formula), run_time=1.2)
        self.wait(5.0)

        # Terminal output
        term_text_5 = Paragraph(
            "$ cargo run",
            "Startkapital: 1000.00 €",
            "Jährlicher Zinssatz: 5.00 %",
            "Laufzeit: 10 Jahre",
            "Endbetrag nach 10 Jahren Zinseszins: 1628.89 €",
            font_size=9, line_spacing=0.45, color=GREEN
        ).move_to([editor_x_left + 1.8, -1.8, 0]).align_to(vscode, LEFT).shift(RIGHT * 2.8)

        self.play(FadeIn(terminal_panel), FadeIn(term_text_5), run_time=1.2)
        self.wait(max(0.1, dur_6 - 0.8 - 1.5 - 8.0 - 1.2 - 5.0 - 1.2 - 1.0))

        # Clear VS Code completely
        self.play(
            FadeOut(vscode), FadeOut(code_5), FadeOut(hl_formula),
            FadeOut(terminal_panel), FadeOut(term_text_5), FadeOut(sec6_title),
            run_time=1.0
        )

        # ==========================================
        # SECTION 7: OUTRO
        # ==========================================
        dur_7 = durations["ch13_7_outro"]
        self.add_sound("audio/ch13_7_outro.wav")

        outro_title = Text("Zusammenfassung Kapitel 13", font_size=40, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.8)
        self.play(FadeIn(outro_title, shift=UP), run_time=1.0)

        outro_bullets = VGroup(
            Text("✔ Grundrechenarten bei Ganzzahlen verhalten sich hardwarenah", font_size=15, color=WHITE),
            Text("✔ Divisionen von Integern schneiden Nachkommastellen rigoros ab", font_size=15, color=WHITE),
            Text("✔ Keine impliziten Casts: 'as f64' oder 'as i32' explizit nutzen", font_size=15, color=WHITE),
            Text("✔ Komplexe Mathe wie powf() & sqrt() gibt es direkt auf Floats", font_size=15, color=WHITE),
            Text("✔ Zinseszins-Rechner vereint Arithmetik, Casting und Potenzen", font_size=15, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, -0.6, 0])

        for bullet in outro_bullets:
            self.play(FadeIn(bullet, shift=RIGHT), run_time=0.8)
            self.wait(1.5)

        self.wait(max(0.1, dur_7 - 1.0 - (0.8 + 1.5) * 5 - 1.0))
        self.play(FadeOut(outro_title), FadeOut(outro_bullets), run_time=1.0)
