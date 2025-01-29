import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image, duration, damage, damage_player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.duration = duration
        self.damage = damage
        self.damage_player = damage_player
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        self.screen.blit(self.image, self.rect)
        