import pygame, sys, random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set screen size and create display window
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load fonts and render game over text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background music and play it in a loop
pygame.mixer.music.load("lab_08/Racer/background.wav")
pygame.mixer.music.play(-1)

# Load crash sound
crash_sound = pygame.mixer.Sound("lab_08/Racer/crash.wav")

# Set game clock and speed
clock = pygame.time.Clock()
SPEED = 5

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_08/Racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 40:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < 360:
            self.rect.move_ip(5, 0)

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_08/Racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -100)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

# Initialize coin score
coin_score = 0

# Define Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_08/Racer/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -100)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), -100)

# Load background image
background = pygame.image.load("lab_08/Racer/AnimatedStreet.png")

# Create game objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Group sprites for update and collision detection
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Main game loop
running = True
while running:
    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Display coin score
    coin_display = font_small.render("Coins: " + str(coin_score), True, BLACK)
    DISPLAYSURF.blit(coin_display, (10, 10))

    # Handle quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.stop()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (30, 250))

        final_score = font_small.render("Coins collected: " + str(coin_score), True, BLACK)
        DISPLAYSURF.blit(final_score, (90, 320))

        pygame.display.update()
        pygame.time.wait(7000)
        pygame.quit()
        sys.exit()

    # Check for coin collection
    if pygame.sprite.collide_rect(P1, C1):
        coin_score += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, 360), -100)

    # Update display and set FPS
    pygame.display.update()
    clock.tick(60)