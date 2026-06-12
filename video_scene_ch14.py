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

class RustAntigravityCLIVideo(Scene):
    def construct(self):
        # Set the camera background color
        self.camera.background_color = BG_COLOR

        # ==========================================
        # SECTION 1: INTRO (Duration: 20.29s)
        # ==========================================
        self.add_sound("audio/ch14_1_intro.wav")

        # 0s - 3s: Title and Subtitle
        title = Text("Rust für Anfänger", font_size=46, color=RUST_ORANGE, weight=BOLD)
        subtitle = Text("Kapitel 14: Antigravity CLI", font_size=28, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_group, shift=UP), run_time=1.0)
        self.wait(2.0)  # total 3.0s

        # 3s - 4.5s: Move Title to Top
        title_small = Text("Kapitel 14: Antigravity CLI", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_small), run_time=1.5)  # total 4.5s

        # 4.5s - 5.5s: Wait
        self.wait(1.0)  # total 5.5s

        # 5.5s - 7.5s: Draw central terminal box
        term_rect = RoundedRectangle(corner_radius=0.15, width=4.5, height=1.3, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 0.6, 0])
        term_text = Text("$ agy", font_size=24, color=CYAN, font="Monospace", weight=BOLD).move_to(term_rect.get_center())
        term_group = VGroup(term_rect, term_text)
        
        self.play(FadeIn(term_group, scale=0.8), run_time=1.5)
        self.wait(0.5)  # total 7.5s

        # 7.5s - 13.5s: Bullet points under terminal
        bullets = VGroup(
            Text("• Googles Agentic Development Platform", font_size=16, color=WHITE),
            Text("• Offizieller Nachfolger des Gemini CLI", font_size=16, color=WHITE),
            Text("• Tastatur-gesteuert & extrem leichtgewichtig", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(term_group, DOWN, buff=0.5)
        
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT), run_time=1.0)
        self.wait(1.5)  # total 12.0s

        # 12.0s - 19.29s: Wait for speech to finish
        self.wait(20.29 - 12.0 - 1.0)  # total 19.29s

        # 19.29s - 20.29s: Transition (Fade out all nodes but keep Title)
        self.play(
            FadeOut(term_group),
            FadeOut(bullets),
            run_time=1.0
        )  # total 20.29s


        # ==========================================
        # SECTION 2: INSTALLATION & LAUNCH (Duration: 25.86s)
        # ==========================================
        self.add_sound("audio/ch14_2_install_start.wav")

        # 0s - 1.0s: Transition title small text
        title_install = Text("14. Installation & Start", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_install), run_time=1.0)  # total 1.0s

        self.wait(1.0)  # total 2.0s

        # macOS / Linux Terminal Window
        mac_linux_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=3.6, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([-3.2, -0.6, 0])
        mac_linux_hdr = Rectangle(width=5.8, height=0.4, stroke_width=0, fill_color="#1e293b", fill_opacity=1.0).next_to(mac_linux_rect.get_top(), DOWN, buff=0.2)
        mac_linux_title = Text("Terminal (macOS / Linux)", font_size=10, color=WHITE, weight=BOLD).move_to(mac_linux_hdr.get_center())
        mac_linux_prompt = Text("$ curl -fsSL https://antigravity.google/cli/install.sh | bash", font_size=8, color=CYAN, font="Monospace").next_to(mac_linux_hdr, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)
        mac_linux_dest = Text("Installiert in:\n~/.local/bin/agy", font_size=10, color=WHITE).next_to(mac_linux_prompt, DOWN, buff=0.5, aligned_edge=LEFT)
        mac_linux_group = VGroup(mac_linux_rect, mac_linux_hdr, mac_linux_title, mac_linux_prompt, mac_linux_dest)

        # Windows PowerShell Window
        win_rect = RoundedRectangle(corner_radius=0.15, width=5.8, height=3.6, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([3.2, -0.6, 0])
        win_hdr = Rectangle(width=5.8, height=0.4, stroke_width=0, fill_color="#1e293b", fill_opacity=1.0).next_to(win_rect.get_top(), DOWN, buff=0.2)
        win_title = Text("PowerShell (Windows)", font_size=10, color=WHITE, weight=BOLD).move_to(win_hdr.get_center())
        win_prompt = Text("PS> irm https://antigravity.google/cli/install.ps1 | iex", font_size=8, color=PURPLE, font="Monospace").next_to(win_hdr, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.2)
        win_dest = Text("Verwendung über:\nagy", font_size=10, color=WHITE).next_to(win_prompt, DOWN, buff=0.5, aligned_edge=LEFT)
        win_group = VGroup(win_rect, win_hdr, win_title, win_prompt, win_dest)

        # Fade in install windows
        self.play(
            FadeIn(mac_linux_group, shift=UP),
            FadeIn(win_group, shift=UP),
            run_time=1.5
        )  # total 3.5s
        self.wait(7.5)  # total 11.0s

        # Transition to Launch Panel
        launch_rect = RoundedRectangle(corner_radius=0.15, width=8.5, height=3.8, color=GREEN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        launch_title = Text("Starten & Prompt", font_size=16, color=GREEN, weight=BOLD).next_to(launch_rect.get_top(), DOWN, buff=0.3)
        
        launch_commands = VGroup(
            Text("$ cd /dein/projektpfad", font_size=12, color=CYAN, font="Monospace"),
            Text("$ agy", font_size=12, color=CYAN, font="Monospace"),
            Text("Assistent startet... Gib Aufgaben direkt ein:", font_size=11, color=WHITE),
            Text("> \"Erstelle helper.rs und implementiere Rundung...\"", font_size=11, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(launch_title, DOWN, buff=0.4)
        launch_group = VGroup(launch_rect, launch_title, launch_commands)

        self.play(
            FadeOut(mac_linux_group, shift=LEFT),
            FadeOut(win_group, shift=RIGHT),
            FadeIn(launch_group, scale=0.9),
            run_time=1.5
        )  # total 12.5s
        self.wait(25.86 - 12.5 - 1.0)  # total 24.86s

        # Transition out
        self.play(
            FadeOut(launch_group),
            run_time=1.0
        )  # total 25.86s


        # ==========================================
        # SECTION 3: CONFIGURATION & PATHS (Duration: 25.83s)
        # ==========================================
        self.add_sound("audio/ch14_3_settings_paths.wav")

        title_paths = Text("14. Einstellungen & Verzeichnisse", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_paths), run_time=1.0)  # total 1.0s

        self.wait(1.0)  # total 2.0s

        # Directory Tree Card
        tree_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        tree_title = Text("Pfade im Benutzerverzeichnis (~/.gemini/antigravity-cli/)", font_size=13, color=YELLOW, weight=BOLD).next_to(tree_rect.get_top(), DOWN, buff=0.3)
        
        path_settings = VGroup(
            Text("├── settings.json", font_size=12, color=CYAN, font="Monospace"),
            Text("│   └── Globale Einstellungen (Themes, Berechtigungen)", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        path_brain = VGroup(
            Text("├── brain/", font_size=12, color=CYAN, font="Monospace"),
            Text("│   └── <conversation-id>/ (Logs & Transkripte der Chats)", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        path_plugins = VGroup(
            Text("└── plugins/", font_size=12, color=CYAN, font="Monospace"),
            Text("    └── plugins_name/ (Erweiterungen & MCP-Server)", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        tree_details = VGroup(
            path_settings,
            path_brain,
            path_plugins
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(tree_title, DOWN, buff=0.4).shift(RIGHT * 0.4)
        
        tree_group = VGroup(tree_rect, tree_title, tree_details)

        self.play(FadeIn(tree_group, scale=0.9), run_time=1.5)  # total 3.5s
        self.wait(3.5)  # total 7.0s

        # Highlight settings.json
        box_settings = SurroundingRectangle(path_settings, color=RUST_ORANGE, buff=0.1, stroke_width=1.5)
        self.play(Create(box_settings), run_time=1.0)
        self.wait(4.0)  # total 12.0s

        # Highlight brain/ folder
        box_brain = SurroundingRectangle(path_brain, color=RUST_ORANGE, buff=0.1, stroke_width=1.5)
        self.play(Transform(box_settings, box_brain), run_time=1.0)
        self.wait(5.0)  # total 18.0s

        # Highlight plugins/ folder
        box_plugins = SurroundingRectangle(path_plugins, color=RUST_ORANGE, buff=0.1, stroke_width=1.5)
        self.play(Transform(box_settings, box_plugins), run_time=1.0)
        self.wait(25.83 - 19.0 - 1.0)  # total 24.83s

        # Transition out
        self.play(
            FadeOut(tree_group),
            FadeOut(box_settings),
            run_time=1.0
        )  # total 25.83s


        # ==========================================
        # SECTION 4: PROJECT CONFIGURATION & SKILLS (Duration: 30.14s)
        # ==========================================
        self.add_sound("audio/ch14_4_project_configs.wav")

        title_proj = Text("14. Projektregeln & Custom Skills", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_proj), run_time=1.0)  # total 1.0s

        self.wait(1.0)  # total 2.0s

        # Project folder card
        proj_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        proj_title = Text("Lokale Konfiguration im Projektverzeichnis", font_size=13, color=CYAN, weight=BOLD).next_to(proj_rect.get_top(), DOWN, buff=0.3)
        
        file_agents = VGroup(
            Text("├── AGENTS.md", font_size=12, color=RUST_ORANGE, font="Monospace"),
            Text("│   └── Projektregeln, Standards, Kontext für den Agenten", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        file_skills = VGroup(
            Text("└── SKILLS.md", font_size=12, color=RUST_ORANGE, font="Monospace"),
            Text("    └── Custom Skills (Playbooks) für wiederkehrende Abläufe", font_size=10, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        file_tree = VGroup(file_agents, file_skills).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(proj_title, DOWN, buff=0.4).shift(RIGHT * 0.4)
        proj_group = VGroup(proj_rect, proj_title, file_tree)

        self.play(FadeIn(proj_group, scale=0.9), run_time=1.5)  # total 3.5s
        self.wait(2.5)  # total 6.0s

        # Highlight AGENTS.md
        box_agents = SurroundingRectangle(file_agents, color=YELLOW, buff=0.1, stroke_width=1.5)
        self.play(Create(box_agents), run_time=1.0)
        self.wait(2.0)  # total 9.0s

        # Highlight SKILLS.md
        box_skills = SurroundingRectangle(file_skills, color=YELLOW, buff=0.1, stroke_width=1.5)
        self.play(Transform(box_agents, box_skills), run_time=1.0)
        self.wait(2.0)  # total 12.0s

        # Transition to Subagent Rules detail card
        rules_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=YELLOW, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        rules_title = Text("Subagenten-Regeln in AGENTS.md", font_size=14, color=YELLOW, weight=BOLD).next_to(rules_rect.get_top(), DOWN, buff=0.3)
        
        rules_list = VGroup(
            Text("• branch-Modus erzwingen (für sichere Code-Änderungen)", font_size=11, color=WHITE),
            Text("• Schreibrechte eingrenzen (z.B. nur für Ordner /src)", font_size=11, color=WHITE),
            Text("• Unerwünschte Befehle verbieten (z.B. keine curl Netzwerkaufrufe)", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(rules_title, DOWN, buff=0.4)
        rules_group = VGroup(rules_rect, rules_title, rules_list)

        self.play(
            FadeOut(box_agents),
            FadeOut(proj_group),
            FadeIn(rules_group, scale=0.9),
            run_time=1.5
        )  # total 13.5s
        self.wait(7.5)  # total 21.0s

        # Transition to trigger box @run-tests simulation
        trigger_box = RoundedRectangle(corner_radius=0.08, width=5.5, height=1.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.98, stroke_width=1.5).move_to([0, -0.6, 0])
        trigger_text = Text("agy > @run-tests", font_size=14, color=GREEN, font="Monospace").move_to(trigger_box.get_center())
        trigger_group = VGroup(trigger_box, trigger_text)

        self.play(
            FadeOut(rules_group),
            FadeIn(trigger_group, shift=UP),
            run_time=1.5
        )  # total 22.5s
        self.wait(30.14 - 22.5 - 1.0)  # total 29.14s

        # Transition out
        self.play(
            FadeOut(trigger_group),
            run_time=1.0
        )  # total 30.14s


        # ==========================================
        # SECTION 5: SUBAGENTS & WORKSPACES (Duration: 32.77s)
        # ==========================================
        self.add_sound("audio/ch14_5_subagents_outro.wav")

        title_sub = Text("14. Delegation & Subagenten", font_size=26, color=RUST_ORANGE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Transform(title_group, title_sub), run_time=1.0)  # total 1.0s

        self.wait(1.0)  # total 2.0s

        # Nodes diagram
        main_node = RoundedRectangle(corner_radius=0.12, width=2.8, height=1.0, color=PURPLE, fill_color=TERM_BG, fill_opacity=0.9, stroke_width=2.5).move_to([0, 1.2, 0])
        main_text = Text("Haupt-Agent", font_size=12, color=PURPLE, weight=BOLD).move_to(main_node.get_center())
        main_group = VGroup(main_node, main_text)

        sub1_node = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.0, color=CYAN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([-3.2, -1.0, 0])
        sub1_text = Text("Subagent 1\nCode-Recherche", font_size=10, color=CYAN, weight=BOLD).move_to(sub1_node.get_center())
        sub1_group = VGroup(sub1_node, sub1_text)

        sub2_node = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.0, color=GREEN, fill_color=LIGHT_BG, fill_opacity=0.9, stroke_width=2).move_to([3.2, -1.0, 0])
        sub2_text = Text("Subagent 2\nDebugger / Tests", font_size=10, color=GREEN, weight=BOLD).move_to(sub2_node.get_center())
        sub2_group = VGroup(sub2_node, sub2_text)

        arrow1 = Arrow(start=[0, 0.6, 0], end=[-3.2, -0.4, 0], stroke_width=3, color=GRAY)
        arrow2 = Arrow(start=[0, 0.6, 0], end=[3.2, -0.4, 0], stroke_width=3, color=GRAY)

        dia_group = VGroup(main_group, sub1_group, sub2_group, arrow1, arrow2)

        self.play(FadeIn(main_group, shift=DOWN), run_time=1.5)  # total 3.5s
        self.wait(1.5)  # total 5.0s

        self.play(
            Create(arrow1),
            FadeIn(sub1_group, shift=RIGHT),
            run_time=1.5
        )  # total 6.5s
        self.wait(1.5)  # total 8.0s

        self.play(
            Create(arrow2),
            FadeIn(sub2_group, shift=LEFT),
            run_time=1.5
        )  # total 9.5s
        self.wait(4.0)  # total 13.5s

        # Transition to Subagent Workspace modes card
        ws_rect = RoundedRectangle(corner_radius=0.15, width=9.0, height=4.2, color=CYAN, fill_color=TERM_BG, fill_opacity=0.95, stroke_width=2).move_to([0, -0.6, 0])
        ws_title = Text("Subagenten-Verzeichnis Modi (Workspaces)", font_size=14, color=CYAN, weight=BOLD).next_to(ws_rect.get_top(), DOWN, buff=0.3)
        
        ws_modes = VGroup(
            Text("• inherit -> Arbeitet im selben Ordner wie der Hauptagent", font_size=11, color=WHITE),
            Text("• branch  -> Erstellt eine isolierte Kopie des Projekts", font_size=11, color=WHITE),
            Text("• share   -> Nutzt ein geteiltes Verzeichnis (wie git worktree)", font_size=11, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(ws_title, DOWN, buff=0.4)
        ws_group = VGroup(ws_rect, ws_title, ws_modes)

        self.play(
            FadeOut(dia_group),
            FadeIn(ws_group, scale=0.9),
            run_time=1.5
        )  # total 15.0s
        self.wait(10.5)  # total 25.5s

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
            FadeOut(ws_group),
            FadeIn(outro_group, scale=0.8),
            FadeIn(gear, shift=UP),
            run_time=2.0
        )  # total 27.5s

        spin_time = 32.77 - 27.5 - 1.0  # spin_time is 4.27s
        self.play(Rotate(gear, angle=180 * DEGREES), run_time=spin_time, rate_func=linear)  # total 31.77s

        # Final FadeOut
        self.play(
            FadeOut(outro_group),
            FadeOut(gear),
            run_time=1.0
        )  # total 32.77s
