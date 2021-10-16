import pygame

BIRD_COLOUR = (225,0,0)
PIPE_COLOUR = (0,225,0)
FLOOR_COLOUR = (0,0,0)

class Bird(pygame.sprite.Sprite):
    
    def __init__(self, colour, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BIRD_COLOUR)
        
        pygame.draw.rect(self.image, colour, pygame.Rect(0,0,height,width))
        self.rect = self.image.get_rect()

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, colour, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(PIPE_COLOUR)
        
        pygame.draw.rect(self.image, colour, pygame.Rect(0,0,height,width))
        self.rect = self.image.get_rect()  
        
class Floor(pygame.sprite.Sprite):
    
    def __init__(self, colour, height, width):
        super().__init__() 
        
        self.image = pygame.Surface([width, height])
        self.image.fill(FLOOR_COLOUR) 
        
        pygame.draw.rect(self.image, colour, pygame.Rect(0,0,height,width))
        self.rect = self.image.get_rect()     
        
        
    
    
    