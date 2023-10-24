#cmd 
#pip install pygame
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_COLOR = (0, 128, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT - 50, 30, 30)
ball_speed_x = BALL_SPEED
ball_speed_y = -BALL_SPEED

# Paddle properties
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 10, 120, 10)

# Bricks
bricks = []
for i in range(5):
    for j in range(8):
        brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 50, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # Update the ball's position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y

    # Game over condition
    if ball.top >= HEIGHT:
        game_over = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw everything
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.delay(30)

# Game over screen
font = pygame.font.Font(None, 36)
text = font.render("Game Over!", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a while before quitting
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
sys.exit()
