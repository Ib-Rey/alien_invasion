import pygame.font
class Scoreboard():
    '''Класс для вывода игровой информации'''
    def __init__(self, ai_settings, screen, stats):
        '''инициализирует атр подсчета очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Настройка шрифта для вывода счета
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #Подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        
    
    def prep_score(self):
        '''Преобразует текущий счет в графическое изображение'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.i_color)
        #Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Выводит счет на экран'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        '''Ппеобразует рекордный счет в графическое изображение'''
        high_score = self.stats.high_score
        high_score_str = "{:,}".format(high_score)
        
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.i_color)
        # Рекорд выравнивается по центру левой стороны
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    



