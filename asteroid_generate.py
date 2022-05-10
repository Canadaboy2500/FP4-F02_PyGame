import pygame
WHITE = (255, 255, 255)
RED = (0, 0, 255)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size, speed, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        self.width = size
        self.height = size
        self.speed = speed
        self.color = color
        
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
    
    def respawn(self, size, speed, color):
        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        self.width = size
        self.height = size
        self.speed = speed
        
        pygame.draw.rect(self.image, color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
    
    def move_right(self, pixels):
        self.rect.x += pixels
        
    def move_left(self, pixels):
        self.rect.x -= pixels
        
    def move_up(self, pixels):
        self.rect.y -= pixels
        
    def move_down(self, pixels):
        self.rect.y += pixels
    