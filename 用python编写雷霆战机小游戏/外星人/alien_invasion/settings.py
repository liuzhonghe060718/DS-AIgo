#储存所有设置的类

class Settings:
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船设置

        self.ship_limit=2

        #子弹设置

        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=	255 ,193 ,37
        self.bullet_pierce=False

        #外星人设置

        self.fleet_drop_speed=0.25


        #以什么样的节奏加快游戏(动态设置）
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()

        #外星人子弹设置
        self.alien_bullet_speed_factor=3

    def initialize_dynamic_settings(self):
        """初始化随游戏变化的设置"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #控制外星人的左右
        self.fleet_direction = 1
        #积分
        self.alien_points = 100
        #血量
        self.alien_max_health = 10
        self.bullet_alien_max_health=5
        # 子弹伤害
        self.bullet_hurt =10
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        #怪血量增加
        self.alien_max_health+=4
        self.bullet_alien_max_health+=3
        #积分
        self.alien_points=int(self.alien_points*self.speedup_scale)


