
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from alien_invasion.scoreboard import Scoreboard

import game_functions as gf



class AlienInvasion:
    def __init__(self):
        pygame.init()#初始化游戏让模块正常工作
        self.clock=pygame.time.Clock()#控制帧率
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#创建一个显示窗口
        pygame.display.set_caption("Alien Invasion")#窗口的标题



        self.bg_color=(230,230,230)#设置背景色
    def run_game(self):#开始游戏主循环
        #创建一个储存游戏统计信息的实例
        stats=GameStats(self.settings)
        #创造一个飞船
        ship = Ship(self.screen,self.settings)
        #创造储存子弹的编组（编组：类似于列表，存储一系列sprite，统一管理和操作）
        bullets=Group()
        #创建外星人编组
        aliens=Group()
        gf.create_fleet(self.settings,self.screen,ship,aliens,stats)
        #创建外星人子弹编组
        alien_bullets = Group()
        #创建play按钮
        play_button=Button(self.settings,self.screen,"PLAY")
        #创建计分板
        sb=Scoreboard(self.settings,self.screen,stats)
        while True:
            gf.check_events(ship,self.settings,self.screen,bullets,aliens,stats,play_button,sb)
            if stats.game_active:
                ship.update()
                #对编著进行调用函数时，编组将自动对其中的每个精灵调用它
                gf.update_bullets(self.settings,self.screen,ship,aliens,bullets,stats,sb,alien_bullets)
                gf.update_aliens(self.settings,stats,self.screen,ship,aliens,bullets,sb,alien_bullets)
            gf.update_screen(self.settings,self.screen,ship,bullets,aliens,stats,play_button,sb,alien_bullets)
            self.clock.tick(60)#设置帧率，一般动态游戏为60，越高越牛逼
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()