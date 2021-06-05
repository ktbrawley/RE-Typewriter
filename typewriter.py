#!/usr/local/bin/python3

import time
import Services.audio_player as audio_player
import Services.save_util as save_util

space_soundeffect = "Sound-Effects\Typewriter_Space.mp3"
char_soundeffect = "Sound-Effects\Typewriter_Character.mp3"


def saveProgress():
    save_room = save_util.getSaveRoom()
    save_count = save_util.getSaveCount()
    user = save_util.get_username()

    # Format save statement
    save_info = f"{user} / {save_count} / {save_room}\n"

    for char in save_info:
        if char == " ":
            audio_player.play(space_soundeffect)
        else:
            audio_player.play(char_soundeffect)
        print(char, sep="", end="", flush=True)
        time.sleep(.2)

    # Mark end of saving progress
    audio_player.play(space_soundeffect)
    save_util.writeSaveToFile(save_info)

    if __debug__:
        input('\nPress any key to return to the world of Survival Horror...')
    else:
        print()

    askUserToSave()


def exitProgram():
    audio_player.fadeout()
    time.sleep(1)
    exit()


def askUserToSave():
    user_choice = input(
        'Would you like to save your progress? (y/n): ').lower()
    if user_choice == 'y':
        saveProgress()
    elif user_choice == 'n':
        exitProgram()
    else:
        askUserToSave()


# ===================================================
# MAIN
# ====================================================
audio_player.init()
audio_player.playSaveTheme()
askUserToSave()
