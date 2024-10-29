import pygame
import toolbox

class water_balloon(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x= x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("assets\BalloonSmall.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        
    def update(self):
        self.x += 5
        self.rect.center = (self.x, self.y)
        
        self.screen.blit(self.image, self.rect)
        