import pygame
import toolbox
import projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/Player_04.png")
        self.image_hurt = pygame.image.load("assets/Player_04 - hurt.png")
        self.image_defeated = pygame.image.load("assets/Enemy_01.png")
        # self.image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets\Player_04.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 8
        self.angle = 0 
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
        self.health_max = 30
        self.health = self.health_max
        self.health_bar_width = self.image.get_width()
        self.health_bar_height = 8
        self.health_bar_green = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.health_bar_red = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.alive = True
        self.hurt_timer = 0
    
    def update (self, enemies):
        self.rect.center = (self.x, self.y)
        
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.getHit(0)
                self.getHit(enemy.damage)
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
        if self.alive:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)
        
        
        if self.alive:
            if self.hurt_timer > 0 :
                image_to_rotate = self.image_hurt
                self.hurt_timer -= 1
            else:
                image_to_rotate = self.image
        else:
            image_to_rotate = self.image_defeated
        image_to_draw, image_rect = toolbox.getRotatedImage(image_to_rotate, self.rect, self.angle)
        
        
        self.screen.blit(image_to_draw, image_rect)
        
        self.health_bar_red.x = self.rect.x
        self.health_bar_red.bottom = self.rect.y - 5
        
        pygame.draw.rect(self.screen, (255, 0, 0), self.health_bar_red)
        
        self.health_bar_green.topleft = self.health_bar_red.topleft
        
        health_percentage = self.health / self.health_max
        self.health_bar_green.width = self.health_bar_width * health_percentage
        if self.alive:
            pygame.draw.rect(self.screen, (0, 255, 0), self.health_bar_green)
        
        
        
        
    def move(self, x_movement, y_movement, crates):
        if self.alive:
            test_rect = self.rect
            test_rect.x += self.speed * x_movement
            test_rect.y += self.speed * y_movement
            collision = False
            for crate in crates:
                if test_rect.colliderect(crate.rect):
                    collision = True
            if not collision:
                self.x += self.speed * x_movement
                self.y += self.speed * y_movement
            
        
    def shoot(self):
        if self.shoot_cooldown <= 0 and self.alive:
            self.shoot_cooldown = self.shoot_cooldown_max
            projectile.water_balloon(self.screen, self.x, self.y, self.angle)
            
    def getHit(self, damage):
        if self.alive:
            self.hurt_timer = 5
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.alive = False
            
        
        
        
        