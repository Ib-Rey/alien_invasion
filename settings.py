class Settings():
    #Класс для храения настроек игры

    def __init__(self):
        '''Инициализирует статические настройки игры'''
        #Параметры экрана
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (58, 58, 125)
        # Параметры пули
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 237, 214, 88
        self.bullets_allowed = 3
        #Настройки кораблz
        self.ship_speed_factor = 1.5
        self.ship_limit = 1
        #Настройка пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30
        # fleet direction = 1 движение вправо,а  -1 - влево
        self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dinamic_settings()
    
    def initialize_dinamic_settings(self):
        '''Иницилизирует настройки ,изменяющиеся в ходе игры'''
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 1.2
        self.fleet_direction = 1 # направление движения флота 1  - движение направо

    def increase_speed_factor(self):
        '''Увеличивает настройки скорости'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

