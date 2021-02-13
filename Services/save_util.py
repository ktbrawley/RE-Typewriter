import random
import json
import os

save_file_path = "Save_Data/saved_progress.txt"


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
