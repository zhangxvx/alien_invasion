class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 在任何情况下都不应重置最高得分
        self.read_high_score()
        self.high_score = int(self.contents)

        # 游戏刚启动时处于活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        filename = 'high_score.txt'
        with open(filename) as file_object:
            self.contents = file_object.read()
        if self.contents =='':
            print("high score is null")
            self.contents = 0
