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

class RustOwnershipVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Load durations if they exist, otherwise use sensible defaults
        durations = {
            "ch17_1_intro": 35.0,
            "ch17_2_stack_heap": 35.0,
            "ch17_3_scopes_copy": 32.0,
            "ch17_4_strings": 35.0,
            "ch17_5_move_clone": 33.0,
            "ch17_6_references": 32.0,
            "ch17_7_functions_outro": 35.0
        }
        
        durations_path = "audio/durations_ch17.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # ==========================================
        # SECTION 1: INTRO (3 Speicherverwaltungen & Regeln)
        # ==========================================
        self.add_sound("audio/ch17_1_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 17: Speicherverwaltung & Ownership", font_size=26, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)

        # Move Title to Top
        title_small = Text("Kapitel 17: Speicherverwaltung & Ownership", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        # Three Approaches diagram
        c_width = 3.6
        c_height = 2.8
        
        c1_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.1, 0.4, 0])
        c1_title = Text("Manuell (C/C++)", font_size=12, color=RED, weight=BOLD).next_to(c1_rect.get_top(), DOWN, buff=0.2)
        c1_desc = VGroup(
            Text("• malloc() / free()", font_size=9, color=WHITE),
            Text("• Sehr schnell", font_size=9, color=WHITE),
            Text("• Memory Leaks &", font_size=9, color=RED),
            Text("  Double Frees", font_size=9, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c1_title, DOWN, buff=0.2)
        c1_group = VGroup(c1_rect, c1_title, c1_desc)

        c2_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 0.4, 0])
        c2_title = Text("Garbage Collector", font_size=12, color=YELLOW, weight=BOLD).next_to(c2_rect.get_top(), DOWN, buff=0.2)
        c2_desc = VGroup(
            Text("• Automatischer GC", font_size=9, color=WHITE),
            Text("• Sicher & Bequem", font_size=9, color=WHITE),
            Text("• Kostet CPU &", font_size=9, color=YELLOW),
            Text("  unvorhersehbare Pausen", font_size=9, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c2_title, DOWN, buff=0.2)
        c2_group = VGroup(c2_rect, c2_title, c2_desc)

        c3_rect = RoundedRectangle(corner_radius=0.1, width=c_width, height=c_height, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([4.1, 0.4, 0])
        c3_title = Text("Ownership (Rust)", font_size=12, color=GREEN, weight=BOLD).next_to(c3_rect.get_top(), DOWN, buff=0.2)
        c3_desc = VGroup(
            Text("• Compiler-Prüfung", font_size=9, color=WHITE),
            Text("• Keine Runtime-Kosten", font_size=9, color=WHITE),
            Text("• Schnell wie C", font_size=9, color=GREEN),
            Text("• Sicher wie Python", font_size=9, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(c3_title, DOWN, buff=0.2)
        c3_group = VGroup(c3_rect, c3_title, c3_desc)

        self.play(
            FadeIn(c1_group, shift=UP),
            FadeIn(c2_group, shift=UP),
            FadeIn(c3_group, shift=UP),
            run_time=2.0
        )
        self.wait(6.0)

        # Introduce 3 rules of ownership below cards
        rules_title = Text("Die 3 goldenen Regeln:", font_size=14, color=CYAN, weight=BOLD).move_to([0, -1.8, 0])
        rules_text = VGroup(
            Text("1. Jeder Wert hat genau einen Besitzer (Owner).", font_size=12, color=WHITE),
            Text("2. Es darf niemals zwei Besitzer gleichzeitig geben.", font_size=12, color=WHITE),
            Text("3. Verlässt der Besitzer den Scope ( }), wird der Wert gelöscht (drop).", font_size=12, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(rules_title, DOWN, buff=0.2)
        rules_group = VGroup(rules_title, rules_text)

        self.play(FadeIn(rules_group, shift=UP), run_time=1.5)
        self.wait(10.0)

        # Wait for the audio segment to complete
        remaining_time = durations["ch17_1_intro"] - 1.0 - 2.0 - 1.5 - 0.5 - 2.0 - 6.0 - 1.5 - 10.0
        self.wait(max(1.0, remaining_time))
        
        self.play(
            FadeOut(c1_group),
            FadeOut(c2_group),
            FadeOut(c3_group),
            FadeOut(rules_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 2: STACK VS HEAP (Wo liegen Daten?)
        # ==========================================
        self.add_sound("audio/ch17_2_stack_heap.wav")

        title_sh = Text("17. Stack vs. Heap: Wo liegen Daten?", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sh), run_time=1.0)
        self.wait(1.0)

        # Left: Stack representation
        stack_title = Text("Stack (Der Stapel)", font_size=14, color=CYAN, weight=BOLD).move_to([-3.5, 2.0, 0])
        
        # Draw tabletts stack
        t1 = Rectangle(width=3.0, height=0.5, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-3.5, -1.5, 0])
        t1_lbl = Text("i32: 33 (Fest)", font_size=10, color=WHITE).move_to(t1.get_center())
        t2 = Rectangle(width=3.0, height=0.5, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).next_to(t1, UP, buff=0.1)
        t2_lbl = Text("bool: true (Fest)", font_size=10, color=WHITE).move_to(t2.get_center())
        t3 = Rectangle(width=3.0, height=0.5, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).next_to(t2, UP, buff=0.1)
        t3_lbl = Text("Pointer: 0x01a3 (Zeiger)", font_size=10, color=CYAN).move_to(t3.get_center())
        
        stack_box_group = VGroup(t1, t1_lbl, t2, t2_lbl, t3, t3_lbl)
        stack_footer = Text("LIFO • Fest • Extrem schnell", font_size=11, color=GRAY).next_to(t1, DOWN, buff=0.3)
        stack_group = VGroup(stack_title, stack_box_group, stack_footer)

        # Right: Heap representation
        heap_title = Text("Heap (Der Haufen)", font_size=14, color=YELLOW, weight=BOLD).move_to([3.5, 2.0, 0])
        heap_rect = RoundedRectangle(corner_radius=0.15, width=4.5, height=3.0, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.5, -0.4, 0])
        heap_content = Text("Wachsende Texte\n(z. B. String \"Boris\")\nAdresse: 0x01a3", font_size=11, color=WHITE).move_to(heap_rect.get_center())
        heap_footer = Text("Flexibel • Langsamer", font_size=11, color=GRAY).next_to(heap_rect, DOWN, buff=0.3)
        heap_group = VGroup(heap_title, heap_rect, heap_content, heap_footer)

        # Pointer arrow from Stack to Heap
        ptr_arrow = Arrow(start=[-2.0, 0.3, 0], end=[1.2, 0.3, 0], stroke_width=3, color=CYAN)

        self.play(
            FadeIn(stack_group, shift=RIGHT),
            FadeIn(heap_group, shift=LEFT),
            run_time=2.0
        )
        self.play(Create(ptr_arrow), run_time=1.0)
        self.wait(10.0)

        # Direct Comparison Box
        comp_rect = RoundedRectangle(corner_radius=0.1, width=9.0, height=2.2, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, -0.6, 0])
        comp_content = VGroup(
            Text("Stack: Bekannte Größe beim Kompilieren • Push & Pop • i32, bool", font_size=11, color=CYAN),
            Text("Heap: Dynamische Größe zur Laufzeit • Allokation • String, Vec", font_size=11, color=YELLOW),
            Text("Ownership stellt sicher, dass der Heap freigegeben wird, wenn der Pointer verschwindet.", font_size=10, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(comp_rect.get_center())
        comp_group = VGroup(comp_rect, comp_content)

        # Slide Stack and Heap up slightly to make room
        self.play(
            stack_group.animate.shift(UP * 0.8),
            heap_group.animate.shift(UP * 0.8),
            ptr_arrow.animate.shift(UP * 0.8),
            run_time=1.5
        )
        self.play(FadeIn(comp_group, scale=0.9), run_time=1.5)
        self.wait(8.0)

        remaining_time = durations["ch17_2_stack_heap"] - 1.0 - 1.0 - 2.0 - 1.0 - 10.0 - 1.5 - 1.5 - 8.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(stack_group),
            FadeOut(heap_group),
            FadeOut(ptr_arrow),
            FadeOut(comp_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: SCOPES & COPY TRAIT
        # ==========================================
        self.add_sound("audio/ch17_3_scopes_copy.wav")

        title_scopes = Text("17. Scopes & Der Copy-Trait", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_scopes), run_time=1.0)
        self.wait(1.0)

        # Code block on the left
        code_bg = RoundedRectangle(corner_radius=0.1, width=5.5, height=4.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        code_text = Paragraph(
            "fn main() {",
            "    let age = 33;",
            "    {",
            "        let is_handsome = true;",
            "    } // is_handsome wird gelöscht",
            "",
            "    let time = 2026;",
            "    let year = time; // Kopie!",
            "}",
            font="Monospace", font_size=10, line_spacing=0.45
        ).move_to(code_bg.get_center())
        code_group = VGroup(code_bg, code_text)

        # Explanations on the right
        scope_expl_title = Text("Scopes & Drop-Prinzip", font_size=13, color=CYAN, weight=BOLD).move_to([3.2, 1.2, 0])
        scope_expl_text = VGroup(
            Text("• {} begrenzen Gültigkeit von Daten", font_size=11, color=WHITE),
            Text("• Am Scope-Ende (}) wird drop() aufgerufen", font_size=11, color=WHITE),
            Text("• LIFO: Aufräumen in Gegenreihenfolge", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(scope_expl_title, DOWN, aligned_edge=LEFT, buff=0.25)
        scope_expl = VGroup(scope_expl_title, scope_expl_text)

        copy_expl_title = Text("Der Copy-Trait (Stack)", font_size=13, color=GREEN, weight=BOLD).move_to([3.2, -1.0, 0])
        copy_expl_text = VGroup(
            Text("• Für Stack-Typen (i32, f64, bool, char)", font_size=11, color=WHITE),
            Text("• Zuweisung dupliziert den Wert", font_size=11, color=WHITE),
            Text("• Beide Variablen bleiben voll gültig", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(copy_expl_title, DOWN, aligned_edge=LEFT, buff=0.25)
        copy_expl = VGroup(copy_expl_title, copy_expl_text)

        self.play(FadeIn(code_group, shift=RIGHT), run_time=1.5)
        self.play(FadeIn(scope_expl, shift=LEFT), run_time=1.5)
        self.wait(7.0)

        # Highlight is_handsome drop
        drop_box = SurroundingRectangle(code_text[4], color=RED, buff=0.08, stroke_width=2)
        drop_lbl = Text("drop() wird aufgerufen!", font_size=11, color=RED, weight=BOLD).next_to(code_bg, UP, buff=0.1).shift(RIGHT * 1.5)
        self.play(Create(drop_box), FadeIn(drop_lbl, shift=DOWN), run_time=1.0)
        self.wait(5.0)

        # Show Copy-Trait explanation
        self.play(FadeOut(drop_box), FadeOut(drop_lbl), FadeIn(copy_expl, shift=LEFT), run_time=1.5)
        
        # Highlight Copy code lines
        copy_box = SurroundingRectangle(code_text[7], color=GREEN, buff=0.08, stroke_width=2)
        self.play(Create(copy_box), run_time=1.0)
        self.wait(8.0)

        remaining_time = durations["ch17_3_scopes_copy"] - 1.0 - 1.0 - 1.5 - 1.5 - 7.0 - 1.0 - 5.0 - 1.5 - 1.0 - 8.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(code_group),
            FadeOut(scope_expl),
            FadeOut(copy_expl),
            FadeOut(copy_box),
            run_time=1.0
        )

        # ==========================================
        # SECTION 4: STRINGS (Internal layout)
        # ==========================================
        self.add_sound("audio/ch17_4_strings.wav")

        title_strings = Text("17. Die zwei String-Typen & Innenleben", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_strings), run_time=1.0)
        self.wait(1.0)

        # Left: &str vs String comparison card
        str_comp = RoundedRectangle(corner_radius=0.15, width=4.6, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-4.0, -0.6, 0])
        str_comp_title = Text("&str vs. String", font_size=13, color=CYAN, weight=BOLD).next_to(str_comp.get_top(), DOWN, buff=0.3)
        str_comp_text = VGroup(
            Text("&str (String-Literal):", font_size=11, color=CYAN, weight=BOLD),
            Text("• Fest in Binärdatei eingebrannt", font_size=10, color=WHITE),
            Text("• Unveränderlich", font_size=10, color=WHITE),
            Text("String (Heap-String):", font_size=11, color=YELLOW, weight=BOLD),
            Text("• Liegt dynamisch auf dem Heap", font_size=10, color=WHITE),
            Text("• Veränderbar und wächst", font_size=10, color=WHITE),
            Text("  z. B. String::from(\"Boris\")", font_size=9, color=GRAY, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(str_comp_title, DOWN, aligned_edge=LEFT, buff=0.3)
        str_comp_group = VGroup(str_comp, str_comp_title, str_comp_text)

        # Right: Inside layout of String (Stack + Heap)
        layout_rect = RoundedRectangle(corner_radius=0.15, width=6.2, height=4.2, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.4, -0.6, 0])
        layout_title = Text("Das Innenleben von String", font_size=13, color=YELLOW, weight=BOLD).next_to(layout_rect.get_top(), DOWN, buff=0.3)

        # Stack representation
        s_box = RoundedRectangle(corner_radius=0.08, width=2.4, height=2.2, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([1.5, -0.7, 0])
        s_title = Text("Stack (name)", font_size=10, color=WHITE, weight=BOLD).next_to(s_box.get_top(), DOWN, buff=0.15)
        s_fields = VGroup(
            Text("Pointer: 0x01a3", font_size=9, color=CYAN, font="Monospace"),
            Text("Len: 5", font_size=9, color=WHITE, font="Monospace"),
            Text("Capacity: 5", font_size=9, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(s_title, DOWN, aligned_edge=LEFT, buff=0.2)
        s_group = VGroup(s_box, s_title, s_fields)

        # Heap representation
        h_box = RoundedRectangle(corner_radius=0.08, width=2.4, height=2.2, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([5.0, -0.7, 0])
        h_title = Text("Heap (0x01a3)", font_size=10, color=WHITE, weight=BOLD).next_to(h_box.get_top(), DOWN, buff=0.15)
        h_slots = VGroup(
            Text("[0]: 'B'", font_size=9, color=YELLOW, font="Monospace"),
            Text("[1]: 'o'", font_size=9, color=YELLOW, font="Monospace"),
            Text("[2]: 'r'", font_size=9, color=YELLOW, font="Monospace"),
            Text("[3]: 'i'", font_size=9, color=YELLOW, font="Monospace"),
            Text("[4]: 's'", font_size=9, color=YELLOW, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(h_title, DOWN, aligned_edge=LEFT, buff=0.15)
        h_group = VGroup(h_box, h_title, h_slots)

        ptr_line = Arrow(start=[2.5, -0.4, 0], end=[4.0, -0.4, 0], stroke_width=2.5, color=CYAN)
        layout_group = VGroup(layout_rect, layout_title, s_group, h_group, ptr_line)

        self.play(
            FadeIn(str_comp_group, shift=RIGHT),
            FadeIn(layout_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Animate reallocation ("Umzug") info
        realloc_box = RoundedRectangle(corner_radius=0.1, width=11.0, height=0.9, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -3.1, 0])
        realloc_text = Text("Reallokation (Umzug): Reicht die Kapazität nicht, kopiert Rust die Daten an eine neue Stelle.", font_size=9, color=YELLOW).move_to(realloc_box.get_center())
        realloc_group = VGroup(realloc_box, realloc_text)

        # Shift up to make room
        self.play(
            str_comp_group.animate.shift(UP * 0.4),
            layout_group.animate.shift(UP * 0.4),
            run_time=1.0
        )
        self.play(FadeIn(realloc_group, shift=UP), run_time=1.0)
        self.wait(12.0)

        remaining_time = durations["ch17_4_strings"] - 1.0 - 1.0 - 2.0 - 10.0 - 1.0 - 1.0 - 12.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(str_comp_group),
            FadeOut(layout_group),
            FadeOut(realloc_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: MOVE VS CLONE
        # ==========================================
        self.add_sound("audio/ch17_5_move_clone.wav")

        title_move_clone = Text("17. Move-Semantik vs. .clone()", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_move_clone), run_time=1.0)
        self.wait(1.0)

        # Left: code block
        code_mc_bg = RoundedRectangle(corner_radius=0.1, width=5.5, height=4.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        code_mc_text = Paragraph(
            "fn main() {",
            "    let person = String::from(\"Boris\");",
            "    let genius = person; // MOVE!",
            "    // println!(\"{}\", person); // FEHLER!",
            "",
            "    let a = String::from(\"Welt\");",
            "    let b = a.clone(); // Kopie auf Heap!",
            "    // Beide Variablen sind gültig!",
            "}",
            font="Monospace", font_size=10, line_spacing=0.45
        ).move_to(code_mc_bg.get_center())
        code_mc_group = VGroup(code_mc_bg, code_mc_text)

        # Right: Move visualization diagram
        mc_rect = RoundedRectangle(corner_radius=0.15, width=6.2, height=4.2, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.4, -0.6, 0])
        mc_title = Text("Besitzwechsel (Move)", font_size=13, color=PURPLE, weight=BOLD).next_to(mc_rect.get_top(), DOWN, buff=0.25)
        
        person_v = RoundedRectangle(corner_radius=0.08, width=2.2, height=0.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([1.8, 0.4, 0])
        person_lbl = Text("person", font_size=10, color=CYAN, weight=BOLD).move_to(person_v.get_center())
        
        genius_v = RoundedRectangle(corner_radius=0.08, width=2.2, height=0.6, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([1.8, -0.6, 0])
        genius_lbl = Text("genius", font_size=10, color=GREEN, weight=BOLD).move_to(genius_v.get_center())

        heap_data = RoundedRectangle(corner_radius=0.08, width=2.0, height=1.6, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([5.0, -0.1, 0])
        heap_lbl = Text("Heap-Daten\n\"Boris\"\n(0x01a3)", font_size=9, color=YELLOW).move_to(heap_data.get_center())

        arrow_p = Arrow(start=[2.9, 0.4, 0], end=[4.0, 0.4, 0], stroke_width=2, color=GRAY)
        arrow_g = Arrow(start=[2.9, -0.6, 0], end=[4.0, -0.1, 0], stroke_width=2, color=GREEN)

        mc_dia = VGroup(mc_rect, mc_title, person_v, person_lbl, genius_v, genius_lbl, heap_data, heap_lbl, arrow_p, arrow_g)

        self.play(
            FadeIn(code_mc_group, shift=RIGHT),
            FadeIn(mc_dia, shift=LEFT),
            run_time=2.0
        )
        self.wait(6.0)

        # Animate Move event (cross out person and arrow_p)
        cross = Cross(person_v, stroke_color=RED, stroke_width=4, scale_factor=0.85)
        invalid_lbl = Text("Ungültig!", font_size=10, color=RED, weight=BOLD).next_to(person_v, UP, buff=0.15)
        self.play(Create(cross), FadeIn(invalid_lbl, shift=DOWN), run_time=1.0)
        self.wait(6.0)

        # Highlight clone in code
        clone_box = SurroundingRectangle(code_mc_text[6], color=GREEN, buff=0.08, stroke_width=2)
        self.play(Create(clone_box), run_time=1.0)
        self.wait(8.0)

        remaining_time = durations["ch17_5_move_clone"] - 1.0 - 1.0 - 2.0 - 6.0 - 1.0 - 6.0 - 1.0 - 8.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(code_mc_group),
            FadeOut(mc_dia),
            FadeOut(cross),
            FadeOut(invalid_lbl),
            FadeOut(clone_box),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: REFERENCES (Der Postbote & Copy)
        # ==========================================
        self.add_sound("audio/ch17_6_references.wav")

        title_ref = Text("17. Referenzen & Der Postbote (*)", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_ref), run_time=1.0)
        self.wait(1.0)

        # Code block on the left
        code_ref_bg = RoundedRectangle(corner_radius=0.1, width=5.5, height=4.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        code_ref_text = Paragraph(
            "fn main() {",
            "    let wert = 2;",
            "    let mein_verweis = &wert; // Adresse!",
            "",
            "    println!(\"{}\", *mein_verweis); // 2",
            "",
            "    let ice = \"Cookies\"; // &str",
            "    let des = ice; // Adresse KOPIERT!",
            "}",
            font="Monospace", font_size=10, line_spacing=0.45
        ).move_to(code_ref_bg.get_center())
        code_ref_group = VGroup(code_ref_bg, code_ref_text)

        # Right: Analogy card
        an_rect = RoundedRectangle(corner_radius=0.15, width=6.2, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.4, -0.6, 0])
        an_title = Text("Die Zettel-Analogie", font_size=13, color=CYAN, weight=BOLD).next_to(an_rect.get_top(), DOWN, buff=0.25)
        
        an_content = VGroup(
            Text("• Referenz &wert: Ein kleiner Zettel,", font_size=11, color=WHITE),
            Text("  auf dem die Hausadresse von wert steht.", font_size=10, color=CYAN),
            Text("• Dereferenzierer *mein_verweis:", font_size=11, color=WHITE),
            Text("  Postbote folgt Adresse zum echten Wert.", font_size=10, color=YELLOW),
            Text("• Referenzen (&) kopieren sich selbst:", font_size=11, color=WHITE),
            Text("  Die Adresse wird verdoppelt (Copy).", font_size=10, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(an_title, DOWN, aligned_edge=LEFT, buff=0.3)
        an_group = VGroup(an_rect, an_title, an_content)

        self.play(
            FadeIn(code_ref_group, shift=RIGHT),
            FadeIn(an_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(12.0)

        # Highlight dereferencing
        deref_box = SurroundingRectangle(code_ref_text[4], color=YELLOW, buff=0.08, stroke_width=2)
        self.play(Create(deref_box), run_time=1.0)
        self.wait(5.0)

        # Highlight reference copying
        ref_copy_box = SurroundingRectangle(code_ref_text[7], color=GREEN, buff=0.08, stroke_width=2)
        self.play(
            FadeOut(deref_box),
            Create(ref_copy_box),
            run_time=1.0
        )
        self.wait(6.0)

        remaining_time = durations["ch17_6_references"] - 1.0 - 1.0 - 2.0 - 12.0 - 1.0 - 5.0 - 1.0 - 6.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(code_ref_group),
            FadeOut(an_group),
            FadeOut(ref_copy_box),
            run_time=1.0
        )

        # ==========================================
        # SECTION 7: FUNCTIONS & OUTRO (Ping-Pong)
        # ==========================================
        self.add_sound("audio/ch17_7_functions_outro.wav")

        title_func = Text("17. Funktionen & Eigentums-Ping-Pong", font_size=24, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_func), run_time=1.0)
        self.wait(1.0)

        # Left: code block showing Ping-Pong
        code_fn_bg = RoundedRectangle(corner_radius=0.1, width=5.5, height=4.2, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-3.2, -0.6, 0])
        code_fn_text = Paragraph(
            "fn add_flour(mut meal: String) -> String {",
            "    meal.push_str(\"Mehl, \");",
            "    meal // Zurückgeben",
            "}",
            "",
            "fn main() {",
            "    let mut current_meal = String::new();",
            "    current_meal = add_flour(current_meal);",
            "}",
            font="Monospace", font_size=9, line_spacing=0.45
        ).move_to(code_fn_bg.get_center())
        code_fn_group = VGroup(code_fn_bg, code_fn_text)

        # Right: diagram of ownership Ping-Pong
        pp_rect = RoundedRectangle(corner_radius=0.15, width=6.2, height=4.2, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.4, -0.6, 0])
        pp_title = Text("Das Eigentums-Ping-Pong", font_size=13, color=RED, weight=BOLD).next_to(pp_rect.get_top(), DOWN, buff=0.25)
        
        main_v = RoundedRectangle(corner_radius=0.08, width=1.6, height=0.6, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([1.8, 0.0, 0])
        main_lbl = Text("main()", font_size=10, color=CYAN, weight=BOLD).move_to(main_v.get_center())
        
        func_v = RoundedRectangle(corner_radius=0.08, width=1.8, height=0.6, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([5.0, 0.0, 0])
        func_lbl = Text("add_flour()", font_size=10, color=PURPLE, weight=BOLD).move_to(func_v.get_center())

        arrow_send = CurvedArrow(start_point=[2.6, 0.2, 0], end_point=[4.1, 0.2, 0], color=YELLOW)
        send_lbl = Text("meal (Move)", font_size=8, color=YELLOW).next_to(arrow_send, UP, buff=0.05)

        arrow_recv = CurvedArrow(start_point=[4.1, -0.2, 0], end_point=[2.6, -0.2, 0], color=GREEN)
        recv_lbl = Text("meal (Return)", font_size=8, color=GREEN).next_to(arrow_recv, DOWN, buff=0.05)

        pp_dia = VGroup(pp_rect, pp_title, main_v, main_lbl, func_v, func_lbl, arrow_send, send_lbl, arrow_recv, recv_lbl)

        self.play(
            FadeIn(code_fn_group, shift=RIGHT),
            FadeIn(pp_dia, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Highlight problem and show solution teaser
        solution_box = RoundedRectangle(corner_radius=0.1, width=11.0, height=0.9, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -3.1, 0])
        solution_text = Text("Lösung im nächsten Kapitel: Borrowing (&) - Daten nur ausleihen statt übergeben!", font_size=9, color=GREEN, weight=BOLD).move_to(solution_box.get_center())
        solution_group = VGroup(solution_box, solution_text)

        # Shift up slightly to fit solution box
        self.play(
            code_fn_group.animate.shift(UP * 0.4),
            pp_dia.animate.shift(UP * 0.4),
            run_time=1.0
        )
        self.play(FadeIn(solution_group, shift=UP), run_time=1.0)
        self.wait(8.0)

        # ==========================================
        # OUTRO
        # ==========================================
        outro_title = Text("Vielen Dank fürs Zuschauen!", font_size=32, color=RUST_ORANGE, weight=BOLD)
        outro_subtitle = Text("Kapitel 17: Speicherverwaltung abgeschlossen", font_size=18, color=CYAN).next_to(outro_title, DOWN, buff=0.4)
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
            FadeOut(code_fn_group),
            FadeOut(pp_dia),
            FadeOut(solution_group),
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )

        spin_time = max(1.0, durations["ch17_7_functions_outro"] - 1.0 - 1.0 - 2.0 - 10.0 - 1.0 - 1.0 - 8.0 - 2.0)
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )
