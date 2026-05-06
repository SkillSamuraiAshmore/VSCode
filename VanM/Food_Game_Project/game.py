import pygame
import sys

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FRIED")
runwin = True

def cursor():
    # Get the rectangle of the image
    image = pygame.image.load("assets\images\Open_Palm_Hand.png")
    image_rect = image.get_rect()

    image_rect.topleft = (100, 150) # Example position
    
    #need to use blit to get image on screen

# Main game loop!
while runwin:
   for event in pygame.event.get():
       
        cursor()
        if event.type == pygame.QUIT:
            runwin = False
            pygame.display.update()
            
            window.fill((0, 0, 0))
            pygame.quit()   
            




  
  
  
  
  
  