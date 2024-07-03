import pygame
import spriteSheet
import random

class RadioSignalMinigame:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        for i in range(10):
            self.buttons.append(Button())
        self.highlighted_index = random.randint(0, len(self.buttons))

    def update(self):
        x = 0
        for i in range(len(self.buttons)):
            if i == self.highlighted_index:
                self.buttons[i].state = self.buttons[i].highlighted_red
            self.screen.blit(self.buttons[i].state, (x, 0))
            x += 32

class Button:
    def __init__(self):
        button_sprites = spriteSheet.SpriteSheet('Assets/Button.png')
        self.green = button_sprites.get_image(0, 0, 32, 32)
        self.highlighted_green = button_sprites.get_image(32, 0, 32, 32)
        self.yellow = button_sprites.get_image(0, 32, 32, 32)
        self.highlighted_yellow = button_sprites.get_image(32, 32, 32, 32)
        self.red = button_sprites.get_image(0, 64, 32, 32)
        self.highlighted_red = button_sprites.get_image(32, 64, 32, 32)

        self.highlighted = False
        self.selected = False
        self.state = self.red

    def select(self):
        if self.highlighted == True:
            self.state = self.green
        else:
            self.state = self.yellow
        self.selected = True
    
    def deselect(self):
        if self.highlighted == True:
            self.state = self.highlighted_red
        else:
            self.state = self.red
        self.selected = False