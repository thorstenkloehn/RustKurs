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

class RustToolsVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 22.68s)
        # ==========================================
        self.add_sound("audio/ch3_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 3: KI-Assistenten & Tools", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 3: KI-Assistenten & Tools", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s

        # 4.5s - 5.5s: Wait
        self.wait(1.0)  # total 5.5s

        # 5.5s - 7.5s: Draw central node "KI-Assistent"
        ai_rect = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.1, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0.6, 0])
        ai_text = Text("KI-Assistent", font_size=16, color=PURPLE, weight=BOLD).move_to(ai_rect.get_center())
        ai_group = VGroup(ai_rect, ai_text)
        
        self.play(FadeIn(ai_group, shift=UP), run_time=1.5)
        self.wait(0.5)  # total 7.5s

        # Define the three action nodes
        # Node 1: Tools nutzen
        n1_rect = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([-4.2, -1.6, 0])
        n1_text = Text("Tools\nnutzen", font_size=12, color=CYAN, weight=BOLD).move_to(n1_rect.get_center())
        n1_group = VGroup(n1_rect, n1_text)
        arrow1 = Arrow(start=[0, 0.05, 0], end=[-4.2, -1.1, 0], buff=0, stroke_width=3, color=GRAY)

        # Node 2: Aufgaben erledigen
        n2_rect = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([0, -1.6, 0])
        n2_text = Text("Aufgaben\nerledigen", font_size=12, color=GREEN, weight=BOLD).move_to(n2_rect.get_center())
        n2_group = VGroup(n2_rect, n2_text)
        arrow2 = Arrow(start=[0, 0.05, 0], end=[0, -1.1, 0], buff=0, stroke_width=3, color=GRAY)

        # Node 3: Im Internet suchen
        n3_rect = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.0, color=YELLOW, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([4.2, -1.6, 0])
        n3_text = Text("Internet\nsuchen", font_size=12, color=YELLOW, weight=BOLD).move_to(n3_rect.get_center())
        n3_group = VGroup(n3_rect, n3_text)
        arrow3 = Arrow(start=[0, 0.05, 0], end=[4.2, -1.1, 0], buff=0, stroke_width=3, color=GRAY)

        # 7.5s - 10.0s: Draw Arrow 1 & Node 1
        self.play(Create(arrow1), FadeIn(n1_group, shift=RIGHT), run_time=2.0)
        self.wait(0.5)  # total 10.0s

        # 10.0s - 12.5s: Draw Arrow 2 & Node 2
        self.play(Create(arrow2), FadeIn(n2_group, shift=UP), run_time=2.0)
        self.wait(0.5)  # total 12.5s

        # 12.5s - 15.0s: Draw Arrow 3 & Node 3
        self.play(Create(arrow3), FadeIn(n3_group, shift=LEFT), run_time=2.0)
        self.wait(0.5)  # total 15.0s

        # 15.0s - 21.68s: Wait for the rest of intro speech
        self.wait(21.68 - 15.0)  # total 21.68s

        # 21.68s - 22.68s: Transition (FadeOut all nodes but keep Title)
        self.play(
            FadeOut(ai_group),
            FadeOut(arrow1), FadeOut(n1_group),
            FadeOut(arrow2), FadeOut(n2_group),
            FadeOut(arrow3), FadeOut(n3_group),
            run_time=1.0
        )  # total 22.68s


        # ==========================================
        # SECTION 2: TOOLS (Duration: 25.19s)
        # ==========================================
        self.add_sound("audio/ch3_tools.wav")

        # 0s - 1.0s: Transition title small text
        title_tools = Text("3. Moderne KI-Assistenten", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_tools), run_time=1.0)  # total 1.0s

        # 1.0s - 2.5s: Wait
        self.wait(1.5)  # total 2.5s

        # Define three tool cards
        # Cline Card (Left)
        c1_rect = RoundedRectangle(corner_radius=0.15, width=4.0, height=4.2, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([-4.4, -0.6, 0])
        c1_title = Text("Cline", font_size=18, color=CYAN, weight=BOLD).next_to(c1_rect.get_top(), DOWN, buff=0.3)
        c1_text = Paragraph(
            "• KI-Assistent für VS Code",
            "• Hilft Code schneller zu schreiben",
            "• Unterstützt beim Code-Verstehen",
            font_size=12, line_spacing=0.8, color=WHITE
        ).next_to(c1_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        c1_group = VGroup(c1_rect, c1_title, c1_text)

        # Gemini Card (Center)
        c2_rect = RoundedRectangle(corner_radius=0.15, width=4.0, height=4.2, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([0, -0.6, 0])
        c2_title = Text("Gemini Code Assist", font_size=18, color=PURPLE, weight=BOLD).next_to(c2_rect.get_top(), DOWN, buff=0.3)
        c2_text = Paragraph(
            "• Von Google entwickelt",
            "• Code-Vervollständigung",
            "• Fehlererkennung & Refactoring",
            font_size=12, line_spacing=0.8, color=WHITE
        ).next_to(c2_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        c2_group = VGroup(c2_rect, c2_title, c2_text)

        # GitHub Copilot Card (Right)
        c3_rect = RoundedRectangle(corner_radius=0.15, width=4.0, height=4.2, color=GRAY, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=1.5).move_to([4.4, -0.6, 0])
        c3_title = Text("GitHub Copilot", font_size=18, color=YELLOW, weight=BOLD).next_to(c3_rect.get_top(), DOWN, buff=0.3)
        c3_text = Paragraph(
            "• KI-Paarprogrammierer",
            "• Kontextbasierte Vorschläge",
            "• Generiert aus Kommentaren",
            font_size=12, line_spacing=0.8, color=WHITE
        ).next_to(c3_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        c3_group = VGroup(c3_rect, c3_title, c3_text)

        # 2.5s - 4.5s: FadeIn Cline Card
        self.play(FadeIn(c1_group, shift=UP), run_time=2.0)
        self.wait(4.5)  # total 9.0s (speech explains Cline until ~9s)

        # 9.0s - 11.0s: FadeIn Gemini Card
        self.play(FadeIn(c2_group, shift=UP), run_time=2.0)
        self.wait(5.0)  # total 16.0s (speech explains Gemini until ~16s)

        # 16.0s - 18.0s: FadeIn Copilot Card
        self.play(FadeIn(c3_group, shift=UP), run_time=2.0)
        
        # 18.0s - 25.19s: Wait for the rest of speech. Do not fade out, we transition!
        self.wait(25.19 - 18.0)  # total 25.19s


        # ==========================================
        # SECTION 3: FAVORITES (Duration: 11.80s)
        # ==========================================
        self.add_sound("audio/ch3_favorites.wav")

        # 0s - 1.5s: FadeOut Cline Card, and shift Gemini / Copilot to center positions
        self.play(
            FadeOut(c1_group, shift=LEFT),
            c2_group.animate.move_to([-2.2, -0.6, 0]),
            c3_group.animate.move_to([2.2, -0.6, 0]),
            run_time=1.5
        )  # total 1.5s

        # Create "Favorit" Badges
        badge_c2_rect = RoundedRectangle(corner_radius=0.08, width=1.5, height=0.4, color=GREEN, fill_color=GREEN, fill_opacity=0.2, stroke_width=2).next_to(c2_rect.get_top(), UP, buff=0.15).shift(LEFT * 0.9)
        badge_c2_text = Text("FAVORIT", font_size=10, color=GREEN, weight=BOLD).move_to(badge_c2_rect.get_center())
        badge_c2_group = VGroup(badge_c2_rect, badge_c2_text)

        badge_c3_rect = RoundedRectangle(corner_radius=0.08, width=1.5, height=0.4, color=GREEN, fill_color=GREEN, fill_opacity=0.2, stroke_width=2).next_to(c3_rect.get_top(), UP, buff=0.15).shift(LEFT * 0.9)
        badge_c3_text = Text("FAVORIT", font_size=10, color=GREEN, weight=BOLD).move_to(badge_c3_rect.get_center())
        badge_c3_group = VGroup(badge_c3_rect, badge_c3_text)

        # 1.5s - 3.5s: Highlight selected favorites (scale up, recolor border, fade in badge)
        self.play(
            c2_rect.animate.set_stroke(color=PURPLE, width=4),
            c3_rect.animate.set_stroke(color=YELLOW, width=4),
            FadeIn(badge_c2_group, shift=UP),
            FadeIn(badge_c3_group, shift=UP),
            run_time=2.0
        )  # total 3.5s

        # 3.5s - 10.80s: Wait
        self.wait(10.80 - 3.5)  # total 10.80s

        # 10.80s - 11.80s: FadeOut everything before Section 4
        self.play(
            FadeOut(title_group),
            FadeOut(c2_group), FadeOut(c3_group),
            FadeOut(badge_c2_group), FadeOut(badge_c3_group),
            run_time=1.0
        )  # total 11.80s


        # ==========================================
        # SECTION 4: LEARNING WARNING (Duration: 20.44s)
        # ==========================================
        self.add_sound("audio/ch3_learning.wav")

        # 0s - 1.0s: Section Title
        warn_title = Text("Warum nicht alles der KI überlassen?", font_size=30, color=RED, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(warn_title, shift=UP), run_time=1.0)  # total 1.0s

        # 1.0s - 3.0s: Wait
        self.wait(2.0)  # total 3.0s

        # Left Card (Nur KI nutzen)
        c_left_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=4.0, color=RED, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=2.5).move_to([-3.3, -0.4, 0])
        c_left_title = Text("Reine KI-Nutzung", font_size=18, color=RED, weight=BOLD).next_to(c_left_rect.get_top(), DOWN, buff=0.3)
        c_left_text = Paragraph(
            "• Kein eigener Lerneffekt beim Tippen",
            "• Syntax & Code-Struktur bleiben unklar",
            "• Keine eigene Problemlösungskompetenz",
            "• Hilflosigkeit bei Fehlern & Bugs",
            font_size=12, line_spacing=0.8, color=WHITE
        ).next_to(c_left_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        c_left_group = VGroup(c_left_rect, c_left_title, c_left_text)

        # Right Card (KI als Mentor nutzen)
        c_right_rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=4.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.95, stroke_width=2.5).move_to([3.3, -0.4, 0])
        c_right_title = Text("KI als Mentor & Partner", font_size=18, color=GREEN, weight=BOLD).next_to(c_right_rect.get_top(), DOWN, buff=0.3)
        c_right_text = Paragraph(
            "• Selbst Code schreiben & verinnerlichen",
            "• KI erklärt Konzepte und Compiler-Meldungen",
            "• Eigenständiges Debugging üben",
            "• Tiefes Verständnis & Problemlösung lernen",
            font_size=12, line_spacing=0.8, color=WHITE
        ).next_to(c_right_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        c_right_group = VGroup(c_right_rect, c_right_title, c_right_text)

        # 3.0s - 4.5s: FadeIn Left Card
        self.play(FadeIn(c_left_group, shift=RIGHT), run_time=1.5)
        self.wait(2.5)  # total 7.0s (speech explains warning)

        # 7.0s - 8.5s: FadeIn Right Card
        self.play(FadeIn(c_right_group, shift=LEFT), run_time=1.5)
        self.wait(4.5)  # total 13.0s

        # Banner at the bottom
        banner_rect = RoundedRectangle(corner_radius=0.12, width=11.0, height=0.7, color=RUST_ORANGE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -3.1, 0])
        banner_text = Text("Nutze KI als Unterstützung, aber lerne das Programmieren selbst!", font_size=13, color=RUST_ORANGE, weight=BOLD).move_to(banner_rect.get_center())
        banner_group = VGroup(banner_rect, banner_text)

        # 13.0s - 14.5s: FadeIn bottom banner
        self.play(FadeIn(banner_group, scale=0.9), run_time=1.5)
        
        # 14.5s - 19.44s: Wait
        self.wait(19.44 - 14.5)  # total 19.44s

        # 19.44s - 20.44s: FadeOut everything
        self.play(
            FadeOut(warn_title),
            FadeOut(c_left_group),
            FadeOut(c_right_group),
            FadeOut(banner_group),
            run_time=1.0
        )  # total 20.44s
