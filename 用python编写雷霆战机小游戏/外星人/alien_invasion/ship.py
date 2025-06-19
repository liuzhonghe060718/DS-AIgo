import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_settings):
        """初始化飞船"""
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像 并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #在飞船的舒心center中储存小数值
        self.center=float(self.rect.centerx)
        #移动标志（处理长按持续移动）
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''根据移动标志更新飞船位置'''
        #更新center值而不是centerx（后者无法存小数）
        if self.moving_right and self.rect.right<self.screen_rect.right:#防止跑出屏幕外
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor
        #根据center更新rect对象
        self.rect.centerx=self.center
    def blitme(self):
        #指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.center=self.screen_rect.centerx
