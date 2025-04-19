import pygame, sys, random
import psycopg2

# Database connection
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        score INT,
        level INT
    );
""")
conn.commit()

username = input("Enter your username: ")
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()

print("Welcome", username, "! Your user ID is", user_id)

cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
last = cur.fetchone()
if last:
    print("Last score:", last[0], "Level:", last[1])
else:
    print("No previous scores found.")

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 10
font = pygame.font.SysFont("Verdana", 20)

def get_walls(level):
    walls = []
    if level == 1:
        return []
    elif level == 2:
        for x in range(0, WIDTH, CELL_SIZE):
            walls.append((x, HEIGHT // 2))
    elif level == 3:
        for y in range(0, HEIGHT, CELL_SIZE):
            walls.append((WIDTH // 2, y))
    elif level >= 4:
        for x in range(0, WIDTH, CELL_SIZE):
            walls.append((x, CELL_SIZE))
            walls.append((x, HEIGHT - CELL_SIZE * 2))
        for y in range(CELL_SIZE * 2, HEIGHT - CELL_SIZE * 2, CELL_SIZE):
            walls.append((CELL_SIZE, y))
            walls.append((WIDTH - CELL_SIZE * 2, y))
    return walls

def generate_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            value = random.choice([1, 2, 3])
            time_spawned = pygame.time.get_ticks()
            return {"pos": (x, y), "value": value, "time": time_spawned}

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
paused = False
score = 0
level = 1
walls = get_walls(level)
food = generate_food()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    print("Paused. Score:", score, "Level:", level)
                    save = input("Save result? (y/n): ").lower()
                    if save == 'y':
                        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                        conn.commit()
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if paused:
        pygame.display.flip()
        clock.tick(10)
        continue

    head_x, head_y = snake[0]
    if direction == "UP": head_y -= CELL_SIZE
    elif direction == "DOWN": head_y += CELL_SIZE
    elif direction == "LEFT": head_x -= CELL_SIZE
    elif direction == "RIGHT": head_x += CELL_SIZE

    new_head = (head_x, head_y)

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake or new_head in walls:
        screen.fill(BLACK)
        screen.blit(font.render("GAME OVER", True, RED), (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (WIDTH // 2 - 60, HEIGHT // 2))
        screen.blit(font.render(f"Level: {level}", True, WHITE), (WIDTH // 2 - 60, HEIGHT // 2 + 30))
        pygame.display.flip()
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
        conn.commit()
        pygame.time.wait(3000)
        pygame.quit()
        cur.close()
        conn.close()
        sys.exit()

    if new_head == food["pos"]:
        snake.insert(0, new_head)
        score += food["value"]
        food = generate_food()
        if score % 4 == 0:
            level += 1
            FPS += 2
            walls = get_walls(level)
    elif pygame.time.get_ticks() - food["time"] > 5000:
        food = generate_food()
    else:
        snake.insert(0, new_head)
        snake.pop()

    pygame.draw.rect(screen, RED, (*food["pos"], CELL_SIZE, CELL_SIZE))
    screen.blit(font.render(str(food["value"]), True, WHITE), (food["pos"][0]+5, food["pos"][1]+2))

    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), (*wall, CELL_SIZE, CELL_SIZE))

    for i, block in enumerate(snake):
        color = (255, 255, 0) if i == 0 else GREEN
        pygame.draw.rect(screen, color, (*block, CELL_SIZE, CELL_SIZE))

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()в