def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，然后计算一行可容纳多少个
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建一群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕容纳多少外星人"""
    available_space_y=(ai_settings.screen_height-(2*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows


