class Settings():
    #Класс для храения настроек игры

    def __init__(self):
        '''Инициализирует настройки игры'''
        #Параметры экрана
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (58, 58, 125)

    #Настройки корабля
    ship_speed_factor = 1.5