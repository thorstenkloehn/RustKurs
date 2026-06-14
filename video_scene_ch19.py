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

class RustBorrowingVideo(Scene):
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
            "ch19_1_intro": 35.0,
            "ch19_2_borrowing_types": 35.0,
            "ch19_3_borrow_checker_rules": 40.0,
            "ch19_4_lifetimes": 35.0,
            "ch19_5_copy_vs_move": 35.0,
            "ch19_6_dangling_references_outro": 35.0
        }
        
        durations_path = "audio/durations_ch19.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # ==========================================
        # SECTION 1: INTRO (Move vs Borrowing)
        # ==========================================
        self.add_sound("audio/ch19_1_intro.wav")

        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 19: Referenzen & Borrowing (Ausleihen)", font_size=22, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)

        # Move Title to Top
        title_small = Text("Kapitel 19: Referenzen & Borrowing", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(0.5)

        # Move vs Borrowing side-by-side comparison
        box_width = 5.2
        box_height = 3.2
        
        # Left: Move (Tedious ownership flow)
        move_rect = RoundedRectangle(corner_radius=0.1, width=box_width, height=box_height, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.2, -0.4, 0])
        move_title = Text("Ownership Move (Umständlich)", font_size=12, color=RED, weight=BOLD).next_to(move_rect.get_top(), DOWN, buff=0.2)
        move_flow = VGroup(
            Text("main() besitzt 'Teig'", font_size=9, color=WHITE),
            Text("└──► mehl_hinzufuegen(Teig)  [MOVE]", font_size=9, color=YELLOW),
            Text("     └──► bearbeitet und gibt zurück...", font_size=9, color=WHITE),
            Text("◄─────────────────────────────────┘ [RETURN]", font_size=9, color=YELLOW),
            Text("main() erhält wieder Besitz", font_size=9, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(move_title, DOWN, buff=0.25)
        move_group = VGroup(move_rect, move_title, move_flow)

        # Right: Borrowing (Simple referencing)
        borrow_rect = RoundedRectangle(corner_radius=0.1, width=box_width, height=box_height, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.2, -0.4, 0])
        borrow_title = Text("Borrowing & (Ausleihen)", font_size=12, color=GREEN, weight=BOLD).next_to(borrow_rect.get_top(), DOWN, buff=0.2)
        borrow_flow = VGroup(
            Text("main() besitzt 'Teig'", font_size=9, color=WHITE),
            Text("├──► zeige_mahlzeit(&Teig)   [Lese-Adresse]", font_size=9, color=GREEN),
            Text("├──► mehl_hinzufuegen(&mut Teig) [Schreib-Adresse]", font_size=9, color=GREEN),
            Text("│", font_size=9, color=GRAY),
            Text("main() behält Besitz die ganze Zeit!", font_size=9, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(borrow_title, DOWN, buff=0.25)
        borrow_group = VGroup(borrow_rect, borrow_title, borrow_flow)

        self.play(
            FadeIn(move_group, shift=RIGHT),
            FadeIn(borrow_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Wait for the audio segment to complete
        remaining_time = durations["ch19_1_intro"] - 1.0 - 2.0 - 1.5 - 0.5 - 2.0 - 10.0
        self.wait(max(1.0, remaining_time))
        
        self.play(
            FadeOut(move_group),
            FadeOut(borrow_group),
            run_time=1.0
        )

        # ==========================================
        # SECTION 2: THE 4 BORROWING TYPES
        # ==========================================
        self.add_sound("audio/ch19_2_borrowing_types.wav")

        title_types = Text("19. Die 4 Übergabe-Arten in Rust", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_types), run_time=1.0)
        self.wait(1.0)

        # Table showing parameter passing modes
        table_headers = ["Syntax", "Typ", "Besitz?", "Schreiben?", "Beschreibung"]
        header_v = VGroup(*[Text(h, font_size=9.5, color=CYAN, weight=BOLD) for h in table_headers]).arrange(RIGHT, buff=0.6).move_to([0, 1.6, 0])
        
        rows = [
            ["rezept: String", "Wert (In)", "Ja (Move)", "Nein", "Eigentum geht verloren, schreibgeschützt."],
            ["mut rezept: String", "Wert (In/Out)", "Ja (Move)", "Ja", "Eigentum geht verloren, veränderbar."],
            ["rezept: &String", "Ref (&)", "Nein (Leihe)", "Nein", "Leseadresse. Standard für Anzeige."],
            ["rezept: &mut String", "Ref (&mut)", "Nein (Leihe)", "Ja", "Schreibadresse. Direktes Ändern."]
        ]
        
        row_groups = VGroup()
        for idx, row in enumerate(rows):
            col_colors = [WHITE, WHITE, YELLOW if "Ja" in row[2] else GREEN, GREEN if "Ja" in row[3] else RED, GRAY]
            col_v = VGroup()
            for c_idx, cell in enumerate(row):
                fs = 8.5 if c_idx == 4 else 9
                cell_text = Text(cell, font_size=fs, color=col_colors[c_idx])
                col_v.add(cell_text)
            
            # Align the elements horizontally manually to form columns
            col_v[0].move_to([-4.8, 0.8 - idx*0.7, 0])
            col_v[1].move_to([-2.6, 0.8 - idx*0.7, 0])
            col_v[2].move_to([-1.0, 0.8 - idx*0.7, 0])
            col_v[3].move_to([0.6, 0.8 - idx*0.7, 0])
            col_v[4].move_to([3.8, 0.8 - idx*0.7, 0])
            
            row_groups.add(col_v)

        # Align headers to columns
        header_v[0].move_to([-4.8, 1.6, 0])
        header_v[1].move_to([-2.6, 1.6, 0])
        header_v[2].move_to([-1.0, 1.6, 0])
        header_v[3].move_to([0.6, 1.6, 0])
        header_v[4].move_to([3.8, 1.6, 0])

        self.play(FadeIn(header_v, shift=UP), run_time=1.5)
        self.play(FadeIn(row_groups, shift=DOWN), run_time=2.0)
        self.wait(4.0)

        # Highlight &String
        lese_highlight = SurroundingRectangle(row_groups[2], color=CYAN, stroke_width=2)
        lese_label = Text("Lese-Referenz (Standard)", font_size=8, color=CYAN).next_to(lese_highlight, LEFT, buff=0.15)
        self.play(Create(lese_highlight), FadeIn(lese_label, shift=RIGHT), run_time=1.0)
        self.wait(5.0)

        # Highlight &mut String
        schreib_highlight = SurroundingRectangle(row_groups[3], color=GREEN, stroke_width=2)
        schreib_label = Text("Schreib-Referenz (Exklusiv)", font_size=8, color=GREEN).next_to(schreib_highlight, LEFT, buff=0.15)
        self.play(
            ReplacementTransform(lese_highlight, schreib_highlight),
            ReplacementTransform(lese_label, schreib_label),
            run_time=1.5
        )
        self.wait(8.0)

        remaining_time = durations["ch19_2_borrowing_types"] - 1.0 - 1.0 - 1.5 - 2.0 - 4.0 - 1.0 - 5.0 - 1.5 - 8.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(header_v),
            FadeOut(row_groups),
            FadeOut(schreib_highlight),
            FadeOut(schreib_label),
            run_time=1.0
        )

        # ==========================================
        # SECTION 3: BORROW CHECKER RULES (Car painting)
        # ==========================================
        self.add_sound("audio/ch19_3_borrow_checker_rules.wav")

        title_rules = Text("19. Die 2 Borrowing-Regeln & Datenkonflikte", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_rules), run_time=1.0)
        self.wait(1.0)

        # Text rules
        rules_box = RoundedRectangle(corner_radius=0.1, width=11.6, height=1.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, 1.2, 0])
        rules_text = Paragraph(
            "Regel 1: Beliebig viele unveränderliche Referenzen (&T) gleichzeitig erlaubt.",
            "Regel 2: Nur EINE veränderliche Referenz (&mut T) gleichzeitig erlaubt.",
            "Niemals beides gleichzeitig! Entweder viele Leser ODER ein Schreiber.",
            font="Monospace", font_size=9, color=WHITE, line_spacing=0.4
        ).move_to(rules_box.get_center())
        rules_v = VGroup(rules_box, rules_text)
        
        self.play(FadeIn(rules_v, shift=DOWN), run_time=1.5)
        self.wait(4.0)

        # Visual: Car Collision (Klaus and Sabine painting/driving the car)
        car_bg = RoundedRectangle(corner_radius=0.15, width=10.0, height=2.4, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -1.2, 0])
        
        # Draw a simple car representation
        car_body = Rectangle(width=2.5, height=0.6, color=RED, fill_color=RED, fill_opacity=0.9).move_to([0, -1.2, 0])
        car_roof = Polygon([-0.8, -0.9, 0], [0.8, -0.9, 0], [0.5, -0.6, 0], [-0.5, -0.6, 0], color=RED, fill_color=RED, fill_opacity=0.9)
        wheel1 = Circle(radius=0.25, color=GRAY, fill_color=TERM_BG, fill_opacity=1).move_to([-0.7, -1.5, 0])
        wheel2 = Circle(radius=0.25, color=GRAY, fill_color=TERM_BG, fill_opacity=1).move_to([0.7, -1.5, 0])
        car_group = VGroup(car_body, car_roof, wheel1, wheel2)

        klaus = Text("Klaus (Leser): Will rotes Auto", font_size=9, color=CYAN).move_to([-3.4, -0.8, 0])
        klaus_arrow = Arrow(start=[-2.2, -0.8, 0], end=[-1.2, -1.1, 0], stroke_width=2.5, color=CYAN)
        klaus_group = VGroup(klaus, klaus_arrow)

        sabine = Text("Sabine (Schreiber): Malt es Blau", font_size=9, color=GREEN).move_to([3.4, -0.8, 0])
        sabine_arrow = Arrow(start=[2.2, -0.8, 0], end=[1.2, -1.1, 0], stroke_width=2.5, color=GREEN)
        sabine_group = VGroup(sabine, sabine_arrow)

        self.play(
            FadeIn(car_bg),
            FadeIn(car_group),
            run_time=1.5
        )
        self.play(
            FadeIn(klaus_group, shift=RIGHT),
            FadeIn(sabine_group, shift=LEFT),
            run_time=1.5
        )
        self.wait(5.0)

        # Conflict! Change car body color and show warning
        conflict_flash = Flash(car_body, color=YELLOW, flash_radius=1.8, num_lines=15)
        car_blue_body = Rectangle(width=2.5, height=0.6, color=CYAN, fill_color=CYAN, fill_opacity=0.9).move_to([0, -1.2, 0])
        car_blue_roof = Polygon([-0.8, -0.9, 0], [0.8, -0.9, 0], [0.5, -0.6, 0], [-0.5, -0.6, 0], color=CYAN, fill_color=CYAN, fill_opacity=0.9)
        car_blue_group = VGroup(car_blue_body, car_blue_roof, wheel1.copy(), wheel2.copy())
        
        warning_sign = Text("❌ DATENKONFLIKT / DATA RACE", font_size=12, color=RED, weight=BOLD).move_to([0, -0.4, 0])
        self.play(
            conflict_flash,
            Transform(car_group, car_blue_group),
            FadeIn(warning_sign, scale=0.8),
            run_time=1.5
        )
        self.wait(10.0)

        remaining_time = durations["ch19_3_borrow_checker_rules"] - 1.0 - 1.0 - 1.5 - 4.0 - 1.5 - 1.5 - 5.0 - 1.5 - 10.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(rules_v),
            FadeOut(car_bg),
            FadeOut(car_group),
            FadeOut(klaus_group),
            FadeOut(sabine_group),
            FadeOut(warning_sign),
            run_time=1.0
        )

        # ==========================================
        # SECTION 4: LIFETIMES (NLL)
        # ==========================================
        self.add_sound("audio/ch19_4_lifetimes.wav")

        title_life = Text("19. Non-Lexical Lifetimes (NLL)", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_life), run_time=1.0)
        self.wait(1.0)

        # Side-by-side: Left (sequential: OK), Right (overlapping: Error)
        # Left: OK
        ok_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=4.2, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.2, -0.8, 0])
        ok_title = Text("Nacheinander (🟢 OK)", font_size=11, color=GREEN, weight=BOLD).next_to(ok_box.get_top(), DOWN, buff=0.25)
        ok_code = Paragraph(
            "let mut auto = String::from(\"Rot\");",
            "let lackierer = &mut auto; // Beginn",
            "lackierer.push_str(\"...\"); // Ende ◄──",
            "",
            "let betrachter = &auto; // 🟢 Erlaubt",
            "println!(\"{}\", betrachter);",
            font="Monospace", font_size=8, line_spacing=0.5
        ).next_to(ok_title, DOWN, buff=0.35).align_to(ok_box, LEFT).shift(RIGHT * 0.3)
        ok_group = VGroup(ok_box, ok_title, ok_code)

        # Right: Error
        err_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=4.2, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.2, -0.8, 0])
        err_title = Text("Gleichzeitig (🔴 FEHLER)", font_size=11, color=RED, weight=BOLD).next_to(err_box.get_top(), DOWN, buff=0.25)
        err_code = Paragraph(
            "let mut auto = String::from(\"Rot\");",
            "let lackierer = &mut auto; // Beginn",
            "let betrachter = &auto; // ❌ FEHLER",
            "",
            "// lackierer lebt noch bis hierhin:",
            "println!(\"{}, {}\", lackierer, betrachter);",
            font="Monospace", font_size=8, line_spacing=0.5
        ).next_to(err_title, DOWN, buff=0.35).align_to(err_box, LEFT).shift(RIGHT * 0.3)
        err_group = VGroup(err_box, err_title, err_code)

        self.play(
            FadeIn(ok_group, shift=RIGHT),
            FadeIn(err_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Draw braces showing lifetimes on both sides
        ok_brace = BraceBetweenPoints([-1.8, -0.6, 0], [-1.8, -0.0, 0], color=GREEN)
        ok_lbl = Text("lackierer aktiv", font_size=6.5, color=GREEN).next_to(ok_brace, RIGHT, buff=0.1)
        ok_lifetime_vis = VGroup(ok_brace, ok_lbl)

        err_brace = BraceBetweenPoints([4.8, -1.9, 0], [4.8, -0.6, 0], color=RED)
        err_lbl = Text("lackierer aktiv (Konflikt!)", font_size=6.5, color=RED).next_to(err_brace, RIGHT, buff=0.1)
        err_lifetime_vis = VGroup(err_brace, err_lbl)

        self.play(
            Create(ok_lifetime_vis),
            Create(err_lifetime_vis),
            run_time=1.5
        )
        self.wait(10.0)

        remaining_time = durations["ch19_4_lifetimes"] - 1.0 - 1.0 - 2.0 - 10.0 - 1.5 - 10.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(ok_group),
            FadeOut(err_group),
            FadeOut(ok_lifetime_vis),
            FadeOut(err_lifetime_vis),
            run_time=1.0
        )

        # ==========================================
        # SECTION 5: COPY VS MOVE
        # ==========================================
        self.add_sound("audio/ch19_5_copy_vs_move.wav")

        title_cm = Text("19. Zuweisung: Copy vs. Move bei Referenzen", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_cm), run_time=1.0)
        self.wait(1.0)

        # Split screen: Left (Lese-Ref Copy), Right (Schreib-Ref Move)
        # Left: Copy
        copy_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-3.2, -0.8, 0])
        copy_title = Text("&T: Unveränderliche Ref (Copy)", font_size=11, color=CYAN, weight=BOLD).next_to(copy_box.get_top(), DOWN, buff=0.25)
        copy_code = Paragraph(
            "let kaffee = String::from(\"Mokka\");",
            "let leser1 = &kaffee; // zeigt auf kaffee",
            "let leser2 = leser1;  // Kopie!",
            "",
            "// Beide dürfen gleichzeitig lesen:",
            "println!(\"{} & {}\", leser1, leser2);",
            font="Monospace", font_size=8, line_spacing=0.5
        ).next_to(copy_title, DOWN, buff=0.35).align_to(copy_box, LEFT).shift(RIGHT * 0.3)
        copy_vis = VGroup(
            Text("leser1 (0x55aa) ──► kaffee", font_size=8, color=CYAN),
            Text("leser2 (0x55aa) ──► kaffee", font_size=8, color=CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(copy_code, DOWN, buff=0.35)
        copy_group = VGroup(copy_box, copy_title, copy_code, copy_vis)

        # Right: Move
        move_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=4.2, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.2, -0.8, 0])
        move_title = Text("&mut T: Veränderliche Ref (Move)", font_size=11, color=GREEN, weight=BOLD).next_to(move_box.get_top(), DOWN, buff=0.25)
        move_code = Paragraph(
            "let mut kaffee = String::from(\"Mokka\");",
            "let schreiber1 = &mut kaffee; // Stift 1",
            "let schreiber2 = schreiber1;  // Move!",
            "",
            "// schreiber1 ist ungültig!",
            "// println!(\"{}\", schreiber1); // ❌ Fehler!",
            font="Monospace", font_size=8, line_spacing=0.5
        ).next_to(move_title, DOWN, buff=0.35).align_to(move_box, LEFT).shift(RIGHT * 0.3)
        move_vis = VGroup(
            Text("schreiber1 ──► [INVALD/MOVED]", font_size=8, color=RED),
            Text("schreiber2 (Stift) ──► kaffee (mut)", font_size=8, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(move_code, DOWN, buff=0.35)
        move_group = VGroup(move_box, move_title, move_code, move_vis)

        self.play(
            FadeIn(copy_group, shift=RIGHT),
            FadeIn(move_group, shift=LEFT),
            run_time=2.0
        )
        self.wait(10.0)

        # Cross out schreiber1
        s1_cross = Cross(move_vis[0], stroke_color=RED, stroke_width=2.5, scale_factor=0.9)
        self.play(Create(s1_cross), run_time=1.0)
        self.wait(10.0)

        remaining_time = durations["ch19_5_copy_vs_move"] - 1.0 - 1.0 - 2.0 - 10.0 - 1.0 - 10.0
        self.wait(max(1.0, remaining_time))

        self.play(
            FadeOut(copy_group),
            FadeOut(move_group),
            FadeOut(s1_cross),
            run_time=1.0
        )

        # ==========================================
        # SECTION 6: DANGLING REFERENCES & OUTRO
        # ==========================================
        self.add_sound("audio/ch19_6_dangling_references_outro.wav")

        title_dang = Text("19. Dangling References & Outro", font_size=22, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_dang), run_time=1.0)
        self.wait(1.0)

        # Code showing error
        err_box = RoundedRectangle(corner_radius=0.1, width=10.0, height=2.8, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 0.3, 0])
        err_title = Text("Dangling Reference (Totzeiger) blockiert", font_size=11, color=RED, weight=BOLD).next_to(err_box.get_top(), DOWN, buff=0.25)
        err_console = Paragraph(
            "fn erstelle_stadt() -> &String {",
            "    let stadt = String::from(\"New York\");",
            "    &stadt // ❌ FEHLER: stadt wird am Ende der Funktion gelöscht!",
            "} // ◄── stadt stirbt hier. Adresse zeigt ins Nichts!",
            font="Monospace", font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(err_title, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.4)
        err_group = VGroup(err_box, err_title, err_console)

        self.play(FadeIn(err_group, scale=0.9), run_time=1.5)
        self.wait(8.0)

        # Highlight function end drop
        drop_rect = SurroundingRectangle(err_console[3], color=RED, stroke_width=2)
        warning_msg = Text("Speicher von 'New York' wird am Scope-Ende freigegeben!", font_size=9, color=RED, weight=BOLD).next_to(err_box, DOWN, buff=0.2)
        self.play(Create(drop_rect), FadeIn(warning_msg, shift=UP), run_time=1.0)
        self.wait(8.0)

        # Transition to Outro
        outro_title = Text("Vielen Dank fürs Zuschauen!", font_size=32, color=RUST_ORANGE, weight=BOLD)
        outro_subtitle = Text("Kapitel 19: Referenzen & Borrowing abgeschlossen", font_size=18, color=CYAN).next_to(outro_title, DOWN, buff=0.4)
        outro_group = VGroup(outro_title, outro_subtitle).move_to([0, -0.2, 0])

        # Spin Gear
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
            FadeOut(drop_rect),
            FadeOut(warning_msg),
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )

        spin_time = max(1.0, durations["ch19_6_dangling_references_outro"] - 1.0 - 1.0 - 1.5 - 8.0 - 1.0 - 8.0 - 2.0)
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )
