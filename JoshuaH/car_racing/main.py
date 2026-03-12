#from asyncio.base_futures import _FINISHED
import pygame
import time
import math
from utils import scale_image

GRASS = scale_image (pygame.image.load("JoshuaH/car_racing/imgs/grass.jpg"), 2.5)
print(GRASS)
TRACK = pygame.image.load("JoshuaH/car_racing/imgs\\track.png")

TRACK_BORDER = pygame.image.load("JoshuaH/car_racing/imgs/track-border.png")
FINISH = pygame.image.load("JoshuaH/car_racing/imgs/finish.png")

RED_CAR = scale_image(pygame.image.load("JoshuaH/car_racing/imgs/red-car.png"), 0.55)
GREY_CAR = scale_image(pygame.image.load("JoshuaH/car_racing/imgs/grey-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("car_racing")

FPS = 60

class AbstractCar:
  def __init__(self, max_vel, rotation_vel):
    self.max_vel = max_vel
    self.vel = 0
    self.rotation_vel = rotation_vel
    self.angle = 0

def draw(win, images):
  for img, pos in images
    win.blit(img, pos)

run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]

while run:
  clock.tick(FPS)
    
  draw(WIN, images)
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      break
  
pygame.quit()
    