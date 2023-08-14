import sys
#Модуль sys завершает игру по команде игрока

import pygame
def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Alien Invasion")

    
    

    #Запуск основного цикла игры
    while True:
        #отслеживание событий на клавиатуре и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Отображение последнего прорисованного экрана
        pygame.display.flip()
run_game()        
    