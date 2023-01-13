import pygame
from pygame.locals import *
import sys
from pathlib import Path

grafikk_path = Path(__file__).resolve().parent

ball_path = str(grafikk_path) + '\Grafikk\png_ball.png'
piratskip1_path = str(grafikk_path) + '\Grafikk\Piratskip1.png'
piratskip0_path = str(grafikk_path) + '\Grafikk\Piratskip0.png'
piratskipm1_path = str(grafikk_path) + '\Grafikk\Piratskip-1.png'



anicount = 0



color_ocean = (0,30,127)
window_width = 1500
window_height = 850
fps = 28

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

class Spillerbåt:
    def __init__(self, animasjon, sprite=0):
        self.ani = animasjon           
        self.idle_boat = [pygame.image.load(piratskip1_path), pygame.image.load(piratskip0_path), pygame.image.load(piratskipm1_path),pygame.image.load(piratskip0_path)]
        self.idle_boat = [pygame.transform.scale(self.idle_boat[0], (120,120)),pygame.transform.scale(self.idle_boat[1], (120,120)),pygame.transform.scale(self.idle_boat[2], (120,120)),pygame.transform.scale(self.idle_boat[3], (120,120))]
        
        
    
    def idle(self):
        #window.blit(self.idle_boat[self.ani], (100,200))
        
        window.blit(self.idle_boat[self.ani//18], (350,250))
                  
        



#ball_bilde = pygame.image.load(ball_path)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.fill(color_ocean)

    #window.blit(pygame.image.load(piratskip1_path),(100,200))


    clock.tick(fps)

    Spillerbåt(anicount).idle()
    anicount +=1
    if anicount >= 72:
        anicount=0
    pygame.display.update()
