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

def update_bullets(aliens, bullets):
    """Обновляет позиции пули и уничтожает старые пули"""
    # Обновление позиции пуль
    bullets.update()
        #Удаление старых пуль за экраном
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #Проверка попаданий пришельца
    #При обнаружении попадания удалить пулю и пришельца
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(ai_settings, screen, ship, bullets):
     if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    #Создает флот пришельцев
    
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number) 
    
    #Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number, row_number)
       
        

def get_number_aliens_x(ai_settings, alien_width):
    #Вычисляет количество пришельцев в ряду
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Создает пришельца и размещает его в ряду
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    #Определяет количество рядов, помещающихся на экране
    available_space_y = (ai_settings.screen_height - 
                            (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
def update_aliens(ai_settings, aliens):
    #Проверяет достиг ли флот края экрана после чего
    # Обновляет позиции всех пришельцев на флоте
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    #Реагирует на достижение пришельцем края экрана
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    #Опускает флот и меняет направление флота
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

        
           


             
                

