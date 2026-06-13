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

class RustOwnershipDetailedVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Continuous watermark footer
        watermark = Text(
            "Auszüge aus 'The Rust Programming Language' (MIT/Apache 2.0) | Autoren: Steve Klabnik, Carol Nichols & Rust-Community",
            font_size=8.5,
            color=GRAY,
            fill_opacity=0.65
        ).to_edge(DOWN, buff=0.15)
        self.add(watermark)

        # Load durations if they exist, otherwise use sensible defaults
        durations = {
            "ch18_1_intro": 35.0,
            "ch18_2_stack_heap": 35.0,
            "ch18_3_rules_scopes": 35.0,
            "ch18_4_move_copy": 35.0,
            "ch18_5_clone_structs": 35.0,
            "ch18_6_errors_outro": 35.0
        }
        
        durations_path = "audio/durations_ch18.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # ==========================================
        # SECTION 1: INTRO (3 Speicherverwaltungen)
        # ==========================================
        self.add_sound("audio/ch18_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 18: Das Ownership-System im Detail", font_size=24, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)

        # Move Title to Top
        title_small = Text("Kapitel 18: Das Ownership-System im Detail", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        # Three Approaches diagram
        c_width = 3.6
        c_height = 3.0
        
        c1_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.1, 0.2, 0])
        c1_title = Text("Manuell (C/C++)", font_size=12, color=RED, weight=BOLD).next_to(c1_rect.get_top(), DOWN, buff=0.2)
        c1_desc = VGroup(
            Text("• malloc() / free()", font_size=9, color=WHITE),
            Text("• Sehr schnell", font_size=9, color=WHITE),
            Text("• Fehleranfällig:", font_size=9, color=RED),
            Text("  Memory Leaks &", font_size=9, color=RED),
            Text("  Double Frees", font_size=9, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c1_title, DOWN, buff=0.25)
        c1_group = VGroup(c1_rect, c1_title, c1_desc)

        c2_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 0.2, 0])
        c2_title = Text("Garbage Collector", font_size=12, color=YELLOW, weight=BOLD).next_to(c2_rect.get_top(), DOWN, buff=0.2)
        c2_desc = VGroup(
            Text("• Automatisches GC (Java/Go)", font_size=9, color=WHITE),
            Text("• Sicher & Bequem", font_size=9, color=WHITE),
            Text("• Nachteile:", font_size=9, color=YELLOW),
            Text("  Kostet CPU & RAM,", font_size=9, color=YELLOW),
            Text("  unvorhersehbare Pausen", font_size=9, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c2_title, DOWN, buff=0.25)
        c2_group = VGroup(c2_rect, c2_title, c2_desc)

        c3_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([4.1, 0.2, 0])
        c3_title = Text("Ownership (Rust)", font_size=12, color=GREEN, weight=BOLD).next_to(c3_rect.get_top(), DOWN, buff=0.2)
        c3_desc = VGroup(
            Text("• Statische Compiler-Prüfung", font_size=9, color=WHITE),
            Text("• Keine Runtime-Kosten (Zero-Cost)", font_size=9, color=WHITE),
            Text("• Sicherheit von Java", font_size=9, color=GREEN),
            Text("• Performance von C", font_size=9, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c3_title, DOWN, buff=0.25)
        c3_group = VGroup(c3_rect, c3_title, c3_desc)

        self.play(
            FadeIn(c1_group, shift=UP),
            FadeIn(c2_group, shift=UP),
            FadeIn(c3_group, shift=UP),
            run_time=2.0
        )
        self.wait(10.0)

        # Transition text
        trans_txt = Text("Rust verlagert die Speicherverwaltung komplett in die Kompilierzeit.", font_size=13, color=CYAN).move_to([0, -1.8, 0])
        self.play(FadeIn(trans_txt, shift=UP), run_time=1.5)
        self.wait(8.0)

        # Wait for the audio segment to complete
        remaining_time = durations["ch18_1_intro"] - 1.0 - 2.0 - 1.5 - 0.5 - 2.0 - 10.0 - 1.5 - 8.0
        self.wait(max(1.0, remaining_time))
        
        self.play(
            FadeOut(c1_group),
            FadeOut(c2_group),
            FadeOut(c3_group),
            FadeOut(trans_txt),
            run_time=1.0
        )

        # ==========================================
        # SECTION 2: STACK VS HEAP
        # ==========================================
        self.add_sound("audio/ch18_2_stack_heap.wav")

        title_sh = Text("18. Anatomie des Speichers: Stack vs. Heap", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sh), run_time=1.0)
        self.wait(1.0)

        # Left: Stack
        stack_title = Text("Stack (Stapel)", font_size=14, color=CYAN, weight=BOLD).move_to([-3.5, 2.0, 0])
        st1 = Rectangle(width=3.2, height=0.45, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-3.5, -1.2, 0])
        st1_lbl = Text("i32: 100 (Fest)", font_size=9, color=WHITE).move_to(st1.get_center())
        st2 = Rectangle(width=3.2, height=0.45, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).next_to(st1, UP, buff=0.1)
        st2_lbl = Text("f64: 3.14 (Fest)", font_size=9, color=WHITE).move_to(st2.get_center())
        st3 = Rectangle(width=3.2, height=0.45, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).next_to(st2, UP, buff=0.1)
        st3_lbl = Text("Pointer: 0x55aa (Zeiger)", font_size=9, color=CYAN).move_to(st3.get_center())
        
        stack_box_group = VGroup(st1, st1_lbl, st2, st2_lbl, st3, st3_lbl)
        stack_desc = VGroup(
            Text("• Last In, First Out (LIFO)", font_size=10, color=WHITE),
            Text("• Nur feste Größen", font_size=10, color=WHITE),
            Text("• Schneller Stack-Pointer", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(stack_box_group, UP, buff=0.3)
        stack_group = VGroup(stack_title, stack_box_group, stack_desc)

        # Right: Heap
        heap_title = Text("Heap (Haufen)", font_size=14, color=YELLOW, weight=BOLD).move_to([3.5, 2.0, 0])
        heap_rect = RoundedRectangle(corner_radius=0.15, width=4.5, height=2.5, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.5, -0.4, 0])
        heap_content = Text("Dynamische Daten\n(z.B. String \"Rust\")\nAdresse: 0x55aa", font_size=10, color=WHITE).move_to(heap_rect.get_center())
        heap_desc = VGroup(
            Text("• Dynamische Allokation", font_size=10, color=WHITE),
            Text("• Pointer auf Stack zeigt hin", font_size=10, color=WHITE),
            Text("• Latenz durch Indirektion", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(heap_rect, UP, buff=0.3)
        heap_group = VGroup(heap_title, heap_rect, heap_content, heap_desc)

        ptr_arrow = Arrow(start=[-1.8, 0.1, 0], end=[1.2, -0.4, 0], stroke_width=3, color=CYAN)

        self.play(
            FadeIn(stack_group, shift=RIGHT),
            FadeIn(heap_group, shift=LEFT),
            run_time=2.0
        )
        self.play(Create(ptr_arrow), run_time=1.0)
        self.wait(10.0)

        # Cache Locality Info Box
        info_box = RoundedRectangle(corner_radius=0.1, width=11.0, height=0.9, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, -2.4, 0])
        info_text = Text("Cache-Lokalität: Stack liegt dicht beisammen (schnell), Heap liegt verstreut (Cache-Misses).", font_size=9, color=CYAN).move_to(info_box.get_center())
        info_group = VGroup(info_box, info_text)

        self.play(FadeIn(info_group, shift=UP), run_time=1.5)
        self.wait(10.0)

        remaining_time = durations["ch18_2_stack_heap"] - 1.0 - 1.0 - 2.0 - 1.0 - 10.0 - 1.5 - 10.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(stack_group),
            FadeOut(heap_group),
            FadeOut(ptr_arrow),
            FadeOut(info_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: RULES & SCOPES
        # ==========================================
        self.add_sound("audio/ch18_3_rules_scopes.wav")

        title_rules = Text("18. Die 3 Ownership-Regeln & Scopes (RAII)", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_rules), run_time=1.0)
        self.wait(1.0)

        # Show the rules
        rules_v = VGroup(
            Text("1. Jeder Wert in Rust hat einen Besitzer (Owner).", font_size=12, color=WHITE, weight=BOLD),
            Text("2. Es kann immer nur einen Besitzer gleichzeitig geben.", font_size=12, color=CYAN, weight=BOLD),
            Text("3. Verlässt der Besitzer den Scope, wird der Wert gelöscht (drop).", font_size=12, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, 1.2, 0])

        self.play(FadeIn(rules_v, shift=UP), run_time=2.0)
        self.wait(6.0)

        # Code block demonstrating scope drop
        code_scope_bg = RoundedRectangle(corner_radius=0.1, width=8.0, height=2.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, -1.4, 0])
        code_scope_text = Paragraph(
            "fn main() {",
            "    {",
            "        let s = String::from(\"Rust\"); // s wird erzeugt",
            "    } // ◄── Scope-Ende! drop(s) wird automatisch aufgerufen",
            "}",
            font="Monospace", font_size=10, line_spacing=0.4
        ).move_to(code_scope_bg.get_center())
        code_scope_group = VGroup(code_scope_bg, code_scope_text)

        self.play(FadeIn(code_scope_group, scale=0.9), run_time=1.5)
        self.wait(5.0)

        # Highlight drop
        drop_ring = SurroundingRectangle(code_scope_text[3], color=RED, buff=0.08, stroke_width=2)
        drop_call_text = Text("RAII-Prinzip: Automatisches drop() gibt Heap-Speicher deterministisch frei.", font_size=10, color=RED, weight=BOLD).next_to(code_scope_bg, UP, buff=0.1)
        self.play(Create(drop_ring), FadeIn(drop_call_text, shift=DOWN), run_time=1.0)
        self.wait(10.0)

        remaining_time = durations["ch18_3_rules_scopes"] - 1.0 - 1.0 - 2.0 - 6.0 - 1.5 - 5.0 - 1.0 - 10.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(rules_v),
            FadeOut(code_scope_group),
            FadeOut(drop_ring),
            FadeOut(drop_call_text),
            run_time=1.0
        )

        # ==========================================
        # SECTION 4: MOVE VS COPY
        # ==========================================
        self.add_sound("audio/ch18_4_move_copy.wav")

        title_move = Text("18. Move-Semantik vs. Copy-Trait", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_move), run_time=1.0)
        self.wait(1.0)

        # Split screen: Left (Move), Right (Copy)
        # Left: Move
        move_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.8, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        move_title = Text("Move (Heap-Daten)", font_size=12, color=CYAN, weight=BOLD).next_to(move_box.get_top(), DOWN, buff=0.2)
        move_code = Paragraph(
            "let s1 = String::from(\"Hi\");",
            "let s2 = s1;",
            "// s1 ist ab hier UNGÜLTIG!",
            font="Monospace", font_size=10, line_spacing=0.45
        ).next_to(move_title, DOWN, buff=0.3).align_to(move_box, LEFT).shift(RIGHT * 0.4)
        
        move_vis = VGroup(
            Text("s1 (Stack) ──┐", font_size=9, color=GRAY),
            Text("            ├─► Heap: \"Hi\" (0x12a)", font_size=9, color=YELLOW),
            Text("s2 (Stack) ──┘", font_size=9, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(move_code, DOWN, buff=0.3)
        move_group = VGroup(move_box, move_title, move_code, move_vis)

        # Right: Copy
        copy_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.8, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.2, -0.6, 0])
        copy_title = Text("Copy (Stack-Daten)", font_size=12, color=GREEN, weight=BOLD).next_to(copy_box.get_top(), DOWN, buff=0.2)
        copy_code = Paragraph(
            "let x = 42; // i32",
            "let y = x;",
            "// Beide bleiben gültig!",
            font="Monospace", font_size=10, line_spacing=0.45
        ).next_to(copy_title, DOWN, buff=0.3).align_to(copy_box, LEFT).shift(RIGHT * 0.4)
        
        copy_vis = VGroup(
            Text("x = 42 (Stack)", font_size=9, color=GREEN),
            Text("y = 42 (Stack)", font_size=9, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(copy_code, DOWN, buff=0.5)
        copy_group = VGroup(copy_box, copy_title, copy_code, copy_vis)

        self.play(
            FadeIn(move_group, shift=RIGHT),
            FadeIn(copy_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Cross out s1 in move diagram
        s1_cross = Cross(move_vis[0], stroke_color=RED, stroke_width=3, scale_factor=0.95)
        self.play(Create(s1_cross), run_time=1.0)
        self.wait(12.0)

        remaining_time = durations["ch18_4_move_copy"] - 1.0 - 1.0 - 2.0 - 10.0 - 1.0 - 12.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(move_group),
            FadeOut(copy_group),
            FadeOut(s1_cross),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: CLONE & STRUCT OWNERSHIP
        # ==========================================
        self.add_sound("audio/ch18_5_clone_structs.wav")

        title_clone = Text("18. .clone() & Struct-Ownership", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_clone), run_time=1.0)
        self.wait(1.0)

        # Left: clone vs struct code
        code_cl_bg = RoundedRectangle(corner_radius=0.1, width=5.6, height=4.0, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        code_cl_text = Paragraph(
            "let s2 = s1.clone(); // Kopie!",
            "",
            "struct Server {",
            "    name: String,",
            "}",
            "",
            "let s = Server {",
            "    name: String::from(\"A\"),",
            "};",
            "let n = s.name; // Partial Move!",
            font="Monospace", font_size=9, line_spacing=0.4
        ).move_to(code_cl_bg.get_center())
        code_cl_group = VGroup(code_cl_bg, code_cl_text)

        # Right: Struct visualization card
        struct_card = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.3, -0.6, 0])
        struct_title = Text("Partial Move (Teil-Besitzwechsel)", font_size=12, color=PURPLE, weight=BOLD).next_to(struct_card.get_top(), DOWN, buff=0.2)
        
        s_rect = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([1.8, -0.8, 0])
        s_lbl = Text("Struktur 's'", font_size=10, color=CYAN, weight=BOLD).next_to(s_rect.get_top(), DOWN, buff=0.15)
        s_field_lbl = Text("name: [MOVED]", font_size=9, color=RED).next_to(s_lbl, DOWN, buff=0.2)
        s_group = VGroup(s_rect, s_lbl, s_field_lbl)

        n_rect = RoundedRectangle(corner_radius=0.08, width=2.0, height=0.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([4.8, -0.8, 0])
        n_lbl = Text("Variable 'n'", font_size=10, color=GREEN, weight=BOLD).next_to(n_rect.get_top(), DOWN, buff=0.1)
        n_val = Text("\"A\" (Heap)", font_size=9, color=YELLOW).next_to(n_lbl, DOWN, buff=0.08)
        n_group = VGroup(n_rect, n_lbl, n_val)

        p_arrow = Arrow(start=[2.3, -0.8, 0], end=[3.8, -0.8, 0], stroke_width=2.5, color=RED)
        struct_vis_group = VGroup(struct_card, struct_title, s_group, n_group, p_arrow)

        self.play(
            FadeIn(code_cl_group, shift=RIGHT),
            FadeIn(struct_vis_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(8.0)

        # Cross out s because of partial move
        s_cross = Cross(s_rect, stroke_color=RED, stroke_width=4, scale_factor=0.9)
        invalid_struct_lbl = Text("s ist unvollständig!", font_size=9, color=RED, weight=BOLD).next_to(s_rect, UP, buff=0.1)
        self.play(Create(s_cross), FadeIn(invalid_struct_lbl, shift=DOWN), run_time=1.0)
        self.wait(12.0)

        remaining_time = durations["ch18_5_clone_structs"] - 1.0 - 1.0 - 2.0 - 8.0 - 1.0 - 12.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(code_cl_group),
            FadeOut(struct_vis_group),
            FadeOut(s_cross),
            FadeOut(invalid_struct_lbl),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: ERRORS & OUTRO
        # ==========================================
        self.add_sound("audio/ch18_6_errors_outro.wav")

        title_err = Text("18. Compiler-Fehler & Ausblick", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_err), run_time=1.0)
        self.wait(1.0)

        # Show error box
        err_box = RoundedRectangle(corner_radius=0.1, width=10.0, height=2.6, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 0.4, 0])
        err_title = Text("Compiler-Fehler E0382: Use of moved value", font_size=12, color=RED, weight=BOLD).next_to(err_box.get_top(), DOWN, buff=0.2)
        err_console = Paragraph(
            "error[E0382]: borrow of moved value: `s1`",
            "  --> src/main.rs:5:18",
            "   | let s2 = s1; // value moved here",
            "   | println!(\"{}\", s1); // value borrowed here after move",
            font="Monospace", font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(err_title, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.4)
        err_group = VGroup(err_box, err_title, err_console)

        self.play(FadeIn(err_group, scale=0.9), run_time=1.5)
        self.wait(10.0)

        # Transition to Outro
        outro_title = Text("Vielen Dank fürs Zuschauen!", font_size=32, color=RUST_ORANGE, weight=BOLD)
        outro_subtitle = Text("Kapitel 18: Das Ownership-System abgeschlossen", font_size=18, color=CYAN).next_to(outro_title, DOWN, buff=0.4)
        outro_group = VGroup(outro_title, outro_subtitle).move_to([0, -0.2, 0])

        # Spin Gear (Visualizing Rust)
        gear_center = Circle(radius=0.6, color=RUST_ORANGE, stroke_width=4).next_to(outro_group, UP, buff=0.6)
        teeth = VGroup()
        num_teeth = 12
        for i in range(num_teeth):
            angle = i * (360 / num_teeth) * DEGREES
            tooth = Rectangle(width=0.18, height=0.25, color=RUST_ORANGE, fill_opacity=1, stroke_width=0)
            tooth.move_to(gear_center.get_center())
            tooth.shift(0.65 * np.array([np.cos(angle), np.sin(angle), 0]))
            tooth.rotate(angle)
            teeth.add(tooth)
        inner_circle = Circle(radius=0.25, color=BG_COLOR, stroke_width=0, fill_opacity=1).move_to(gear_center.get_center())
        gear = VGroup(gear_center, teeth, inner_circle)

        self.play(
            FadeOut(title_group),
            FadeOut(err_group),
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )

        spin_time = max(1.0, durations["ch18_6_errors_outro"] - 1.0 - 1.0 - 1.5 - 10.0 - 2.0)
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )
