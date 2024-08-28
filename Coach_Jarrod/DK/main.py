# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame

pygame.init()
WIDTH = 900
HEIGHT = 950
surface = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame_x,frame_y, width, height, scale_x,scale_y, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (frame_x, frame_y, width, height))
		image = pygame.transform.scale(image, (width * scale_x, height * scale_y))
		image.set_colorkey(colour)

		return image

sprite_sheet_image = pygame.image.load(f'Coach_Jarrod/DK/assets/sprite_sheet.png').convert_alpha()
cinema_sheet_image = pygame.image.load(f'Coach_Jarrod/DK/assets/Cinematics.png').convert_alpha()

sprite_sheet = SpriteSheet(sprite_sheet_image)
cinema_sheet = SpriteSheet(cinema_sheet_image)

BG=(0,255,80)
img_bg= (0, 91, 127)
BLACK = (0,0,0)

frame_0 = sprite_sheet.get_image(2.5,0, 24, 40, 2,2, img_bg)
frame_1 = sprite_sheet.get_image(3.5,0, 24, 40, 2,2, img_bg)
frame_2 = sprite_sheet.get_image(4.5,0, 24, 40, 2,2, img_bg)
frame_3 = sprite_sheet.get_image(5.5,0, 24, 40, 2,2, img_bg)

Cinematics = cinema_sheet.get_image(0, 230,50, 260, 3.5,3.5, img_bg)

def scale_images(Type,loc_x, loc_y,x,y):
    if Type =="cinema":
        img = cinema_sheet.get_image(loc_x,loc_y, x, y, surface.get_width()/x,surface.get_height()/y, img_bg)
        return img
    elif Type =="sprite":
        img = sprite_sheet.get_image(loc_x,loc_y, x, y, surface.get_width()*0.003,surface.get_height()*0.003, img_bg)
        return img

run = True
while run:
    #update background
    surface.fill(BLACK)
    
    #show frame image
    # screen.blit(frame_0, (0, 0))
    # screen.blit(frame_1, (72, 0))
    # screen.blit(frame_2, (150, 0))
    # screen.blit(frame_3, (250, 0))
    surface.blit(scale_images("cinema",0,50,230,260), (-20, 0))
    surface.blit(scale_images("sprite",65,10,15,20), (surface.get_width()*0.5, surface.get_height()*0.5))
    
	#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
pygame.quit()