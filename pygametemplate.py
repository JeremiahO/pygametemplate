# Pygame template - skeleton for a new pygame project

import pygame
import random

# First thing we need to do is tell pygame to make a windowThere
WIDTH = 360
HEIGHT = 480
FPS = 30

# Next thing were going to do is pygame.init() this initialize our pygame
pygame.init()

# We also want to include mixer this allows sounds in our game
pygame.mixer.init()

# Now we can create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Determine the size of the screen
pygame.display.set_caption("My Game") # Determines the title of the game at the top of the screen
clock = pygame.time.Clock()

# Game loop

# Were are using this to control our game, running or not running
running = True
while running:

    # Keep loop running at right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
