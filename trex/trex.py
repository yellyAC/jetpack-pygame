import pygame

# Initialize pygame
pygame.init()

# Screen size constants
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

# Pygame window
screen = pygame.display \
    .set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize backgorund
background = pygame.image.load('morning.png')
background = pygame.transform \
    .scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_x_1 = 0
background_x_2 = background.get_width()
background_y = 0
background_speed = 1

# Setup fps management
FPS = 60
clock = pygame.time.Clock()

is_game_running = True
while is_game_running:
    clock.tick(FPS)

    # Animate background 
    background_x_1 -= background_speed
    background_x_2 -= background_speed
    if background_x_1 < background.get_width() * -1:
        background_x_1 = background.get_width()
    if background_x_2 < background.get_width() * -1:
        background_x_2 = background.get_width()

    # Draw background
    screen.blit(background, \
        (background_x_1, background_y))
    screen.blit(background, \
        (background_x_2, background_y))
    
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            is_game_running = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                is_game_running = False

    pygame.display.update()

