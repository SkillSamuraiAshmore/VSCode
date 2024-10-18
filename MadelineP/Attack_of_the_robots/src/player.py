import pygame
from os.path import abspath

class player():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(abspath("MadelineP\Attack_of_the_robots\\assets\Player_03.png"))
    def update (self):
        self.screen.blit(self.image, (self.x, self.y))