import pygame
import math

pygame.init()

# Nastavenie okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Shooting")

# Farby
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Súradnice stredu terča
target_x = WIDTH // 2
target_y = HEIGHT // 2

# Polomery zón bodovania
radii = [20, 40, 60]  # Malý (10b), stredný (5b), veľký (2b)
points = [10, 5, 2]   # Body pre jednotlivé zóny

score = 0
running = True

while running:
    screen.fill(WHITE)
    
    # Kreslenie terča (3 kruhy)
    pygame.draw.circle(screen, RED, (target_x, target_y), radii[2], 2)
    pygame.draw.circle(screen, BLUE, (target_x, target_y), radii[1], 2)
    pygame.draw.circle(screen, GREEN, (target_x, target_y), radii[0], 2)

    # Vykreslenie skóre
    font = pygame.font.Font(None, 36)
    text = font.render(f"Skóre: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # Vzdialenosť kliknutia od stredu terča
            dist = math.sqrt((mx - target_x) ** 2 + (my - target_y) ** 2)

            # Určenie bodovania podľa zásahu
            for i in range(len(radii)):
                if dist <= radii[i]:
                    score += points[i]
                    break  # Pridá body len raz

    pygame.display.flip()

pygame.quit()
