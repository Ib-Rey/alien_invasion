


import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Создание экземпляра GameStats и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #Создание корабля
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")
   

    
    

    #Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)                       
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()        
    