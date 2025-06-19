import sys
from time import sleep
import random

import pygame

from bullet import Bullet

from alien import Alien

from bullet_alien import BulletAlien

def check_events(ship,ai_settings,screen,bullets,aliens,stats,play_button,sb):#响应鼠标和键盘事件
    for event in pygame.event.get():  # 侦听事件，构建事件循环
        if event.type == pygame.QUIT:
            stats._save_high_score()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #pygame.mouse.get_pos()返回一个元组，是单机鼠标史鼠标的x和y坐标
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb,mouse_x,mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings,screen,event,ship,bullets,stats,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb,mouse_x,mouse_y):
    """点击按钮时开始新游戏"""
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and not stats.game_active:
        #隐藏光标
        pygame.mouse.set_visible(False)
        #rect.collidepoint(mouse_x,mouse_y)检查位置是否在rect内
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active=True
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #重置积分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        sb.prep_ammo()
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
        #创建新的，飞船居中
        create_fleet(ai_settings,screen,ship,aliens,stats)
        ship.center_ship()


def check_keydown_events(ai_settings,screen,event,ship,bullets,stats,sb):
    """响应按下"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
         ship.moving_left = True
    #创造一颗子弹，把它加到编组里
    elif event.key == pygame.K_SPACE:
        if stats.ammo>0:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            stats.ammo-=1
            sb.prep_ammo()
def check_keyup_events(event,ship):
    """响应松开"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb,alien_bullets):
    screen.fill(ai_settings.bg_color)# 每次循环重绘屏幕，FILL方法用于处理SURFACE，接受一个颜色实参
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets:
        alien_bullet.draw_bullet()
    ship.blitme()
    #对编组使用draw时，pygame自动绘制编组的每个元素，位置由元素的rect属性决定
    aliens.draw(screen)
    for alien in aliens:
        alien.draw_health_bar()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()


    pygame.display.flip()  # 让最近绘制的屏幕可见

def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb,alien_bullets):
    bullets.update()
    alien_bullets.update()
    # 删除超出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            stats.ammo+=1
            sb.prep_ammo()
            sb.show_score()
    for bullet in alien_bullets.copy():
        if bullet.rect.bottom>=ai_settings.screen_height:
            alien_bullets.remove(bullet)
    for alien in aliens:
        if isinstance(alien,BulletAlien) and alien.bullet and alien.has_bullet:
            alien_bullets.add(alien.bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb,alien_bullets)



def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb,alien_bullets):
    """响应子弹和外星人的碰撞"""
    # sprite.groupcollide方法将每个子弹和每个外星人的rect比较，并返回一个字典（包含碰撞的子弹和外星人，键是子弹，值是击中的外星人），
    # 最后两个实参执行删除操作，（True，True）表示全部删除，如果想模拟高能子弹，将第一个实参变为False，则子弹可穿透
    if ai_settings.bullet_pierce:
        collisions = pygame.sprite.groupcollide(bullets, aliens, False, False)
    else:
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    if collisions:
        for aliens in collisions.values():
            for alien in aliens:
                dead=alien.take_damage(ai_settings.bullet_hurt)
                if dead:
                    stats.score+=ai_settings.alien_points*len(aliens)
            stats.ammo+=1
            sb.prep_score()
            sb.prep_ammo()
            sb.show_score()
        check_high_score(stats, sb)
    cut_bullets=pygame.sprite.groupcollide(bullets,alien_bullets,True,True)
    for bullets in cut_bullets.values():
        for bullet in bullets:
            bullet.mother.has_bullet=False
            stats.ammo+=1
            sb.prep_ammo()
    #没有了就创造新的
    if len(aliens) == 0:
        stats.ammo += len(bullets)
        bullets.empty()
        #提高等级并调用函数更新等级图像
        stats.level+=1
        stats.ammo+=1

        sb.prep_ammo()
        sb.prep_level()
        #芜湖 加速！
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens,stats)


def create_fleet(ai_settings,screen,ship,aliens,stats):
    """创建外星人群"""
    #创建一个外星人，然后计算一行可容纳多少个
    numbers=stats.level*3
    #创建一群
    for number in range(numbers):
        create_random_alien(ai_settings,screen,aliens,ship.rect.height)



def create_random_alien(ai_settings,screen,aliens,ship_height):
    """创建一个外星人放在此行"""
    luck_num=random.randint(1,3)
    if luck_num!=1:
        alien = Alien(ai_settings, screen)
    else:
        alien=BulletAlien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height=alien.rect.height
    margin=10
    max_x=ai_settings.screen_width-alien_width-margin
    max_y=ai_settings.screen_height-alien_height-ship_height-5 *alien_height
    for _ in range(20):
        alien.rect.x = random.randint(margin,max_x)
        alien.rect.y=random.randint(margin,max_y)
        alien.x =float(alien.rect.x)
        alien.y=float(alien.rect.y)
        if not pygame.sprite.spritecollideany(alien,aliens):
            break
    alien.draw_health_bar()
    aliens.add(alien)

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人放在此行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    alien.draw_health_bar()
    aliens.add(alien)







def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

"""def change_fleet_direction(ai_settings,aliens):
    #将整群外星人下移，并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1"""

def change_fleet_direction(ai_settings,aliens):
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """响应被外星人撞到的飞船"""
    if stats.ship_left>0:
        #减一艘剩余飞船，清空外星人和子弹
        stats.ship_left-=1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        #重新创建飞船和外星人
        create_fleet(ai_settings,screen,ship,aliens,stats)
        ship.center_ship()
        stats.ammo=stats.level
        sb.prep_ammo()
        #暂停
        sleep(0.5)
    else:
        stats.game_active=False
        #重新显示光标
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """外星人检查是否到达底部"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb,alien_bullets):
    """更新外星人"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检测是否有外星人到达屏幕边缘
    #方法spritecollideany()接受一个精灵和一个编组的参数，遍历编组寻找第一个与精灵碰撞的成员
    if pygame.sprite.spritecollideany(ship,aliens) or pygame.sprite.spritecollideany(ship,alien_bullets):
        ship_hit(ai_settings,stats,screen,ship, aliens, bullets,sb)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def check_high_score(stats,sb):
    #检查更新最高分
    if stats.high_score<stats.score:
        stats.high_score=stats.score
        sb.prep_high_score()
    sb.show_score()






