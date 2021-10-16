import pygame
from pygame.locals import *
from pygame.sprite import Group
import sprites
import random
pygame.init()
# COLOURS
SKY = (117,217,242)
WHITE = (225,225,225)
RED = (225,0,0)
GREEN = (0,225,0)
BLACK = (0,0,0)

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600



WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('crazy cube')

def Game_Loop():
    loop = False
    start_loop = True
    isjump = False
    tmp = 0
    score = 0
    all_sprites_list = pygame.sprite.Group()
    wall_sprites_list = pygame.sprite.Group()
    pipe_sprites_lsit = pygame.sprite.Group()
    bottom_sprites_list = pygame.sprite.Group()
    top_sprites_list = pygame.sprite.Group()
    
    bird1 = sprites.Bird(RED, 45, 45)
    bird1.rect.x = 200
    bird1.rect.y = 300
    all_sprites_list.add(bird1)
    #################################################################
    pipe1 = sprites.Pipe(GREEN, 600, 160)
    pipe1.rect.x = 400
    pipe1.rect.y = -360
    all_sprites_list.add(pipe1)
    pipe_sprites_lsit.add(pipe1)
    top_sprites_list.add(pipe1)
    
    pipe2 = sprites.Pipe(GREEN, 500, 160)
    pipe2.rect.x = 400
    pipe2.rect.y = 400
    all_sprites_list.add(pipe2)
    pipe_sprites_lsit.add(pipe2)
    bottom_sprites_list.add(pipe2)
    #################################################################
    pipe3 = sprites.Pipe(GREEN, 600, 160)
    pipe3.rect.x = 700
    pipe3.rect.y = -390
    all_sprites_list.add(pipe3)
    pipe_sprites_lsit.add(pipe3)
    top_sprites_list.add(pipe3)
    
    pipe4 = sprites.Pipe(GREEN, 500, 160)
    pipe4.rect.x = 700
    pipe4.rect.y = 380
    all_sprites_list.add(pipe4)
    pipe_sprites_lsit.add(pipe4)
    bottom_sprites_list.add(pipe4)
    ###################################################################
    pipe5 = sprites.Pipe(GREEN, 600, 160)
    pipe5.rect.x = 1000
    pipe5.rect.y = -400
    all_sprites_list.add(pipe5)
    pipe_sprites_lsit.add(pipe5)
    top_sprites_list.add(pipe5)
    
    pipe6 = sprites.Pipe(GREEN, 500, 160)
    pipe6.rect.x = 1000
    pipe6.rect.y = 380
    all_sprites_list.add(pipe6)
    pipe_sprites_lsit.add(pipe6)
    bottom_sprites_list.add(pipe6)
    ###################################################################
    floor1 = sprites.Floor(BLACK, 25, 1000)
    floor1.rect.x = 0
    floor1.rect.y = 575
    all_sprites_list.add(floor1)
    wall_sprites_list.add(floor1)
    
    while start_loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_loop = False
                    loop = True
    
    
    while loop:
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isjump = True
        # allows the cube/bird to jump. 
        if isjump == True:
            bird1.rect.y -= 30
            isjump = False
        else:
            bird1.rect.y += 2 
            
        # to move the pipes towards the left side of the screen
        for i in pipe_sprites_lsit:
            i.rect.x -= 2
        
        
        for i in bottom_sprites_list:
            if i.rect.x == 0:
                rand = random.randrange(370, 550)
                i.rect.y = rand
                tmp = rand
        
        for i in top_sprites_list:
            if i.rect.x == 0:
                change = tmp - 750
                i.rect.y = change
                score +=1
                 
                 
        for i in pipe_sprites_lsit:
            if i.rect.x == 0:
                i.rect.x += 900
                
                
        #check for collisions with the floor and the pipes 
        wall_collision_list = pygame.sprite.spritecollide(bird1, wall_sprites_list, False)
        for i in wall_collision_list:
            print("game over ")
            loop = False
            
        pipe_collision_lsit = pygame.sprite.spritecollide(bird1, pipe_sprites_lsit, False)
        for i in pipe_collision_lsit:
            print("game over your score is " + str(score)) 
            loop = False 
                  
        WINDOW.fill(SKY)
        all_sprites_list.update()
        all_sprites_list.draw(WINDOW)
        pygame.display.update()
        fpsClock.tick(FPS)
        




Game_Loop()

pygame.quit()