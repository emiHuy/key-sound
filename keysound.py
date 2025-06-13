from pynput import keyboard
import pygame
import random

def key_pressed(key):
    animal_crossing_theme(key)

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

def mario_theme(key):
    try:
        if key == keyboard.Key.enter:
            play_sound("assets/sounds/mario/pipe.wav")
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.space:
            play_sound("assets/sounds/mario/jump.wav", 0.9)
        elif key.char.isalpha():
            play_sound("assets/sounds/mario/fireball.wav", 0.8)
        elif key.char.isnumeric():
            play_sound("assets/sounds/mario/bump.wav", 0.8)
        else:
            play_sound("assets/sounds/mario/bump.wav", 0.8)
    except:
         play_sound("assets/sounds/mario/coin.wav", 0.5)

def animal_crossing_theme(key):
    try:
        if key == keyboard.Key.enter:
            play_sound("assets/sounds/animal-crossing/confirm.mp3", 0.3)
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.space or key.char.isalpha() or key.char.isnumeric():
            play_sound("assets/sounds/animal-crossing/intense.mp3", 1.4)
        else:
            play_sound("assets/sounds/animal-crossing/greetings.mp3", 1.2)
    except:
         play_sound("assets/sounds/animal-crossing/decline.mp3", 0.8)

def run():
    pygame.mixer.init()
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input() 

if __name__ == "__main__":
    run()