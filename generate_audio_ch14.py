import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch14_1_intro": (
        "Willkommen zum vierzehnten Kapitel unseres Rust-Kurses für Anfänger. In dieser Lektion stellen wir "
        "das Antigravity CLI vor – das offizielle, terminalbasierte Interface für Googles Antigravity-Entwicklungsplattform. "
        "Es dient als leichtgewichtige, tastaturgesteuerte Alternative zur Desktop-App und unterstützt dich direkt "
        "bei der agentenbasierten Softwareentwicklung."
    ),
    "ch14_2_install_start": (
        "Die Installation erfolgt plattformabhängig über ein kurzes Terminal-Skript. Unter macOS und Linux lädst du es "
        "direkt in deine Bash, unter Windows nutzt du die PowerShell. Nach der Installation startest du das CLI einfach, "
        "indem du in deinen Projektordner navigierst und den Befehl a g y aufrufst. Beim ersten Start wirst du durch ein "
        "kurzes Setup für Farbthemen und Darstellungsmodi geführt, danach kannst du dem Agenten direkt Aufgaben in natürlicher Sprache stellen."
    ),
    "ch14_3_settings_paths": (
        "Wo speichert das CLI seine Daten? Alle Konfigurationen und Gesprächsprotokolle liegen unter Punkt gemini slash "
        "antigravity-cli in deinem Benutzerverzeichnis. Deine persistenten Einstellungen werden in der Datei settings Punkt json "
        "gespeichert. Die gesamten Transkripte und Logdateien deiner Sitzungen findest du im Ordner brain, sortiert nach der "
        "jeweiligen Konversations-I-D. Plugins und MCP-Serverkonfigurationen werden im Ordner plugins abgelegt."
    ),
    "ch14_4_project_configs": (
        "Für die Steuerung der Agenten in deinem konkreten Projekt nutzt das CLI zwei wichtige lokale Dateien im Projektverzeichnis. "
        "Die Datei agents Punkt m d enthält projektspezifische Richtlinien, Verzeichnis-Zuweisungen und Design-Ausschlüsse. "
        "Hier kannst du explizite Regeln für Subagenten definieren, wie zum Beispiel die Einschränkung von Schreibrechten auf bestimmte Ordner, "
        "das Verbieten von Systembefehlen oder das Erzwingen des branch-Modus für kritische Codeänderungen. Die Datei skills Punkt m d "
        "beschreibt wiederum Custom Skills für wiederkehrende Aufgaben."
    ),
    "ch14_5_subagents_outro": (
        "Für sehr komplexe Aufgaben kann das CLI im Hintergrund spezialisierte Subagenten erstellen. Diese arbeiten in eigenen Workspace-Verzeichnissen "
        "und bieten drei Modi: Erstens, in-her-it: Der Subagent nutzt denselben Ordner wie der Hauptagent. Zweitens, branch: Es wird eine komplett isolierte Kopie "
        "des Verzeichnisses zum gefahrlosen Experimentieren erstellt. Und drittens, share: Ein geteilter Arbeitsbereich ähnlich einem Git Worktree, der Speicherplatz "
        "spart. Das war unser Tutorial zum Antigravity CLI. Probiere es direkt aus, vielen Dank fürs Zuschauen und viel Erfolg!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.05, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        # Calculate duration in seconds
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations_ch14.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations_ch14.json")

if __name__ == "__main__":
    main()
