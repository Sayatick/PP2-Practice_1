import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
CENTER = (WIDTH // 2, HEIGHT // 2)

clock_image = pygame.image.load("lab_07/clock.png")
clock_image = pygame.transform.scale(clock_image, (WIDTH, HEIGHT))

right_hand = pygame.image.load("lab_07/min_hand.png")
left_hand = pygame.image.load("lab_07/sec_hand.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

running = True
while running:
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -(minutes * 6)
    print(minute_angle)
    second_angle = -(seconds * 6 - 60)
    print(second_angle)

    screen.fill((255, 255, 255))
    screen.blit(clock_image, (0, 0))

    rotated_minute_hand = pygame.transform.rotate(right_hand, minute_angle)
    min_rect = rotated_minute_hand.get_rect(center=CENTER)
    screen.blit(rotated_minute_hand, min_rect.topleft)

    rotated_second_hand = pygame.transform.rotate(left_hand, second_angle)
    sec_rect = rotated_second_hand.get_rect(center=CENTER)
    screen.blit(rotated_second_hand, sec_rect.topleft)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()
