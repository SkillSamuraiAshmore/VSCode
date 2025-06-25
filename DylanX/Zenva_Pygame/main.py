
import pygame,sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode()
pygame.display.set_caption("My special game ") 

grey=pygame.Color(100,100,100,1)
white=pygame.Color(255,255,255,1)

#apple=pygame.image.load("assets/apple.png")
#apple_rect=apple.get_rect()
#apple_rect.x=50
#apple_rect.y=100

#rect  = pygame.Rect(500,10,200,100)
#triangle_coords= [(100,50),(125,100) ,(175,100),(75,100)]

while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    
    pygame.draw.arc(screen,grey,pygame.Rect(50,50,100,100),0,3.1415926535897932384626)
    
    #pygame.draw.ellipse(screen,grey,pygame.Rect(50,50,100,200))
    #pygame.draw.rect(screen,grey,pygame.Rect(50,50,100,200),1)
    
    #pygame.draw.lines(screen,grey,False,[(50,250),(50,50),(250,250),(250,50)],5)
    #pygame.draw.line(screen,grey,(50,50),(200,100),5)
    
    #pygame.draw.rect(screen,grey,apple_rect,1)
    #screen.blit(apple, apple_rect)
    
    #pygame.draw.circle(screen,grey,(100,100),50)
    
    #pygame.draw.rect(screen,grey,rect, 5)
    
    #pygame.draw.polygon(screen,grey,triangle_coords)
    
    pygame.display.flip()
    clock.tick(60)
    

