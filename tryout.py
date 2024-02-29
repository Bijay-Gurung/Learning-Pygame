import pygame
import random

# pygame setup
pygame.init()
# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Assigning player as rectangle
snake = [pygame.Rect(300, 250, 50, 50)]  # Initialize as a list
# Initializing the size of snake
snake_size = 1

# Food
food = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)

# game Loop
running = True
while running:

    # refilling the screen with color
    screen.fill((0, 0, 0))

    # displaying player in frame
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), segment)

    # displaying food in frame
    pygame.draw.rect(screen, (255, 0, 0), food)

    # check if the snake eats the food
    if snake[0].colliderect(food):
        # Respawning food at random location
        food.x = random.randint(0, SCREEN_WIDTH - 20)
        food.y = random.randint(0, SCREEN_HEIGHT - 20)

        # Increasing snake size
        snake_size += 1

        # Adding new segment to the snake body
        new_segment = pygame.Rect(snake[-1].x, snake[-1].y, 50, 50)
        snake.append(new_segment)

    # Update the position of each segment
    for i in range(len(snake) - 1, 0, -1):
        snake[i].x = snake[i - 1].x
        snake[i].y = snake[i - 1].y

    # player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and snake[0].left > 0:
        snake[0].move_ip(-1, 0)
    elif key[pygame.K_d] and snake[0].right < SCREEN_WIDTH:
        snake[0].move_ip(1, 0)
    elif key[pygame.K_w] and snake[0].top > 0:
        snake[0].move_ip(0, -1)
    elif key[pygame.K_s] and snake[0].bottom < SCREEN_HEIGHT:
        snake[0].move_ip(0, 1)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if it clicks the close button then the game loop will stop
            running = False

    # Rendering the snake
    for segment in snake[:snake_size]:
        # Render only up to snake_size segments
        pygame.draw.rect(screen, (0, 255, 0), segment)

    # Rendering food
    pygame.draw.rect(screen, (255, 0, 0), food)

    # Update display
    pygame.display.update()

pygame.quit()
