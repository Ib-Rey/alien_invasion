import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Реагирует на нажатие клавиш'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        #созлание новой пули и включение ее в группу bullets
       
    elif event.key ==pygame.K_q:
        sys.exit()
   


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        

     

def check_events(ai_settings, screen, ship, bullets, aliens):
    '''Обработка нажатия клавиш и события мыши'''
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
       
def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''Обновляет изображения на экране и отображает новый экран'''
    #При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #allien.blitme()
    aliens.draw(screen)
    #Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(bullets):
    """Обновляет позиции пули и уничтожает старые пули"""
    # Обновление позиции пуль
    bullets.update()
        #Удаление старых пуль за экраном
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
     if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    #Создает флот пришельцев
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    #Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2*alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


        
           


             
                

