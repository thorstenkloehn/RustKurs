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
LIGHT_BG = "#1e293b"      # slate-800 for card backgrounds

class RustIntroVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 28.37s)
        # ==========================================
        self.add_sound("audio/intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 1: Was ist Rust?", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 1: Was ist Rust?", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s

        # 4.5s - 6s: Create Gear
        gear_center = Circle(radius=1.1, color=RUST_ORANGE, stroke_width=8)
        teeth = VGroup()
        num_teeth = 12
        for i in range(num_teeth):
            angle = i * (360 / num_teeth) * DEGREES
            tooth = Rectangle(width=0.35, height=0.45, color=RUST_ORANGE, fill_opacity=1, stroke_width=0)
            tooth.move_to(gear_center.get_center())
            tooth.shift(1.2 * np.array([np.cos(angle), np.sin(angle), 0]))
            tooth.rotate(angle)
            teeth.add(tooth)
        inner_circle = Circle(radius=0.45, color=BG_COLOR, stroke_width=0, fill_opacity=1)
        gear = VGroup(gear_center, teeth, inner_circle)
        
        self.play(Create(gear), run_time=1.5)  # total 6.0s
        
        # Add continuous rotation to the gear
        gear.add_updater(lambda m, dt: m.rotate(-0.25 * dt))

        # 6s - 7.5s: Shift Gear Left
        self.play(gear.animate.shift(LEFT * 3.5), run_time=1.5)  # total 7.5s

        # Bullets Group (Right)
        bullet1 = Text("• Außergewöhnliche Geschwindigkeit", font_size=22, color=WHITE)
        bullet2 = Text("• Hohe Zuverlässigkeit", font_size=22, color=WHITE)
        bullet3 = Text("• Garantierte Speichersicherheit", font_size=22, color=WHITE)
        bullets = VGroup(bullet1, bullet2, bullet3).arrange(DOWN, aligned_edge=LEFT, buff=0.6).shift(RIGHT * 1.5 + UP * 0.5)

        # 7.5s - 9s: Wait before Bullet 1
        self.wait(1.5)  # total 9.0s

        # 9s - 10s: Show Bullet 1
        self.play(FadeIn(bullet1, shift=RIGHT), run_time=1.0)  # total 10.0s

        # 10s - 13s: Wait before Bullet 2
        self.wait(3.0)  # total 13.0s

        # 13s - 14s: Show Bullet 2
        self.play(FadeIn(bullet2, shift=RIGHT), run_time=1.0)  # total 14.0s

        # 14s - 18s: Wait before Bullet 3
        self.wait(4.0)  # total 18.0s

        # 18s - 19s: Show Bullet 3
        self.play(FadeIn(bullet3, shift=RIGHT), run_time=1.0)  # total 19.0s

        # 19s - 21s: Wait before Highlight Box
        self.wait(2.0)  # total 21.0s

        # 21s - 22.5s: Show Compiler Highlight Box
        highlight_box = RoundedRectangle(corner_radius=0.15, width=5.5, height=1.1, color=PURPLE, fill_color=PURPLE, fill_opacity=0.15, stroke_width=2).shift(DOWN * 2.0 + RIGHT * 1.5)
        highlight_text = Text("Direkt zur Kompilierzeit gelöst\ndurch das Ownership-System!", font_size=16, color=PURPLE, weight=BOLD)
        highlight_text.move_to(highlight_box.get_center())
        
        self.play(FadeIn(highlight_box), FadeIn(highlight_text), run_time=1.5)  # total 22.5s

        # 22.5s - 27.37s: Wait for intro audio to end
        self.wait(27.37 - 22.5)  # total 27.37s

        # 27.37s - 28.37s: Transition (FadeOut)
        self.play(
            FadeOut(title_group),
            FadeOut(gear),
            FadeOut(bullets),
            FadeOut(highlight_box),
            FadeOut(highlight_text),
            run_time=1.0
        )  # total 28.37s

        # Remove updater from gear to clean up memory
        gear.clear_updaters()

        # ==========================================
        # SECTION 2: VERGLEICH (Duration: 30.85s)
        # ==========================================
        self.add_sound("audio/vergleich.wav")

        # 0s - 1.0s: Section Title
        v_title = Text("Rust im Vergleich", font_size=32, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(v_title, shift=UP), run_time=1.0)  # total 1.0s
        
        # 1.0s - 2.5s: Shift Title Up and create axes
        # Setup graph axes manually for complete visual control
        origin = [-3.5, -2.2, 0]
        x_axis = Arrow(start=origin, end=[3.8, -2.2, 0], color=GRAY, stroke_width=4, tip_length=0.25)
        y_axis = Arrow(start=origin, end=[-3.5, 2.6, 0], color=GRAY, stroke_width=4, tip_length=0.25)
        x_label = Text("Geschwindigkeit & Performance", font_size=16, color=GRAY).next_to(x_axis, DOWN, buff=0.2)
        y_label = Text("Sicherheit", font_size=16, color=GRAY).next_to(y_axis, LEFT, buff=0.2).rotate(90 * DEGREES)
        
        self.play(
            Create(x_axis), Create(y_axis),
            FadeIn(x_label), FadeIn(y_label),
            run_time=1.5
        )  # total 2.5s

        # 2.5s - 6.0s: Wait before C/C++
        self.wait(3.5)  # total 6.0s

        # 6.0s - 7.0s: Plot C/C++ (High speed, Low safety)
        cpp_pos = [2.5, -1.2, 0]
        cpp_dot = Dot(point=cpp_pos, color=RED, radius=0.18)
        cpp_label = Text("C / C++\n(Manuelle Speicherverwaltung)", font_size=14, color=RED).next_to(cpp_dot, UP+LEFT, buff=0.1)
        self.play(
            GrowFromCenter(cpp_dot),
            FadeIn(cpp_label, shift=UP),
            run_time=1.0
        )  # total 7.0s

        # 7.0s - 12.0s: Wait before Python
        self.wait(5.0)  # total 12.0s

        # 12.0s - 13.0s: Plot Python (Low speed, High safety)
        py_pos = [-2.0, 1.8, 0]
        py_dot = Dot(point=py_pos, color=CYAN, radius=0.18)
        py_label = Text("Python\n(Garbage Collector / Interpretiert)", font_size=14, color=CYAN).next_to(py_dot, DOWN+RIGHT, buff=0.1)
        self.play(
            GrowFromCenter(py_dot),
            FadeIn(py_label, shift=DOWN),
            run_time=1.0
        )  # total 13.0s

        # 13.0s - 18.0s: Wait before Rust
        self.wait(5.0)  # total 18.0s

        # 18.0s - 19.5s: Plot Rust (High speed, High safety)
        rust_pos = [2.5, 1.8, 0]
        rust_dot = Dot(point=rust_pos, color=RUST_ORANGE, radius=0.2)
        rust_label = Text("Rust\n(Ownership & Borrowing)", font_size=15, color=RUST_ORANGE, weight=BOLD).next_to(rust_dot, DOWN+LEFT, buff=0.15)
        
        # Let's animate a pulsing ring around Rust dot for emphasis
        pulse_ring = Circle(radius=0.2, color=RUST_ORANGE, stroke_width=2).move_to(rust_pos)
        
        self.play(
            GrowFromCenter(rust_dot),
            FadeIn(rust_label, shift=UP),
            pulse_ring.animate.scale(3.5).set_opacity(0),
            run_time=1.5
        )  # total 19.5s

        # 19.5s - 24.5s: Wait before Highlight Box
        self.wait(5.0)  # total 24.5s

        # 24.5s - 26.0s: Dashed Box and Text: Best of both worlds
        rect_to_dash = Rectangle(width=3.6, height=2.4, color=RUST_ORANGE, stroke_width=2).move_to([1.5, 1.2, 0])
        dashed_box = DashedVMobject(rect_to_dash, num_dashes=30)
        best_text = Text("Das Beste aus beiden Welten!", font_size=18, color=RUST_ORANGE, weight=BOLD).next_to(dashed_box, DOWN, buff=0.2)
        self.play(
            Create(dashed_box),
            FadeIn(best_text, shift=UP),
            run_time=1.5
        )  # total 26.0s

        # 26.0s - 29.85s: Wait for Vergleich audio to end
        self.wait(29.85 - 26.0)  # total 29.85s

        # 29.85s - 30.85s: Transition (FadeOut)
        self.play(
            FadeOut(v_title), FadeOut(x_axis), FadeOut(y_axis),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(cpp_dot), FadeOut(cpp_label),
            FadeOut(py_dot), FadeOut(py_label),
            FadeOut(rust_dot), FadeOut(rust_label),
            FadeOut(dashed_box), FadeOut(best_text),
            run_time=1.0
        )  # total 30.85s

        # ==========================================
        # SECTION 2.5: EINSATZGEBIETE (Duration: 39.98s)
        # ==========================================
        self.add_sound("audio/einsatzgebiete.wav")

        # 0s - 1.0s: Section Title
        e_title = Text("Einsatzgebiete im IT-Sektor", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(e_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Wait/Prepare Cards
        card_w, card_h = 3.8, 4.4
        e_card1 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-4.2, -0.6, 0])
        e_card2 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([0, -0.6, 0])
        e_card3 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([4.2, -0.6, 0])

        ec1_title = Text("Systeme & OS", font_size=16, color=RED, weight=BOLD).next_to(e_card1.get_top(), DOWN, buff=0.3)
        ec1_desc = Paragraph(
            "• Android (Google)",
            "  System-Dienste",
            "• Windows (Microsoft)",
            "  Kernel-Komponenten",
            "• Linux Kernel",
            "  Offizielle Integration",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(ec1_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        ec2_title = Text("Cloud & Netzwerk", font_size=16, color=CYAN, weight=BOLD).next_to(e_card2.get_top(), DOWN, buff=0.3)
        ec2_desc = Paragraph(
            "• AWS (Amazon)",
            "  Firecracker microVM",
            "• Cloudflare Edge",
            "  Proxy-Infrastruktur",
            "• Hohe Effizienz",
            "  Senkt Serverkosten",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(ec2_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        ec3_title = Text("Web-Tools & Wasm", font_size=16, color=PURPLE, weight=BOLD).next_to(e_card3.get_top(), DOWN, buff=0.3)
        ec3_desc = Paragraph(
            "• Next.js Compiler",
            "  SWC & Turbopack",
            "• Deno Runtime",
            "  JS/TS Engine",
            "• WebAssembly",
            "  Speed im Browser",
            font_size=11, line_spacing=0.5, color=WHITE
        ).next_to(ec3_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        self.wait(1.5)  # total 2.5s

        # 2.5s - 5.0s: Wait before Card 1
        self.wait(2.5)  # total 5.0s

        # 5.0s - 6.5s: Card 1 fades in
        self.play(FadeIn(e_card1, shift=UP), FadeIn(ec1_title), FadeIn(ec1_desc), run_time=1.5)  # total 6.5s

        # 6.5s - 17.0s: Wait before Card 2
        self.wait(10.5)  # total 17.0s

        # 17.0s - 18.5s: Card 2 fades in
        self.play(FadeIn(e_card2, shift=UP), FadeIn(ec2_title), FadeIn(ec2_desc), run_time=1.5)  # total 18.5s

        # 18.5s - 28.0s: Wait before Card 3
        self.wait(9.5)  # total 28.0s

        # 28.0s - 29.5s: Card 3 fades in
        self.play(FadeIn(e_card3, shift=UP), FadeIn(ec3_title), FadeIn(ec3_desc), run_time=1.5)  # total 29.5s

        # 29.5s - 38.98s: Wait for Einsatzgebiete audio to end
        self.wait(39.98 - 29.5 - 1.0)  # total 38.98s

        # 38.98s - 39.98s: Transition (FadeOut)
        self.play(
            FadeOut(e_title),
            FadeOut(e_card1), FadeOut(ec1_title), FadeOut(ec1_desc),
            FadeOut(e_card2), FadeOut(ec2_title), FadeOut(ec2_desc),
            FadeOut(e_card3), FadeOut(ec3_title), FadeOut(ec3_desc),
            run_time=1.0
        )  # total 39.98s

        # ==========================================
        # SECTION 3: VORTEILE (Duration: 25.88s)
        # ==========================================
        self.add_sound("audio/vorteile.wav")

        # 0s - 1.0s: Section Title
        vort_title = Text("Vorteile von Rust für Anfänger", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(vort_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Wait/Prepare Cards
        # We will render 3 cards side-by-side
        card_w, card_h = 3.8, 4.4
        card1 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-4.2, -0.6, 0])
        card2 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([0, -0.6, 0])
        card3 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([4.2, -0.6, 0])

        c1_title = Text("1. Genialer Compiler", font_size=16, color=RUST_ORANGE, weight=BOLD).next_to(card1.get_top(), DOWN, buff=0.3)
        c1_desc = Paragraph(
            "• Weltklasse-Fehlermeldungen",
            "• Präzise Hilfe bei Bugs",
            "• Schlägt Lösungen vor",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(c1_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        c2_title = Text("2. Cargo Paketmanager", font_size=16, color=CYAN, weight=BOLD).next_to(card2.get_top(), DOWN, buff=0.3)
        c2_desc = Paragraph(
            "• Kinderleichte Abhängigkeiten",
            "• Ein Befehl zum Kompilieren",
            "• Automatisierte Tests",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(c2_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        c3_title = Text("3. Saubere Gewohnheiten", font_size=16, color=PURPLE, weight=BOLD).next_to(card3.get_top(), DOWN, buff=0.3)
        c3_desc = Paragraph(
            "• Speichersicher von Anfang an",
            "• Verhindert schlechten Code",
            "• Starke Typisierung & API",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(c3_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)

        self.wait(1.5)  # total 2.5s
        
        # 2.5s - 3.0s: Wait before Card 1
        self.wait(0.5)  # total 3.0s

        # 3.0s - 4.5s: Card 1 fades in
        self.play(FadeIn(card1, shift=UP), FadeIn(c1_title), FadeIn(c1_desc), run_time=1.5)  # total 4.5s

        # 4.5s - 10.0s: Wait before Card 2
        self.wait(5.5)  # total 10.0s

        # 10.0s - 11.5s: Card 2 fades in
        self.play(FadeIn(card2, shift=UP), FadeIn(c2_title), FadeIn(c2_desc), run_time=1.5)  # total 11.5s

        # 11.5s - 17.0s: Wait before Card 3
        self.wait(5.5)  # total 17.0s

        # 17.0s - 18.5s: Card 3 fades in
        self.play(FadeIn(card3, shift=UP), FadeIn(c3_title), FadeIn(c3_desc), run_time=1.5)  # total 18.5s

        # 18.5s - 24.88s: Wait for Vorteile audio to end
        self.wait(25.88 - 18.5 - 1.0)  # total 24.88s

        # 24.88s - 25.88s: Transition (FadeOut)
        self.play(
            FadeOut(vort_title),
            FadeOut(card1), FadeOut(c1_title), FadeOut(c1_desc),
            FadeOut(card2), FadeOut(c2_title), FadeOut(c2_desc),
            FadeOut(card3), FadeOut(c3_title), FadeOut(c3_desc),
            run_time=1.0
        )  # total 25.88s

        # ==========================================
        # SECTION 4: NACHTEILE (Duration: 23.83s)
        # ==========================================
        self.add_sound("audio/nachteile.wav")

        # 0s - 1.0s: Section Title
        n_title = Text("Herausforderungen & Belohnung", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(n_title, shift=UP), run_time=1.0)  # total 1.0s

        # Left Column: Herausforderungen
        left_header = Text("Die Herausforderungen", font_size=20, color=RED, weight=BOLD).move_to([-3.4, 1.4, 0])
        n_bullet1 = Text("• Steile Lernkurve", font_size=18, color=WHITE).move_to([-3.4, 0.6, 0])
        n_bullet2 = Text("• Borrow-Checker Frustration", font_size=18, color=WHITE).move_to([-3.4, -0.2, 0])
        n_bullet3 = Text("• Längere Kompilierzeiten", font_size=18, color=WHITE).move_to([-3.4, -1.0, 0])

        # Right Column: Die Belohnung
        right_header = Text("Warum es sich lohnt", font_size=20, color=GREEN, weight=BOLD).move_to([3.4, 1.4, 0])
        p_bullet1 = Text("• Extrem gefragte Entwickler", font_size=18, color=WHITE).move_to([3.4, 0.6, 0])
        p_bullet2 = Text("• Super sicherer & schneller Code", font_size=18, color=WHITE).move_to([3.4, -0.2, 0])
        p_bullet3 = Text("• Bessere Programmierpraktiken", font_size=18, color=WHITE).move_to([3.4, -1.0, 0])

        # Align columns
        for b in [n_bullet1, n_bullet2, n_bullet3]:
            b.align_to(left_header, LEFT)
        for b in [p_bullet1, p_bullet2, p_bullet3]:
            b.align_to(right_header, LEFT)

        # 1.0s - 2.5s: Fade in Left Header
        self.play(FadeIn(left_header, shift=RIGHT), run_time=1.5)  # total 2.5s

        # 2.5s - 3.0s: Wait before Left Bullet 1
        self.wait(0.5)  # total 3.0s

        # 3.0s - 4.0s: Left Bullet 1
        self.play(FadeIn(n_bullet1, shift=UP), run_time=1.0)  # total 4.0s

        # 4.0s - 8.0s: Wait before Left Bullet 2
        self.wait(4.0)  # total 8.0s

        # 8.0s - 9.0s: Left Bullet 2
        self.play(FadeIn(n_bullet2, shift=UP), run_time=1.0)  # total 9.0s

        # 9.0s - 13.0s: Wait before Left Bullet 3
        self.wait(4.0)  # total 13.0s

        # 13.0s - 14.0s: Left Bullet 3
        self.play(FadeIn(n_bullet3, shift=UP), run_time=1.0)  # total 14.0s

        # 14.0s - 17.0s: Wait before Right Column
        self.wait(3.0)  # total 17.0s

        # 17.0s - 18.5s: Right Column Header & Bullets
        self.play(
            FadeIn(right_header, shift=LEFT),
            FadeIn(p_bullet1, shift=UP),
            FadeIn(p_bullet2, shift=UP),
            FadeIn(p_bullet3, shift=UP),
            run_time=1.5
        )  # total 18.5s

        # 18.5s - 21.0s: Wait before Outro Text
        self.wait(2.5)  # total 21.0s

        # 21.0s - 22.5s: Outro Card "Lass uns direkt loslegen!"
        outro_card = RoundedRectangle(corner_radius=0.15, width=7.0, height=1.0, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).shift(DOWN * 2.5)
        outro_text = Text("Lass uns direkt loslegen!", font_size=22, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        
        self.play(
            FadeIn(outro_card),
            Write(outro_text),
            run_time=1.5
        )  # total 22.5s

        # 22.5s - 22.83s: Wait
        self.wait(23.83 - 22.5 - 1.0)  # total 22.83s

        # 22.83s - 23.83s: FadeOut everything
        self.play(
            FadeOut(n_title),
            FadeOut(left_header), FadeOut(n_bullet1), FadeOut(n_bullet2), FadeOut(n_bullet3),
            FadeOut(right_header), FadeOut(p_bullet1), FadeOut(p_bullet2), FadeOut(p_bullet3),
            FadeOut(outro_card), FadeOut(outro_text),
            run_time=1.0
        )  # total 23.83s
