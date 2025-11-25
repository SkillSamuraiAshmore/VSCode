import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("My Game")
#pygame.display.set_icon()

white = pygame.Color(255, 255, 255, 1)

#rect = pygame.Rect(800, 400, 200, 200)
triangle_coordinates = [(100, 50), (125, 100), (75, 100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(white)
    #pygame.draw.rect(screen, "black", rect, 0, 20)
    #pygame.draw.circle(screen, "blue", (600, 500), 100)
    pygame.draw.polygon(screen, "red", triangle_coordinates)
    
    pygame.display.flip()
    #pygame.display.update()
            
    clock.tick(60)