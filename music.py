import pygame
import time
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

SONG = "song.mp3"
START_AT = 181
DURATION = 238

lyrics = [
    (1.35, "Alo jole Alo jolee.."),
    (5, "Amar mone amar monee.."),
    (9, "Tomar chobi chokher samne ese vasee.."),
    (16.4, "Brishti pore brishti poree.."),
    (20, "Thother majhe golpo jome.."),
    (24, "Tomay ami khujhi sarakkhon.."),
    (29, "Ei amar mon.."),
    (34.3, "Ei amar mon.."),
    (37, "Ei amar mon.."),
    (46, "Tumi..")
]

def fmt(seconds):
    seconds = int(seconds)
    return f"{seconds // 60:02}:{seconds % 60:02}"

pygame.mixer.init()
pygame.mixer.music.load(SONG)

# Start song at 2:57
pygame.mixer.music.play(start=START_AT)

start = time.time()
index = 0
current_line = ""
typed_chars = 0
last_type = 0

try:
    while pygame.mixer.music.get_busy():
        elapsed = time.time() - start
        song_time = START_AT + elapsed

        # Select the correct lyric line
        while index < len(lyrics) and elapsed >= lyrics[index][0]:
            current_line = lyrics[index][1]
            typed_chars = 0
            last_type = time.time()
            index += 1

        # Typewriter effect
        if typed_chars < len(current_line):
            if time.time() - last_type >= 0.10:
                typed_chars += 1
                last_type = time.time()

        progress = min(song_time / DURATION, 1.0)
        width = 30
        filled = int(progress * width)
        bar = "█" * filled + "░" * (width - filled)

        # Redraw terminal without scrolling
        sys.stdout.write("\033[H\033[J\033[?25l")

        print(Fore.CYAN + "Level Five :: Tumi (Official Single) "
              + Fore.GREEN + "[● PLAYING]\n")

        print(Fore.WHITE + "» " +
              Fore.YELLOW + current_line[:typed_chars] + "\n")

        print(
            fmt(song_time), "/", fmt(DURATION),
            "[" + Fore.MAGENTA + bar + Style.RESET_ALL + "]"
        )

        sys.stdout.flush()
        time.sleep(0.05)

finally:
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
    pygame.mixer.music.stop()
    pygame.mixer.quit()