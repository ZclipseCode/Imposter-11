import pygame
import spriteSheet
import random

class RadioSignalMinigame:
    def __init__(self, screen):
        # number buttons
        self.screen = screen
        self.buttons = []
        for i in range(10):
            self.buttons.append(Button())
        self.active_index = random.randint(0, len(self.buttons) - 1)
        self.selected_index = 0
        self.select_button(self.selected_index)

        # randomize number button
        self.randomize_timer = 0
        self.randomize_interval = 1

        # dials
        self.wasd_dial = Dial()
        self.arrows_dial = Dial()

    def update(self, keys, delta_time):
        self.keys = keys
        self.player_input()

        # randomize number button
        self.randomize_timer += delta_time
        if (self.randomize_timer > self.randomize_interval):
            self.randomize_timer = 0
            new_active_index = self.active_index
            while new_active_index == self.active_index:
                new_active_index = random.randint(0, len(self.buttons) - 1)
            self.activate_button(new_active_index)

        x = 50
        for i in range(len(self.buttons)):
            if i == self.active_index:
                self.buttons[i].activate()
            self.screen.blit(self.buttons[i].state, (x, 0))
            x += 40
        
        # dials
        self.screen.blit(self.wasd_dial.state, (50, 100))
        self.screen.blit(self.arrows_dial.state, (300, 100))
    
    def player_input(self):
        if self.keys[pygame.K_1]:
            self.select_button(0)
        elif self.keys[pygame.K_2]:
            self.select_button(1)
        elif self.keys[pygame.K_3]:
            self.select_button(2)
        elif self.keys[pygame.K_4]:
            self.select_button(3)
        elif self.keys[pygame.K_5]:
            self.select_button(4)
        elif self.keys[pygame.K_6]:
            self.select_button(5)
        elif self.keys[pygame.K_7]:
            self.select_button(6)
        elif self.keys[pygame.K_8]:
            self.select_button(7)
        elif self.keys[pygame.K_9]:
            self.select_button(8)
        elif self.keys[pygame.K_0]:
            self.select_button(9)
    
    def select_button(self, new_selected_index):
        self.buttons[self.selected_index].deselect()
        self.selected_index = new_selected_index
        self.buttons[self.selected_index].select()
    
    def activate_button(self, new_active_index):
        self.buttons[self.active_index].deactivate()
        self.active_index = new_active_index
        self.buttons[self.active_index].activate()

class Button:
    def __init__(self):
        button_sprites = spriteSheet.SpriteSheet('Assets/Button.png')
        self.green = button_sprites.get_image(0, 0, 32, 32)
        self.highlighted_green = button_sprites.get_image(32, 0, 32, 32)
        self.yellow = button_sprites.get_image(0, 32, 32, 32)
        self.highlighted_yellow = button_sprites.get_image(32, 32, 32, 32)
        self.red = button_sprites.get_image(0, 64, 32, 32)
        self.highlighted_red = button_sprites.get_image(32, 64, 32, 32)
        # increase image size
        self.green = pygame.transform.scale(self.green, (50, 50))
        self.highlighted_green = pygame.transform.scale(self.highlighted_green, (50, 50))
        self.yellow = pygame.transform.scale(self.yellow, (50, 50))
        self.highlighted_yellow = pygame.transform.scale(self.highlighted_yellow, (50, 50))
        self.red = pygame.transform.scale(self.red, (50, 50))
        self.highlighted_red = pygame.transform.scale(self.highlighted_red, (50, 50))

        self.active = False
        self.selected = False
        self.state = self.red

    def select(self):
        if self.active:
            self.state = self.highlighted_green
        else:
            self.state = self.highlighted_red
        self.selected = True
    
    def deselect(self):
        if self.active:
            self.state = self.yellow
        else:
            self.state = self.red
        self.selected = False

    def activate(self):
        if self.selected:
            self.state = self.highlighted_green
        else:
            self.state = self.yellow
        self.active = True

    def deactivate(self):
        if self.selected:
            self.state = self.highlighted_red
        else:
            self.state = self.red
        self.active = False

class Dial:
    def __init__(self):
        dial_sprites = spriteSheet.SpriteSheet('Assets/Dial.png')
        self.dial_correct = dial_sprites.get_image(0, 0, 32, 32)
        self.dial_incorrect = dial_sprites.get_image(0, 32, 32, 32)
        # increase image size
        self.dial_correct = pygame.transform.scale(self.dial_correct, (150, 150))
        self.dial_incorrect = pygame.transform.scale(self.dial_incorrect, (150, 150))

        self.state = self.dial_incorrect