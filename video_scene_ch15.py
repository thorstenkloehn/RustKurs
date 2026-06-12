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

class RustControlStructuresVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 24.66s)
        # ==========================================
        self.add_sound("audio/ch15_1_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 15: Kontrollstrukturen", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 15: Kontrollstrukturen", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s
        self.wait(0.5)  # total 5.0s

        # 5.0s - 8.0s: Draw control structures split diagram
        split_node = RoundedRectangle(corner_radius=0.1, width=3.2, height=0.8, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([0, 1.2, 0])
        split_text = Text("Kontrollstrukturen", font_size=12, color=PURPLE, weight=BOLD).move_to(split_node.get_center())
        split_group = VGroup(split_node, split_text)

        dec_node = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-2.5, -0.4, 0])
        dec_text = Text("Entscheidungen\n(if, match)", font_size=10, color=CYAN, weight=BOLD).move_to(dec_node.get_center())
        dec_group = VGroup(dec_node, dec_text)

        loop_node = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([2.5, -0.4, 0])
        loop_text = Text("Wiederholungen\n(loop, while, for)", font_size=10, color=GREEN, weight=BOLD).move_to(loop_node.get_center())
        loop_group = VGroup(loop_node, loop_text)

        arrow_dec = Arrow(start=[0, 0.8, 0], end=[-2.5, 0.0, 0], stroke_width=3, color=GRAY)
        arrow_loop = Arrow(start=[0, 0.8, 0], end=[2.5, 0.0, 0], stroke_width=3, color=GRAY)

        dia_group = VGroup(split_group, dec_group, loop_group, arrow_dec, arrow_loop)
        self.play(
            FadeIn(split_group, shift=DOWN),
            Create(arrow_dec),
            Create(arrow_loop),
            FadeIn(dec_group, shift=RIGHT),
            FadeIn(loop_group, shift=LEFT),
            run_time=2.0
        )  # total 7.0s
        self.wait(1.0)  # total 8.0s

        # 8.0s - 15.0s: Bullet points detailing practical usage
        bullets = VGroup(
            Text("• Benutzereingaben prüfen & steuern", font_size=13, color=WHITE),
            Text("• Zustandsmaschinen & Spielabläufe lenken", font_size=13, color=WHITE),
            Text("• Datenströme & Listen verarbeiten", font_size=13, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.8, 0])

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 13.0s

        # Wait for the audio segment to complete (24.66s)
        self.wait(24.66 - 13.0 - 1.0)  # total 23.66s
        self.play(
            FadeOut(dia_group),
            FadeOut(bullets),
            run_time=1.0
        )  # total 24.66s


        # ==========================================
        # SECTION 2: EXPRESSIONS VS STATEMENTS (Duration: 22.49s)
        # ==========================================
        self.add_sound("audio/ch15_2_expressions.wav")

        title_expr = Text("15. Ausdrücke vs. Anweisungen", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_expr), run_time=1.0)  # total 1.0s
        self.wait(1.0)  # total 2.0s

        # Statements Card (Left)
        stmt_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=RED, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.2, -0.6, 0])
        stmt_title = Text("Anweisungen (Statements)", font_size=13, color=RED, weight=BOLD).next_to(stmt_rect.get_top(), DOWN, buff=0.3)
        stmt_list = VGroup(
            Text("• Führen eine Aktion aus", font_size=11, color=WHITE),
            Text("• Liefern keinen Wert zurück", font_size=11, color=WHITE),
            Text("• Enden fast immer mit ;", font_size=11, color=WHITE),
            Text("Beispiel:\nlet x = 5;", font_size=11, color=GRAY, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(stmt_title, DOWN, buff=0.4)
        stmt_group = VGroup(stmt_rect, stmt_title, stmt_list)

        # Expressions Card (Right)
        expr_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.2, -0.6, 0])
        expr_title = Text("Ausdrücke (Expressions)", font_size=13, color=GREEN, weight=BOLD).next_to(expr_rect.get_top(), DOWN, buff=0.3)
        expr_list = VGroup(
            Text("• Berechnen ein Ergebnis", font_size=11, color=WHITE),
            Text("• Geben einen Wert zurück", font_size=11, color=WHITE),
            Text("• Enden OHNE Semikolon", font_size=11, color=WHITE),
            Text("Beispiel:\n5 + 5", font_size=11, color=CYAN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(expr_title, DOWN, buff=0.4)
        expr_group = VGroup(expr_rect, expr_title, expr_list)

        self.play(
            FadeIn(stmt_group, shift=RIGHT),
            FadeIn(expr_group, shift=LEFT),
            run_time=2.0
        )  # total 4.0s
        self.wait(6.0)  # total 10.0s

        # Highlight Expression Code
        highlight_box = SurroundingRectangle(expr_list[3], color=YELLOW, buff=0.1, stroke_width=2)
        self.play(Create(highlight_box), run_time=1.0)
        self.wait(3.0)  # total 14.0s

        # Wait for speech to complete
        self.wait(22.49 - 14.0 - 1.0)  # total 21.49s
        self.play(
            FadeOut(stmt_group),
            FadeOut(expr_group),
            FadeOut(highlight_box),
            run_time=1.0
        )  # total 22.49s


        # ==========================================
        # SECTION 3: DECISIONS WITH IF/ELSE (Duration: 19.01s)
        # ==========================================
        self.add_sound("audio/ch15_3_if_else.wav")

        title_if = Text("15. Entscheidungen mit if und else", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_if), run_time=1.0)  # total 1.0s
        self.wait(1.0)  # total 2.0s

        # Code Window for if expression
        code_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=3.8, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        code_title = Text("if-Bedingung als Ausdruck (Expression)", font_size=13, color=CYAN, weight=BOLD).next_to(code_rect.get_top(), DOWN, buff=0.3)
        
        code_content = VGroup(
            Text("let bedingung = true;", font_size=11, color=GRAY, font="Monospace"),
            Text("let nummer = if bedingung {", font_size=11, color=WHITE, font="Monospace"),
            Text("    5  // Zurückgegebener Wert 1", font_size=11, color=GREEN, font="Monospace"),
            Text("} else {", font_size=11, color=WHITE, font="Monospace"),
            Text("    6  // Zurückgegebener Wert 2 (Gleicher Typ!)", font_size=11, color=GREEN, font="Monospace"),
            Text("};", font_size=11, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(code_title, DOWN, buff=0.3)
        code_group = VGroup(code_rect, code_title, code_content)

        self.play(FadeIn(code_group, scale=0.9), run_time=1.5)  # total 3.5s
        self.wait(4.5)  # total 8.0s

        # Highlight matching return types
        type_highlight1 = SurroundingRectangle(code_content[2], color=YELLOW, buff=0.08, stroke_width=1.5)
        type_highlight2 = SurroundingRectangle(code_content[4], color=YELLOW, buff=0.08, stroke_width=1.5)
        
        self.play(
            Create(type_highlight1),
            Create(type_highlight2),
            run_time=1.0
        )  # total 9.0s
        self.wait(4.0)  # total 13.0s

        # Wait for audio to finish
        self.wait(19.01 - 13.0 - 1.0)  # total 18.01s
        self.play(
            FadeOut(code_group),
            FadeOut(type_highlight1),
            FadeOut(type_highlight2),
            run_time=1.0
        )  # total 19.01s


        # ==========================================
        # SECTION 4: PATTERN MATCHING WITH MATCH (Duration: 20.71s)
        # ==========================================
        self.add_sound("audio/ch15_4_match.wav")

        title_match = Text("15. Musterabgleich mit match", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_match), run_time=1.0)  # total 1.0s
        self.wait(1.0)  # total 2.0s

        # Match Pattern Box
        match_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        match_title = Text("match wuerfel { ... }", font_size=13, color=PURPLE, weight=BOLD).next_to(match_rect.get_top(), DOWN, buff=0.3)
        
        match_arms = VGroup(
            Text("match wuerfel {", font_size=11, color=WHITE, font="Monospace"),
            Text("    1 => println!(\"Eins gewürfelt!\"),", font_size=11, color=CYAN, font="Monospace"),
            Text("    2 => println!(\"Zwei gewürfelt!\"),", font_size=11, color=CYAN, font="Monospace"),
            Text("    3 => println!(\"Drei gewürfelt!\"),", font_size=11, color=CYAN, font="Monospace"),
            Text("    _ => println!(\"Anderer Wert!\"), // Platzhalter fängt alles ab", font_size=11, color=GREEN, font="Monospace"),
            Text("}", font_size=11, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(match_title, DOWN, buff=0.3)
        match_group = VGroup(match_rect, match_title, match_arms)

        self.play(FadeIn(match_group, scale=0.9), run_time=1.5)  # total 3.5s
        self.wait(4.5)  # total 8.0s

        # Highlight exhaustiveness rule (Vollständigkeit)
        exhaust_rect = SurroundingRectangle(match_arms[4], color=YELLOW, buff=0.08, stroke_width=1.5)
        exhaust_text = Text("Vollständigkeit (Exhaustiveness) wird erzwungen!", font_size=11, color=YELLOW, weight=BOLD).next_to(match_rect, DOWN, buff=0.2)
        
        self.play(
            Create(exhaust_rect),
            FadeIn(exhaust_text, shift=UP),
            run_time=1.5
        )  # total 9.5s
        self.wait(5.0)  # total 14.5s

        # Wait for audio to finish
        self.wait(20.71 - 14.5 - 1.0)  # total 19.71s
        self.play(
            FadeOut(match_group),
            FadeOut(exhaust_rect),
            FadeOut(exhaust_text),
            run_time=1.0
        )  # total 20.71s


        # ==========================================
        # SECTION 5: LOOP & WHILE (Duration: 23.38s)
        # ==========================================
        self.add_sound("audio/ch15_5_loop_while.wav")

        title_loop_while = Text("15. Schleifen: loop und while", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_loop_while), run_time=1.0)  # total 1.0s
        self.wait(1.0)  # total 2.0s

        # Left Card (loop)
        l_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.2, -0.6, 0])
        l_title = Text("loop (Endlosschleife)", font_size=13, color=CYAN, weight=BOLD).next_to(l_rect.get_top(), DOWN, buff=0.3)
        l_code = VGroup(
            Text("let ergebnis = loop {", font_size=10, color=WHITE, font="Monospace"),
            Text("    zaehler += 1;", font_size=10, color=GRAY, font="Monospace"),
            Text("    if zaehler == 10 {", font_size=10, color=WHITE, font="Monospace"),
            Text("        break zaehler * 2;", font_size=10, color=GREEN, font="Monospace"),
            Text("    }", font_size=10, color=WHITE, font="Monospace"),
            Text("};", font_size=10, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(l_title, DOWN, buff=0.3)
        l_group = VGroup(l_rect, l_title, l_code)

        # Right Card (while)
        w_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.2, -0.6, 0])
        w_title = Text("while (Bedingte Schleife)", font_size=13, color=GREEN, weight=BOLD).next_to(w_rect.get_top(), DOWN, buff=0.3)
        w_code = VGroup(
            Text("while countdown > 0 {", font_size=10, color=WHITE, font="Monospace"),
            Text("    println!(\"{}...\", countdown);", font_size=10, color=GRAY, font="Monospace"),
            Text("    countdown -= 1;", font_size=10, color=GRAY, font="Monospace"),
            Text("}", font_size=10, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(w_title, DOWN, buff=0.4)
        w_group = VGroup(w_rect, w_title, w_code)

        self.play(
            FadeIn(l_group, shift=RIGHT),
            FadeIn(w_group, shift=LEFT),
            run_time=2.0
        )  # total 4.0s
        self.wait(5.0)  # total 9.0s

        # Highlight loop return value and while condition
        break_highlight = SurroundingRectangle(l_code[3], color=YELLOW, buff=0.08, stroke_width=1.5)
        cond_highlight = SurroundingRectangle(w_code[0], color=YELLOW, buff=0.08, stroke_width=1.5)
        
        self.play(
            Create(break_highlight),
            Create(cond_highlight),
            run_time=1.0
        )  # total 10.0s
        self.wait(6.0)  # total 16.0s

        # Wait for audio to finish
        self.wait(23.38 - 16.0 - 1.0)  # total 22.38s
        self.play(
            FadeOut(l_group),
            FadeOut(w_group),
            FadeOut(break_highlight),
            FadeOut(cond_highlight),
            run_time=1.0
        )  # total 23.38s


        # ==========================================
        # SECTION 6: FOR & LABELS (Duration: 22.78s)
        # ==========================================
        self.add_sound("audio/ch15_6_for_labels.wav")

        title_for_labels = Text("15. Zählschleifen & Schleifen-Labels", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_for_labels), run_time=1.0)  # total 1.0s
        self.wait(1.0)  # total 2.0s

        # Left Card (for loops)
        for_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.2, -0.6, 0])
        for_title = Text("for (Sicher & Schnell)", font_size=13, color=CYAN, weight=BOLD).next_to(for_rect.get_top(), DOWN, buff=0.3)
        for_code = VGroup(
            Text("// Bereich (Range)", font_size=10, color=GRAY, font="Monospace"),
            Text("for i in 1..=4 { ... }", font_size=10, color=WHITE, font="Monospace"),
            Text("", font_size=5),
            Text("// Array-Iterator (Sicher!)", font_size=10, color=GRAY, font="Monospace"),
            Text("for tag in tage.iter() { ... }", font_size=10, color=GREEN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(for_title, DOWN, buff=0.4)
        for_group = VGroup(for_rect, for_title, for_code)

        # Right Card (loop labels)
        lbl_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=4.0, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.2, -0.6, 0])
        lbl_title = Text("Schleifen-Labels (Benennung)", font_size=13, color=PURPLE, weight=BOLD).next_to(lbl_rect.get_top(), DOWN, buff=0.3)
        lbl_code = VGroup(
            Text("'aeusserer: loop {", font_size=10, color=GREEN, font="Monospace"),
            Text("    loop {", font_size=10, color=WHITE, font="Monospace"),
            Text("        // Bricht äußere Schleife ab!", font_size=9, color=GRAY, font="Monospace"),
            Text("        break 'aeusserer;", font_size=10, color=GREEN, font="Monospace"),
            Text("    }", font_size=10, color=WHITE, font="Monospace"),
            Text("}", font_size=10, color=WHITE, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(lbl_title, DOWN, buff=0.3)
        lbl_group = VGroup(lbl_rect, lbl_title, lbl_code)

        self.play(
            FadeIn(for_group, shift=RIGHT),
            FadeIn(lbl_group, shift=LEFT),
            run_time=2.0
        )  # total 4.0s
        self.wait(5.0)  # total 9.0s

        # Highlight iterator and labels
        iter_hl = SurroundingRectangle(for_code[4], color=YELLOW, buff=0.08, stroke_width=1.5)
        label_hl1 = SurroundingRectangle(lbl_code[0], color=YELLOW, buff=0.08, stroke_width=1.5)
        label_hl2 = SurroundingRectangle(lbl_code[3], color=YELLOW, buff=0.08, stroke_width=1.5)

        self.play(
            Create(iter_hl),
            Create(label_hl1),
            Create(label_hl2),
            run_time=1.0
        )  # total 10.0s
        self.wait(6.0)  # total 16.0s

        # Wait for audio to finish
        self.wait(22.78 - 16.0 - 1.0)  # total 21.78s
        self.play(
            FadeOut(for_group),
            FadeOut(lbl_group),
            FadeOut(iter_hl),
            FadeOut(label_hl1),
            FadeOut(label_hl2),
            run_time=1.0
        )  # total 22.78s


        # ==========================================
        # SECTION 7: OUTRO (Duration: 11.73s)
        # ==========================================
        self.add_sound("audio/ch15_7_outro.wav")

        # Transition to Outro Title
        outro_title = Text("Vielen Dank fürs Zuschauen!", font_size=32, color=RUST_ORANGE, weight=BOLD)
        outro_subtitle = Text("Viel Erfolg beim Rust programmieren!", font_size=18, color=CYAN).next_to(outro_title, DOWN, buff=0.4)
        outro_group = VGroup(outro_title, outro_subtitle).move_to([0, 0, 0])

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
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )  # total 2.0s

        spin_time = 11.73 - 2.0 - 1.0  # spin_time is 8.73s
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)  # total 10.73s

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )  # total 11.73s
