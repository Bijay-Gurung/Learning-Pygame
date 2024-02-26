import pygame

# pygame setup
pygame.init()
# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Assigning player as rectangle
player = pygame.Rect((300,250,50,50))

# game Loop
running = True
while running:

    # refilling the screen with color
    screen.fill((0,0,0))

    # displaying player in frame
    pygame.draw.rect(screen, (255,0,0), player)

    # player movement
    key = pygame.key.get_pressed()
    """
    when we move the plyer it keep the traces beacuse it save our history. to remove the traces we have to refill
    the screen with color.
    """
    if key[pygame.K_a] == True and player.left > 0:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True and player.right < SCREEN_WIDTH:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True and player.top > 0:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0,1)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if it click the close button then the game loop will stop
            running = False

    pygame.display.update()
pygame.quit()