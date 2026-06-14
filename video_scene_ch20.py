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

class RustReferencesVideo(Scene):
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
            "ch20_1_intro": 35.54,
            "ch20_2_references_concept": 35.35,
            "ch20_3_immutable_borrowing": 33.32,
            "ch20_4_mutable_borrowing": 30.44,
            "ch20_5_data_races": 32.36,
            "ch20_6_mixing_borrows": 29.95,
            "ch20_7_dangling_references": 27.01,
            "ch20_8_conclusion_rules": 29.85
        }
        
        durations_path = "audio/durations_ch20.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # Compute total audio duration and required padding per section to hit exactly 300.0 seconds
        total_audio = sum(durations.values())
        padding_per_section = (300.0 - total_audio) / 8.0
        print(f"Total audio: {total_audio}s. Padding per section: {padding_per_section}s.")

        def get_wait_time(key, anim_time):
            d_i = durations[key]
            # wait_time + anim_time + 1.0 (transition) = d_i + padding_per_section
            wait_val = d_i + padding_per_section - anim_time - 1.0
            return max(0.1, wait_val)

        # ==========================================
        # SECTION 1: INTRO (Speicher-Problem & Borrowing)
        # ==========================================
        self.add_sound("audio/ch20_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 20: Referenzen & Borrowing (Ausleihen)", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(3.0)

        # Move Title to Top
        title_small = Text("Kapitel 20: Referenzen & Borrowing", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Draw Ownership Move vs. Borrowing comparison
        box_w, box_h = 5.2, 3.2
        
        # Left: Move (Tedious ownership flow)
        move_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.2, -0.4, 0])
        move_title = Text("Ownership Move (Eigentum geht verloren)", font_size=11, color=RED, weight=BOLD).next_to(move_box.get_top(), DOWN, buff=0.2)
        move_flow = VGroup(
            Text("let s1 = String::from(\"Hallo\");", font_size=9, color=WHITE),
            Text("let len = berechne(s1); [MOVE]", font_size=9, color=YELLOW),
            Text("                         │", font_size=9, color=GRAY),
            Text("s1 ist danach ungültig und tot! ❌", font_size=9, color=RED),
            Text("Wert muss per return zurückgegeben werden.", font_size=8, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(move_title, DOWN, buff=0.25)
        move_group = VGroup(move_box, move_title, move_flow)

        # Right: Borrowing (Simple referencing)
        borrow_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.2, -0.4, 0])
        borrow_title = Text("Borrowing & (Ausleihen)", font_size=11, color=GREEN, weight=BOLD).next_to(borrow_box.get_top(), DOWN, buff=0.2)
        borrow_flow = VGroup(
            Text("let s1 = String::from(\"Hallo\");", font_size=9, color=WHITE),
            Text("let len = berechne_laenge(&s1); [LEIHE]", font_size=9, color=GREEN),
            Text("                          │", font_size=9, color=GRAY),
            Text("s1 bleibt weiterhin voll gültig! 🟢", font_size=9, color=GREEN),
            Text("Nur die Adresse (&s1) wird ausgeliehen.", font_size=8, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(borrow_title, DOWN, buff=0.25)
        borrow_group = VGroup(borrow_box, borrow_title, borrow_flow)

        self.play(
            FadeIn(move_group, shift=RIGHT),
            FadeIn(borrow_group, shift=LEFT),
            run_time=2.0
        )
        
        # Calculate and execute dynamic wait
        # Animations: 1.5 + 3.0 + 1.5 + 1.0 + 2.0 = 9.0 seconds
        self.wait(get_wait_time("ch20_1_intro", 9.0))
        
        self.play(
            FadeOut(move_group),
            FadeOut(borrow_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 2: HOW REFERENCES WORK IN MEMORY
        # ==========================================
        self.add_sound("audio/ch20_2_references_concept.wav")

        title_mem = Text("20. Wie Referenzen im Speicher liegen", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_mem), run_time=1.0)
        self.wait(1.0)

        # Memory Diagram: Stack and Heap
        # Stack Card
        stack_card = RoundedRectangle(corner_radius=0.1, width=5.0, height=3.5, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.2, -0.5, 0])
        stack_title = Text("STACK", font_size=12, color=CYAN, weight=BOLD).next_to(stack_card.get_top(), DOWN, buff=0.2)
        
        # Heap Card
        heap_card = RoundedRectangle(corner_radius=0.1, width=5.0, height=3.5, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.2, -0.5, 0])
        heap_title = Text("HEAP", font_size=12, color=PURPLE, weight=BOLD).next_to(heap_card.get_top(), DOWN, buff=0.2)
        
        self.play(
            FadeIn(stack_card, shift=UP),
            FadeIn(heap_card, shift=UP),
            FadeIn(stack_title),
            FadeIn(heap_title),
            run_time=1.5
        )
        self.wait(2.0)

        # Variables in Stack
        # Owner s1
        s1_box = RoundedRectangle(corner_radius=0.05, width=4.0, height=1.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([-3.2, 0.4, 0])
        s1_text = Paragraph(
            "s1 (Owner / String)",
            "Zeiger: 0x5000 | Länge: 5",
            font="Monospace", font_size=8, color=WHITE
        ).move_to(s1_box.get_center())
        
        # Reference s
        s_box = RoundedRectangle(corner_radius=0.05, width=4.0, height=1.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([-3.2, -1.0, 0])
        s_text = Paragraph(
            "s (Referenz / &String)",
            "Speicheradresse: 0x2000",
            font="Monospace", font_size=8, color=WHITE
        ).move_to(s_box.get_center())
        
        # Heap Data
        heap_val = RoundedRectangle(corner_radius=0.05, width=4.0, height=1.0, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1).move_to([3.2, 0.4, 0])
        heap_text = Paragraph(
            "Adresse 0x5000 (Heap-Daten)",
            "[ 'H', 'a', 'l', 'l', 'o' ]",
            font="Monospace", font_size=8, color=WHITE
        ).move_to(heap_val.get_center())

        self.play(FadeIn(s1_box), FadeIn(s1_text), run_time=1.0)
        self.play(FadeIn(heap_val), FadeIn(heap_text), run_time=1.0)
        
        # Arrow from s1 to heap
        arrow1 = Arrow(start=s1_box.get_right(), end=heap_val.get_left(), color=GREEN, buff=0.1)
        self.play(Create(arrow1), run_time=1.0)
        self.wait(2.0)

        self.play(FadeIn(s_box), FadeIn(s_text), run_time=1.0)
        
        # Arrow from s to s1 (showing referencing/indirection)
        arrow2 = Arrow(start=s_box.get_top(), end=s1_box.get_bottom(), color=CYAN, buff=0.1)
        self.play(Create(arrow2), run_time=1.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 1.0 + 1.0 + 1.0 + 2.0 + 1.0 + 1.0 = 13.5 seconds
        self.wait(get_wait_time("ch20_2_references_concept", 13.5))

        self.play(
            FadeOut(stack_card), FadeOut(stack_title),
            FadeOut(heap_card), FadeOut(heap_title),
            FadeOut(s1_box), FadeOut(s1_text),
            FadeOut(s_box), FadeOut(s_text),
            FadeOut(heap_val), FadeOut(heap_text),
            FadeOut(arrow1), FadeOut(arrow2),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: IMMUTABLE REFERENCE (&T)
        # ==========================================
        self.add_sound("audio/ch20_3_immutable_borrowing.wav")

        title_imm = Text("20. Unveränderliche Referenzen (&T)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_imm), run_time=1.0)
        self.wait(1.0)

        # Box representing the original value
        orig_card = RoundedRectangle(corner_radius=0.1, width=3.5, height=1.8, color=GRAY, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.0, 0])
        orig_title = Text("Wert: s1 (String)", font_size=10, color=WHITE, weight=BOLD).next_to(orig_card.get_top(), DOWN, buff=0.2)
        orig_val = Text("\"Hallo\"", font_size=14, color=WHITE).next_to(orig_title, DOWN, buff=0.3)
        orig_group = VGroup(orig_card, orig_title, orig_val)

        # Multiple reader references pointing to original value
        r1_card = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.5, -1.2, 0])
        r1_txt = Paragraph("r1 (&String)", "liest \"Hallo\"", font_size=8, color=CYAN).move_to(r1_card.get_center())
        
        r2_card = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -1.2, 0])
        r2_txt = Paragraph("r2 (&String)", "liest \"Hallo\"", font_size=8, color=CYAN).move_to(r2_card.get_center())
        
        r3_card = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.2, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.5, -1.2, 0])
        r3_txt = Paragraph("r3 (&String)", "liest \"Hallo\"", font_size=8, color=CYAN).move_to(r3_card.get_center())

        arrow_r1 = Arrow(start=r1_card.get_top(), end=orig_card.get_left(), color=CYAN, buff=0.1)
        arrow_r2 = Arrow(start=r2_card.get_top(), end=orig_card.get_bottom(), color=CYAN, buff=0.1)
        arrow_r3 = Arrow(start=r3_card.get_top(), end=orig_card.get_right(), color=CYAN, buff=0.1)

        self.play(FadeIn(orig_group, shift=DOWN), run_time=1.5)
        self.wait(2.0)
        
        self.play(
            FadeIn(r1_card, shift=UP), FadeIn(r1_txt), Create(arrow_r1),
            FadeIn(r2_card, shift=UP), FadeIn(r2_txt), Create(arrow_r2),
            FadeIn(r3_card, shift=UP), FadeIn(r3_txt), Create(arrow_r3),
            run_time=2.0
        )
        self.wait(3.0)

        # Text banner: "Beliebig viele Lese-Referenzen zur gleichen Zeit erlaubt! 🟢"
        banner = RoundedRectangle(corner_radius=0.05, width=10.0, height=0.8, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1).move_to([0, 2.2, 0])
        banner_txt = Text("Erlaubt: Beliebig viele Lese-Referenzen (unveränderlich) gleichzeitig! 🟢", font_size=10, color=GREEN)
        banner_v = VGroup(banner, banner_txt)
        
        self.play(FadeIn(banner_v, shift=DOWN), run_time=1.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 2.0 + 3.0 + 1.0 = 11.5 seconds
        self.wait(get_wait_time("ch20_3_immutable_borrowing", 11.5))

        self.play(
            FadeOut(orig_group),
            FadeOut(r1_card), FadeOut(r1_txt), FadeOut(arrow_r1),
            FadeOut(r2_card), FadeOut(r2_txt), FadeOut(arrow_r2),
            FadeOut(r3_card), FadeOut(r3_txt), FadeOut(arrow_r3),
            FadeOut(banner_v),
            run_time=1.0
        )

        # ==========================================
        # SECTION 4: MUTABLE REFERENCE (&mut T)
        # ==========================================
        self.add_sound("audio/ch20_4_mutable_borrowing.wav")

        title_mut = Text("20. Veränderliche Referenzen (&mut T)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_mut), run_time=1.0)
        self.wait(1.0)

        # Original Value box
        orig_mut_card = RoundedRectangle(corner_radius=0.1, width=3.8, height=1.8, color=GRAY, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.2, 0])
        orig_mut_title = Text("Variable: let mut s1 (String)", font_size=10, color=WHITE, weight=BOLD).next_to(orig_mut_card.get_top(), DOWN, buff=0.2)
        orig_mut_val = Text("\"Hallo\"", font_size=14, color=WHITE).next_to(orig_mut_title, DOWN, buff=0.3)
        orig_mut_group = VGroup(orig_mut_card, orig_mut_title, orig_mut_val)

        # Active mutable reference
        writer_card = RoundedRectangle(corner_radius=0.08, width=3.2, height=1.3, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.0, -1.2, 0])
        writer_txt = Paragraph("writer (&mut String)", "ändert Daten direkt", font_size=8, color=GREEN).move_to(writer_card.get_center())
        arrow_writer = Arrow(start=writer_card.get_top(), end=orig_mut_card.get_left(), color=GREEN, buff=0.1)

        self.play(FadeIn(orig_mut_group, shift=DOWN), run_time=1.5)
        self.wait(1.5)
        
        self.play(FadeIn(writer_card, shift=UP), FadeIn(writer_txt), Create(arrow_writer), run_time=1.0)
        self.wait(2.0)

        # Animate the change of s1 value
        new_val = Text("\"Hallo Welt\"", font_size=14, color=GREEN).next_to(orig_mut_title, DOWN, buff=0.3)
        self.play(Transform(orig_mut_val, new_val), run_time=1.0)
        self.wait(3.0)

        # Show warning: Attempting to add a second mutable reference
        writer2_card = RoundedRectangle(corner_radius=0.08, width=3.2, height=1.3, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.0, -1.2, 0])
        writer2_txt = Paragraph("writer2 (&mut String)", "❌ ZWEITER SCHREIBER!", font_size=8, color=RED).move_to(writer2_card.get_center())
        arrow_writer2 = Arrow(start=writer2_card.get_top(), end=orig_mut_card.get_right(), color=RED, buff=0.1)
        
        cross_out = Line(start=writer2_card.get_corner(DL), end=writer2_card.get_corner(UR), color=RED, stroke_width=4)
        cross_out2 = Line(start=writer2_card.get_corner(UL), end=writer2_card.get_corner(DR), color=RED, stroke_width=4)
        cross_group = VGroup(cross_out, cross_out2)

        self.play(FadeIn(writer2_card, shift=UP), FadeIn(writer2_txt), Create(arrow_writer2), run_time=1.0)
        self.wait(1.5)
        self.play(Create(cross_group), run_time=1.0)
        
        # Big warning banner: "Niemals mehr als eine mutable Referenz zur gleichen Zeit!"
        warning_banner = RoundedRectangle(corner_radius=0.05, width=11.0, height=0.8, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, 2.4, 0])
        warning_txt = Text("Verboten: Mehr als ein aktiver Schreiber zur selben Zeit! ❌", font_size=10, color=RED, weight=BOLD)
        warning_v = VGroup(warning_banner, warning_txt)
        
        self.play(FadeIn(warning_v, shift=DOWN), run_time=1.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 1.5 + 1.0 + 2.0 + 1.0 + 3.0 + 1.0 + 1.5 + 1.0 + 1.0 = 16.5 seconds
        self.wait(get_wait_time("ch20_4_mutable_borrowing", 16.5))

        self.play(
            FadeOut(orig_mut_group),
            FadeOut(writer_card), FadeOut(writer_txt), FadeOut(arrow_writer),
            FadeOut(writer2_card), FadeOut(writer2_txt), FadeOut(arrow_writer2),
            FadeOut(cross_group), FadeOut(warning_v),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: DATA RACES
        # ==========================================
        self.add_sound("audio/ch20_5_data_races.wav")

        title_race = Text("20. Warum diese Regel? Datenkonflikte (Data Races)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_race), run_time=1.0)
        self.wait(1.0)

        # Data Race criteria list
        criteria_box = RoundedRectangle(corner_radius=0.1, width=11.0, height=3.6, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -0.4, 0])
        criteria_title = Text("Was ist ein Datenkonflikt (Data Race)?", font_size=12, color=RED, weight=BOLD).next_to(criteria_box.get_top(), DOWN, buff=0.25)
        
        criteria_items = VGroup(
            Text("1. Zwei oder mehr Zeiger greifen gleichzeitig auf dieselbe Adresse zu.", font_size=10, color=WHITE),
            Text("2. Mindestens einer dieser Zeiger schreibt (verändert Daten).", font_size=10, color=WHITE),
            Text("3. Es gibt keinen Synchronisations-Mechanismus (wie Mutexes).", font_size=10, color=WHITE),
            Text("► Folge: Undefiniertes Verhalten, willkürliche Abstürze und Sicherheitslücken.", font_size=10, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(criteria_title, DOWN, buff=0.35)
        
        self.play(FadeIn(criteria_box, shift=DOWN), FadeIn(criteria_title), run_time=1.5)
        self.play(FadeIn(criteria_items, shift=RIGHT), run_time=2.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 = 5.5 seconds
        self.wait(get_wait_time("ch20_5_data_races", 5.5))

        self.play(
            FadeOut(criteria_box),
            FadeOut(criteria_title),
            FadeOut(criteria_items),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: MIXING BORROWS & NLL
        # ==========================================
        self.add_sound("audio/ch20_6_mixing_borrows.wav")

        title_mix = Text("20. Mischen von Lese- und Schreib-Referenzen", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_mix), run_time=1.0)
        self.wait(1.0)

        # Code display box illustrating NLL (Non-Lexical Lifetimes)
        code_box = RoundedRectangle(corner_radius=0.1, width=11.2, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        code_title = Text("Non-Lexical Lifetimes (NLL) im Code", font_size=11, color=CYAN, weight=BOLD).next_to(code_box.get_top(), DOWN, buff=0.2)
        
        code_lines = Paragraph(
            "let mut s = String::from(\"Rust\");",
            "let r1 = &s;      // 🟢 Lese-Referenz beginnt",
            "println!(\"{}\", r1); // Letzte Nutzung von r1 -> r1 erlischt! 💡",
            "",
            "let r2 = &mut s;  // 🟢 Erlaubt! (r1 blockiert nicht mehr)",
            "r2.push_str(\" Kurs\");",
            font="Monospace", font_size=8.5, color=WHITE, line_spacing=0.45
        ).next_to(code_title, DOWN, buff=0.25).align_to(code_box, LEFT).shift(RIGHT * 0.8)

        self.play(FadeIn(code_box, shift=UP), FadeIn(code_title), run_time=1.5)
        self.play(FadeIn(code_lines, shift=DOWN), run_time=2.0)
        self.wait(3.0)

        # Highlight NLL drop point
        drop_highlight = SurroundingRectangle(code_lines[2], color=GREEN, stroke_width=1.5)
        drop_txt = Text("Ausleihe erlischt zeilenbasiert!", font_size=8, color=GREEN).next_to(drop_highlight, RIGHT, buff=0.3)
        
        self.play(Create(drop_highlight), FadeIn(drop_txt, shift=LEFT), run_time=1.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 3.0 + 1.0 = 9.5 seconds
        self.wait(get_wait_time("ch20_6_mixing_borrows", 9.5))

        self.play(
            FadeOut(code_box),
            FadeOut(code_title),
            FadeOut(code_lines),
            FadeOut(drop_highlight),
            FadeOut(drop_txt),
            run_time=1.0
        )

        # ==========================================
        # SECTION 7: DANGLING REFERENCES (E0515)
        # ==========================================
        self.add_sound("audio/ch20_7_dangling_references.wav")

        title_dang = Text("20. Dangling References (Totzeiger)", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_dang), run_time=1.0)
        self.wait(1.0)

        # Show the dangerous function code
        dang_code_box = RoundedRectangle(corner_radius=0.1, width=11.2, height=3.6, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        dang_code_title = Text("Lokaler Referenz-Fehler (Dangling Reference)", font_size=11, color=RED, weight=BOLD).next_to(dang_code_box.get_top(), DOWN, buff=0.2)
        
        dang_code = Paragraph(
            "fn erzeuge_referenz() -> &String {",
            "    let s = String::from(\"Hallo\"); // s lebt nur in der Funktion",
            "    &s // ❌ FEHLER: s wird gleich gelöscht, Zeiger zeigt ins Leere!",
            "}",
            "",
            "Lösung: Eigentum übergeben -> Rückgabetyp 'String' statt '&String'",
            font="Monospace", font_size=8.5, color=WHITE, line_spacing=0.45
        ).next_to(dang_code_title, DOWN, buff=0.25).align_to(dang_code_box, LEFT).shift(RIGHT * 0.8)

        self.play(FadeIn(dang_code_box, shift=UP), FadeIn(dang_code_title), run_time=1.5)
        self.play(FadeIn(dang_code, shift=DOWN), run_time=2.0)
        self.wait(4.0)

        # Highlight error line
        err_highlight = SurroundingRectangle(dang_code[2], color=RED, stroke_width=1.5)
        err_label = Text("s stirbt am Funktionsende! 💀", font_size=8, color=RED).next_to(err_highlight, RIGHT, buff=0.3)
        self.play(Create(err_highlight), FadeIn(err_label, shift=LEFT), run_time=1.0)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 4.0 + 1.0 = 10.5 seconds
        self.wait(get_wait_time("ch20_7_dangling_references", 10.5))

        self.play(
            FadeOut(dang_code_box),
            FadeOut(dang_code_title),
            FadeOut(dang_code),
            FadeOut(err_highlight),
            FadeOut(err_label),
            run_time=1.0
        )

        # ==========================================
        # SECTION 8: CONCLUSION & RULES SUMMARY
        # ==========================================
        self.add_sound("audio/ch20_8_conclusion_rules.wav")

        title_concl = Text("20. Zusammenfassung: Die 2 goldenen Regeln", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_concl), run_time=1.0)
        self.wait(1.0)

        # Nice big rule board
        board = RoundedRectangle(corner_radius=0.15, width=11.6, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2.5).move_to([0, -0.4, 0])
        
        rule1_title = Text("Regel 1: Leser- & Schreiber-Exklusivität", font_size=12, color=CYAN, weight=BOLD)
        rule1_desc = Text("Entweder beliebig viele Lese-Referenzen (&T) ODER exklusiv eine Schreib-Referenz (&mut T).", font_size=9, color=WHITE)
        rule1_v = VGroup(rule1_title, rule1_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        rule2_title = Text("Regel 2: Lebenszeit-Gültigkeit", font_size=12, color=CYAN, weight=BOLD)
        rule2_desc = Text("Referenzen müssen immer auf gültigen Speicher zeigen und dürfen den Besitzer nie überleben.", font_size=9, color=WHITE)
        rule2_v = VGroup(rule2_title, rule2_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        rules_layout = VGroup(rule1_v, rule2_v).arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to(board.get_center())

        self.play(Create(board), run_time=1.5)
        self.play(FadeIn(rules_layout, shift=UP), run_time=2.0)
        self.wait(5.0)

        outro_text = Text("Vielen Dank fürs Zuschauen! Übe fleißig mit den Challenges.", font_size=14, color=YELLOW).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(outro_text, shift=DOWN), run_time=1.5)
        
        # Calculate and execute dynamic wait
        # Animations: 1.0 + 1.0 + 1.5 + 2.0 + 5.0 + 1.5 = 12.0 seconds
        self.wait(get_wait_time("ch20_8_conclusion_rules", 12.0))

        self.play(
            FadeOut(board),
            FadeOut(rules_layout),
            FadeOut(outro_text),
            FadeOut(title_group),
            run_time=1.0
        )
        self.wait(0.1)
