import pygame, sys, random
import psycopg2

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

print("Welcome ", username, "! Your user ID is", user_id)

cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
last = cur.fetchone()
if last:
    print("Last score: ",last[0]," Level: ", last[1])
else:
    print("No previous scores found.")

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

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
paused = False

def generate_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            value = random.choice([1, 2, 3])
            time_spawned = pygame.time.get_ticks()
            return {"pos": (x, y), "value": value, "time": time_spawned}

food = generate_food()
score = 0
level = 1

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pause toggle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    print("Game Paused. Score: ",score, "Level: ", level)
                    save = input("Do you want to save your result? (y/n): ").lower()
                    if save == 'y':
                        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                        conn.commit()
                        print("Score saved.")
                    else:
                        print("Score not saved.")
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if paused:
        pygame.display.flip()
        clock.tick(10)
        continue

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

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake:
        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2))
        screen.blit(level_text, (WIDTH // 2 - 60, HEIGHT // 2 + 30))
        pygame.display.flip()

        # ADDED codes
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
        conn.commit()
        print("GAME OVER\nFinal Score: ", score, " Level: ", level,"Saved! ;) ")

        pygame.time.wait(4000)
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
    elif pygame.time.get_ticks() - food["time"] > 5000:
        food = generate_food()
    else:
        snake.insert(0, new_head)
        snake.pop()

    pygame.draw.rect(screen, RED, (*food["pos"], CELL_SIZE, CELL_SIZE))
    value_text = font.render(str(food["value"]), True, WHITE)
    screen.blit(value_text, (food["pos"][0] + 5, food["pos"][1] + 2))

    for i, block in enumerate(snake):
        color = (255, 255, 0) if i == 0 else GREEN
        pygame.draw.rect(screen, color, (*block, CELL_SIZE, CELL_SIZE))

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (WIDTH - 100, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()