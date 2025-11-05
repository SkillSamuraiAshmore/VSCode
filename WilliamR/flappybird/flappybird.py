import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

#window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),                
               pygame.image.load("assets/bird_up.png")]
background_images = pygame.image.load("assets/background.png")               
game_over_images = pygame.image.load("assets/game_over.png")                
ground_image =     pygame.image.load("assets/ground.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
start_image =   pygame.image.load("assets/start.png")                
game_over_images = pygame.image.load("assets/background.png")                

               
#game

scroll_speed =  1
bird_start_position = (100, 250)

class bird(pygame.sprite.Sprite):
    def __init__(self):
      self.image = bird_images[0]
      self.rect = self.image.get_rect()
      self.rect.center = bird_start_position
      self.image_index = 0
    def update(self):
        #animate
        self.image_index += 1  
      
      
      
      
      
      
      
      
      
      
      
      
class Ground(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image           
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    
    def update(self):
        #moveground
        self.rect.x -= scroll_speed
        if self.rect.x <=  -win_width:
            self.kill()


def quit_game():
    #EXIT game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            


            
#main method


def main():
    #Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(bird())
    
   #Instantiate initial ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    run = True
    while run:
        #quit
        #TODO:fix
        quit_game
        
        #reset
        window.fill(( 0, 0, 0))
        
        
        
        
       
        #drawbackground
        window.blit(background_images, (0, 0))
        
        #spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground)) 
    
        #draw - pipes, ground and bird
        ground.draw(window)
        bird.draw(window)
        # update
        ground.update()
        bird.update
        
        clock.tick(60)
        pygame.display.update()
main()