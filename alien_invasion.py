


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Создание корабля
    ship = Ship(screen)
    #Назначение цвета фона
    bg_color = (230, 230, 230)

    
    

    #Запуск основного цикла игры
    while True:
        gf.check_events(ship)
        ship.update()
        
        gf.update_screen(ai_settings, screen, ship)
run_game()        
    