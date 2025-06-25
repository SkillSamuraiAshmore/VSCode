
import pygame,sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode()
pygame.display.set_caption("My special game ")
red=pygame.Color(255,0,0,1)
grey=pygame.Color(100,100,100,1)
white=pygame.Color(255,255,255,1)

while True:
    for event in  pygame.event.get():T
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    pygame.display.flip()
    clock.tick(60)
    

