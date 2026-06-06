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

def create_terminal_window(width, height, title_text):
    window = RoundedRectangle(corner_radius=0.15, width=width, height=height, color=GRAY, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2)
    # Header line separating title bar
    header_bar = Line(
        start=[-width/2, height/2 - 0.45, 0], 
        end=[width/2, height/2 - 0.45, 0], 
        color=GRAY, 
        stroke_width=2
    )
    # Window control dots (Red, Yellow, Green)
    red_dot = Circle(radius=0.07, color=RED, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.25, height/2 - 0.22, 0])
    yellow_dot = Circle(radius=0.07, color=YELLOW, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.45, height/2 - 0.22, 0])
    green_dot = Circle(radius=0.07, color=GREEN, fill_opacity=1, stroke_width=0).move_to([-width/2 + 0.65, height/2 - 0.22, 0])
    # Window Title
    title = Text(title_text, font_size=11, color=GRAY).move_to([0, height/2 - 0.22, 0])
    
    return VGroup(window, header_bar, red_dot, yellow_dot, green_dot, title)

class RustInstallVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 17.88s)
        # ==========================================
        self.add_sound("audio/ch2_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 2: Installation & Setup", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 2: Installation & Setup", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s

        # 4.5s - 5.0s: Wait
        self.wait(0.5)  # total 5.0s

        # 5.0s - 6.5s: Ubuntu OS Badge Card
        ubuntu_card = RoundedRectangle(corner_radius=0.15, width=6.5, height=3.5, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([0, -0.4, 0])
        u_title = Text("Plattform: Ubuntu Linux", font_size=18, color=CYAN, weight=BOLD).next_to(ubuntu_card.get_top(), DOWN, buff=0.3)
        u_bullets = Paragraph(
            "• Voraussetzung: build-essential",
            "• Editor: Visual Studio Code",
            "• Erweiterung: rust-analyzer",
            "• Installation: rustup Manager",
            font_size=14, line_spacing=0.6, color=WHITE
        ).next_to(u_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.4)
        u_group = VGroup(ubuntu_card, u_title, u_bullets)

        self.play(FadeIn(u_group, shift=UP), run_time=1.5)  # total 6.5s

        # 6.5s - 16.88s: Wait
        self.wait(17.88 - 6.5 - 1.0)  # total 16.88s

        # 16.88s - 17.88s: Transition (FadeOut)
        self.play(FadeOut(title_group), FadeOut(u_group), run_time=1.0)  # total 17.88s

        # ==========================================
        # SECTION 2: BUILD-ESSENTIAL (Duration: 31.15s)
        # ==========================================
        self.add_sound("audio/ch2_build_essential.wav")

        # 0s - 1.0s: Section Title
        be_title = Text("1. Voraussetzung: build-essential", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(be_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Shift Title Up and wait
        self.wait(1.5)  # total 2.5s

        # 2.5s - 4.0s: Wait before terminal draw
        self.wait(1.5)  # total 4.0s

        # 4.0s - 5.5s: Draw Terminal (Left)
        term_w, term_h = 5.6, 4.0
        terminal = create_terminal_window(term_w, term_h, "Terminal - build-essential").move_to([-3.4, -0.6, 0])
        self.play(FadeIn(terminal, shift=RIGHT), run_time=1.5)  # total 5.5s

        # Terminal text placeholders
        cmd1 = Text("$ sudo apt update", font_size=13, font="Courier", color=WHITE).move_to([-5.8, 0.7, 0]).align_to(terminal[0], LEFT).shift(RIGHT * 0.3)
        cmd2 = Text("$ sudo apt install build-essential", font_size=13, font="Courier", color=WHITE).move_to([-5.8, 0.1, 0]).align_to(terminal[0], LEFT).shift(RIGHT * 0.3)
        
        # 5.5s - 7.0s: Type/Show command 1
        self.play(Write(cmd1), run_time=1.5)  # total 7.0s

        # 7.0s - 12.0s: Wait before card explanation
        self.wait(5.0)  # total 12.0s

        # 12.0s - 13.5s: Explanatory Card (Right)
        expl_card = RoundedRectangle(corner_radius=0.15, width=5.6, height=4.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([3.4, -0.6, 0])
        expl_title = Text("Was ist build-essential?", font_size=16, color=CYAN, weight=BOLD).next_to(expl_card.get_top(), DOWN, buff=0.3)
        expl_bullets = Paragraph(
            "• Enthält C-Bibliotheken (glibc)",
            "• Enthält Compiler (gcc & g++)",
            "• Enthält Hilfstools wie make",
            "• Wichtig für den Linker von Rust",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(expl_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        expl_group = VGroup(expl_card, expl_title, expl_bullets)

        self.play(FadeIn(expl_group, shift=LEFT), run_time=1.5)  # total 13.5s

        # 13.5s - 16.0s: Wait before Command 2
        self.wait(2.5)  # total 16.0s

        # 16.0s - 17.5s: Type/Show command 2
        self.play(Write(cmd2), run_time=1.5)  # total 17.5s

        # 17.5s - 30.15s: Wait for build-essential audio to end
        self.wait(31.15 - 17.5 - 1.0)  # total 30.15s

        # 30.15s - 31.15s: Transition (FadeOut)
        self.play(
            FadeOut(be_title),
            FadeOut(terminal), FadeOut(cmd1), FadeOut(cmd2),
            FadeOut(expl_group),
            run_time=1.0
        )  # total 31.15s


        # ==========================================
        # SECTION 3: VS CODE & RUST-ANALYZER (Duration: 29.23s)
        # ==========================================
        self.add_sound("audio/ch2_vscode.wav")

        # 0s - 1.0s: Section Title
        vs_title = Text("2. Editor: VS Code & rust-analyzer", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(vs_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Shift title/Wait
        self.wait(1.5)  # total 2.5s

        # 2.5s - 4.0s: Wait before Left Card
        self.wait(1.5)  # total 4.0s

        # 4.0s - 5.5s: Visual Studio Code Card (Left)
        vs_card = RoundedRectangle(corner_radius=0.15, width=5.6, height=4.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([-3.4, -0.6, 0])
        vs_header = Text("Visual Studio Code", font_size=16, color=CYAN, weight=BOLD).next_to(vs_card.get_top(), DOWN, buff=0.3)
        vs_desc = Paragraph(
            "• Beliebte Entwicklungsumgebung",
            "• Snap-Installation über Terminal:",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(vs_header, DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT * 0.3)
        
        # Sub-terminal inside card
        vs_term = create_terminal_window(5.0, 1.2, "Installation").next_to(vs_desc, DOWN, buff=0.2)
        vs_cmd = Text("$ sudo snap install --classic code", font_size=10, font="Courier", color=WHITE).move_to(vs_term[0].get_center())
        vs_group = VGroup(vs_card, vs_header, vs_desc, vs_term, vs_cmd)

        self.play(FadeIn(vs_group, shift=RIGHT), run_time=1.5)  # total 5.5s

        # 5.5s - 14.0s: Wait before Right Card
        self.wait(14.0 - 5.5)  # total 14.0s

        # 14.0s - 15.5s: rust-analyzer Card (Right)
        ra_card = RoundedRectangle(corner_radius=0.15, width=5.6, height=4.0, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.9).move_to([3.4, -0.6, 0])
        ra_header = Text("rust-analyzer Extension", font_size=16, color=PURPLE, weight=BOLD).next_to(ra_card.get_top(), DOWN, buff=0.3)
        ra_bullets = Paragraph(
            "• Offizielles Sprach-Plugin",
            "• Intelligente Codevervollständigung",
            "• Syntax-Highlighting & Formatierung",
            "• Echtzeit-Fehleranzeige beim Tippen",
            font_size=12, line_spacing=0.6, color=WHITE
        ).next_to(ra_header, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        ra_group = VGroup(ra_card, ra_header, ra_bullets)

        self.play(FadeIn(ra_group, shift=LEFT), run_time=1.5)  # total 15.5s

        # 15.5s - 28.23s: Wait for VS Code audio to end
        self.wait(29.23 - 15.5 - 1.0)  # total 28.23s

        # 28.23s - 29.23s: Transition (FadeOut)
        self.play(
            FadeOut(vs_title),
            FadeOut(vs_group),
            FadeOut(ra_group),
            run_time=1.0
        )  # total 29.23s


        # ==========================================
        # SECTION 4: RUST-INSTALLATION (Duration: 34.45s)
        # ==========================================
        self.add_sound("audio/ch2_rustup.wav")

        # 0s - 1.0s: Section Title
        rust_title = Text("3. Rust installieren via rustup", font_size=30, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(rust_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Wait
        self.wait(1.5)  # total 2.5s

        # 2.5s - 4.0s: Wait before terminal draw
        self.wait(1.5)  # total 4.0s

        # 4.0s - 5.5s: Draw Large Terminal (Center)
        term_w2, term_h2 = 9.8, 4.2
        terminal_big = create_terminal_window(term_w2, term_h2, "Terminal - Rustup Installer").move_to([0, -0.6, 0])
        self.play(FadeIn(terminal_big, shift=UP), run_time=1.5)  # total 5.5s

        # Terminal script simulation
        t_line1 = Text("$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh", font_size=11, font="Courier", color=WHITE).move_to([-4.6, 0.9, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        
        t_prompt1 = Text("1) Proceed with installation (default)", font_size=10, font="Courier", color=GRAY).move_to([-4.6, 0.4, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_prompt2 = Text("2) Customize installation", font_size=10, font="Courier", color=GRAY).move_to([-4.6, 0.1, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_prompt3 = Text("3) Cancel installation", font_size=10, font="Courier", color=GRAY).move_to([-4.6, -0.2, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_input = Text("> 1", font_size=10, font="Courier", color=WHITE).move_to([-4.6, -0.6, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_prompt_group = VGroup(t_prompt1, t_prompt2, t_prompt3)

        t_success = Text("Rust is installed now. Great!", font_size=11, font="Courier", color=GREEN).move_to([-4.6, -1.0, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_line2 = Text("$ rustc --version", font_size=11, font="Courier", color=WHITE).move_to([-4.6, -1.4, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)
        t_output = Text("rustc 1.80.0 (sha 2026-06-06)", font_size=11, font="Courier", color=CYAN).move_to([-4.6, -1.8, 0]).align_to(terminal_big[0], LEFT).shift(RIGHT * 0.4)

        # 5.5s - 6.0s: Wait
        self.wait(0.5)  # total 6.0s

        # 6.0s - 7.0s: Show curl command
        self.play(Write(t_line1), run_time=1.0)  # total 7.0s

        # 7.0s - 13.0s: Wait before installer prompt
        self.wait(6.0)  # total 13.0s

        # 13.0s - 14.5s: Show installer choices
        self.play(FadeIn(t_prompt_group, shift=DOWN), run_time=1.5)  # total 14.5s

        # 14.5s - 16.0s: Wait
        self.wait(1.5)  # total 16.0s

        # 16.0s - 17.0s: Type "1" to proceed
        self.play(Write(t_input), run_time=1.0)  # total 17.0s

        # 17.0s - 24.0s: Wait (simulation of loading)
        self.wait(7.0)  # total 24.0s

        # 24.0s - 25.5s: Show Success, type rustc check, show output
        self.play(
            FadeIn(t_success),
            Write(t_line2),
            run_time=1.5
        )
        self.play(FadeIn(t_output), run_time=0.5)  # total 26.0s

        # 26.0s - 28.0s: Wait
        self.wait(2.0)  # total 28.0s

        # 28.0s - 29.5s: Outro Card overlay
        outro_card = RoundedRectangle(corner_radius=0.15, width=7.5, height=1.2, color=RUST_ORANGE, fill_color=BG_COLOR, fill_opacity=1, stroke_width=3).shift(DOWN * 0.6)
        outro_text = Text("Dein System ist jetzt bereit!", font_size=22, color=RUST_ORANGE, weight=BOLD).move_to(outro_card.get_center())
        outro_group = VGroup(outro_card, outro_text)
        
        self.play(
            FadeIn(outro_group, scale=0.8),
            run_time=1.5
        )  # total 29.5s

        # 29.5s - 33.45s: Wait
        self.wait(34.45 - 29.5 - 1.0)  # total 33.45s

        # 33.45s - 34.45s: FadeOut everything
        self.play(
            FadeOut(rust_title),
            FadeOut(terminal_big),
            FadeOut(t_line1), FadeOut(t_prompt_group), FadeOut(t_input),
            FadeOut(t_success), FadeOut(t_line2), FadeOut(t_output),
            FadeOut(outro_group),
            run_time=1.0
        )  # total 34.45s
