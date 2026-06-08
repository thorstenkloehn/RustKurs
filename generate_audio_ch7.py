import os
import json
from kokoro_onnx import Kokoro
import soundfile as sf
from pydub import AudioSegment

model_path = "/home/thorsten/kurs/checkpoints/kokoro-german/kokoro-martin.onnx"
voices_path = "/home/thorsten/kurs/checkpoints/kokoro-german/voices-martin.npz"

segments = {
    "ch7_1_intro": (
        "Willkommen zu Kapitel sieben. In dieser Lektion setzen wir unser Wissen in die Praxis um. "
        "Wir programmieren gemeinsam ein kleines Übungsprojekt, in dem wir die wichtigsten Datentypen "
        "und Variablenkonzepte aus den letzten Kapiteln vertiefen. Wir beginnen in der main-Funktion "
        "und legen als erstes eine Ganzzahl an."
    ),
    "ch7_2_ganzzahl": (
        "Wir deklarieren eine unveränderliche Variable ganzzahl vom Typ i32 mit dem Wert zehn. "
        "Um diesen Wert im Terminal auszugeben, nutzen wir das println-Makro auf zwei verschiedene Arten. "
        "Zuerst verwenden wir die direkte Interpolation mit geschweiften Klammern und dem Variablennamen. "
        "Danach nutzen wir die klassische Schreibweise, bei der die geschweiften Klammern als leere Platzhalter dienen "
        "und die Variable als Argument übergeben wird."
    ),
    "ch7_3_buchstabe_und_positional": (
        "Als Nächstes deklarieren wir eine Variable namens buchstabe vom Typ char, der wir den Buchstaben 'b' in einfachen "
        "Anführungszeichen zuweisen. Um beide Variablen auszugeben, nutzen wir Positionsargumente im println-Makro. "
        "Durch die Angabe von null und eins in den geschweiften Klammern können wir steuern, welches Argument an welcher "
        "Stelle im Text eingefügt wird. Das sorgt für maximale Flexibilität."
    ),
    "ch7_4_mutability_warning": (
        "Jetzt demonstrieren wir den Unterschied zwischen veränderlichen und unveränderlichen Variablen. "
        "Wir deklarieren eine Variable namens ganzahl, schreiben sie aber absichtlich mit nur einem 'z'. "
        "Zunächst machen wir sie veränderbar mit dem Schlüsselwort mut und weisen ihr den Startwert Null zu. "
        "Direkt in der nächsten Zeile weisen wir ihr den Wert zehn zu. Im Anschluss geben wir sie auf dem Bildschirm aus."
    ),
    "ch7_5_floats": (
        "Nun kommen die Fließkommazahlen ins Spiel. Wir erstellen eine Variable kommazahl vom Typ f64 und weisen ihr "
        "den Wert drei Komma eins vier drei vier vier zu. Um die Formatierung zu üben, versuchen wir im println-Makro, "
        "die Anzeige zu begrenzen. Wir verwenden dazu einen Formatbezeichner, der den Wert strukturiert ausgeben soll."
    ),
    "ch7_6_second_char": (
        "Zuletzt legen wir eine weitere char-Variable namens buchstabe mit dem großen Buchstaben 'B' an. Da in Rust Variablen "
        "standardmäßig unveränderlich sind und wir denselben Namen wiederverwenden, nutzen wir hier das Konzept des Shadowings. "
        "Die neue Variable überschattet die alte und wird anschließend mit println! ausgegeben."
    ),
    "ch7_7_first_run_warnings": (
        "Wir speichern unsere Datei und starten das Projekt im Terminal mit cargo run. Rust kompiliert den Code, aber "
        "der Compiler warnt uns. Er zeigt uns eine gelbe Warnung an: Die Variable ganzahl wird zwar als veränderbar deklariert "
        "und ihr wird der Wert zehn zugewiesen, aber der ursprüngliche Wert Null wird niemals gelesen. Das ist eine "
        "sogenannte ungenutzte Zuweisung, ein unused assignment. Wir schauen uns die Erklärung dazu in der VS Code "
        "AI-Hilfe auf der rechten Seite an, die uns detailliert erklärt, was das Problem ist."
    ),
    "ch7_8_refactoring": (
        "Wir beheben das Problem, indem wir den Code bereinigen. Da die Zuweisung des Wertes Null und die anschließende Mutation "
        "redundant sind, initialisieren wir ganzahl direkt mit dem Wert zehn und entfernen das mut-Schlüsselwort sowie die "
        "redundante Zuweisung. Die alte Mutation kommentieren wir aus. Wir führen das Programm erneut aus. Die Warnung über "
        "das unused assignment ist verschwunden. Der Compiler weist uns lediglich darauf hin, dass ganzahl nicht veränderbar "
        "sein muss. Das Programm gibt alle Werte korrekt im Terminal aus. Damit haben wir unser erstes Übungsprojekt erfolgreich "
        "abgeschlossen und die Grundlagen der Datentypen und Variablen gefestigt! Bis zum nächsten Kapitel."
    )
}

# Timestamps in milliseconds based on video visual events
start_times_ms = {
    "ch7_1_intro": 2000,
    "ch7_2_ganzzahl": 45000,
    "ch7_3_buchstabe_und_positional": 130000,
    "ch7_4_mutability_warning": 250000,
    "ch7_5_floats": 410000,
    "ch7_6_second_char": 530000,
    "ch7_7_first_run_warnings": 670000,
    "ch7_8_refactoring": 770000
}

def main():
    os.makedirs("audio", exist_ok=True)
    print("Loading Kokoro...")
    kokoro = Kokoro(model_path, voices_path)
    
    durations = {}
    
    # 1. Generate individual WAV files with speed=1.05 to sound modern and fit timings
    for name, text in segments.items():
        print(f"Generating audio for: {name}...")
        samples, sample_rate = kokoro.create(text, voice="martin", speed=1.05, lang="de")
        
        output_file = f"audio/{name}.wav"
        sf.write(output_file, samples, sample_rate)
        
        duration = len(samples) / sample_rate
        durations[name] = duration
        print(f"Saved {output_file} ({duration:.2f} seconds)")
        
    with open("audio/durations_ch7.json", "w") as f:
        json.dump(durations, f, indent=4)
        
    # 2. Assemble them using pydub
    print("\nAssembling full audio track...")
    # 13m 58.65s = 838.65s = 838650 ms
    video_duration_ms = 838650
    full_audio = AudioSegment.silent(duration=video_duration_ms, frame_rate=48000)
    
    for name in segments.keys():
        wav_path = f"audio/{name}.wav"
        segment_audio = AudioSegment.from_wav(wav_path)
        start_ms = start_times_ms[name]
        
        print(f"Overlaying {name} at {start_ms/1000:.2f}s...")
        full_audio = full_audio.overlay(segment_audio, position=start_ms)
        
    # Export final audio track
    output_audio_path = "audio/ch7_voiceover.wav"
    full_audio.export(output_audio_path, format="wav")
    print(f"Saved completed audio track to {output_audio_path}")

if __name__ == "__main__":
    main()
