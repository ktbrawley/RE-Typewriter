from pygame import mixer

save_theme = "${cwd}/../Sound-Effects/secureplace.wav"


def init():
    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    mixer.init()
    print()


def play(sound, volume=0.4):
    queuedSound = mixer.Sound(sound)
    channel = mixer.find_channel()
    channel.set_volume(volume)
    channel.play(queuedSound)


def stop():
    mixer.stop()


def fadeout():
    mixer.fadeout(1000)


def playSaveTheme(theme=save_theme):
    play(theme, volume=0.3)
