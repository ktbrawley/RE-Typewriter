#!/usr/local/bin/python3

from pygame import mixer
import time
import random
import json
import os

space_soundeffect = "C:\Dev\Projects\RE-Typewriter\Sound-Effects\Typewriter_Space.mp3"
char_soundeffect = "C:\Dev\Projects\RE-Typewriter\Sound-Effects\Typewriter_Character.mp3"
save_file_path = "Save_Data/saved_progress.txt"

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
mixer.init()


def play(sound, volume=0.4):
    queuedSound = mixer.Sound(sound)
    channel = mixer.find_channel()
    channel.set_volume(volume)
    channel.play(queuedSound)


def getSaveRoom():
    f = open('Save_Data/save_room_locations.json', 'r').read()
    rooms = json.loads(f)
    room = random.choice(rooms)
    return room['name']


def getSaveCount():
    saves = 0
    if os.path.isfile(save_file_path):
        f = open(save_file_path, 'r')
        saves = len(f.readlines())
    else:
        f = open(save_file_path, 'x')
        f.close()

    save_count = saves + 1
    return f'0{save_count}' if save_count < 10 else f'{save_count}'


def writeSaveToFile(save_info):
    f = open(save_file_path, 'a')
    f.write(save_info)
    f.close()


def get_username():
    return os.getlogin()


def saveProgress():
    save_room = getSaveRoom()
    save_count = getSaveCount()
    user = get_username()

    # Format save statement
    save_info = f"{user} / {save_count} / {save_room}\n"

    for char in save_info:
        if char == " ":
            play(space_soundeffect)
        else:
            play(char_soundeffect)
        print(char, sep="", end="", flush=True)
        time.sleep(.28)

    play(space_soundeffect)
    writeSaveToFile(save_info)
    input('Press any key to exit...\n')
    mixer.fadeout(1000)
    time.sleep(1)


def playSaveTheme():
    save_theme = "Sound-Effects/secureplace.wav"
    play(save_theme, volume=0.3)
    # ===================================================
    # MAIN
    # ====================================================


playSaveTheme()
user_choice = input('Would you like to save your progress?')
saveProgress()
