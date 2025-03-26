import pygame, sys, random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()
FPS = 10  # starting speed

# Fonts
font = pygame.font.SysFont("Verdana", 20)

# Snake and food setup
snake = [(100, 100), (80, 100), (60, 100)]  # initial body
direction = "RIGHT"

# Function to generate food at valid position
# Generate new food with weight and timestamp
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            value = random.choice([1, 2, 3])  # Random weight
            timer = pygame.time.get_ticks()  # Save spawn time
            return {"pos": (x, y), "value": value, "time": timer}

food = generate_food()
score = 0
level = 1

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Control snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    if direction == "DOWN":
        head_y += CELL_SIZE
    if direction == "LEFT":
        head_x -= CELL_SIZE
    if direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # ✅ Border collision detection
        # ✅ Border or self-collision ends game
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake):
        # Show Game Over Screen
        screen.fill(BLACK)

        game_over_text = font.render("GAME OVER", True, RED)
        final_score_text = font.render(f"Score: {score}", True, WHITE)
        final_level_text = font.render(f"Level: {level}", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(final_score_text, (WIDTH // 2 - 60, HEIGHT // 2))
        screen.blit(final_level_text, (WIDTH // 2 - 60, HEIGHT // 2 + 30))

        pygame.display.flip()
        pygame.time.wait(3000)  # 3 seconds pause

        pygame.quit()
        sys.exit()
        
    # Eat food
    if new_head == food["pos"]:
        snake.insert(0, new_head)
        score += food["value"]
        food = generate_food()

        # ✅ Level system: every 4 food = next level
        if score % 4 == 0:
            level += 1
            FPS += 2  # Increase speed
            
    # ✅ Check if food expired (5 seconds)
    if pygame.time.get_ticks() - food["time"] > 5000:  # 5000 ms = 5 sec
        food = generate_food()

    else:
        snake.insert(0, new_head)
        snake.pop()

    # Draw food
    pygame.draw.rect(screen, RED, (*food["pos"], CELL_SIZE, CELL_SIZE))
    
    # Show food value on top of food
    value_text = font.render(str(food["value"]), True, WHITE)
    screen.blit(value_text, (food["pos"][0] + 5, food["pos"][1] + 2))

    # Draw snake with yellow head and green body
    for i, block in enumerate(snake):
        if i == 0:
            pygame.draw.rect(screen, (255, 255, 0), (*block, CELL_SIZE, CELL_SIZE))  # Yellow head
        else:
            pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))  # Green body
        
    # ✅ Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()