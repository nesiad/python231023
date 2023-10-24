import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 색깔
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_speed = 5

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# 블록 설정
block_width = 70
block_height = 20
block_x = (WIDTH - block_width) // 2
block_y = 100

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 패들 충돌 처리
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    if (
        ball_y >= paddle_y - ball_radius
        and paddle_x <= ball_x <= paddle_x + paddle_width
    ):
        ball_speed_y = -ball_speed_y

    # 블록과 공 충돌 처리
    if (
        block_x <= ball_x <= block_x + block_width
        and block_y <= ball_y <= block_y + block_height
    ):
        ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, BLUE, (block_x, block_y, block_width, block_height))

    pygame.display.update()