import pygame, sys


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode
pygame.display.set_caption("My Game")


while True:
  for event in pygame.event.get():  
    if event.type == pygame.QUIT:
      pygame.quit()
      
      sys.exit()
  
  screen.fill("white")    
  pygame.display.flip()
  
    clock.tick(60)
    previous_time = clock.get_time()
    fps = clock.get_fps()
    print(previous_time)
    print = (fps)