from pynput import keyboard
import pygame
import random

def key_pressed(key):
    minecraft_theme(key)
    # pygame.mixer.music.load("assets/sounds/pop.mp3")
    # pygame.mixer.music.play(loops=0)

def play_sound(path, volume=1):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    sound.play()

def minecraft_theme(key):
    try:
        if key == keyboard.Key.enter:
            play_sound("assets/sounds/minecraft/click.wav")
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.space:
            variation = random.randint(1,4)
            play_sound("assets/sounds/minecraft/sand/sand" + str(variation) + ".wav")
        elif key.char.isalpha():
            variation = random.randint(1,4)
            play_sound("assets/sounds/minecraft/wood/wood" + str(variation) + ".wav")
        elif key.char.isnumeric():
            variation = random.randint(1,4)
            play_sound("assets/sounds/minecraft/stone/stone" + str(variation) + ".wav")
        else:
            variation = random.randint(1,4)
            play_sound("assets/sounds/minecraft/grass/grass" + str(variation) + ".wav", 0.6)
    except:
        play_sound("assets/sounds/minecraft/pop.wav", 0.6)
    
if __name__ == "__main__":
    pygame.mixer.init()
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()
