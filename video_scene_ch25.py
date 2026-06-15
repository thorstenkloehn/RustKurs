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

class RustSlicesVideo(Scene):
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
            "ch25_1_intro": 35.0,
            "ch25_2_definition": 35.0,
            "ch25_3_problem": 35.0,
            "ch25_4_naive": 35.0,
            "ch25_5_anatomy": 35.0,
            "ch25_6_solution": 35.0,
            "ch25_7_tutorial": 35.0,
            "ch25_8_outro": 35.0
        }
        
        durations_path = "audio/durations_ch25.json"
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
        # SECTION 1: INTRO
        # ==========================================
        self.add_sound("audio/ch25_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 25: Der Slice-Typ (Slices)", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 25: Der Slice-Typ (Slices)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Intro bullet points
        bullets = VGroup(
            Text("• Sicherer, allokationsfreier Speicherzugriff", font_size=16, color=WHITE),
            Text("• Referenzierung von Teilausschnitten (Sub-sequences)", font_size=16, color=WHITE),
            Text("• Ohne Speicherbesitz (keine Ownership-Übernahme)", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, -0.6, 0])

        self.play(LaggedStart(*(FadeIn(b, shift=RIGHT) for b in bullets), lag_ratio=0.3), run_time=2.0)
        self.wait(2.0)

        # Total anim time: 1.5 + 2.5 + 1.5 + 1.0 + 2.0 + 2.0 = 10.5 seconds
        self.wait(get_wait_time("ch25_1_intro", 10.5))
        self.play(FadeOut(bullets), run_time=1.0)

        # ==========================================
        # SECTION 2: DEFINITION & SPEICHERLAYOUT (FAT POINTER)
        # ==========================================
        self.add_sound("audio/ch25_2_definition.wav")

        title_def = Text("25. Definition & Speicherlayout (Fat Pointer)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_def), run_time=1.0)
        self.wait(1.0)

        # Draw Stack & Heap representation
        stack_lbl = Text("STACK (16 Bytes)", font_size=11, color=CYAN, weight=BOLD).move_to([-4.0, 1.2, 0])
        heap_lbl = Text("HEAP ( hello world )", font_size=11, color=PURPLE, weight=BOLD).move_to([2.5, 1.2, 0])
        
        # Stack representation of Slice (Fat Pointer)
        fat_pointer_box = RoundedRectangle(corner_radius=0.1, width=4.0, height=1.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.2, 0])
        fat_ptr_lbl = Text("Slice: &str (Fat Pointer)", font_size=10, color=CYAN).next_to(fat_pointer_box.get_top(), DOWN, buff=0.2)
        ptr_val = Paragraph("ptr: 0x10A6 (Adresse)\nlen: 5      (Länge)", font_size=9, color=WHITE, font="Monospace").next_to(fat_ptr_lbl, DOWN, buff=0.15)
        fat_ptr_group = VGroup(fat_pointer_box, fat_ptr_lbl, ptr_val)

        # Heap memory cells for "hello world"
        heap_cells = VGroup()
        chars = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
        for i, char in enumerate(chars):
            cell_box = Square(side_length=0.45, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.8, stroke_width=1.5)
            cell_lbl = Text(char, font_size=14, color=WHITE, font="Monospace").move_to(cell_box.get_center())
            cell = VGroup(cell_box, cell_lbl).move_to([0.25 + i * 0.46, -0.2, 0])
            heap_cells.add(cell)

        # Draw Arrow from Stack ptr to Heap cell 6 (w)
        arrow = Arrow(
            start=fat_pointer_box.get_right() + UP*0.1,
            end=heap_cells[6].get_bottom() + DOWN*0.1,
            color=RUST_ORANGE,
            stroke_width=2.5,
            max_stroke_width_to_length_ratio=6
        )
        arrow_lbl = Text("zeigt auf 'w'", font_size=8, color=RUST_ORANGE).next_to(arrow, UP, buff=0.1).shift(LEFT * 0.4)

        # Bracket showing length = 5
        bracket = Brace(heap_cells[6:11], direction=UP, color=GREEN)
        bracket_lbl = Text("len = 5 (world)", font_size=9, color=GREEN).next_to(bracket, UP, buff=0.15)

        self.play(FadeIn(stack_lbl), FadeIn(heap_lbl), FadeIn(fat_ptr_group), run_time=1.5)
        self.play(LaggedStart(*(FadeIn(c, shift=UP) for c in heap_cells), lag_ratio=0.1), run_time=1.5)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=1.0)
        self.play(FadeIn(bracket), FadeIn(bracket_lbl), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 1.5 + 1.0 + 1.0 + 3.0 = 10.0 seconds
        self.wait(get_wait_time("ch25_2_definition", 10.0))
        self.play(FadeOut(stack_lbl), FadeOut(heap_lbl), FadeOut(fat_ptr_group), FadeOut(heap_cells), FadeOut(arrow), FadeOut(arrow_lbl), FadeOut(bracket), FadeOut(bracket_lbl), run_time=1.0)

        # ==========================================
        # SECTION 3: PROBLEM (OUT-OF-SYNC)
        # ==========================================
        self.add_sound("audio/ch25_3_problem.wav")

        title_prob = Text("25. Das Problem: Out-of-Sync-Indizes", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_prob), run_time=1.0)
        self.wait(1.0)

        # Visual illustration of Out-of-Sync Index
        list_lbl = Text("String im Speicher (Datenquelle):", font_size=11, color=WHITE).move_to([-2.0, 1.2, 0])
        string_box = RoundedRectangle(corner_radius=0.1, width=6.0, height=0.8, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-2.0, 0.4, 0])
        string_val = Text('"hello world"', font_size=14, color=WHITE, font="Monospace").move_to(string_box.get_center())
        string_group = VGroup(string_box, string_val)

        idx_lbl = Text("Index-Variable (Stack):", font_size=11, color=WHITE).move_to([3.0, 1.2, 0])
        idx_box = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.8, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.0, 0.4, 0])
        idx_val = Text("word_end = 5", font_size=12, color=YELLOW, font="Monospace").move_to(idx_box.get_center())
        idx_group = VGroup(idx_box, idx_val)

        self.play(FadeIn(list_lbl), FadeIn(string_group), FadeIn(idx_lbl), FadeIn(idx_group), run_time=1.5)
        self.wait(2.0)

        # Mutate the source: string is cleared!
        cleared_val = Text('""', font_size=14, color=RED, font="Monospace").move_to(string_box.get_center())
        mutate_lbl = Text("s.clear()", font_size=12, color=RED, weight=BOLD).next_to(string_box, DOWN, buff=0.2)
        
        self.play(
            Transform(string_val, cleared_val),
            string_box.animate.set_color(RED),
            FadeIn(mutate_lbl, shift=DOWN),
            run_time=1.5
        )
        self.wait(1.5)

        # Danger indicator
        danger_box = RoundedRectangle(corner_radius=0.15, width=9.0, height=1.2, color=RED, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.8, 0])
        danger_text = Paragraph(
            "Gefahr: word_end verweist immer noch auf Index 5!\nEin Zugriff führt zum Absturz (Panic) oder undefiniertem Verhalten.",
            font_size=9, color=RED, alignment="center"
        ).move_to(danger_box.get_center())
        danger_group = VGroup(danger_box, danger_text)

        self.play(FadeIn(danger_group, shift=UP), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.0 + 1.5 + 1.5 + 1.5 + 3.0 = 13.0 seconds
        self.wait(get_wait_time("ch25_3_problem", 13.0))
        self.play(FadeOut(list_lbl), FadeOut(string_group), FadeOut(idx_lbl), FadeOut(idx_group), FadeOut(mutate_lbl), FadeOut(danger_group), run_time=1.0)

        # ==========================================
        # SECTION 4: DER NAIVE VERSUCH (CODE)
        # ==========================================
        self.add_sound("audio/ch25_4_naive.wav")

        title_naive = Text("25. Der naive Versuch (Ohne Slices)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_naive), run_time=1.0)
        self.wait(1.0)

        # Show code editor
        editor = create_terminal_window(10.5, 4.4, "src/main.rs").move_to([0, -0.4, 0])
        code = Paragraph(
            "fn first_word(s: &String) -> usize {",
            "    let bytes = s.as_bytes();",
            "    for (i, &item) in bytes.iter().enumerate() {",
            "        if item == b' ' { return i; }",
            "    }",
            "    s.len()",
            "}",
            "",
            "fn main() {",
            "    let mut s = String::from(\"hello world\");",
            "    let word_end = first_word(&s); // = 5",
            "    s.clear(); // String geleert (Länge = 0)",
            "    let first = &s[0..word_end]; // 💥 LAUFZEIT-PANIK!",
            "}",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(editor[1], DOWN, buff=0.25).align_to(editor[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor), FadeIn(code), run_time=1.5)
        self.wait(3.0)

        # Highlight issue lines
        h1 = SurroundingRectangle(code[11], color=RED, stroke_width=1.5)
        h2 = SurroundingRectangle(code[12], color=RED, stroke_width=1.5)
        self.play(Create(h1), Create(h2), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 3.0 + 1.5 + 3.0 = 11.0 seconds
        self.wait(get_wait_time("ch25_4_naive", 11.0))
        self.play(FadeOut(editor), FadeOut(code), FadeOut(h1), FadeOut(h2), run_time=1.0)

        # ==========================================
        # SECTION 5: ANATOMIE DES FEHLERS
        # ==========================================
        self.add_sound("audio/ch25_5_anatomy.wav")

        title_anatomy = Text("25. Die Anatomie des Fehlers (Laufzeit)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_anatomy), run_time=1.0)
        self.wait(1.0)

        # Visualizing memory before and after clear
        title_before = Text("Vor s.clear():", font_size=12, color=GREEN, weight=BOLD).move_to([-3.0, 1.2, 0])
        state_before = Paragraph(
            "s.len()   = 11\n"
            "s.cap()   = 11\n"
            "word_end  = 5",
            font="Monospace", font_size=11, color=WHITE, line_spacing=0.5
        ).next_to(title_before, DOWN, buff=0.3)
        g_before = VGroup(title_before, state_before)

        title_after = Text("Nach s.clear():", font_size=12, color=RED, weight=BOLD).move_to([3.0, 1.2, 0])
        state_after = Paragraph(
            "s.len()   = 0  (verändert!)\n"
            "s.cap()   = 11\n"
            "word_end  = 5  (unverändert!)",
            font="Monospace", font_size=11, color=WHITE, line_spacing=0.5
        ).next_to(title_after, DOWN, buff=0.3)
        g_after = VGroup(title_after, state_after)

        self.play(FadeIn(g_before, shift=LEFT), run_time=1.5)
        self.wait(2.0)
        self.play(FadeIn(g_after, shift=RIGHT), run_time=1.5)
        self.wait(2.0)

        # Show the panic output box
        console = create_terminal_window(10.5, 1.8, "Terminal - Laufzeitabsturz").move_to([0, -1.8, 0])
        panic_text = Paragraph(
            "thread 'main' panicked at src/main.rs:13:19:\n"
            "byte index 5 is out of bounds of ``",
            font="Monospace", font_size=9, color=RED, line_spacing=0.5
        ).next_to(console[1], DOWN, buff=0.25).align_to(console[0], LEFT).shift(RIGHT * 0.6)
        console_group = VGroup(console, panic_text)

        self.play(FadeIn(console_group, shift=UP), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.0 + 1.5 + 2.0 + 1.5 + 3.0 = 13.5 seconds
        self.wait(get_wait_time("ch25_5_anatomy", 13.5))
        self.play(FadeOut(g_before), FadeOut(g_after), FadeOut(console_group), run_time=1.0)

        # ==========================================
        # SECTION 6: DIE LÖSUNG (BORROW CHECKER)
        # ==========================================
        self.add_sound("audio/ch25_6_solution.wav")

        title_sol = Text("25. Die Lösung: String-Slices & Borrow Checker", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sol), run_time=1.0)
        self.wait(1.0)

        # Show corrected code editor
        editor_sol = create_terminal_window(10.5, 3.4, "src/main.rs").move_to([0, 0.4, 0])
        code_sol = Paragraph(
            "fn first_word(s: &str) -> &str { // Rückgabetyp: &str",
            "    let bytes = s.as_bytes();",
            "    for (i, &item) in bytes.iter().enumerate() {",
            "        if item == b' ' { return &s[0..i]; }",
            "    }",
            "    &s[..]",
            "}",
            "",
            "fn main() {",
            "    let mut s = String::from(\"hello world\");",
            "    let word = first_word(&s); // 🟢 Unveränderliche Ausleihe",
            "    s.clear(); // 🛑 FEHLER: s ist durch 'word' blockiert!",
            "    println!(\"{}\", word); // Letzte Nutzung von 'word'",
            "}",
            font="Monospace", font_size=7.5, color=WHITE, line_spacing=0.4
        ).next_to(editor_sol[1], DOWN, buff=0.25).align_to(editor_sol[0], LEFT).shift(RIGHT * 0.6)
        
        self.play(FadeIn(editor_sol), FadeIn(code_sol), run_time=1.5)
        self.wait(2.5)

        # Show compiler error output below
        compiler_out = create_terminal_window(10.5, 2.0, "Compiler Error Output").move_to([0, -2.2, 0])
        err_msg = Paragraph(
            "error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable\n"
            "  --> src/main.rs:12:5\n"
            "11 |     let word = first_word(&s); // immutable borrow occurs here\n"
            "12 |     s.clear(); // mutable borrow occurs here",
            font="Monospace", font_size=8, color=RED, line_spacing=0.4
        ).next_to(compiler_out[1], DOWN, buff=0.2).align_to(compiler_out[0], LEFT).shift(RIGHT * 0.6)
        comp_group = VGroup(compiler_out, err_msg)

        h_err = SurroundingRectangle(code_sol[11], color=RED, stroke_width=1.5)
        self.play(FadeIn(comp_group, shift=UP), Create(h_err), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 3.0 = 10.5 seconds
        self.wait(get_wait_time("ch25_6_solution", 10.5))
        self.play(FadeOut(editor_sol), FadeOut(code_sol), FadeOut(comp_group), FadeOut(h_err), run_time=1.0)

        # ==========================================
        # SECTION 7: LOG-PARSER TUTORIAL
        # ==========================================
        self.add_sound("audio/ch25_7_tutorial.wav")

        title_tut = Text("25. Praxistutorial: Log-Parser", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_tut), run_time=1.0)
        self.wait(1.0)

        # Log parsing code example
        editor_tut = create_terminal_window(11.0, 3.4, "src/log_parser.rs").move_to([0, 0.4, 0])
        code_tut = Paragraph(
            "fn parse_log_line(line: &str) -> Option<(&str, &str)> {",
            "    if !line.starts_with('[') { return None; }",
            "    let end_bracket = line.find(']')?;",
            "    let log_level = &line[1..end_bracket]; // Slice 1",
            "    let msg_start = end_bracket + 2;",
            "    if msg_start > line.len() { return None; }",
            "    let message = &line[msg_start..];      // Slice 2",
            "    Some((log_level, message))",
            "}",
            font="Monospace", font_size=8.5, color=WHITE, line_spacing=0.45
        ).next_to(editor_tut[1], DOWN, buff=0.25).align_to(editor_tut[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor_tut), FadeIn(code_tut), run_time=1.5)
        self.wait(2.5)

        # Log String parsing visualization
        log_string_lbl = Text("Eingabe-String:", font_size=10, color=GRAY).move_to([-3.5, -1.8, 0])
        log_entry_box = RoundedRectangle(corner_radius=0.1, width=7.0, height=0.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([1.5, -1.8, 0])
        
        # Display the parts of the log line
        p1 = Text("[", font_size=11, color=GRAY, font="Monospace")
        p2 = Text("WARNUNG", font_size=11, color=YELLOW, font="Monospace", weight=BOLD)
        p3 = Text("] ", font_size=11, color=GRAY, font="Monospace")
        p4 = Text("Verbindung neu aufgebaut", font_size=11, color=WHITE, font="Monospace")
        log_parts = VGroup(p1, p2, p3, p4).arrange(RIGHT, buff=0.05).move_to(log_entry_box.get_center())

        self.play(FadeIn(log_string_lbl), FadeIn(log_entry_box), FadeIn(log_parts), run_time=1.5)
        self.wait(1.5)

        # Highlight extracted slices
        br1 = Brace(p2, direction=DOWN, color=YELLOW)
        br1_lbl = Text("level", font_size=8, color=YELLOW).next_to(br1, DOWN, buff=0.1)

        br2 = Brace(p4, direction=DOWN, color=CYAN)
        br2_lbl = Text("message", font_size=8, color=CYAN).next_to(br2, DOWN, buff=0.1)

        self.play(Create(br1), FadeIn(br1_lbl), Create(br2), FadeIn(br2_lbl), run_time=1.5)
        self.wait(2.5)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 1.5 + 1.5 + 2.5 = 13.0 seconds
        self.wait(get_wait_time("ch25_7_tutorial", 13.0))
        self.play(
            FadeOut(editor_tut), FadeOut(code_tut), 
            FadeOut(log_string_lbl), FadeOut(log_entry_box), FadeOut(log_parts),
            FadeOut(br1), FadeOut(br1_lbl), FadeOut(br2), FadeOut(br2_lbl),
            run_time=1.0
        )

        # ==========================================
        # SECTION 8: OUTRO
        # ==========================================
        self.add_sound("audio/ch25_8_outro.wav")

        title_outro = Text("Zusammenfassung & Outro", font_size=24, color=RUST_ORANGE, weight=BOLD).move_to([0, 1.2, 0])
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Key Takeaways
        takeaways = VGroup(
            Text("1. Zero-Cost Abstraction", font_size=14, color=CYAN, weight=BOLD),
            Text("   Slices benötigen keinen Heap-Speicher und kopieren keine Daten.", font_size=11, color=WHITE),
            Text("2. Kompilierzeit-Sicherheit", font_size=14, color=PURPLE, weight=BOLD),
            Text("   Der Borrow Checker verbietet Mutationen der Datenquelle während der Nutzung.", font_size=11, color=WHITE),
            Text("3. Flexible API-Parameters", font_size=14, color=GREEN, weight=BOLD),
            Text("   Dank Deref Coercion akzeptiert &str sowohl Literale als auch &String-Referenzen.", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, -1.0, 0])

        self.play(LaggedStart(*(FadeIn(t, shift=RIGHT) for t in takeaways), lag_ratio=0.25), run_time=2.5)
        self.wait(5.0)

        # Total anim time: 1.0 + 1.0 + 2.5 + 5.0 = 9.5 seconds
        self.wait(get_wait_time("ch25_8_outro", 9.5))

        # Final fade out
        self.play(FadeOut(title_group), FadeOut(takeaways), run_time=1.5)
        self.wait(1.0)
