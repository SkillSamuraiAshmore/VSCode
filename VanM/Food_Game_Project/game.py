import pygame
import sys

def forHire_Text():
    forHire_image = pygame.image.load("VanM\Food_Game_Project\\backdrops\For_Hire.jpg")
    font = pygame.font.SysFont('Pixelify Sans', 30)
    text_surface = font.render('Hello, i see you finished your coffe and look its not my personal business but ypu seem like a typical person we need around here please come fore hire', True, (255, 255, 255))
    Hire_rect = text_surface.get_rect(midtop=(320, 10))
    window.blit(forHire_image, cursor_pos)
pygame.init()

pygame.mouse.set_visible(False) 

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1200
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FRIED")
runwin = True

def cursor():
    # Get the rectangle of the image
    cursor_image = pygame.image.load("assets\images\Open_Palm_Hand.png")
    # cursor_rect = cursor_image.get_rect()
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    cursor_pos = (mouse_X, mouse_Y) 
    
    window.blit(cursor_image, cursor_pos)

# Main game loop!
while runwin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runwin = False
    
    window.fill((0, 0, 0))
    cursor()
    
    pygame.display.update()
        
        
        
pygame.quit()         




  
  
  
  
  
  