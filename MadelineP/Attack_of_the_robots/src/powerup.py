import pygame
import random
import toolbox

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, screen, x, y ):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.pick_power = random.randint(0, 1)
        if self.pick_power == 0:
            self.image = pygame.image.load("assets/powerupCrate.png")
            self.background_image = pygame.image.load("assets/powerupBackgroundBlue.png")
            self.power_type = 'crateammo'
            
        elif self.pick_power == 1:
            self.image = pygame.image.load("assets/powerupExplosiveBarrel.png")
            self.background_image = pygame.image.load("assets/powerupBackgroundBlue.png")
            self.power_type = 'explosiveammo'
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.background_angle = 0
        self.spinning_speed = 2
        self.despawn_timer = 400 
        
    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.powerUp(self.power_type)
            self.kill()
        self.despawn_timer -= 1
        if self.despawn_timer <= 0:
            self.kill()
        self.background_angle += self.spinning_speed
        bg_image_to_draw, bg_rect = toolbox.getRotatedImage(self.background_image, self.rect, self.background_angle)
        
        self.screen.blit(bg_image_to_draw, bg_rect)
        self.screen.blit(self.image, self.rect)