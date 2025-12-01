import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 20
clock = pygame.time.Clock()
# Set game values

SNAKE_SIZE = 20


head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0
# Set colors
green = (0, 255, 0)
dark_green = (10, 50, 10)
red = (255, 0, 0)
dark_red = (150, 0, 0)
white = (255, 255, 255)
# Set fonts
font = pygame.font.SysFont("gabriola", 48)

# Set text
title_text = font.render("~~snake~~", True, green, dark_red)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render("Score: 0", True, green, dark_red)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("Game Over", True, red, dark_red)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Continue", True, red, dark_green)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)
# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, red, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, green, head_coord)

body_coords = []

# The main game loop
running = True
is_paused = False
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dx = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dx = SNAKE_SIZE

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentilalyl move all of the snakes body by one position in the list
    body_coords.insert(0, head_coord)
    body_coords.pop(0)
    # Update the x,y position of the snakes head and make a new coordinate
    snake_dx = head_x
    snake_dy = head_y
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        pygame.display.update()
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_paused = False
                running = False
            if event.type == pygame.KEYDOWN:
                score = 0

    # Check for collisions

    # Update HUD
    score_text = font.render(f"Score: {score}", True, green, dark_red)
    # Fill the surface
    display_surface.fill(white)

    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    # Blit assets
    pygame.draw.rect(display_surface, green, head_coord)
    pygame.draw.rect(display_surface, red, apple_coord)
    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)
# End the game
pygame.quit()
