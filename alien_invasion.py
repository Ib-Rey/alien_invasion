import sys
#Модуль sys завершает игру по команде игрока

import pygame
from settings import Settings
from ship import Ship
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
        #отслеживание событий на клавиатуре и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #При каждом проходе цикла перерисовывается экран
            screen.fill(ai_settings.bg_color)
            ship.blitme()
        #Отображение последнего прорисованного экрана
        pygame.display.flip()
run_game()        
    