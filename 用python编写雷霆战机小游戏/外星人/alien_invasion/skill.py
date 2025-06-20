class Skill:
    def __init__(self,name,apply_effect):
        self.name=name
        self.apply_effect=apply_effect


def bullet_wider(ai_settings,stats):
    ai_settings.bullet_width+=100

def bullet_faster(ai_settings,stats):
    ai_settings.bullet_speed_factor*=1.5

def hurt_increase(ai_settings,stats):
    ai_settings.bullet_hurt+=7

def ship_move_faster(ai_settings,stats):
    ai_settings.ship_speed_factor *=1.4

def more_ships(ai_settings,stats):
    stats.ship_left+=1

def pierce_bullet(ai_settings,stats):
    ai_settings.bullet_pierce=True

def more_bullets(ai_settings,stats):
    stats.ammo+=2


skills_poll=[Skill("your bullets will be wider",bullet_wider),
             Skill("your bullets will be faster",bullet_faster),
             Skill("hurt of bullet increase",hurt_increase),
             Skill('your ship moves faster',ship_move_faster),
             Skill('have more ships',more_ships),
             Skill('have more bullets',more_bullets)]



