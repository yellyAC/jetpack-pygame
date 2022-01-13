import pygame

# Initialize pygame
pygame.init()

# Intialize screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up background
background = pygame.image.load('background.jpg')

# Set up ship
ship = pygame.image.load('ship.png')
ship = pygame.transform.scale(ship, (100, 100))
ship_x = (SCREEN_WIDTH / 2) - (ship.get_width() / 2)
ship_y = SCREEN_HEIGHT - (ship.get_height())

print(ship.get_width())
print(ship.get_height())

# Set up fps
clock = pygame.time.Clock()
game_loop = True; fps = 30

# Draw background
bg_x = 0
bg_y_1 = 0
bg_y_2 = background.get_height()

speed = 5
movement_speed = 5

# Bala
bullets = []
bullet_image = pygame.image.load('bullet.png')
bullet_image = pygame.transform.scale(bullet_image, (12, 12))

print ("background width" + str(background.get_width()))
print ("background height" + str(background.get_height()))

while game_loop:
    # Modulate frames 
    clock.tick(fps) 

    # Animate
    bg_y_1 = bg_y_1 + speed
    bg_y_2 = bg_y_2 + speed

    # Reset position if y lagpas
    if bg_y_1 > background.get_height():
        bg_y_1 = background.get_height()
    if bg_y_2 > background.get_height():
        bg_y_2 = background.get_height()

    print(bg_y_2)

    screen.blit(background, (bg_x, bg_y_1))
    screen.blit(background, (bg_x, bg_y_2))

    screen.blit(ship, (ship_x, ship_y))

    for bullet in bullets:
         screen.blit(bullet_image, pygame.Rect(bullet[0], bullet[1], bullet_image.get_width(), bullet_image.get_height()))

    for b in range(len(bullets)):
        bullets[b][1] -= 10

    for bullet in bullets[:]:
        if bullet[1] < 0:
            bullets.remove(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_y = ship_y - movement_speed
    if keys[pygame.K_DOWN]:
        ship_y = ship_y + movement_speed
    if keys[pygame.K_LEFT]:
        ship_x = ship_x - movement_speed
    if keys[pygame.K_RIGHT]:
        ship_x = ship_x + movement_speed
    if keys[pygame.K_SPACE]:
        bullets.append([ship_x + ship.get_width() / 2, ship_y])

    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            game_loop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                game_loop = False
            

    pygame.display.update()
