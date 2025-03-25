import pygame
import sys
import random
import helpers
import numpy as np
import os


SIZE_X = 850
SIZE_Y = 600
pygame.init()

screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
pygame.display.set_caption('Pygame Physics Simulation')

cross_img = pygame.image.load('cross.png')
terc_img = pygame.image.load('terc.png')

physics_offset_strength = 0
physics_x_offset = 0
physics_y_offset = 0
wind_strength = 0
wind_direction_x = random.choice([-1, 0, 1])
wind_direction_y = random.choice([-1, 0, 1])
wind_direction = helpers.define_wind_direction(wind_direction_x, wind_direction_y)

dots = []

button_width = 150
button_height = 40
button_margin = 10
center_x = SIZE_X // 2
center_y = SIZE_Y // 2

menu_width = 300
menu_height = 150

input_text = ""
input_active = False

menu_input_text = ""
menu_input_active = False

start_button_rect =        pygame.Rect(SIZE_X - button_width - 20, 50, button_width, button_height)
reset_button_rect =        pygame.Rect(SIZE_X - button_width - 20, 50 + button_height + button_margin, button_width, button_height)
scoreboard_button_rect =   pygame.Rect(SIZE_X - button_width - 20, 50 + 2 * (button_height + button_margin), button_width, button_height)
wind_up_button_rect =      pygame.Rect(SIZE_X - button_width - 20, 50 + 3 * (button_height + button_margin), button_width, button_height)
wind_down_button_rect =    pygame.Rect(SIZE_X - button_width - 20, 50 + 4 * (button_height + button_margin), button_width, button_height)
physics_up_button_rect =   pygame.Rect(SIZE_X - button_width - 20, 50 + 5 * (button_height + button_margin), button_width, button_height)
physics_down_button_rect = pygame.Rect(SIZE_X - button_width - 20, 50 + 6 * (button_height + button_margin), button_width, button_height)
save_button_rect =         pygame.Rect(SIZE_X - button_width - 20, 50 + 8 * (button_height + button_margin), button_width, button_height)
back_button_rect =         pygame.Rect(SIZE_X - button_width - 20, 50 + 10 * (button_height + button_margin), button_width, button_height)
input_box =                pygame.Rect(SIZE_X - button_width - 20, 50 + 7 * (button_height + button_margin), button_width, button_height)
menu_rect =                pygame.Rect(center_x-menu_width/2, center_y-menu_height/2, menu_width, menu_height)
menu_cancel_rect =         pygame.Rect(center_x-menu_width/2+menu_width-60-5, center_y-menu_height/2+menu_height-30-5, 60, 30)
menu_confirm_rect =        pygame.Rect(center_x-menu_width/2+menu_width-60-5-60-5, center_y-menu_height/2+menu_height-30-5, 60, 30)
menu_input_rect =          pygame.Rect(center_x-menu_width/2+5, center_y-menu_height/2+5, menu_width-10, 30)
random_rect =              pygame.Rect(center_x-menu_width/2+20, center_y-menu_height/2+20, menu_width-40, 30)
normal_rect =              pygame.Rect(center_x-menu_width/2+20, center_y-menu_height/2+60, menu_width-40, 30)

font = pygame.font.Font(None, 26)
font_input = pygame.font.Font(None, 36)
font_hint = pygame.font.Font(None, 16)

start_text = font.render("Start", True, (255, 255, 255))
reset_text = font.render("Reset", True, (255, 255, 255))
scoreboard_text = font.render("Scoreboard", True, (255, 255, 255))
wind_up_text = font.render("Wind Up", True, (255, 255, 255))
wind_down_text = font.render("Wind Down", True, (255, 255, 255))
physics_up_text = font.render("Physics Up", True, (255, 255, 255))
physics_down_text = font.render("Physics Down", True, (255, 255, 255))
save_text = font.render("Save", True, (255, 255, 255))
ok_text = font.render("OK", True, (255, 255, 255))
cancel_text = font.render("Cancel", True, (255, 255, 255))
wind_direction_text = font.render(wind_direction, True, (0, 0, 0))
input_hint_text = font_hint.render("Enter amount of shoots", True, (0, 0, 0))
normal_text = font.render("Normalized split", True, (255, 255, 255))
random_text = font.render("Randomized split", True, (255, 255, 255))

mouse_inside = True
game_state = "game"
simulation_run = False
simulation_menu = False
save_menu = False
empty_screen = True
simulation = ""

file_path = os.path.join(os.path.dirname(__file__), 'save.txt')

running = True
while running:
    screen.fill((255, 255, 255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    wind_offset_x = wind_strength *3 * wind_direction_x
    wind_offset_y = wind_strength *3 * wind_direction_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.WINDOWENTER:
            mouse_inside = True
        elif event.type == pygame.WINDOWLEAVE:
            mouse_inside = False
        if game_state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if empty_screen:
                    if mouse_x < 600:
                        dots.append((physicsed_x + wind_offset_x, physicsed_y + wind_offset_y))

                    if start_button_rect.collidepoint(mouse_x, mouse_y): # Start button
                        simulation_menu = True
                        empty_screen = False
                        input_active = False
                    elif reset_button_rect.collidepoint(mouse_x, mouse_y): # Reset button
                        dots = []
                        wind_strength = 0
                        physics_offset_strength = 0
                        input_text = ""
                    elif scoreboard_button_rect.collidepoint(mouse_x, mouse_y): # Scoreboard button
                        game_state = "scoreboard"
                    elif wind_up_button_rect.collidepoint(mouse_x, mouse_y): # Wind up button
                        if wind_strength < 10:
                            wind_strength += 1
                    elif wind_down_button_rect.collidepoint(mouse_x, mouse_y):  # Wind down button
                        if wind_strength > 0:
                            wind_strength -= 1
                    elif physics_up_button_rect.collidepoint(mouse_x, mouse_y): # Physics up button
                        if physics_offset_strength < 10:
                            physics_offset_strength += 1
                    elif physics_down_button_rect.collidepoint(mouse_x, mouse_y):# Physics down button
                        if physics_offset_strength > 0:                
                            physics_offset_strength -= 1
                    elif input_box.collidepoint(mouse_x, mouse_y):
                        input_active = True
                    elif save_button_rect.collidepoint(mouse_x, mouse_y):
                        save_menu = True
                        input_active = False
                        empty_screen = False

                    else: input_active = False
                if simulation_menu:
                    if menu_cancel_rect.collidepoint(mouse_x, mouse_y):
                        simulation_menu = False
                        empty_screen = True
                    elif random_rect.collidepoint(mouse_x, mouse_y):
                        simulation = "random"
                        simulation_run = True
                        simulation_menu = False
                        empty_screen = True
                    elif normal_rect.collidepoint(mouse_x, mouse_y):
                        simulation = "normal"
                        simulation_run = True
                        simulation_menu = False
                        empty_screen = True
                elif save_menu:
                    if menu_cancel_rect.collidepoint(mouse_x, mouse_y):
                        save_menu = False
                        empty_screen = True
                        menu_input_text = ""
                    elif menu_input_rect.collidepoint(mouse_x, mouse_y):
                        menu_input_active = True
                    elif menu_confirm_rect.collidepoint(mouse_x, mouse_y) and menu_input_text != "":
                        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'save.txt')):
                            with open(file_path, 'a') as file:
                                file.write(menu_input_text + "\n")
                        else:
                            with open(file_path, 'w') as file:
                                file.write(menu_input_text + "\n")
                        save_menu = False
                        empty_screen = True
                        menu_input_text = ""

                    else: 
                        menu_input_active = False

            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isdigit() and len(input_text) <=9:  # Povolené len čísla max 9 znakov
                        input_text += event.unicode
            if event.type == pygame.KEYDOWN and menu_input_active:
                if event.key == pygame.K_BACKSPACE:
                    menu_input_text = menu_input_text[:-1]
                elif len(input_text) <=9:  # Povolené max 9 znakov
                        menu_input_text += event.unicode
                        print(menu_input_text)

        elif game_state == "scoreboard":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    game_state = "game"
            
    if game_state == "game":
        physics_x_offset += random.uniform(-physics_offset_strength/10, physics_offset_strength/10)
        physics_y_offset += random.uniform(-physics_offset_strength/10, physics_offset_strength/10)

        physicsed_x = int(mouse_x + physics_x_offset)
        physicsed_y = int(mouse_y + physics_y_offset)

        screen.blit(terc_img, (0, 0))
        if dots:
            for dot in dots:
                pygame.draw.circle(screen, (0, 0, 255), dot, 5)  # Draw red dot

        if mouse_x < terc_img.get_size()[0] and empty_screen:
            pygame.mouse.set_visible(False)
            if physicsed_x > terc_img.get_size()[0]:
                physicsed_x = terc_img.get_size()[0]
            screen.blit(cross_img, (physicsed_x - cross_img.get_width() // 2, physicsed_y - cross_img.get_height() // 2))
        if not mouse_inside or mouse_x > terc_img.get_size()[0]:
            pygame.mouse.set_visible(True)
            physics_x_offset = 0
            physics_y_offset = 0

        # Draws
        pygame.draw.rect(screen, (0, 128, 0), start_button_rect)  # Start button
        pygame.draw.rect(screen, (128, 0, 0), reset_button_rect)  # Reset button
        pygame.draw.rect(screen, (0, 0, 128), scoreboard_button_rect)  # Scoreboard button
        pygame.draw.rect(screen, (0, 0, 0), wind_up_button_rect)  # Wind up button
        pygame.draw.rect(screen, (0, 0, 0), wind_down_button_rect)  # Wind down button
        pygame.draw.rect(screen, (0, 0, 0), physics_up_button_rect)  # Physics up button
        pygame.draw.rect(screen, (0, 0, 0), physics_down_button_rect)  # Physics down button
        pygame.draw.rect(screen, (0, 0, 0), save_button_rect)  # Input box
        pygame.draw.rect(screen, (0, 0, 0) if input_active else (200,200,200), input_box, 2)  # Input box

        # Draw texts
        screen.blit(start_text,        (start_button_rect.x + 20, start_button_rect.y + 5))
        screen.blit(reset_text,        (reset_button_rect.x + 20, reset_button_rect.y + 5))
        screen.blit(scoreboard_text,   (scoreboard_button_rect.x + 20, scoreboard_button_rect.y + 5))
        screen.blit(wind_up_text,      (wind_up_button_rect.x + 20, wind_up_button_rect.y + 5))
        screen.blit(wind_down_text,    (wind_down_button_rect.x + 20, wind_down_button_rect.y + 5))
        screen.blit(physics_up_text,   (physics_up_button_rect.x + 20, physics_up_button_rect.y + 5))
        screen.blit(physics_down_text, (physics_down_button_rect.x + 20, physics_down_button_rect.y + 5))
        screen.blit(font_input.render  (input_text, True, (0, 0, 0)), (input_box.x + 5, input_box.y + 5))
        screen.blit(font.render        (str(wind_strength), True, (0, 0, 0)), (wind_up_button_rect.x -20, wind_up_button_rect.y + 5))
        screen.blit(font.render        (str(physics_offset_strength), True, (0, 0, 0)), (physics_up_button_rect.x -20, physics_up_button_rect.y + 5))
        screen.blit(save_text, (save_button_rect.x + 20, save_button_rect.y + 5))
        screen.blit(wind_direction_text, (wind_up_button_rect.x -55, wind_up_button_rect.y + 5))
        if not input_active and input_text == "":
            screen.blit(input_hint_text, (input_box.x + 10, input_box.y + 15))
        

        if simulation_menu:
            pygame.mouse.set_visible(True)
            pygame.draw.rect(screen, (255, 255, 255), menu_rect)
            pygame.draw.rect(screen, (0, 0, 0), menu_rect,2) #border
            pygame.draw.rect(screen, (0, 0, 0), menu_cancel_rect)
            screen.blit(cancel_text, (menu_cancel_rect.x + 2, menu_cancel_rect.y + 5))
            pygame.draw.rect(screen, (0, 0, 0), random_rect)
            pygame.draw.rect(screen, (0, 0, 0), normal_rect)
            screen.blit(random_text, (random_rect.x + 60, random_rect.y + 5))
            screen.blit(normal_text, (normal_rect.x + 62, normal_rect.y + 5))

        elif save_menu:
            pygame.mouse.set_visible(True)
            pygame.draw.rect(screen, (255, 255, 255), menu_rect)
            pygame.draw.rect(screen, (0, 0, 0), menu_rect,2) #border
            pygame.draw.rect(screen, (0, 0, 0), menu_confirm_rect)
            screen.blit(ok_text, (menu_confirm_rect.x + 2, menu_confirm_rect.y + 5))
            pygame.draw.rect(screen, (0, 0, 0), menu_cancel_rect)
            screen.blit(cancel_text, (menu_cancel_rect.x + 2, menu_cancel_rect.y + 5))
            pygame.draw.rect(screen, (0, 0, 0) if menu_input_active else (200,200,200), menu_input_rect, 2)
            if not menu_input_active and menu_input_text == "":
                screen.blit(font.render("Enter name", True, (0, 0, 0)), (menu_input_rect.x + 5, menu_input_rect.y + 5))
            else:
                screen.blit(font.render(menu_input_text, True, (0, 0, 0)), (menu_input_rect.x + 5, menu_input_rect.y + 5))
        
        if simulation_run and simulation == "random" and input_text != "":
            for i in range(int(input_text)):
                sim_pos_x = random.randint(0,terc_img.get_size()[0])
                sim_pos_y = random.randint(0,terc_img.get_size()[1])
                dots.append((sim_pos_x, sim_pos_y))
            simulation_run = False
            input_text = ""

        elif simulation_run and simulation == "normal" and input_text != "":
            for i in range(int(input_text)):
                sim_pos_x = np.random.normal(terc_img.get_size()[0]//2, 85) + physics_x_offset + wind_offset_x
                sim_pos_y = np.random.normal(terc_img.get_size()[1]//2, 85) + physics_y_offset + wind_offset_y
                dots.append((sim_pos_x, sim_pos_y))
            simulation_run = False
            input_text = ""


    elif game_state == "scoreboard":
        pygame.mouse.set_visible(True)

        font = pygame.font.Font(None, 26)
        back_text = font.render("Back", True, (255, 255, 255))
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (0, 0, 0), back_button_rect)
        screen.blit(back_text, (back_button_rect.x + 20, back_button_rect.y + 5))
        

    pygame.display.flip()

pygame.quit()
sys.exit()
