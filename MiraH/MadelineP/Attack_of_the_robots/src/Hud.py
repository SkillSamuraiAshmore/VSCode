import pygame


class HUD():
    def __init__(self, screen, player):
       
        self.screen = screen
        self.player = player
        
        self.state = 'ingame'
        
        self.hud_font = pygame.font.SysFont("comicsans", 30)
        
        # self.score_text = self.hud_font.render("Score", True, (255, 255, 255))
        
    def update(self):
        self.score_text = self.hud_font.render("Score: " + str(self.player.score), True, (255, 255, 255))
        self.screen.blit(self.score_text, (10, 10))
        

class ammoTile():
    def __init__(self, screen, icon, font):
        self.screen = screen
        self.icon = icon
        self.font = font
        self.bg_image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets/hudTile.png")
        
    def update(self, x, y, ammo):
        tile_rect = self.bg_image.get_rect()