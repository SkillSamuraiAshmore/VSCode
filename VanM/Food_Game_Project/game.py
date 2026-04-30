import pygame
import sys

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Food Game")
runwin = True
while runwin:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runwin = False
            pygame.display.update()
            window.fill((0, 0, 0))
pygame.quit()

  
  
  
  
  
  