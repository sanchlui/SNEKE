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
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)  # make a text object
title_rect = title_text.get_rect()  # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH // 2,
                     WINDOW_HEIGHT // 2)  # places the box containing the text object's center to the middle of the screen.

# TODO: make a score_text object and assign a font render to it with text "Score: 0", antialias of True, color of GREEN, background color of DARKRED
# TODO: make a score_rect object by assigning score_text.get_rect() to it.
# TODO: place the topleft of score_rect to an x coordinate of 10 and y coordinate of 10

# TODO: make a game_over_text object and assign a font render to it with text "GAMEOVER", antialias of True, color of RED, background color of DARKRED
# TODO: make a game_over_rect object by assigning game_over_text.get_rect() to it.
# TODO: place the center of game_over_rect to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT

# TODO: make a continue_text  object and assign a font render to it with text "Press any key to play again", antialias of True, color of RED, background color of DARKGREEN
# TODO: make a continue_rect  object by assigning continue_text.get_rect() to it.
# TODO: place the center of continue_rect  to an x coordinate of half the WINDOW_WIDTH and y coordinate of half the WINDOW_HEIGHT + 64

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

# TODO: make a tuple for the head coordinates named head_coord and set to head_x, head_y, SNAKE_SIZE, SNAKE_SIZE
# TODO: make head_rect in a way similar to apple_rect, but with color GREEN instead.

body_coords = []

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        # TODO: check if the event.type is pygame.KEYDOWN
            # Inside the block of the if statement where we checked if the eventy type is KEYDOWN
            # TODO: check if the event.key is pygame.K_LEFT.
                # Inside the block of the K_LEFT if statement
                # TODO: assign -1 * SNAKE_SIZE 'TO' snake_dx.  This moves the snake 1 SNAKE_SIZE to the left.
                # TODO: assign 0 'TO' snake_dy.  We may have been moving up or down.  This cancels that movement out.
            # TODO: check if the event.key is pygame.K_RIGHT.
                # Inside the block of the K_RIGHT if statement.
                # TODO: assign SNAKE_SIZE 'TO' snake_dx.  This moves the snake 1 SNAKE_SIZE to the right.
                # TODO: assign 0 'TO' snake_dy.  We may have been moving up or down.  This cancels that movement out.
            # TODO: check if the event.key is pygame.K_UP.
                # Inside the block of the K_UP if statement.
                # TODO: assign 0 'TO' snake_dx.  We may have been moving left or right.  This cancels that movement out.
                # TODO: assign -1 * SNAKE_SIZE 'TO' snake_dx. This moves the snake 1 SNAKE_SIZE up.
            # TODO: check if the event.key is pygame.K_DOWN.
                # Inside the block of the K_DOWN if statement.
                # TODO: assign 0 'TO' snake_dx.  We may have been moving left or right.  This cancels that movement out.
                # TODO: assign SNAKE_SIZE 'TO' snake_dx. This moves the snake 1 SNAKE_SIZE down.


    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list
    # TODO: call body_coords's insert function passing in the index (0) and head_coord
    # TODO: call body_coords's pop function passing in no arguments.

    # Update the x,y position of the snakes head and make a new coordinate
    # TODO: add snake_dx 'TO' head_x
    # TODO: add snake_dy 'TO' head_y
    # TODO: reassign (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE) 'TO' head_coord

    # Check for game over

    # Check for collisions

    # Update HUD
    # TODO: reassign to score_text much like you did previously, but now the text should be an f-string: f"Score: {score}"
    # TODO: same todo just ran out of room:  use same settings for alias, color, and background color

    # Fill the surface
    # TODO: Read below.  One TODO, require's explanation
    ''' 
    The display_surface has a function we can use called fill, which takes one color argument.  
    The act of using display_surface's fill is said as
    "Call display_surface's fill function and pass WHITE in as it's argument."
    It looks like this:  
    1. display_surface.fill(WHITE)
    '''

    # Blit HUD
    # TODO: Read below.  2 TODO's, require's explanation
    '''
    Blitting means copying an image from it's source (the code) to it's destination (the display) 
    This is necessary after updating the source (score changes, snake, and apple change etc.)
    1. "Call display_surface's blit function.  It takes 2 arguments, text and rect surrounding that text.  
    Pass in title_text and title_rect to blit the title to the screen
    2. repeat for a new call to display_surface's blit function passing in score_text and score_rect.  
    "We've just told the title and score to display.  
    '''

    # TODO: Read below.  3 TODO's, require's explanation
    '''
    1. for every body in body_coords do the following
    call pygame.draw.rect and pass in display_surface, DARKGREEN, and body
    2. assign to head_rect the results from calling pygame.draw.rect passing in display_surface, GREEN, and head_coord.
    3. assign to apple_rect the results from calling pygame.draw.rect passing in display_surface, RED, and apple_coord  
    '''



    # Blit assets
    # TODO: Read below.  2 TODO's, require's explanation
    '''
    Calling pygame.draw.rect is a way to blit rectangles.  
    The blit function for display_surface is for direct blitting.  
    2 ways to do similar things.  Update the display
    1. "Call pygame.draw.rect and passing in display_surface, GREEN, and head_coord for the head of the snake
    2. "Call pygame.draw.rct again pass in display_surface, RED, and apple_coord for the apple.  
    '''

    # Update display and tick clock
    # TODO: Read below. 2 TODO's, require's explanation
    '''
    1. Now we update the display by calling pygame.display's update function passing in no arguments.
    
    2. The while loop we are in is super fast.  We actually need to slow it down to our FPS of 20 seconds.  
    That's what our clock variable will do for us.  What until 20 frames have passed every second.  Then continue.  
    This is ticking the clock.   
    to tick the clock call the clock object's tick function passing in FPS
    '''

# End the game
pygame.quit()
