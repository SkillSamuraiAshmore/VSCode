#from asyncio.base_futures import _FINISHED
import pygame
import time
import math

GRASS = pygame.image.load("JoshuaH/car_racing/imgs/grass.jpg")
print(GRASS)
TRACK = pygame.image.load("JoshuaH/car_racing/imgs\\track.png")

TRACK_BORDER = pygame.image.load("JoshuaH/car_racing/imgs/track-border.png")
FINISH = pygame.image.load("JoshuaH/car_racing/imgs/finish.png")

RED_CAR = pygame.image.load("JoshuaH/car_racing/imgs/red-car.png")
GREY_CAR = pygame.image.load("JoshuaH/car_racing/imgs/grey-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("car_racing")

FPS = 60

run = True
clock = pygame.time.Clock()

while run:
  clock.tick(FPS)
  
  WIN.blit(GRASS, (0, 0))
  WIN.blit(TRACK, (0, 0))
  WIN.blit(FINISH, (0, 0))
  
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      break
  
pygame.quit()
    