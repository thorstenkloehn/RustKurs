import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "intro": (
        "Willkommen zum ersten Kapitel unseres Rust-Kurses für Anfänger. Was ist Rust überhaupt? "
        "Rust ist eine moderne Systemprogrammiersprache, die für ihre außergewöhnliche Geschwindigkeit, "
        "Zuverlässigkeit und Speichersicherheit bekannt ist. Sie wurde entwickelt, um Speicherfehler und "
        "Abstürze komplett zu verhindern, ohne dabei Kompromisse bei der Performance einzugehen. "
        "Im Gegensatz zu älteren Sprachen bietet Rust diese Sicherheit direkt zur Kompilierzeit durch "
        "ein einzigartiges Konzept namens Ownership- und Borrow-System."
    ),
    "vergleich": (
        "Vergleichen wir Rust mit anderen bekannten Sprachen. C und C++ bieten zwar eine ähnlich hohe "
        "Performance, aber sie überlassen das Speichermanagement komplett dem Entwickler. Das führt oft "
        "zu kritischen Sicherheitslücken wie Buffer Overflows. Python hingegen ist extrem einfach zu "
        "lernen und speichersicher, läuft dafür aber deutlich langsamer, da es eine interpretierte "
        "Sprache mit einem Garbage Collector ist. Rust verbindet das Beste aus beiden Welten: die rohe "
        "Performance von C++ und die eingebaute Speichersicherheit von Python."
    ),
    "einsatzgebiete": (
        "Wo genau wird Rust eigentlich im IT-Sektor eingesetzt? Die Antwort lautet: Überall dort, "
        "wo maximale Sicherheit und extreme Performance kritisch sind. Erstens: In der Systemprogrammierung. "
        "Google schreibt große Teile von Android in Rust. Microsoft nutzt es für Windows-Kernel-Komponenten, "
        "und sogar im Linux-Kernel ist Rust mittlerweile offiziell integriert. Zweitens: In der Cloud- und "
        "Netzwerkinfrastruktur. Anbieter wie Amazon Web Services oder Cloudflare setzen massiv auf Rust, "
        "da es Ressourcen schont und Kosten senkt. Und drittens: Bei modernen Web-Tools und WebAssembly. "
        "Tools wie Turbopack oder Deno nutzen Rust, um Webanwendungen blitzschnell zu machen."
    ),
    "vorteile": (
        "Für Anfänger bietet Rust einige entscheidende Vorteile. Erstens: Der Compiler ist wie ein "
        "genialer Mentor. Seine Fehlermeldungen sind weltklasse. Sie erklären dir ganz genau, was "
        "falsch ist und machen konkrete Vorschläge zur Behebung. Zweitens: Mit dem Paketmanager Cargo "
        "wird das Verwalten von Abhängigkeiten, das Kompilieren und Testen zum Kinderspiel. Und drittens: "
        "Durch die garantierte Speichersicherheit lernst du von Anfang an, sauberen und korrekten Code zu schreiben."
    ),
    "nachteile": (
        "Es gibt jedoch auch Nachteile für Einsteiger. Die Lernkurve ist sehr steil. Konzepte wie das "
        "Ownership-System, Lifetimes und der Borrow Checker können anfangs frustrierend sein, wenn der "
        "Compiler deinen Code zurückweist. Zudem sind die Kompilierzeiten oft länger als bei einfacheren "
        "Sprachen. Aber lass dich davon nicht entmutigen! Die Mühe lohnt sich, denn Rust-Entwickler "
        "gehören zu den gefragtesten Programmierern weltweit. Lass uns direkt loslegen!"
    )
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.0, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        # Calculate duration in seconds
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("Audio generation complete! Durations saved to audio/durations.json")

if __name__ == "__main__":
    main()
