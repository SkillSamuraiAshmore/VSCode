#SET UP PYGAME

import pygame,sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode()
pygame.display.set_caption("My special game ")
red=pygame.Color(255,0,0,1)
grey=pygame.Color(100,100,100,1)
#GAME LOOP

while True:
    #CHECKING FOR EVENTS
    for event in  pygame.event.get():
        #CHECK FOR QUIT
        if event.type == pygame.QUIT:
            #QUIT
            pygame.quit()
            sys.exit()
    screen.fill(cyan)
    pygame.display.flip()
    #pygame.display.update()
    #SET FPS
    clock.tick(60)
    

