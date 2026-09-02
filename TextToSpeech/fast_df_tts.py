import subprocess
import tempfile
import threading
from playsound import playsound

def speak(text: str, voice: str = "hi-IN-MadhurNeural") -> None:
    try:
        print("Speaking:", text) 

        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            output_file = tmpfile.name

        command = [
            "edge-tts",
            "--voice", voice,
            "--text", text,
            "--write-media", output_file
        ]

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )

        if result.stderr:
            print("STDERR:", result.stderr)

        threading.Thread(target=playsound, args=(output_file,)).start()

    except subprocess.CalledProcessError as e:
        print("Command failed:", e)
        print("STDERR:", e.stderr)
    except Exception as e:
        print(e)

speak("i am jarvis")
speak("hey there i am here to present my topic")