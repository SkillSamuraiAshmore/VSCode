import pygame, sys


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Game")

background_color = "lavender"

rect = pygame.Rect(50, 10, 300, 150)


while True:
  for event in pygame.event.get():  
    if event.type == pygame.QUIT:
      pygame.quit()
      
      sys.exit()
  
    screen.fill(background_color)    
    pygame.draw.rect(screen, "lavenderblush", rect, 5, 20)
    pygame.draw.circle(screen, "aliceblue", (100, 100))

    pygame.display.flip()
    
    
    clock.tick(60)
    
    previous_time = clock.get_time()
    fps = clock.get_fps()
    print(previous_time)
    print(fps)