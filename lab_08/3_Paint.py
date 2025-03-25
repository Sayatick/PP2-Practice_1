import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

# Fill background
screen.fill(WHITE)

# Drawing state
drawing = False
last_pos = None
tool = "brush"  # can be: brush, rect, circle, eraser

# Font for showing tool name
font = pygame.font.SysFont("Arial", 20)

# Clock for FPS
clock = pygame.time.Clock()

def draw_line(surface, color, start, end, width=3):
    pygame.draw.line(surface, color, start, end, width)

def draw_text(text, pos):
    label = font.render(text, True, BLACK)
    screen.blit(label, pos)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            # Rectangle tool
            if tool == "rect":
                x, y = start_pos
                w = end_pos[0] - x
                h = end_pos[1] - y
                pygame.draw.rect(screen, current_color, (x, y, w, h), 3)

            # Circle tool
            elif tool == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 3)

        # Key press (tool switch & color change)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_3:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_4:
                current_color = (0, 0, 255)

    # If using brush or eraser while holding mouse
    if drawing and tool in ["brush", "eraser"]:
        mouse_pos = pygame.mouse.get_pos()
        color = WHITE if tool == "eraser" else current_color
        draw_line(screen, color, last_pos, mouse_pos, width=10)
        last_pos = mouse_pos

    # Draw UI
    draw_text(f"Tool: {tool}", (10, 10))

    pygame.display.flip()
    clock.tick(60)