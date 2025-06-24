import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("My Game")

white = pygame.Color(255, 255, 255, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(white)
    pygame.display.flip()
    #pygame.display.update()
            
    clock.tick(60)