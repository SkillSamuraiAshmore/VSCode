import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width,win_height))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()