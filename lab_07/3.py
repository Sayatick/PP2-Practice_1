import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 25
STEP = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Move the Ball with Arrow Keys")

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

running = True
while running:
    pygame.time.delay(50)
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS > 0:
                ball_y -= STEP
            if event.key == pygame.K_DOWN and ball_y + BALL_RADIUS < HEIGHT:
                ball_y += STEP
            if event.key == pygame.K_LEFT and ball_x - BALL_RADIUS > 0:
                ball_x -= STEP
            if event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS < WIDTH:
                ball_x += STEP

    pygame.display.flip()

pygame.quit()