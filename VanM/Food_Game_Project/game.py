import pygame
import sys

pygame.init()

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1200

pygame.mouse.set_visible(False) 
pygame.display.set_caption("FRIED")

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
runwin = True



def cursor():
    # Get the rectangle of the image
    cursor_image = pygame.image.load("assets\images\Open_Palm_Hand.png")
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    cursor_pos = (mouse_X, mouse_Y) 
    window.blit(cursor_image, cursor_pos)
    print(cursor_pos)

def forHire_Text():
    forHire_image = pygame.image.load("backdrops\For_Hire.jpg")
    font = pygame.font.SysFont('Pixelify Sans', 30)
    text_surface = font.render('Hello, i see you finished your coffe and look its not my personal business but ypu seem like a typical person we need around here please come fore hire', True, (255, 255, 255))
    window.blit(forHire_image, (50, 50))
    Hire_rect = text_surface.get_rect(midtop=(1200, 1200))
    # window.blit(forHire_image, cursor_pos)

forHire_Text()
# Main game loop!
while runwin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runwin = False
    
    # window.fill((0, 0, 0))
    cursor()
    
    pygame.display.update()
        
pygame.quit()         




  
  
  
  
  
  