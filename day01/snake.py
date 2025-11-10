import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
fps = 20
clock = pygame.time.Clock()
# Set game values
snake_size = 20
initialize = 20
head_x = WINDOW_WIDTH / 2
head_y = WINDOW_HEIGHT /2
snake_dx = 0
snake_dy = 0
score = 0
# Set colors
green = (0, 255, 0)
dark_green = (10,50 ,10 )
red = (255,0,0)
dark_red = (150,0,0)
white = (255,255,255)
# Set fonts

# Set text

# Set sounds and music

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentilalyl move all of the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
