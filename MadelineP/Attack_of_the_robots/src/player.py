import pygame
import toolbox
import projectile
from crate import Crate
from crate import Explosive_Crate
class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets/Player_04.png")
        self.image_hurt = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets/Player_04 - hurt.png")
        self.image_defeated = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets/Enemy_01.png")
        # self.image = pygame.image.load("assets/Player_04.png")
        # self.image_hurt = pygame.image.load("assets/Player_04 - hurt.png")
        # self.image_defeated = pygame.image.load("assets/Enemy_01.png")
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
        self.crate_ammo = 10
        self.explosive_crate_ammo = 10
        self.crate_cooldown = 0
        self.crate_cooldown_max = 10
        self.shot_type = 'normal'
        self.special_ammo = 0
        self.score = 0
    
    def update (self, enemies, explosions):
        self.rect.center = (self.x, self.y)
        
        for explosion in explosions:
            if explosion.damage and explosion.damage_player:
                if self.rect.colliderect(explosion.rect):
                    self.getHit(explosion.damage)
        
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.getHit(0)
                self.getHit(enemy.damage)
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
            
        if self.crate_cooldown > 0:
            self.crate_cooldown -= 1
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
                
                if not crate.just_placed:
                    if test_rect.colliderect(crate.rect):
                        collision = True
            
            if not collision:
                self.x += self.speed * x_movement
                self.y += self.speed * y_movement
            
        
    def shoot(self):
        if self.shoot_cooldown <= 0 and self.alive:
            if self.shot_type == 'normal':
                projectile.water_balloon(self.screen, self.x, self.y, self.angle)
            elif self.shot_type == 'splitshot':
                projectile.SplitWaterBalloon(self.screen, self.x, self.y, self.angle-15)
                projectile.SplitWaterBalloon(self.screen, self.x, self.y, self.angle)
                projectile.SplitWaterBalloon(self.screen, self.x, self.y, self.angle+15)
                self.special_ammo -= 1
            elif self.shot_type == 'stream':
                projectile.waterDroplet(self.screen, self.x, self.y, self.angle)
                self.special_ammo -= 1
            elif self.shot_type == 'burst':
                projectile.explosiveWaterBalloon(self.screen, self.x, self.y, self.angle)
                self.special_ammo -= 1
                
            self.shoot_cooldown = self.shoot_cooldown_max
            if self.special_ammo <= 0:
                self.powerUp('normal')

            
    def getHit(self, damage):
        if self.alive:
            self.hurt_timer = 5
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.alive = False
            
        
    def placeCrate(self):
        if self.alive and self.crate_ammo > 0 and self.crate_cooldown <= 0:
            Crate(self.screen, self.x, self.y, self)
            self.crate_ammo -= 1
            self.crate_cooldown = self.crate_cooldown_max
            
    def placeExplosiveCrate(self):
        if self.alive and self.explosive_crate_ammo > 0 and self.crate_cooldown <= 0:
            Explosive_Crate(self.screen, self.x, self.y, self)
            self.explosive_crate_ammo -= 1
            self.crate_cooldown = self.crate_cooldown_max
            
            
    def powerUp(self, power_type):
        if power_type == 'crateammo':
            self.crate_ammo += 10
            self.getScore(10)
        elif power_type == 'explosiveammo':
            self.explosive_crate_ammo += 10
            self.getScore(10)
        elif power_type == "splitshot":
            self.shot_type = 'splitshot'
            self.special_ammo = 40
            self.shoot_cooldown_max = 20
            self.getScore(20)
        elif power_type == 'normal':
            self.shot_type = 'normal'
            self.shoot_cooldown_max = 10
        elif power_type == 'stream':
            self.shot_type = 'stream'
            self.special_ammo = 300
            self.shoot_cooldown_max = 3
            self.getScore(20)
        elif power_type == 'burst':
            self.shot_type = 'burst'
            self.special_ammo = 35
            self.shoot_cooldown_max = 30
            self.getScore(20)
    
    def getScore(self, score):
        if self.alive:
            self.score += score
            