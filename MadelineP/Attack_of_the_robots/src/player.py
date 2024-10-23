import pygame
import toolbox

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets\Player_04.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 8
    
    def update (self):
        self.rect.center = (self.x, self.y)
        
        image_to_draw, image_rect = toolbox.getRotatedImage()
        
        self.screen.blit(self.image, (self.rect))
        
    def move(self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement