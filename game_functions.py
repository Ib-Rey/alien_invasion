import sys
from time import sleep
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
        

     

def check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens):
    '''Обработка нажатия клавиш и события мыши'''
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
       
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''Обновляет изображения на экране и отображает новый экран'''
    #При каждом проходе цикла перерисовывается экран
    #screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_color, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #allien.blitme()
    aliens.draw(screen)
    #Отображение последнего прорисованного экрана
    #Вывод счета
    sb.show_score()
    '''Кнопка play_button появляется только в том случае ,если игра 
    неактивна'''
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    



def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Обновляет позиции пули и уничтожает старые пули"""
    # Обновление позиции пуль
    bullets.update()
        #Удаление старых пуль за экраном
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_allien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_allien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Обработка пуль, попавших в пришельцев
    #Проверка попаданий пришельца
    #При обнаружении попадания удалить пулю и пришельца
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed_factor()
        create_fleet(ai_settings, screen,ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    # ограничивает количество пуль
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
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    #Проверяет достиг ли флот края экрана после чего
    # Обновляет позиции всех пришельцев на флоте
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Проверка коллизий пришелец- корабль
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Ship hit!!!')
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    #Проверка пришельцев, добравшихся до нижнего края
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


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

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''Обрабатывает столкновение корабля с пришельцем'''
    #Уменьшение ship_left
    if stats.ships_left > 0:
        stats.ships_left -= 1 
        # Очистка списков и пришельцев от пуль
        aliens.empty()
        bullets.empty()
        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #Пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''Проверяет добрались ли прищельцы до нижнего края'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #происходит то же, что и при столкновениии с кораблем
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def check_play_button(ai_settings, screen,  stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''Запускает новую игру принажатии кнопки play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Сброс игровых настроек
        ai_settings.initialize_dinamic_settings()
        # Указатель мыши скрывается
        pygame.mouse.set_visible(False)

    
        # Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True
        #Очистка списка пришельцев и пуль
        aliens.empty()
        bullets.empty()
        #Создание нового флота и размещение пришельцев в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_high_score(stats, sb):
    ''' Проверяет новый рекорд'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()      
           


             
                

