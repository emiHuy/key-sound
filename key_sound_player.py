from pynput import keyboard
import pygame
import random
from utils import resource_path

class KeySoundPlayer:
    def __init__(self):
        self._theme = "Minecraft"
        self._volume_adj_factor = 1
        self._listener = None

    def run(self):
        pygame.mixer.init()
        self._listener = keyboard.Listener(on_press=self.key_pressed)
        self._listener.start()
        input()         
    
    def end(self):
        self._listener.stop()
        
    def set_theme(self, new_theme):
        self._theme = new_theme

    def set_volume_adj_factor(self, new_volume_adj_factor):
        self._volume_adj_factor = new_volume_adj_factor

    def key_pressed(self, key):
        match(self._theme):
            case "Minecraft":
                self.minecraft_theme(key)
            case "Super Mario Bros.":
                self.mario_theme(key)
            case "Animal Crossing":
                self.animal_crossing_theme(key)
            case _:
                pass

    def play_sound(self, path, volume=1):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume*self._volume_adj_factor)
        sound.play()

    def minecraft_theme(self, key):
        try:
            if key == keyboard.Key.enter:
                self.play_sound(resource_path("assets/sounds/minecraft/click.wav"))
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.space:
                variation = random.randint(1,4)
                self.play_sound(resource_path("assets/sounds/minecraft/sand/sand" + str(variation) + ".wav"))
            elif key.char.isalpha():
                variation = random.randint(1,4)
                self.play_sound(resource_path("assets/sounds/minecraft/wood/wood" + str(variation) + ".wav"))
            elif key.char.isnumeric():
                variation = random.randint(1,4)
                self.play_sound(resource_path("assets/sounds/minecraft/stone/stone" + str(variation) + ".wav"))
            else:
                variation = random.randint(1,4)
                self.play_sound(resource_path("assets/sounds/minecraft/grass/grass" + str(variation) + ".wav"), 0.6)
        except:
            self.play_sound(resource_path("assets/sounds/minecraft/pop.wav"), 0.6)

    def mario_theme(self, key):
        try:
            if key == keyboard.Key.enter:
                self.play_sound(resource_path("assets/sounds/mario/pipe.wav"))
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.space:
                self.play_sound(resource_path("assets/sounds/mario/jump.wav"), 0.9)
            elif key.char.isalpha():
                self.play_sound(resource_path("assets/sounds/mario/fireball.wav"), 0.8)
            elif key.char.isnumeric():
                self.play_sound(resource_path("assets/sounds/mario/bump.wav"), 0.8)
            else:
                self.play_sound(resource_path("assets/sounds/mario/bump.wav"), 0.8)
        except:
            self.play_sound(resource_path("assets/sounds/mario/coin.wav"), 0.5)

    def animal_crossing_theme(self, key):
        try:
            if key == keyboard.Key.enter:
                self.play_sound(resource_path("assets/sounds/animal-crossing/confirm.mp3"), 0.3)
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.space or key.char.isalpha() or key.char.isnumeric():
                self.play_sound(resource_path("assets/sounds/animal-crossing/intense.mp3"), 1.4)
            else:
                self.play_sound(resource_path("assets/sounds/animal-crossing/greetings.mp3"), 1.2)
        except:
            self.play_sound(resource_path("assets/sounds/animal-crossing/decline.mp3"), 0.8)

if __name__ == "__main__":
    player = KeySoundPlayer()
    player.run()