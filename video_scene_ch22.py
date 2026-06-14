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

class RustPlanningVideo(Scene):
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
            "ch22_1_intro": 35.0,
            "ch22_2_workflow": 35.0,
            "ch22_3_mermaid": 35.0,
            "ch22_4_pseudocode": 35.0,
            "ch22_5_example": 35.0,
            "ch22_6_ai": 35.0,
            "ch22_7_exercise": 35.0,
            "ch22_8_outro": 35.0
        }
        
        durations_path = "audio/durations_ch22.json"
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
        # SECTION 1: INTRO & DIE CODE-FIRST-FALLE
        # ==========================================
        self.add_sound("audio/ch22_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=42, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 22: Der VS Code Planungs-Workflow", font_size=18, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 22: Der VS Code Planungs-Workflow", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Visual comparison: Code-First vs Plan-First
        box_w, box_h = 5.2, 2.0
        
        bad_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=RED, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.2, -0.6, 0])
        bad_title = Text("Der Code-First-Fehler ❌", font_size=12, color=RED, weight=BOLD).next_to(bad_box.get_top(), DOWN, buff=0.25)
        bad_text = Paragraph(
            "- Sofort drauflos tippen\n- Logik & Syntax gleichzeitig lösen\n- Frust durch Compiler-Errors",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(bad_title, DOWN, buff=0.2)
        bad_group = VGroup(bad_box, bad_title, bad_text)

        good_box = RoundedRectangle(corner_radius=0.1, width=box_w, height=box_h, color=GREEN, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.2, -0.6, 0])
        good_title = Text("Der Planungs-Workflow 🟢", font_size=12, color=GREEN, weight=BOLD).next_to(good_box.get_top(), DOWN, buff=0.25)
        good_text = Paragraph(
            "- Erst Logik klären (planung.md)\n- Reine Logikfehler vorab beheben\n- Übersetzen ohne Stress",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(good_title, DOWN, buff=0.2)
        good_group = VGroup(good_box, good_title, good_text)

        comparison = VGroup(bad_group, good_group)
        self.play(FadeIn(comparison, shift=UP), run_time=2.0)

        # Total anim time = 1.5 + 2.5 + 1.5 + 1.0 + 2.0 = 8.5 seconds
        self.wait(get_wait_time("ch22_1_intro", 8.5))

        self.play(FadeOut(comparison), run_time=1.0)

        # ==========================================
        # SECTION 2: DER 5-SCHRITTE-WORKFLOW
        # ==========================================
        self.add_sound("audio/ch22_2_workflow.wav")

        title_steps = Text("22. Die 5 Schritte der Planung", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_steps), run_time=1.0)
        self.wait(1.0)

        # Render 5 timeline blocks
        blocks = VGroup()
        step_texts = [
            "Schritt 1: Anforderungsanalyse (Eingabe, Verarbeitung, Ausgabe)",
            "Schritt 2: Ablauf-Visualisierung (Flussdiagramm mit Mermaid)",
            "Schritt 3: Strukturierter Pseudocode (in planung.md)",
            "Schritt 4: Implementierungs-To-Do-Liste (Checkliste)",
            "Schritt 5: Iterative Codierung & Refactoring in Rust"
        ]
        colors = [CYAN, PURPLE, YELLOW, GREEN, RUST_ORANGE]
        
        for i, (text, col) in enumerate(zip(step_texts, colors)):
            bar = Rectangle(width=11.0, height=0.45, color=col, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, 1.2 - i*0.8, 0])
            lbl = Text(text, font_size=10, color=WHITE).move_to(bar.get_center())
            blocks.add(VGroup(bar, lbl))

        self.play(LaggedStart(*(FadeIn(b, shift=RIGHT) for b in blocks), lag_ratio=0.3), run_time=2.5)
        self.wait(2.0)

        # Total anim time = 1.0 + 1.0 + 2.5 + 2.0 = 6.5 seconds
        self.wait(get_wait_time("ch22_2_workflow", 6.5))

        self.play(FadeOut(blocks), run_time=1.0)

        # ==========================================
        # SECTION 3: ABLAUF-VISUALISIERUNG & MERMAID
        # ==========================================
        self.add_sound("audio/ch22_3_mermaid.wav")

        title_mermaid = Text("22. Ablauf-Visualisierung & Mermaid-Syntax", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_mermaid), run_time=1.0)
        self.wait(1.0)

        # Show Mermaid elements
        card_w, card_h = 2.6, 2.6
        cards = VGroup()
        mermaid_elements = [
            ("Start / Ende", "Oval\n\n`Start([Start])`", CYAN, [-3.9, -0.6, 0]),
            ("Aktion / Zuweisung", "Rechteck\n\n`Init[x = 0]`", PURPLE, [-1.3, -0.6, 0]),
            ("Entscheidung", "Raute\n\n`Check{x > 5?}`", YELLOW, [1.3, -0.6, 0]),
            ("Ein- / Ausgabe", "Parallelogramm\n\n`Out[\\Gib x/]`", GREEN, [3.9, -0.6, 0])
        ]

        for name, syntax, col, pos in mermaid_elements:
            box = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=col, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=1.5).move_to(pos)
            c_title = Text(name, font_size=9, color=col, weight=BOLD).next_to(box.get_top(), DOWN, buff=0.25)
            c_desc = Paragraph(syntax, font_size=7.5, color=WHITE).next_to(c_title, DOWN, buff=0.3)
            cards.add(VGroup(box, c_title, c_desc))

        self.play(FadeIn(cards, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_3_mermaid", 7.0))

        self.play(FadeOut(cards), run_time=1.0)

        # ==========================================
        # SECTION 4: PSEUDOCODE & TROCKENLAUF
        # ==========================================
        self.add_sound("audio/ch22_4_pseudocode.wav")

        title_pseudo = Text("22. Strukturierter Pseudocode & Trockenlauf", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_pseudo), run_time=1.0)
        self.wait(1.0)

        # Display Pseudocode Box and rules side by side
        p_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.0, -0.6, 0])
        p_title = Text("Pseudocode-Muster", font_size=11, color=CYAN, weight=BOLD).next_to(p_box.get_top(), DOWN, buff=0.2)
        p_code = Paragraph(
            "FUNKTION main:",
            "  DEFINIERE x = 10",
            "  WIEDERHOLE solange x > 0:",
            "    GIB AUS x",
            "    x = x - 1",
            "ENDE FUNKTION",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(p_title, DOWN, buff=0.3).align_to(p_box, LEFT).shift(RIGHT * 0.4)
        p_group = VGroup(p_box, p_title, p_code)

        r_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.6, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.0, -0.6, 0])
        r_title = Text("Der Trockenlauf (Desk Checking)", font_size=11, color=YELLOW, weight=BOLD).next_to(r_box.get_top(), DOWN, buff=0.2)
        r_rules = Paragraph(
            "- Logik-Simulation im Kopf\n- Nimm ein Blatt Papier\n- Trage Variablenwerte ein\n- Verhindert 'Off-by-one'-Fehler\n- Findet Endlosschleifen vorab",
            font_size=8.5, color=WHITE, line_spacing=0.4
        ).next_to(r_title, DOWN, buff=0.3).align_to(r_box, LEFT).shift(RIGHT * 0.4)
        r_group = VGroup(r_box, r_title, r_rules)

        self.play(FadeIn(p_group, shift=LEFT), FadeIn(r_group, shift=RIGHT), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_4_pseudocode", 7.0))

        self.play(FadeOut(p_group), FadeOut(r_group), run_time=1.0)

        # ==========================================
        # SECTION 5: PRAXISBEISPIEL: NOTENDURCHSCHNITT
        # ==========================================
        self.add_sound("audio/ch22_5_example.wav")

        title_example = Text("22. Praxisbeispiel: Notendurchschnitt-Rechner", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_example), run_time=1.0)
        self.wait(1.0)

        # Left: Mermaid snippet
        left_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.6, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.0, -0.6, 0])
        left_title = Text("Visueller Ablauf", font_size=11, color=PURPLE, weight=BOLD).next_to(left_box.get_top(), DOWN, buff=0.2)
        left_desc = Paragraph(
            "Start: notendurchschnitt = [1, 2, 4, 5, 2]\n\n"
            "Schleife:\n"
            "  Hole nächste Note aus Array\n"
            "  Addiere Note zu Summe\n\n"
            "Ende:\n"
            "  Durchschnitt = Summe / Anzahl\n"
            "  Ausgabe Durchschnitt",
            font_size=8, color=WHITE, line_spacing=0.4
        ).next_to(left_title, DOWN, buff=0.3).align_to(left_box, LEFT).shift(RIGHT * 0.4)
        left_group = VGroup(left_box, left_title, left_desc)

        # Right: Rust Implementation
        right_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.6, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.0, -0.6, 0])
        right_title = Text("Implementierung in Rust", font_size=11, color=GREEN, weight=BOLD).next_to(right_box.get_top(), DOWN, buff=0.2)
        right_code = Paragraph(
            "let noten = [1, 2, 4, 5, 2];\n"
            "let mut summe = 0.0;\n"
            "let anzahl = noten.len() as f64;\n\n"
            "for note in noten.iter() {\n"
            "    summe += *note as f64;\n"
            "}\n\n"
            "let schnitt = summe / anzahl;\n"
            "println!(\"Schnitt: {:.2}\", schnitt);",
            font_size=7.5, color=WHITE, line_spacing=0.2
        ).next_to(right_title, DOWN, buff=0.3).align_to(right_box, LEFT).shift(RIGHT * 0.4)
        right_group = VGroup(right_box, right_title, right_code)

        self.play(FadeIn(left_group, shift=LEFT), FadeIn(right_group, shift=RIGHT), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_5_example", 7.0))

        self.play(FadeOut(left_group), FadeOut(right_group), run_time=1.0)

        # ==========================================
        # SECTION 6: KI ALS PARTNER (AI-ASSISTED PLANNING)
        # ==========================================
        self.add_sound("audio/ch22_6_ai.wav")

        title_ai = Text("22. KI-Assistenten im Planungs-Workflow", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_ai), run_time=1.0)
        self.wait(1.0)

        # Three steps for using AI in planning
        c1 = RoundedRectangle(corner_radius=0.1, width=3.6, height=3.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-4.0, -0.4, 0])
        c1_title = Text("1. Anforderungen", font_size=12, color=CYAN, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.25)
        c1_desc = Paragraph(
            "- Frage nach Edge Cases\n- Kläre Unklarheiten\n- EVA-Schema prüfen",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c1_title, DOWN, buff=0.3)
        c1_group = VGroup(c1, c1_title, c1_desc)

        c2 = RoundedRectangle(corner_radius=0.1, width=3.6, height=3.2, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        c2_title = Text("2. Logik-Check", font_size=12, color=YELLOW, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.25)
        c2_desc = Paragraph(
            "- Mermaid entwerfen\n- Pseudocode-Review\n- Logische Fehler finden",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c2_title, DOWN, buff=0.3)
        c2_group = VGroup(c2, c2_title, c2_desc)

        c3 = RoundedRectangle(corner_radius=0.1, width=3.6, height=3.2, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([4.0, -0.4, 0])
        c3_title = Text("3. Dokumentation", font_size=12, color=GREEN, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.25)
        c3_desc = Paragraph(
            "- Vorschläge vergleichen\n- In planung.md sammeln\n- Bewusst entscheiden",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(c3_title, DOWN, buff=0.3)
        c3_group = VGroup(c3, c3_title, c3_desc)

        self.play(
            FadeIn(c1_group, shift=UP),
            FadeIn(c2_group, shift=UP),
            FadeIn(c3_group, shift=UP),
            run_time=2.0
        )
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_6_ai", 7.0))

        self.play(FadeOut(c1_group), FadeOut(c2_group), FadeOut(c3_group), run_time=1.0)

        # ==========================================
        # SECTION 7: ÜBUNGSAUFGABE (WARENKORB-REHNER)
        # ==========================================
        self.add_sound("audio/ch22_7_exercise.wav")

        title_exercise = Text("22. Deine Übung: Warenkorb-Rabatt-Rechner", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_exercise), run_time=1.0)
        self.wait(1.0)

        # Requirements Card for Warenkorb-Rabatt-Rechner
        ex_box = RoundedRectangle(corner_radius=0.1, width=9.2, height=3.4, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.5, 0])
        ex_title = Text("Die Anforderungen:", font_size=12, color=YELLOW, weight=BOLD).next_to(ex_box.get_top(), DOWN, buff=0.25)
        ex_bullets = Paragraph(
            "1. Array mit 5 Preisen: `let preise = [12.50, 8.90, 24.00, 15.00, 5.50];`\n"
            "2. Berechne die Summe aller Preise.\n"
            "3. Falls Summe > 50.00 €, ziehe 10% Rabatt ab.\n"
            "4. Schlage 19% Mehrwertsteuer auf den rabattierten Betrag auf.\n"
            "5. Gib Netto-Summe, Rabattbetrag, MwSt und Brutto-Endpreis aus.",
            font_size=9, color=WHITE, line_spacing=0.5
        ).next_to(ex_title, DOWN, buff=0.3).align_to(ex_box, LEFT).shift(RIGHT * 0.5)
        ex_group = VGroup(ex_box, ex_title, ex_bullets)

        self.play(FadeIn(ex_group, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_7_exercise", 7.0))

        self.play(FadeOut(ex_group), run_time=1.0)

        # ==========================================
        # SECTION 8: OUTRO
        # ==========================================
        self.add_sound("audio/ch22_8_outro.wav")

        title_outro = Text("22. Zusammenfassung & Ausblick", font_size=20, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Summary box
        out_box = RoundedRectangle(corner_radius=0.1, width=8.0, height=3.0, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.4, 0])
        out_title = Text("Das nimmst du mit:", font_size=12, color=GREEN, weight=BOLD).next_to(out_box.get_top(), DOWN, buff=0.25)
        out_text = Paragraph(
            "- Plane stets vor dem Schreiben von Code!\n"
            "- Mermaid & Pseudocode helfen dir, Logikfehler zu vermeiden.\n"
            "- Die To-Do-Liste leitet dich strukturiert ans Ziel.\n"
            "- Nutze KIs als Mentoren und nicht als Abkürzung.",
            font_size=9, color=WHITE, line_spacing=0.4
        ).next_to(out_title, DOWN, buff=0.3).align_to(out_box, LEFT).shift(RIGHT * 0.5)
        out_group = VGroup(out_box, out_title, out_text)

        self.play(FadeIn(out_group, shift=UP), run_time=2.0)
        self.wait(3.0)

        # Total anim time = 1.0 + 1.0 + 2.0 + 3.0 = 7.0 seconds
        self.wait(get_wait_time("ch22_8_outro", 7.0))

        # Final fade out
        self.play(FadeOut(out_group), FadeOut(title_group), run_time=1.0)
        self.wait(1.0)
