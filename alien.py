import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #класс представоляющий одного пришельца
    def __init__(self, ai_settings, screen):
        '''И нициализирует пришельца  изадает его начальную позицию'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Загрузка изображения пришельца и назначение аттрибута rect
        self.image = pygame.image.load('images/ship1.png')
        self.rect = self.image.get_rect()
        #Каждый новый пришелец появляется в левом верхнем краю экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Сохраненние позиции пришельца
        self.x = float(self.rect.x)
    def blitme(self):
        #Выводит пришельца в текущем полпжении
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Перемещает пришельца вправо или влево
        self.x += (self.ai_settings.alien_speed_factor*
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        #Возвращает true если пришелец находится у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

        
