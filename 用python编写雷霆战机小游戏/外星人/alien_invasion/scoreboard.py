from pygame.sprite import Group

import pygame.font

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #显示得分信息时用的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        # 准备包含得分的初始图像
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()
        self.prep_ammo()

    def prep_score(self):
        """将得分转化成一幅渲染的图像"""
        rounded_score=int(round(self.stats.score,-1))
        score_str='now score: '+"{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #将得分放在屏幕右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.ammo_image,self.ammo_rect)

    def prep_high_score(self):
        """将最高分转换为渲染的图像"""
        high_score=int(round(self.stats.high_score,-1))
        high_score_str="highest score: "+"{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        #最高分放中间
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top

    def prep_level(self):
        """等级的显示"""
        level_str="now level: "+str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.ai_settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ships(self):
        """剩余的飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.screen,self.ai_settings)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def prep_ammo(self):
        """剩余的弹药"""
        ammo_str="your ammo: "+str(self.stats.ammo)
        self.ammo_image=self.font.render(ammo_str,True,self.text_color,self.ai_settings.bg_color)
        self.ammo_rect=self.ammo_image.get_rect()
        self.ammo_rect.right=self.score_rect.right
        self.ammo_rect.top=self.level_rect.bottom+10



