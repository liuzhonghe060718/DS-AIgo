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


skills_poll=[Skill("your bullets will be wider",bullet_wider()),Skill("your bullets will be faster",bullet_faster()),Skill("hurt of bullet increase",hurt_increase())]

def show_skill_selection(player):
    import random
    import pygame

    selected_skills = random.sample(skills_pool, 3)

    # 显示简单文字按钮选择
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 32)

        for i, skill in enumerate(selected_skills):
            text = font.render(f"{i+1}. {skill.name} - {skill.description}", True, (255, 255, 255))
            screen.blit(text, (50, 100 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    index = event.key - pygame.K_1
                    selected_skills[index].apply_effect(player)
                    running = False
