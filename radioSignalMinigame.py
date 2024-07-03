import pygame
import spriteSheet

class RadioSignalMinigame:
    def __init__(self, screen):
        self.screen = screen
        buttonSprites = spriteSheet.SpriteSheet('Assets/Button.png')
        self.button = buttonSprites.get_image(0, 0, 32, 32)

    def update(self):
        self.screen.blit(self.button, (0, 0))