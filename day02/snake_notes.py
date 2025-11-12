import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
# TODO: make a variable (constant) called FPS and initialize to 20
clock = pygame.time.Clock()

# Set game values
# TODO: make a variable (constant) named SNAKE_SIZE and initialize to 20

# TODO: make a variable named head_x and assign half of the WINDOW_WIDTH to it.  use integer division //  (i.e. 11 / 2 is 5.5,  11//2 is 5)
# TODO: make a variable named head_y and assign half of the WINDOW_HEIGHT + 100 to it.  use integer division //

# TODO: make a variable named snake_dx and assign 0 to it.
# TODO: repeat for a variable named snake_dy

# TODO: make a variable named score and assign 0 to it.

# Set colors
GREEN = (0, 255, 0)  # (r, g, b)
# TODO: make a DARKGREEN color with rgb(10, 50, 10)
# TODO: make a RED
DARKRED = (150, 0, 0)
# TODO: make a WHITE

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED) #make a text object
title_rect = title_text.get_rect() # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) # places the box containing the text object's center to the middle of the screen.

#TODO: make a score_text object and assign a font render to it with text "Score: 0", antialias of True, color of GREEN, background color of DARKRED
#TODO: make a score_rect object by assigning score_text.get_rect() to it.
#TODO: place the topleft of score_rect to an x coordinate of 10 and y coordinate of 10

#TODO: make a game_over_text object and assign a font render to it with text "GAMEOVER", antialias of True, color of RED, background color of DARKRED
#TODO: make a game_over_rect object by assigning game_over_text.get_rect() to it.
#TODO: place the center of game_over_rect to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT

#TODO: make a continue_text  object and assign a font render to it with text "Press any key to play again", antialias of True, color of RED, background color of DARKGREEN
#TODO: make a continue_rect  object by assigning continue_text.get_rect() to it.
#TODO: place the center of continue_rect  to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT + 64

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

# TODO: make a tuple for the head coordinates named head_coord and set to head_x, head_y, SNAKE_SIZE, SNAKE_SIZE
# TODO: make head_rect in a way similar to apple_rect, but with color GREEN instead.


# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list

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

