elif self.y < - self.image.get_height():
            self.kill()
            
        elif self.y > self.screen.get_height() + self.image.get_height():
            self.kill()