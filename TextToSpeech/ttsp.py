import asyncio
import edge_tts
import os
import time

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
VOICE = "en-CA-ClaraNeural"

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

AUDIO_FILE = os.path.join(
    BASE_DIR,
    "Agies.mp3"
)

pygame.mixer.init()


async def generate_audio(text):

    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save(AUDIO_FILE)


def speak(text):

    try:

        total_start = time.perf_counter()

        # Generate audio
        print("\nGenerating audio...")

        tts_start = time.perf_counter()

    
        pygame.mixer.music.stop()

        try:
            pygame.mixer.music.unload()
        except:
            pass

        asyncio.run(
            generate_audio(text)
        )

        tts_end = time.perf_counter()

        print(
            f"TTS generation : "
            f"{tts_end - tts_start:.3f} sec"
        )

    
        # Load audio

        load_start = time.perf_counter()

        pygame.mixer.music.load(AUDIO_FILE)

        load_end = time.perf_counter()

        print(
            f"Audio loading  : "
            f"{load_end - load_start:.3f} sec"
        ) 


        # Play

        print("Speaking...")

        playback_start = time.perf_counter()

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(20)

        playback_end = time.perf_counter()

        print(
            f"Playback time  : "
            f"{playback_end - playback_start:.3f} sec"
        )

        
        # Total

        total_end = time.perf_counter()

        print(
            f"Total time     : "
            f"{total_end - total_start:.3f} sec"
        )

        print("-" * 45)

    except Exception as e:

        print(
            "TTS Error:",
            e
        )


speak("Hello sir, I am Jarvis")
speak("I am your personal assistant, I can help you with your daily tasks")