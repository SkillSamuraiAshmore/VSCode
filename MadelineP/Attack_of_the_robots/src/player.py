import pygame
from os.path import abspath

class Player():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(abspath("MadelineP\Attack_of_the_robots\\assets\Player_04.png"))
        self.speed = 5
    
    def update (self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def move(self):
        self.x += self.speed
        self.y += self.speed