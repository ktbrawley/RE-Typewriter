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


def play(sound):
    mixer.music.load(sound)
    mixer.music.set_volume(0.4)
    mixer.music.play()
    mixer.fadeout(1)


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

    return saves + 1


def writeSaveToFile(save_info):
    f = open(save_file_path, 'a')
    f.write(save_info)
    f.close()


def saveProgress():
    save_room = getSaveRoom()
    save_count = getSaveCount()
    save_info = f"Claire / {save_count} / {save_room}\n"

    for char in save_info:
        if char == " ":
            play(space_soundeffect)
        else:
            play(char_soundeffect)
        print(char, sep="", end="", flush=True)
        time.sleep(.28)

    play(space_soundeffect)
    writeSaveToFile(save_info)
    print()
# ===================================================
# MAIN
# ====================================================


saveProgress()
