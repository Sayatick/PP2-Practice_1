import pygame
import sys
import math

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

# Fill background with white
screen.fill(WHITE)

# Drawing state
drawing = False
last_pos = None
start_pos = None
tool = "brush"  # default tool

# Font for UI
font = pygame.font.SysFont("Arial", 20)

# Clock for FPS
clock = pygame.time.Clock()

# Function to draw a simple line
def draw_line(surface, color, start, end, width=3):
    pygame.draw.line(surface, color, start, end, width)

# Function to display tool name
def draw_text(text, pos):
    label = font.render(text, True, BLACK)
    screen.blit(label, pos)

# Main game loop
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

        # Mouse release (for shapes)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos
            w = x2 - x1
            h = y2 - y1

            if tool == "rect":
                pygame.draw.rect(screen, current_color, (x1, y1, w, h), 3)

            elif tool == "circle":
                radius = int(math.hypot(w, h))
                pygame.draw.circle(screen, current_color, start_pos, radius, 3)

            elif tool == "square":
                side = min(abs(w), abs(h))
                pygame.draw.rect(screen, current_color, (x1, y1, side, side), 3)

            elif tool == "rtriangle":
                # Right triangle from corner
                pygame.draw.polygon(screen, current_color, [(x1, y1), (x1, y2), (x2, y2)], 3)

            elif tool == "etriangle":
                # Equilateral triangle from base
                side = abs(x2 - x1)
                height = side * (3**0.5) / 2
                points = [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)]
                pygame.draw.polygon(screen, current_color, points, 3)

            elif tool == "rhombus":
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, center_y - dy),  # Top
                    (center_x + dx, center_y),  # Right
                    (center_x, center_y + dy),  # Bottom
                    (center_x - dx, center_y)   # Left
                ]
                pygame.draw.polygon(screen, current_color, points, 3)

        # Keyboard controls
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
                current_color = (255, 0, 0)  # Red
            elif event.key == pygame.K_3:
                current_color = (0, 255, 0)  # Green
            elif event.key == pygame.K_4:
                current_color = (0, 0, 255)  # Blue
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "rtriangle"
            elif event.key == pygame.K_y:
                tool = "etriangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"

    # Freehand drawing
    if drawing and tool in ["brush", "eraser"]:
        mouse_pos = pygame.mouse.get_pos()
        color = WHITE if tool == "eraser" else current_color
        draw_line(screen, color, last_pos, mouse_pos, width=10)
        last_pos = mouse_pos

    # UI display
    screen.fill(WHITE, (0, 0, 180, 30))  # Clear top area for label
    draw_text(f"Tool: {tool}", (10, 5))

    pygame.display.flip()
    clock.tick(60)