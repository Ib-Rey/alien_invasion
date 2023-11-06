class GameStats():
    #Отслеживание статистики
    def __init__(self, ai_settings):
        #Иницилизирует статистику
        self.ai_settings = ai_settings
        self.reset_stats()
        #Игра запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        #инициализирует статистику, изменяющуюся в ходе игры
        self.ships_left = self.ai_settings.ship_limit
