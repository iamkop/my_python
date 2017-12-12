class Settings:
    """存储设置参数"""

    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的速度
        self.ship_speed_factor = 1.5
