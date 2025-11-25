import pygame, sys, math

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Special Game")

background_color = "white"

circle_x=50
circle_y=50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
                circle_x -= 1
    if keys[pygame.K_RIGHT]:
        circle_x += 1
    if keys[pygame.K_UP]:
        circle_y -= 1
    if keys[pygame.K_DOWN]:
        circle_y += 1


    screen.fill(background_color)
    

    pygame.draw.circle(screen,"red",(circle_x,circle_y),20)
    
    pygame.display.flip()
    
    clock.tick(60)
    

