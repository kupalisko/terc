import math
import pygame

def define_wind_direction(wind_direction_x,wind_direction_y):
    
    wind_direction = ""
    
    if wind_direction_y == 1:
        wind_direction += "S"
    elif wind_direction_y == -1:
        wind_direction += "N"
    
    if wind_direction_x == 1:
        wind_direction += "E"
    elif wind_direction_x == -1:
        wind_direction += "W"
    
    return wind_direction if wind_direction else "X"

def get_score(shoot,radii,points,target_x,target_y):
    mx, my = shoot
    dist = math.sqrt((mx - target_x) ** 2 + (my - target_y) ** 2)
    for i in range(len(radii)):
        if dist <= radii[i]:
            return points[i]
    return 0

def draw_table(screen,font,rows):
    headers = ["ID", "Name", "Score", "Shoots", "Average"]
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    WIDTH, HEIGHT = 600, 600

    screen.fill(WHITE)
    
    # Výška riadkov
    row_height = 40  
    start_y = 50  
    
    # Kreslenie hlavičky tabuľky
    for col, header in enumerate(headers):
        text = font.render(header, True, BLACK)
        screen.blit(text, (col * 120 + 10, start_y))

    pygame.draw.line(screen, BLACK, (0, start_y + row_height), (WIDTH, start_y + row_height), 2)

    # Kreslenie riadkov
    for i, row in enumerate(rows):
        y = start_y + (i + 1) * row_height
        for j, cell in enumerate(row):
            text = font.render(str(cell), True, BLACK)
            screen.blit(text, (j * 120 + 10, y+10))
        
        pygame.draw.line(screen, GRAY, (0, y + row_height), (WIDTH, y + row_height), 1)