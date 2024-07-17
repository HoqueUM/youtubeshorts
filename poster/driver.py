from reddit_getter import get_text
import subprocess
from editor import editor
from deleter import deleter
import time

def driver():
    text, title = get_text()
    try:
        command = f"echo '{text}' | piper --model en_US-lessac-medium --output_file tts_audio.mp3"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        output = e.output
        print(output)
    
    editor()

    try:
        command = f'python3 uploader.py --file="final_clip_with_subtitles.mp4" --title="{title}" --description="{title}" --keywords="reddit,shorts,funny,gaming,mems" --category="20" --privacyStatus="public"'
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")
    

    deleter()

    return True

if __name__ == '__main__':
    while(True):
        driver()
        time.sleep(600)