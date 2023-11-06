class GameStats():
    #Отслеживание статистики
    def __init__(self, ai_settings):
        #Иницилизирует статистику
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        #инициализирует статистику, изменяющуюся в ходе игры
        self.ships_left = self.ai_settings.ship_limit