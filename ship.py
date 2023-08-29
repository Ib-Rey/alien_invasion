import pygame

class Ship():

    def __init__(self, screen):
        #Инициализирует корабль и задает первонач. позицию
        self.screen = screen
        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/scuter1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_right = False
    def update(self):
        '''Обновляет позицию корабля с учетом флага'''
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        #Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)