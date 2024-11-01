import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.player = player
        self.image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets\Enemy_03.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        self.rect.center = (self.x, self.y)
        
        self.screen.blit(self.image, self.rect)
        