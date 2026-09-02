import  asyncio
import threading
import os
import edge_tts
import pygame 
import time

Voice = "en-PH-RosaNeural"
BUFFER_SIZE =1024

def remove_file(file_path):
    for _ in range(5):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            break
        except PermissionError:
            import time
            time.sleep(0.2)

async def amain(TEXT,output_file)-> None:
    try:
        cm_text = edge_tts.Communicate(TEXT,Voice)
        await cm_text.save(output_file)
        thread = threading.Thread(target=play_audio,args=(output_file,))
        thread.start()
        thread.join()

    except Exception as e:
        print(e)
    finally:
        remove_file(output_file)        


def play_audio(file_path):
    try:
        pygame.mixer.init()

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.quit()

    except Exception as e:
        print(e)


def speak(Text,output_file=None):
   try:
    if output_file is None:
     output_file=f"{os.getcwd()}/speech.mp3"
     asyncio.run(amain(Text,output_file))
   except Exception as e:
       print(e)

speak("hello i am jarvis")
speak("hello buddy,may i ")