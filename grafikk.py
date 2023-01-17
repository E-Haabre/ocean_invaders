import pygame
from pygame.locals import *
import sys
from pathlib import Path

grafikk_path = Path(__file__).resolve().parent
grafikk_path = str(grafikk_path) + "\Grafikk"

pritaskip_path = str(grafikk_path) + "\Pirat_spiller"
piratskip1_path = str(pritaskip_path) + '\Piratskip1.png'
piratskip0_path = str(pritaskip_path) + '\Piratskip0.png'
piratskipm1_path = str(pritaskip_path) + '\Piratskip-1.png'

squid_path = str(grafikk_path) + "\Blekksprut"
squid0_path = str(squid_path) + "\squid0.png"
squid1_path = str(squid_path) + "\squid1.png"

shark_path = str(grafikk_path) + "\Shark"
sharkL2u_path = str(shark_path) + "\sharkL2(under).png"
sharkL1u_path = str(shark_path) + "\sharkL1(under).png"
shark0u_path = str(shark_path) + "\shark0(under).png"
sharkR1u_path = str(shark_path) + "\sharkR1(under).png"
sharkR2u_path = str(shark_path) + "\sharkR2(under).png"

sharkL2o_path = str(shark_path) + "\shark0(over).png"
sharkL1o_path = str(shark_path) + "\shark0(over).png"
shark0o_path = str(shark_path) + "\shark0(over).png"
sharkR1o_path = str(shark_path) + "\shark0(over).png"
sharkR2o_path = str(shark_path) + "\shark0(over).png"


pirat_sprites = [piratskip1_path, piratskip0_path, piratskipm1_path, piratskip0_path]
squid_sprites = [squid0_path, squid1_path]
sharku_sprites = [sharkL2u_path, sharkL1u_path, shark0u_path, sharkR1u_path, sharkR2u_path, sharkR1u_path, sharkL1u_path]
sharko_sprites = [sharkL2o_path, sharkL1o_path, shark0o_path, sharkR1o_path, sharkR2o_path]


anicount = 0



color_ocean = (118,200,213)
window_width = 1500
window_height = 850
fps = 28

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

class Animer:
    def __init__(self, count, tick, sprite, scale, pos, L1 = [], L2 = []):
        self.count = count
        self.tick = tick
        self.sprite = sprite
        self.pos = pos
        self.load = L1
        self.transform = L2
        self.scale = scale

    def prep(self):
        for i in range(0,len(self.sprite)):
            self.load.append(pygame.image.load(self.sprite[i]))
            self.transform.append(pygame.transform.scale(self.load[i], self.scale))

    def animer(self):
        
        window.blit(self.transform[self.count//self.tick], self.pos)
    
"""
class Spillerbåt:
    def __init__(self, animasjon):
        self.ani = animasjon           
        self.idle_boat = [pygame.image.load(piratskip1_path), pygame.image.load(piratskip0_path), pygame.image.load(piratskipm1_path),pygame.image.load(piratskip0_path)]
        self.idle_boat = [pygame.transform.scale(self.idle_boat[0], (120,120)),pygame.transform.scale(self.idle_boat[1], (120,120)),pygame.transform.scale(self.idle_boat[2], (120,120)),pygame.transform.scale(self.idle_boat[3], (120,120))]
        
        
    
    def idle(self):

        window.blit(self.idle_boat[self.ani//18], (550,350))
"""

class fiender:
    def __init__(self, animasjon, level=0):
        self.ani = animasjon
        self.level = level



    def squid(self):
        s

                  
#prep_båt = Animer(anicount,18,pirat_sprites, (120,120), 0).prep()
#prep_squid = Animer(anicount,18,squid_sprites, (60,120), 0).prep()
prep_sharku = Animer(0,0,sharku_sprites, (60,120), 0).prep()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.fill(color_ocean)

    #window.blit(pygame.image.load(piratskip1_path),(100,200))


    clock.tick(fps)

    #Spillerbåt(anicount).idle()
    Animer(anicount,10, 0, 0, (400, 400)).animer()
    anicount +=1
    if anicount >= 72:
        anicount=0
    pygame.display.update()
