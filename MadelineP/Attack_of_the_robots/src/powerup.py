import pygame
import random
import toolbox

class powerUp(pygame.sprite.Sprite):
    def __init__(self, screen, x, y ):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen 
        self.x
        self.y
        self.pick_power = random.randint(0, 0)
        if self.pick_power == 0:
            self.image = pygame.image.load("assets/powerupCrate.png")
            self.background_image = pygame.image.load("assets/powerupBackgroundBlue.png")
            self.power_type = 'crateammo'
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.background_angle = 0
        self.spinning_speed = 2