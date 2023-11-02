class Settings():
    #Класс для храения настроек игры

    def __init__(self):
        '''Инициализирует настройки игры'''
        #Параметры экрана
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (58, 58, 125)
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 237, 214, 88
        self.bullets_allowed = 3
    #Настройки кораблz
    ship_speed_factor = 1.5

