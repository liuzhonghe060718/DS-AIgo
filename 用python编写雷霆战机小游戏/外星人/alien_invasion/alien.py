import pygame
from pygame.sprite import Sprite




class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        '''初始化外星人并设置初始位置'''
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载外新人图像，设置rect属性
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        #，每个外星人初始化在屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #储存准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        #给外星人加血条
        self.max_health=ai_settings.alien_max_health
        self.health=self.max_health

        #有关发射子弹的设置
        self.last_shot_time = pygame.time.get_ticks()  # 当前时间（毫秒）
        self.shot_interval = 2000  # 每2000毫秒发射一次（2秒）

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        """向左或右移动外星人"""
        self.x+=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.y+=self.ai_settings.fleet_drop_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def check_edges(self):
        """外星人处于屏幕边缘，返回TRUE"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def take_damage(self,hurt):
        self.health-=hurt
        if self.health<=0:
            #死亡的常用函数，self.kill()，用来将精灵从编组中删除
            self.kill()
            return True
        return False

    def draw_health_bar(self):
        bar_width=self.rect.width
        bar_height=5
        health_ratio=self.health/self.max_health
        health_bar_rect=pygame.Rect(self.rect.left,self.rect.top-bar_height-2,bar_width*health_ratio,bar_height)
        border_rect=pygame.Rect(self.rect.left,self.rect.top-bar_height-2,bar_width ,bar_height)
        pygame.draw.rect(self.screen,(255,255,255),border_rect)

        pygame.draw.rect(self.screen,(255,0,0),health_bar_rect)#红色血条

