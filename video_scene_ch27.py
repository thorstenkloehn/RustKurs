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

class RustStructsVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Continuous watermark footer
        watermark = Text(
            "Rust Kurs | Kapitel 27: Eigene Datentypen mit Structs",
            font_size=8.0,
            color=GRAY,
            fill_opacity=0.65
        ).to_edge(DOWN, buff=0.15)
        self.add(watermark)

        # Default durations (will be updated by JSON)
        durations = {
            "ch27_1_intro": 15.0,
            "ch27_2_definition": 15.0,
            "ch27_3_problem": 15.0,
            "ch27_4_naive": 15.0,
            "ch27_5_anatomy": 15.0,
            "ch27_6_solution": 15.0,
            "ch27_7_tutorial": 15.0,
            "ch27_8_deepdive": 15.0,
            "ch27_9_exercises": 15.0,
            "ch27_10_learning": 15.0,
            "ch27_11_outro": 15.0
        }
        
        durations_path = "audio/durations_ch27.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        def get_wait_time(key, anim_time):
            d_i = durations[key]
            wait_val = d_i + 0.5 - anim_time
            return max(0.1, wait_val)

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        self.add_sound("audio/ch27_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=38, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 27: Eigene Datentypen mit Structs", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 27: Eigene Datentypen mit Structs", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Intro bullet points
        bullets = VGroup(
            Text("• Datenkapselung & Speicherlayout (Stack vs. Heap)", font_size=16, color=WHITE),
            Text("• Verhalten binden (Methoden & Assoziierte Funktionen)", font_size=16, color=WHITE),
            Text("• Fortgeschrittene Muster (Builder & Type-State)", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, -0.6, 0])

        self.play(LaggedStart(*(FadeIn(b, shift=RIGHT) for b in bullets), lag_ratio=0.3), run_time=2.0)
        self.wait(2.0)

        # Total anim time: 1.5 + 2.5 + 1.5 + 1.0 + 2.0 + 2.0 = 10.5 seconds
        self.wait(get_wait_time("ch27_1_intro", 10.5))
        self.play(FadeOut(bullets), run_time=1.0)

        # ==========================================
        # SECTION 2: DEFINITION
        # ==========================================
        self.add_sound("audio/ch27_2_definition.wav")

        title_def = Text("27. Die Definition: Die drei Arten von Structs", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_def), run_time=1.0)
        self.wait(1.0)

        # Draw three comparison cards
        card_w, card_h = 3.6, 2.2
        card1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.4, 0])
        card1_title = Text("Klassisches Struct", font_size=12, color=GRAY, weight=BOLD).next_to(card1.get_top(), DOWN, buff=0.2)
        card1_desc = Paragraph("• Benannte Felder\n• Punktzugriff (.x)\n• Aktenmappe", font_size=9, color=WHITE, line_spacing=0.4).next_to(card1_title, DOWN, buff=0.2).align_to(card1, LEFT).shift(RIGHT * 0.4)
        g_card1 = VGroup(card1, card1_title, card1_desc)

        card2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0.0, -0.4, 0])
        card2_title = Text("Tuple Struct", font_size=12, color=CYAN, weight=BOLD).next_to(card2.get_top(), DOWN, buff=0.2)
        card2_desc = Paragraph("• Namenlose Felder\n• Indexzugriff (.0)\n• Newtype-Muster", font_size=9, color=WHITE, line_spacing=0.4).next_to(card2_title, DOWN, buff=0.2).align_to(card2, LEFT).shift(RIGHT * 0.4)
        g_card2 = VGroup(card2, card2_title, card2_desc)

        card3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([4.0, -0.4, 0])
        card3_title = Text("Unit-Like Struct", font_size=12, color=PURPLE, weight=BOLD).next_to(card3.get_top(), DOWN, buff=0.2)
        card3_desc = Paragraph("• Keine Felder (ZST)\n• Reine Typinfo (0B)\n• Marker für Traits", font_size=9, color=WHITE, line_spacing=0.4).next_to(card3_title, DOWN, buff=0.2).align_to(card3, LEFT).shift(RIGHT * 0.4)
        g_card3 = VGroup(card3, card3_title, card3_desc)

        self.play(FadeIn(g_card1, shift=UP), run_time=1.0)
        self.play(FadeIn(g_card2, shift=UP), run_time=1.0)
        self.play(FadeIn(g_card3, shift=UP), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 3.0 = 8.0 seconds
        self.wait(get_wait_time("ch27_2_definition", 8.0))
        self.play(FadeOut(g_card1), FadeOut(g_card2), FadeOut(g_card3), run_time=1.0)

        # ==========================================
        # SECTION 3: DAS PROBLEM
        # ==========================================
        self.add_sound("audio/ch27_3_problem.wav")

        title_prob = Text("27. Das Problem: Unstrukturierte Daten & Typsicherheit", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_prob), run_time=1.0)
        self.wait(1.0)

        # Graphic comparing: Loose variables vs. Tuple vs. Struct
        box1 = create_terminal_window(3.5, 3.2, "Lose Variablen").move_to([-4.0, -0.6, 0])
        b1_content = Paragraph("let width = 30;\nlet height = 50;\n\nKein erzwungener\nZusammenhang!", font_size=8, color=WHITE, line_spacing=0.4).next_to(box1[1], DOWN, buff=0.2).align_to(box1[0], LEFT).shift(RIGHT * 0.3)
        g_box1 = VGroup(box1, b1_content)

        box2 = create_terminal_window(3.5, 3.2, "Tupel (30, 50)").move_to([0.0, -0.6, 0])
        b2_content = Paragraph("let rect = (30, 50);\n\nZugriff über Indizes:\nrect.0  *  rect.1\n\nVerwechslungsgefahr!", font_size=8, color=WHITE, line_spacing=0.4).next_to(box2[1], DOWN, buff=0.2).align_to(box2[0], LEFT).shift(RIGHT * 0.3)
        g_box2 = VGroup(box2, b2_content)

        box3 = create_terminal_window(3.5, 3.2, "Struct Rectangle").move_to([4.0, -0.6, 0])
        b3_content = Paragraph("let r = Rectangle {\n    width: 30,\n    height: 50,\n};\n\nr.width * r.height", font_size=8, color=GREEN, line_spacing=0.4).next_to(box3[1], DOWN, buff=0.2).align_to(box3[0], LEFT).shift(RIGHT * 0.3)
        g_box3 = VGroup(box3, b3_content)

        self.play(FadeIn(g_box1, shift=LEFT), run_time=1.0)
        self.play(FadeIn(g_box2, shift=UP), run_time=1.0)
        self.play(FadeIn(g_box3, shift=RIGHT), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 3.0 = 8.0 seconds
        self.wait(get_wait_time("ch27_3_problem", 8.0))
        self.play(FadeOut(g_box1), FadeOut(g_box2), FadeOut(g_box3), run_time=1.0)

        # ==========================================
        # SECTION 4: NAIVER VERSUCH
        # ==========================================
        self.add_sound("audio/ch27_4_naive.wav")

        title_naive = Text("27. Der naive Versuch: Referenzen & Falsche Mutabilität", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_naive), run_time=1.0)
        self.wait(1.0)

        # Show code editor with invalid code
        editor = create_terminal_window(10.5, 4.4, "src/main.rs").move_to([0, -0.4, 0])
        code = Paragraph(
            "struct User {",
            "    username: &str, // FEHLER: Referenz ohne Lifetime!",
            "    mut email: String, // FEHLER: Partielle Mutabilität!",
            "    active: bool,",
            "}",
            "",
            "fn main() {",
            "    let user1 = User {",
            "        username: \"someusername123\",",
            "        email: String::from(\"someone@example.com\"),",
            "        active: true,",
            "    };",
            "}",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(editor[1], DOWN, buff=0.25).align_to(editor[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor), FadeIn(code), run_time=1.5)
        self.wait(2.5)

        # Highlight missing trait usage lines
        h1 = SurroundingRectangle(code[1], color=RED, stroke_width=1.5)
        h2 = SurroundingRectangle(code[2], color=RED, stroke_width=1.5)
        
        self.play(Create(h1), Create(h2), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 3.0 = 10.5 seconds
        self.wait(get_wait_time("ch27_4_naive", 10.5))
        self.play(FadeOut(editor), FadeOut(code), FadeOut(h1), FadeOut(h2), run_time=1.0)

        # ==========================================
        # SECTION 5: ANATOMIE DES FEHLERS
        # ==========================================
        self.add_sound("audio/ch27_5_anatomy.wav")

        title_anatomy = Text("27. Die Anatomie des Fehlers: Lebensdauern & Syntax", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_anatomy), run_time=1.0)
        self.wait(1.0)

        # Show terminal compiler output
        terminal = create_terminal_window(11.0, 4.4, "Terminal - cargo check").move_to([0, -0.4, 0])
        err_msg = Paragraph(
            "error[E0106]: missing lifetime specifier",
            " --> src/main.rs:2:15",
            "  |",
            "2 |     username: &str,",
            "  |               ^ expected named lifetime parameter",
            "  |",
            "error: expected identifier, found keyword `mut`",
            " --> src/main.rs:3:5",
            "  |",
            "3 |     mut email: String,",
            "  |     ^^^ expected identifier",
            font="Monospace", font_size=8.0, color=RED, line_spacing=0.4
        ).next_to(terminal[1], DOWN, buff=0.25).align_to(terminal[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(terminal), FadeIn(err_msg), run_time=1.5)
        self.wait(2.5)

        # Highlight lifetime error
        h_err = SurroundingRectangle(err_msg[0], color=YELLOW, stroke_width=1.5)
        h_mut = SurroundingRectangle(err_msg[6], color=YELLOW, stroke_width=1.5)
        self.play(Create(h_err), Create(h_mut), run_time=1.5)
        self.wait(2.5)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 2.5 = 10.0 seconds
        self.wait(get_wait_time("ch27_5_anatomy", 10.0))
        self.play(FadeOut(terminal), FadeOut(err_msg), FadeOut(h_err), FadeOut(h_mut), run_time=1.0)

        # ==========================================
        # SECTION 6: DIE LÖSUNG
        # ==========================================
        self.add_sound("audio/ch27_6_solution.wav")

        title_sol = Text("27. Die Lösung: Besitzende Typen & Instanz-Mutabilität", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sol), run_time=1.0)
        self.wait(1.0)

        # Show code editor with clean working code
        editor_sol = create_terminal_window(10.5, 4.4, "src/main.rs").move_to([0, -0.4, 0])
        code_sol = Paragraph(
            "struct User {",
            "    username: String, // String besitzt die Heap-Daten",
            "    email: String,    // String besitzt die Heap-Daten",
            "    active: bool,",
            "}",
            "",
            "fn main() {",
            "    // Gesamte Instanz wird veränderbar deklariert",
            "    let mut user1 = User {",
            "        username: String::from(\"someusername123\"),",
            "        email: String::from(\"someone@example.com\"),",
            "        active: true,",
            "    };",
            "    user1.email = String::from(\"anotheremail@example.com\");",
            "}",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(editor_sol[1], DOWN, buff=0.2).align_to(editor_sol[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor_sol), FadeIn(code_sol), run_time=1.5)
        self.wait(2.5)

        # Highlight correct ownership and mut
        h_sol1 = SurroundingRectangle(code_sol[1], color=GREEN, stroke_width=1.5)
        h_sol2 = SurroundingRectangle(code_sol[8], color=GREEN, stroke_width=1.5)
        self.play(Create(h_sol1), Create(h_sol2), run_time=1.5)
        self.wait(2.5)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 2.5 = 10.0 seconds
        self.wait(get_wait_time("ch27_6_solution", 10.0))
        self.play(FadeOut(editor_sol), FadeOut(code_sol), FadeOut(h_sol1), FadeOut(h_sol2), run_time=1.0)

        # ==========================================
        # SECTION 7: TUTORIAL
        # ==========================================
        self.add_sound("audio/ch27_7_tutorial.wav")

        title_tut = Text("27. Praxis-Tutorial: Die Rechteck-Engine", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_tut), run_time=1.0)
        self.wait(1.0)

        # Code block containing the impl block
        editor_tut = create_terminal_window(10.5, 4.4, "src/main.rs").move_to([0, -0.4, 0])
        code_tut = Paragraph(
            "struct Rectangle { width: u32, height: u32 }",
            "",
            "impl Rectangle {",
            "    // Methode (erfordert &self als ersten Parameter)",
            "    fn area(&self) -> u32 {",
            "        self.width * self.height",
            "    }",
            "",
            "    // Assoziierte Funktion (Konstruktor ohne self)",
            "    fn square(size: u32) -> Self {",
            "        Self { width: size, height: size }",
            "    }",
            "}",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(editor_tut[1], DOWN, buff=0.2).align_to(editor_tut[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor_tut), FadeIn(code_tut), run_time=1.5)
        self.wait(2.5)

        # Visual marker for area method vs. square associated function
        h_method = SurroundingRectangle(code_tut[4], color=CYAN, stroke_width=1.5)
        h_assoc = SurroundingRectangle(code_tut[9], color=PURPLE, stroke_width=1.5)
        self.play(Create(h_method), Create(h_assoc), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 3.0 = 10.5 seconds
        self.wait(get_wait_time("ch27_7_tutorial", 10.5))
        self.play(FadeOut(editor_tut), FadeOut(code_tut), FadeOut(h_method), FadeOut(h_assoc), run_time=1.0)

        # ==========================================
        # SECTION 8: DEEP DIVE
        # ==========================================
        self.add_sound("audio/ch27_8_deepdive.wav")

        title_dive = Text("27. Deep Dive: Speicherlayout & Typzustände", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_dive), run_time=1.0)
        self.wait(1.0)

        # Visualizing Speicher Alignment & Padding
        # We draw a grid representation of memory bytes
        mem_cells = VGroup()
        for i in range(8):
            cell = Square(side_length=0.7, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5)
            lbl = Text(f"Byte {i}", font_size=8, color=GRAY).next_to(cell.get_bottom(), UP, buff=0.08)
            mem_cells.add(VGroup(cell, lbl))
        mem_cells.arrange(RIGHT, buff=0.15).move_to([0, 0.4, 0])

        # Fill cell 0 with 'a' (u8)
        cell_a = mem_cells[0][0]
        cell_a.set_color(CYAN)
        a_text = Text("a\n(u8)", font_size=10, color=CYAN).move_to(cell_a.get_center())

        # Fill cell 1 with 'Padding'
        cell_pad = mem_cells[1][0]
        cell_pad.set_color(RED).set_fill(color=RED, opacity=0.15)
        pad_text = Text("Padding", font_size=7, color=RED).move_to(cell_pad.get_center())

        # Fill cell 2 and 3 with 'c' (u16)
        cell_c1 = mem_cells[2][0]
        cell_c2 = mem_cells[3][0]
        cell_c1.set_color(PURPLE)
        cell_c2.set_color(PURPLE)
        c_text = Text("c (u16)", font_size=10, color=PURPLE).move_to(VGroup(cell_c1, cell_c2).get_center())

        # Fill cell 4, 5, 6, 7 with 'b' (u32)
        cell_b = VGroup(*(mem_cells[i][0] for i in range(4, 8)))
        for c in cell_b:
            c.set_color(GREEN)
        b_text = Text("b (u32)", font_size=10, color=GREEN).move_to(cell_b.get_center())

        self.play(FadeIn(mem_cells), run_time=1.5)
        self.play(Write(a_text), Write(pad_text), Write(c_text), Write(b_text), run_time=2.0)
        self.wait(2.0)

        # Animate Type-State-Pattern transition (Draft -> Configured)
        state_flow = VGroup(
            RoundedRectangle(corner_radius=0.1, width=2.4, height=1.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-3.0, -1.8, 0]),
            Arrow(start=[-1.6, -1.8, 0], end=[1.6, -1.8, 0], color=RUST_ORANGE, stroke_width=3),
            RoundedRectangle(corner_radius=0.1, width=2.4, height=1.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([3.0, -1.8, 0])
        )
        lbl_draft = Text("Request<Draft>", font_size=9, color=WHITE).move_to(state_flow[0].get_center())
        lbl_cfg = Text("Request<Configured>", font_size=9, color=WHITE).move_to(state_flow[2].get_center())
        lbl_arrow = Text(".set_body()", font_size=8, color=RUST_ORANGE).next_to(state_flow[1], UP, buff=0.1)

        self.play(FadeIn(state_flow), Write(lbl_draft), Write(lbl_cfg), Write(lbl_arrow), run_time=2.0)
        self.wait(2.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.0 + 2.0 + 2.0 + 2.0 = 11.5 seconds
        self.wait(get_wait_time("ch27_8_deepdive", 11.5))
        self.play(
            FadeOut(mem_cells), FadeOut(a_text), FadeOut(pad_text), FadeOut(c_text), FadeOut(b_text),
            FadeOut(state_flow), FadeOut(lbl_draft), FadeOut(lbl_cfg), FadeOut(lbl_arrow),
            run_time=1.0
        )

        # ==========================================
        # SECTION 9: ÜBUNGEN
        # ==========================================
        self.add_sound("audio/ch27_9_exercises.wav")

        title_ex = Text("27. Drei praktische Übungen", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_ex), run_time=1.0)
        self.wait(1.0)

        # Three exercise cards
        card_w, card_h = 3.8, 3.8
        e_card1 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-4.2, -0.6, 0])
        e_card2 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([0, -0.6, 0])
        e_card3 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([4.2, -0.6, 0])

        ec1_title = Text("1. Buchdaten", font_size=14, color=CYAN, weight=BOLD).next_to(e_card1.get_top(), DOWN, buff=0.3)
        ec1_desc = Paragraph(
            "• Struct Book erstellen\n"
            "• Manuelles Default-Trait\n"
            "• Formatierungs-Methode\n"
            "  für Beschreibungen",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(ec1_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        ec2_title = Text("2. Bankkonto", font_size=14, color=PURPLE, weight=BOLD).next_to(e_card2.get_top(), DOWN, buff=0.3)
        ec2_desc = Paragraph(
            "• Konto mit Historie\n"
            "• Deposit & Withdraw\n"
            "• Fehlerbehandlung via\n"
            "  Result<(), String>",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(ec2_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        ec3_title = Text("3. 3D-Vektor", font_size=14, color=RUST_ORANGE, weight=BOLD).next_to(e_card3.get_top(), DOWN, buff=0.3)
        ec3_desc = Paragraph(
            "• Tuple Struct Vector3D\n"
            "• Skalar- & Kreuzprodukt\n"
            "• Manuelle impls von\n"
            "  From, PartialEq & Deref",
            font_size=10, line_spacing=0.5, color=WHITE
        ).next_to(ec3_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        self.play(FadeIn(e_card1, shift=UP), FadeIn(ec1_title), FadeIn(ec1_desc), run_time=1.0)
        self.play(FadeIn(e_card2, shift=UP), FadeIn(ec2_title), FadeIn(ec2_desc), run_time=1.0)
        self.play(FadeIn(e_card3, shift=UP), FadeIn(ec3_title), FadeIn(ec3_desc), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 3.0 = 8.0 seconds
        self.wait(get_wait_time("ch27_9_exercises", 8.0))
        self.play(
            FadeOut(e_card1), FadeOut(ec1_title), FadeOut(ec1_desc),
            FadeOut(e_card2), FadeOut(ec2_title), FadeOut(ec2_desc),
            FadeOut(e_card3), FadeOut(ec3_title), FadeOut(ec3_desc),
            run_time=1.0
        )

        # ==========================================
        # SECTION 10: LERNSTRATEGIE
        # ==========================================
        self.add_sound("audio/ch27_10_learning.wav")

        title_learn = Text("27. Lernstrategie: Fehler provozieren", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_learn), run_time=1.0)
        self.wait(1.0)

        # Draw a big chalkboard-like card
        learn_card = RoundedRectangle(corner_radius=0.15, width=10.0, height=4.2, color=RUST_ORANGE, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([0, -0.5, 0])
        lc_title = Text("Compiler-Guided Learning", font_size=15, color=RUST_ORANGE, weight=BOLD).next_to(learn_card.get_top(), DOWN, buff=0.3)
        
        bullets_learn = VGroup(
            Text("1. Schreiben Sie funktionierenden Code.", font_size=13, color=WHITE),
            Text("2. Provozieren Sie mutwillig Fehler (z.B. unmutables Ändern).", font_size=13, color=WHITE),
            Text("3. Studieren Sie die präzisen Compiler-Ausgaben laut.", font_size=13, color=WHITE),
            Text("4. Verinnerlichen Sie das Fehlermuster für die Praxis.", font_size=13, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(lc_title, DOWN, buff=0.4).shift(LEFT * 1.5)

        self.play(FadeIn(learn_card), FadeIn(lc_title), run_time=1.0)
        self.play(LaggedStart(*(FadeIn(b, shift=RIGHT) for b in bullets_learn), lag_ratio=0.3), run_time=2.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 2.0 + 3.0 = 8.0 seconds
        self.wait(get_wait_time("ch27_10_learning", 8.0))
        self.play(FadeOut(learn_card), FadeOut(lc_title), FadeOut(bullets_learn), run_time=1.0)

        # ==========================================
        # SECTION 11: OUTRO
        # ==========================================
        self.add_sound("audio/ch27_11_outro.wav")

        title_outro = Text("Zusammenfassung & Ausblick", font_size=20, color=RUST_ORANGE, weight=BOLD).move_to([0, 1.5, 0])
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        summary_points = VGroup(
            Text("✔ Structs kapseln zusammengehörige Daten sicher", font_size=14, color=WHITE),
            Text("✔ impl-Blöcke binden Methoden und Konstruktoren", font_size=14, color=WHITE),
            Text("✔ Zero-Cost durch Monomorphisierung und Inlining", font_size=14, color=WHITE),
            Text("✔ GitHub-Code: Start- und End-Branch verfügbar", font_size=14, color=CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, -0.4, 0])

        self.play(LaggedStart(*(FadeIn(pt, shift=UP) for pt in summary_points), lag_ratio=0.3), run_time=2.0)
        self.wait(3.0)

        # Let's show a nice pulsing final note
        repo_note = Text("github.com/thorstenkloehn/RustKurs", font_size=12, color=RUST_ORANGE).next_to(summary_points, DOWN, buff=0.6)
        self.play(Write(repo_note), run_time=1.0)
        self.wait(2.0)

        # Total anim time: 1.0 + 1.0 + 2.0 + 3.0 + 1.0 + 2.0 = 10.0 seconds
        self.wait(get_wait_time("ch27_11_outro", 10.0))
        self.play(FadeOut(title_group), FadeOut(summary_points), FadeOut(repo_note), run_time=1.0)
