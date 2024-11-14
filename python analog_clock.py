import pygame
import math
import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")

# Load font
font = pygame.font.Font(None, 36)

def draw_clock_face():
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS)
    
    # Draw hour markers and numbers
    for hour in range(1, 13):
        angle = math.radians(hour * 30)  # 360 degrees / 12 hours = 30 degrees per hour
        x = CENTER[0] + RADIUS * 0.7 * math.cos(angle - math.pi / 2)
        y = CENTER[1] + RADIUS * 0.7 * math.sin(angle - math.pi / 2)
        
        # Render the hour number
        text = font.render(str(hour), True, BLACK)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def draw_hand(length, angle, width, color):
    end_x = CENTER[0] + length * math.cos(angle - math.pi / 2)
    end_y = CENTER[1] + length * math.sin(angle - math.pi / 2)
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

def draw_clock():
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute + seconds / 60  # Include seconds to minutes
    hours = now.hour % 12 + minutes / 60  # Include minutes to hours

    # Draw clock face
    draw_clock_face()

    # Draw hands with updated lengths
    draw_hand(RADIUS * 0.6, math.radians(hours * 30), 8, BLACK)  # Smaller hour hand
    draw_hand(RADIUS * 0.8, math.radians(minutes * 6), 6, BLACK)  # Minute hand
    draw_hand(RADIUS * 0.7, math.radians(seconds * 6), 4, BLACK)  # Second hand

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(GRAY)

        # Draw the clock
        draw_clock()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()