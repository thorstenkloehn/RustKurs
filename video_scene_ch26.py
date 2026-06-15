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

class RustAgentsVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # Continuous watermark footer
        watermark = Text(
            "Rust Kurs | Kapitel 26: KI-Agenten & autonome Software-Ingenieure",
            font_size=8.0,
            color=GRAY,
            fill_opacity=0.65
        ).to_edge(DOWN, buff=0.15)
        self.add(watermark)

        # Default durations (will be updated by JSON)
        durations = {
            "ch26_1_intro": 15.0,
            "ch26_2_definition": 15.0,
            "ch26_3_problem": 15.0,
            "ch26_4_naive": 15.0,
            "ch26_5_anatomy": 15.0,
            "ch26_6_solution": 15.0,
            "ch26_7_tutorial": 15.0,
            "ch26_8_security": 15.0,
            "ch26_9_outro": 15.0
        }
        
        durations_path = "audio/durations_ch26.json"
        if os.path.exists(durations_path):
            try:
                with open(durations_path, "r") as f:
                    durations.update(json.load(f))
            except Exception as e:
                print(f"Error loading durations: {e}")

        # Compute section wait times (Pause between sections is exactly 1.5 seconds)
        # We want the total duration of section block i to be exactly durations[key] + 1.5.
        # If the animations in the block take `anim_time` seconds, and the exit transition takes 1.0s:
        # wait_time = durations[key] + 1.5 - anim_time - 1.0 = durations[key] + 0.5 - anim_time
        def get_wait_time(key, anim_time):
            d_i = durations[key]
            wait_val = d_i + 0.5 - anim_time
            return max(0.1, wait_val)

        # ==========================================
        # SECTION 1: INTRO
        # ==========================================
        self.add_sound("audio/ch26_1_intro.wav")

        title = Text("Rust-Videokurs für Anfänger", font_size=38, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 26: KI-Agenten & autonome Software-Ingenieure", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.5)
        self.wait(2.5)

        # Transform title to top banner
        title_small = Text("Kapitel 26: KI-Agenten & autonome Software-Ingenieure", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)
        self.wait(1.0)

        # Intro bullet points
        bullets = VGroup(
            Text("• Autonome Handlungszyklen (Planung & Ausführung)", font_size=16, color=WHITE),
            Text("• Werkzeugnutzung (Terminals, Compiler & Git)", font_size=16, color=WHITE),
            Text("• Fehlerbehebung per Feedback-Schleife (Loops)", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, -0.6, 0])

        self.play(LaggedStart(*(FadeIn(b, shift=RIGHT) for b in bullets), lag_ratio=0.3), run_time=2.0)
        self.wait(2.0)

        # Total anim time: 1.5 + 2.5 + 1.5 + 1.0 + 2.0 + 2.0 = 10.5 seconds
        self.wait(get_wait_time("ch26_1_intro", 10.5))
        self.play(FadeOut(bullets), run_time=1.0)

        # ==========================================
        # SECTION 2: DEFINITION
        # ==========================================
        self.add_sound("audio/ch26_2_definition.wav")

        title_def = Text("26. Die Definition: Assistent vs. Autopilot", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_def), run_time=1.0)
        self.wait(1.0)

        # Draw three comparison cards
        card_w, card_h = 3.6, 2.2
        card1 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.0, -0.4, 0])
        card1_title = Text("IDE-Erweiterung", font_size=12, color=GRAY, weight=BOLD).next_to(card1.get_top(), DOWN, buff=0.2)
        card1_desc = Paragraph("• Schlägt Code vor\n• Reaktiv im Editor\n• 'Fahrlehrer'", font_size=9, color=WHITE, line_spacing=0.4).next_to(card1_title, DOWN, buff=0.2).align_to(card1, LEFT).shift(RIGHT * 0.4)
        g_card1 = VGroup(card1, card1_title, card1_desc)

        card2 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0.0, -0.4, 0])
        card2_title = Text("CLI-Agent", font_size=12, color=CYAN, weight=BOLD).next_to(card2.get_top(), DOWN, buff=0.2)
        card2_desc = Paragraph("• Arbeitet im Terminal\n• Führt Tests & Git aus\n• 'Lokaler Autopilot'", font_size=9, color=WHITE, line_spacing=0.4).next_to(card2_title, DOWN, buff=0.2).align_to(card2, LEFT).shift(RIGHT * 0.4)
        g_card2 = VGroup(card2, card2_title, card2_desc)

        card3 = RoundedRectangle(corner_radius=0.1, width=card_w, height=card_h, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([4.0, -0.4, 0])
        card3_title = Text("Web-Plattform", font_size=12, color=PURPLE, weight=BOLD).next_to(card3.get_top(), DOWN, buff=0.2)
        card3_desc = Paragraph("• Eigene Sandbox & Browser\n• Löst komplexe Tasks\n• 'Voller Autopilot'", font_size=9, color=WHITE, line_spacing=0.4).next_to(card3_title, DOWN, buff=0.2).align_to(card3, LEFT).shift(RIGHT * 0.4)
        g_card3 = VGroup(card3, card3_title, card3_desc)

        self.play(FadeIn(g_card1, shift=UP), run_time=1.0)
        self.play(FadeIn(g_card2, shift=UP), run_time=1.0)
        self.play(FadeIn(g_card3, shift=UP), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 1.0 + 1.0 + 3.0 = 8.0 seconds
        self.wait(get_wait_time("ch26_2_definition", 8.0))
        self.play(FadeOut(g_card1), FadeOut(g_card2), FadeOut(g_card3), run_time=1.0)

        # ==========================================
        # SECTION 3: DAS PROBLEM
        # ==========================================
        self.add_sound("audio/ch26_3_problem.wav")

        title_prob = Text("26. Das Problem: Fragmentierung & Reibungsverluste", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_prob), run_time=1.0)
        self.wait(1.0)

        # Left side: Browser (Web Chat)
        browser = RoundedRectangle(corner_radius=0.1, width=4.5, height=3.0, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.5, -0.6, 0])
        b_title = Text("Web-Browser (Chatbot)", font_size=12, color=PURPLE, weight=BOLD).next_to(browser.get_top(), DOWN, buff=0.2)
        b_content = Paragraph("KI generiert Code:\n  fn append_log_entry(...)\n\nKein lokaler Kontext!\nKein Compiler-Feedback!", font_size=9, color=WHITE, line_spacing=0.4).next_to(b_title, DOWN, buff=0.2).align_to(browser, LEFT).shift(RIGHT * 0.4)
        g_browser = VGroup(browser, b_title, b_content)

        # Right side: IDE (Local Editor)
        ide = RoundedRectangle(corner_radius=0.1, width=4.5, height=3.0, color=GRAY, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2).move_to([3.5, -0.6, 0])
        i_title = Text("Lokale IDE (Editor)", font_size=12, color=GRAY, weight=BOLD).next_to(ide.get_top(), DOWN, buff=0.2)
        i_content = Paragraph("Manuelles Einfügen\n-> Syntaxfehler?\n-> Fehlende Imports?\n-> Compile Error?", font_size=9, color=WHITE, line_spacing=0.4).next_to(i_title, DOWN, buff=0.2).align_to(ide, LEFT).shift(RIGHT * 0.4)
        g_ide = VGroup(ide, i_title, i_content)

        self.play(FadeIn(g_browser, shift=LEFT), FadeIn(g_ide, shift=RIGHT), run_time=1.5)
        self.wait(1.5)

        # Red arrow pointing between them indicating friction
        friction_arrow = DoubleArrow(start=[-1.0, -0.6, 0], end=[1.0, -0.6, 0], color=RED, stroke_width=4.0)
        friction_lbl = Text("Mühsames Kopieren & Einfügen", font_size=9, color=RED).next_to(friction_arrow, UP, buff=0.15)
        
        # Danger warning triangle
        warn_triangle = Triangle(color=RED, fill_color=RED, fill_opacity=0.25, stroke_width=2).scale(0.35).move_to([0, -1.8, 0])
        warn_excl = Text("!", font_size=16, color=RED, weight=BOLD).move_to(warn_triangle.get_center()).shift(UP * 0.02)
        warn_lbl = Text("Reibungsverlust & Fehlerquellen", font_size=9, color=RED).next_to(warn_triangle, DOWN, buff=0.1)
        g_warning = VGroup(friction_arrow, friction_lbl, warn_triangle, warn_excl, warn_lbl)

        self.play(Create(friction_arrow), FadeIn(friction_lbl), run_time=1.0)
        self.play(FadeIn(warn_triangle), FadeIn(warn_excl), FadeIn(warn_lbl), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 1.5 + 1.0 + 1.0 + 3.0 = 10.0 seconds
        self.wait(get_wait_time("ch26_3_problem", 10.0))
        self.play(FadeOut(g_browser), FadeOut(g_ide), FadeOut(g_warning), run_time=1.0)

        # ==========================================
        # SECTION 4: NAIVER VERSUCH
        # ==========================================
        self.add_sound("audio/ch26_4_naive.wav")

        title_naive = Text("26. Der naive Versuch: Einfügen ohne Imports", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_naive), run_time=1.0)
        self.wait(1.0)

        # Show code editor
        editor = create_terminal_window(10.5, 4.4, "src/main.rs").move_to([0, -0.4, 0])
        code = Paragraph(
            "use std::fs::OpenOptions;",
            "",
            "// Funktion zum Anhängen von Protokolleinträgen",
            "fn append_log_entry(filename: &str, message: &str) -> std::io::Result<()> {",
            "    let mut file = OpenOptions::new()",
            "        .create(true)",
            "        .append(true)",
            "        .open(filename)?;",
            "",
            "    // Text in Bytes schreiben (Fehlender Trait std::io::Write!)",
            "    file.write_all(message.as_bytes())?;",
            "    file.write_all(b\"\\n\")?;",
            "    Ok(())",
            "}",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(editor[1], DOWN, buff=0.25).align_to(editor[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(editor), FadeIn(code), run_time=1.5)
        self.wait(2.5)

        # Highlight missing trait usage lines
        h1 = SurroundingRectangle(code[10], color=RED, stroke_width=1.5)
        h2 = SurroundingRectangle(code[11], color=RED, stroke_width=1.5)
        
        self.play(Create(h1), Create(h2), run_time=1.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.5 + 3.0 = 10.5 seconds
        self.wait(get_wait_time("ch26_4_naive", 10.5))
        self.play(FadeOut(editor), FadeOut(code), FadeOut(h1), FadeOut(h2), run_time=1.0)

        # ==========================================
        # SECTION 5: ANATOMIE DES FEHLERS
        # ==========================================
        self.add_sound("audio/ch26_5_anatomy.wav")

        title_anatomy = Text("26. Die Anatomie des Fehlers: Compiler E0599", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_anatomy), run_time=1.0)
        self.wait(1.0)

        # Show terminal compiler output
        terminal = create_terminal_window(11.0, 4.4, "Terminal - cargo check").move_to([0, -0.4, 0])
        err_msg = Paragraph(
            "error[E0599]: no method named `write_all` found for struct `File` in the current scope",
            "  --> src/main.rs:11:10",
            "   |",
            "11 |     file.write_all(message.as_bytes())?;",
            "   |          ^^^^^^^^^ method not found in `File`",
            "   |",
            "   = help: items from traits can only be used if the trait is in scope",
            "help: the following trait is implemented but not in scope; perhaps add a `use` for it:",
            "   |",
            "1  + use std::io::Write;",
            font="Monospace", font_size=8.0, color=WHITE, line_spacing=0.4
        ).next_to(terminal[1], DOWN, buff=0.25).align_to(terminal[0], LEFT).shift(RIGHT * 0.6)

        self.play(FadeIn(terminal), FadeIn(err_msg), run_time=1.5)
        self.wait(2.5)

        # Highlight E0599 in red and recommendation in green
        h_err_code = SurroundingRectangle(err_msg[0], color=RED, stroke_width=1.5)
        h_help_import = SurroundingRectangle(err_msg[9], color=GREEN, stroke_width=1.5)

        self.play(Create(h_err_code), run_time=1.0)
        self.play(Create(h_help_import), run_time=1.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.5 + 1.0 + 1.0 + 3.0 = 11.0 seconds
        self.wait(get_wait_time("ch26_5_anatomy", 11.0))
        self.play(FadeOut(terminal), FadeOut(err_msg), FadeOut(h_err_code), FadeOut(h_help_import), run_time=1.0)

        # ==========================================
        # SECTION 6: DIE LÖSUNG & DER LOOP
        # ==========================================
        self.add_sound("audio/ch26_6_solution.wav")

        title_sol = Text("26. Die Lösung: Der agentische Korrektur-Loop", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sol), run_time=1.0)
        self.wait(1.0)

        # Left side: Corrected Editor
        editor_sol = create_terminal_window(6.0, 4.4, "src/main.rs").move_to([-3.5, -0.4, 0])
        code_sol = Paragraph(
            "use std::fs::OpenOptions;",
            "use std::io::Write; // 🟢 Hinzugefügt!",
            "",
            "fn append_log_entry(",
            "    filename: &str,",
            "    message: &str",
            ") -> std::io::Result<()> {",
            "    let mut file = OpenOptions::new()",
            "        .create(true)",
            "        .append(true)",
            "        .open(filename)?;",
            "    file.write_all(message.as_bytes())?;",
            "    Ok(())",
            "}",
            font="Monospace", font_size=7.5, color=WHITE, line_spacing=0.4
        ).next_to(editor_sol[1], DOWN, buff=0.25).align_to(editor_sol[0], LEFT).shift(RIGHT * 0.4)
        g_sol = VGroup(editor_sol, code_sol)

        # Right side: Circular Reasoning Loop Mobjects
        c_plan = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.8, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.5, 1.2, 0])
        t_plan = Text("1. Planen (Reasoning)", font_size=9, color=CYAN, weight=BOLD).move_to(c_plan.get_center())
        g_plan = VGroup(c_plan, t_plan)

        c_act = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.8, color=PURPLE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([5.5, -0.4, 0])
        t_act = Text("2. Handeln (Code)", font_size=9, color=PURPLE, weight=BOLD).move_to(c_act.get_center())
        g_act = VGroup(c_act, t_act)

        c_obs = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.8, color=RUST_ORANGE, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([3.5, -2.0, 0])
        t_obs = Text("3. Beobachten (Check)", font_size=9, color=RUST_ORANGE, weight=BOLD).move_to(c_obs.get_center())
        g_obs = VGroup(c_obs, t_obs)

        c_success = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.8, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([1.5, -0.4, 0])
        t_success = Text("4. Erfolg (Verifizieren)", font_size=9, color=GREEN, weight=BOLD).move_to(c_success.get_center())
        g_success = VGroup(c_success, t_success)

        # Arrows connecting the loop
        a1 = Arrow(c_plan.get_right(), c_act.get_top(), color=GRAY, stroke_width=2)
        a2 = Arrow(c_act.get_bottom(), c_obs.get_right(), color=GRAY, stroke_width=2)
        a3 = Arrow(c_obs.get_left(), c_success.get_bottom(), color=GRAY, stroke_width=2)
        a4 = Arrow(c_success.get_top(), c_plan.get_left(), color=GRAY, stroke_width=2)
        g_arrows = VGroup(a1, a2, a3, a4)

        self.play(FadeIn(g_sol, shift=LEFT), run_time=1.5)
        self.play(LaggedStart(FadeIn(g_plan), FadeIn(g_act), FadeIn(g_obs), FadeIn(g_success), lag_ratio=0.2), Create(g_arrows), run_time=2.0)
        self.wait(1.5)

        # Highlighting the loop cycle
        self.play(c_plan.animate.set_fill(CYAN, opacity=0.25), run_time=0.6)
        self.play(c_plan.animate.set_fill(LIGHT_BG, opacity=0.9), c_act.animate.set_fill(PURPLE, opacity=0.25), run_time=0.6)
        self.play(c_act.animate.set_fill(LIGHT_BG, opacity=0.9), c_obs.animate.set_fill(RUST_ORANGE, opacity=0.25), run_time=0.6)
        self.play(c_obs.animate.set_fill(LIGHT_BG, opacity=0.9), c_success.animate.set_fill(GREEN, opacity=0.25), run_time=0.6)
        self.play(c_success.animate.set_fill(LIGHT_BG, opacity=0.9), run_time=0.4)
        self.wait(2.0)

        # Total anim time: 1.0 + 1.0 + 1.5 + 2.0 + 1.5 + 0.6 + 0.6 + 0.6 + 0.6 + 0.4 + 2.0 = 11.8 seconds
        self.wait(get_wait_time("ch26_6_solution", 11.8))
        self.play(FadeOut(g_sol), FadeOut(g_plan), FadeOut(g_act), FadeOut(g_obs), FadeOut(g_success), FadeOut(g_arrows), run_time=1.0)

        # ==========================================
        # SECTION 7: TUTORIAL
        # ==========================================
        self.add_sound("audio/ch26_7_tutorial.wav")

        title_tut = Text("26. Praxistutorial: CLI-Agent im Terminal", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_tut), run_time=1.0)
        self.wait(1.0)

        # Show terminal window
        tut_term = create_terminal_window(11.5, 4.4, "Terminal - Claude Code").move_to([0, -0.4, 0])
        self.play(FadeIn(tut_term), run_time=1.0)

        # Typing simulation of prompt
        cmd_prompt = Text("thorsten@rust-pc:~/project$ claudecode", font_size=9, color=GRAY, font="Monospace").next_to(tut_term[1], DOWN, buff=0.2).align_to(tut_term[0], LEFT).shift(RIGHT * 0.6)
        task_prompt = Text("> Implementiere 'read_last_line' in src/log.rs mit Tests.", font_size=9, color=WHITE, font="Monospace").next_to(cmd_prompt, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(FadeIn(cmd_prompt), Write(task_prompt, run_time=2.0))
        self.wait(1.0)

        # Simulation of agent output
        out_lines = VGroup(
            Text("[Planung] Suche nach src/log.rs...", font_size=8, color=CYAN, font="Monospace"),
            Text("[Code] Erstelle read_last_line(path: &str) -> Option<String>", font_size=8, color=PURPLE, font="Monospace"),
            Text("[Test] Führe 'cargo test' im Terminal aus...", font_size=8, color=YELLOW, font="Monospace"),
            Text("       Compiling log_parser v0.1.0 ... done.", font_size=8, color=GRAY, font="Monospace"),
            Text("       Running unittests src/lib.rs ... ok 🟢 (1 test passed)", font_size=8, color=GREEN, font="Monospace"),
            Text("[Erfolg] Datei erfolgreich geändert und verifiziert!", font_size=8, color=GREEN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(task_prompt, DOWN, buff=0.25)

        self.play(LaggedStart(*(FadeIn(line, shift=UP) for line in out_lines), lag_ratio=0.4), run_time=2.5)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 2.0 + 1.0 + 2.5 + 3.0 = 11.5 seconds
        self.wait(get_wait_time("ch26_7_tutorial", 11.5))
        self.play(FadeOut(tut_term), FadeOut(cmd_prompt), FadeOut(task_prompt), FadeOut(out_lines), run_time=1.0)

        # ==========================================
        # SECTION 8: SICHERHEITSASPEKTE
        # ==========================================
        self.add_sound("audio/ch26_8_security.wav")

        title_sec = Text("26. Sicherheitsaspekte bei lokalen Agenten", font_size=18, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sec), run_time=1.0)
        self.wait(1.0)

        # Central agent symbol and container boundary
        agent_box = RoundedRectangle(corner_radius=0.1, width=2.4, height=1.0, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, 0, 0])
        agent_text = Paragraph("KI-Agent\n(Lokales Tool)", font_size=9, color=CYAN, alignment="center").move_to(agent_box.get_center())
        g_agent = VGroup(agent_box, agent_text)

        sandbox_border = DashedVMobject(
            RoundedRectangle(corner_radius=0.15, width=4.5, height=2.4, color=RED, stroke_width=2.5),
            num_dashes=30
        ).move_to([0, 0, 0])
        sandbox_lbl = Text("Docker Sandbox / VM (Isoliert)", font_size=9, color=RED, weight=BOLD).next_to(sandbox_border.get_top(), UP, buff=0.15)
        g_sandbox = VGroup(sandbox_border, sandbox_lbl)

        # Three security shields/principles
        shield1 = RoundedRectangle(corner_radius=0.1, width=3.2, height=1.2, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([-4.4, -1.8, 0])
        shield1_lbl = Paragraph("1. Manuelle Bestätigung\n   Fordern Sie Freigaben\n   für Shell-Befehle", font_size=8, color=WHITE, line_spacing=0.35).move_to(shield1.get_center())
        g_shield1 = VGroup(shield1, shield1_lbl)

        shield2 = RoundedRectangle(corner_radius=0.1, width=3.2, height=1.2, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([0, -1.8, 0])
        shield2_lbl = Paragraph("2. Containerisierung\n   Docker schützt das\n   Host-System", font_size=8, color=WHITE, line_spacing=0.35).move_to(shield2.get_center())
        g_shield2 = VGroup(shield2, shield2_lbl)

        shield3 = RoundedRectangle(corner_radius=0.1, width=3.2, height=1.2, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=1.5).move_to([4.4, -1.8, 0])
        shield3_lbl = Paragraph("3. Git Backup / Branch\n   Commit vor Start\n   sichert Rollbacks", font_size=8, color=WHITE, line_spacing=0.35).move_to(shield3.get_center())
        g_shield3 = VGroup(shield3, shield3_lbl)

        self.play(FadeIn(g_agent), run_time=1.0)
        self.play(Create(sandbox_border), FadeIn(sandbox_lbl), run_time=1.5)
        self.wait(1.0)
        self.play(LaggedStart(FadeIn(g_shield1, shift=UP), FadeIn(g_shield2, shift=UP), FadeIn(g_shield3, shift=UP), lag_ratio=0.3), run_time=2.0)
        self.wait(3.0)

        # Total anim time: 1.0 + 1.0 + 1.0 + 1.5 + 1.0 + 2.0 + 3.0 = 10.5 seconds
        self.wait(get_wait_time("ch26_8_security", 10.5))
        self.play(FadeOut(g_agent), FadeOut(g_sandbox), FadeOut(g_shield1), FadeOut(g_shield2), FadeOut(g_shield3), run_time=1.0)

        # ==========================================
        # SECTION 9: OUTRO
        # ==========================================
        self.add_sound("audio/ch26_9_outro.wav")

        title_outro = Text("Zusammenfassung & Fazit", font_size=22, color=RUST_ORANGE, weight=BOLD).move_to([0, 1.2, 0])
        self.play(Transform(title_group, title_outro), run_time=1.0)
        self.wait(1.0)

        # Key Takeaways
        takeaways = VGroup(
            Text("1. Autonomie statt simpler Text-Chats", font_size=13, color=CYAN, weight=BOLD),
            Text("   KI-Agenten analysieren Fehlermeldungen und reparieren Code selbstständig.", font_size=10, color=WHITE),
            Text("2. Der Compiler als Mentor", font_size=13, color=PURPLE, weight=BOLD),
            Text("   Rusts präzise Fehlerbeschreibungen dienen der KI als perfekte Korrekturvorlage.", font_size=10, color=WHITE),
            Text("3. Sicherheit an erster Stelle", font_size=13, color=GREEN, weight=BOLD),
            Text("   Nutzen Sie Sandboxes, manuelle Audits und Git-Versionierung als Fangnetz.", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.0, 0])

        self.play(LaggedStart(*(FadeIn(t, shift=RIGHT) for t in takeaways), lag_ratio=0.25), run_time=2.5)
        self.wait(4.0)

        # Total anim time: 1.0 + 1.0 + 2.5 + 4.0 = 8.5 seconds
        self.wait(get_wait_time("ch26_9_outro", 8.5))

        # Final fade out
        self.play(FadeOut(title_group), FadeOut(takeaways), run_time=1.5)
        self.wait(1.0)
