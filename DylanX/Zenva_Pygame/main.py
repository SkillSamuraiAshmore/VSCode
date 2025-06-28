import pygame, sys, math

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Special Game")

background_color = "white"

apple = pygame.image.load("apple.png")
rect = apple.get_rect()

rect = rect.move(10, 10)

screen_rect = screen.get_rect()


def check_for_collision():
    return rect.x <= 0 or rect.x + rect.width >= screen_rect.width or rect.y <= 0 or rect.y + rect.height >= screen_rect.height


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not check_for_collision(): 
        rect = rect.move(0, 1) 
    
    screen.fill(background_color)

    screen.blit(apple, rect)
    
    pygame.display.flip()
    
    clock.tick(60)
    

