import pygame
import radioSignalMinigame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
deltaTime = 0
keys = pygame.key.get_pressed()

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

rsm = radioSignalMinigame.RadioSignalMinigame(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * deltaTime
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * deltaTime
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * deltaTime
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * deltaTime

    rsm.update(keys)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # delta time in seconds since last frame, used for framerate-
    # independent physics.
    deltaTime = clock.tick(60) / 1000

pygame.quit()