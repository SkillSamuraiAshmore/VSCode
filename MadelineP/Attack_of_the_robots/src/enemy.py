import pygame
import toolbox
import math

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
        self.angle = 0
        self.speed = 0.9
    
    def update(self):
        
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)
        
        angle_rads = math.radians(self.angle)
        x_move = math.cos(angle_rads) * self.speed
        y_move = -math.sin(angle_rads) * self.speed
        self.x += x_move
        self.y += y_move
        self.rect.center = (self.x, self.y)
        
        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        
        self.screen.blit(image_to_draw, image_rect)
        
