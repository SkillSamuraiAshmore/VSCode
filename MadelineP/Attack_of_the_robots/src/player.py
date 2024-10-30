import pygame
import toolbox
import projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets\Player_04.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 8
        self.angle = 0 
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
        
    
    def update (self):
        self.rect.center = (self.x, self.y)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)
        
        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        
        self.screen.blit(image_to_draw, image_rect)
        
        
    def move(self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement
        
    def shoot(self):
        projectile.water_balloon(self.screen, self.x, self.y, self.angle)
        
        