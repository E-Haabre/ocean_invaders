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
squido0_path = str(squid_path) + "\squid0.png"
squido1_path = str(squid_path) + "\squid1.png"
squid_dykk1_path = str(squid_path) + "\squid_dykk1.png"
squid_dykk2_path = str(squid_path) + "\squid_dykk2.png"
squid0u_path = str(squid_path) + "\squid1(under).png"
squid1u_path = str(squid_path) + "\squid2(under).png"
squid2u_path = str(squid_path) + "\squid3(under).png"


shark_path = str(grafikk_path) + "\Shark"
sharkL2u_path = str(shark_path) + "\sharkL2(under).png"
sharkL1u_path = str(shark_path) + "\sharkL1(under).png"
shark0u_path = str(shark_path) + "\shark0(under).png"
sharkR1u_path = str(shark_path) + "\sharkR1(under).png"
sharkR2u_path = str(shark_path) + "\sharkR2(under).png"

sharkL2o_path = str(shark_path) + "\sharkL2(over).png"
sharkL1o_path = str(shark_path) + "\sharkL1(over).png"
shark0o_path = str(shark_path) + "\shark0(over).png"
sharkR1o_path = str(shark_path) + "\sharkR1(over).png"
sharkR2o_path = str(shark_path) + "\sharkR2(over).png"


pirat_sprites = [piratskip1_path, piratskip0_path, piratskipm1_path, piratskip0_path]
squido_sprites = [squido0_path, squido1_path, squido0_path, squido1_path]
squid_dykk_sprites = [squid_dykk1_path, squid_dykk2_path, squid_dykk1_path, squid_dykk2_path]
squid_opp_sprites = [squid_dykk2_path, squid_dykk1_path, squid_dykk2_path, squid_dykk1_path]
squidu_sprites = [squid0u_path, squid1u_path, squid2u_path, squid1u_path]
sharku_sprites = [sharkR1u_path, sharkR2u_path, sharkR1u_path, shark0u_path, sharkL1u_path, sharkL2u_path, sharkL1u_path,shark0u_path]
sharko_sprites = [sharkR1o_path, sharkR2o_path, sharkR1o_path, shark0o_path, sharkL1o_path, sharkL2o_path, sharkL1o_path, shark0o_path]


count = 0
runde = 0



color_ocean = (118,200,213)
window_width = 1500
window_height = 850
fps = 28

pygame.init()
WINDOW = pygame.display.set_mode((window_width, window_height))
CLOCK = pygame.time.Clock()

class Animer:
    def __init__(self, count, sprite, scale, pos):
        self.count = count
        self.sprite = sprite
        self.pos = pos
        self.load = []
        self.transform = []
        self.scale = scale

    def prep(self):
        for i in range(0,len(self.sprite)):
            self.load.append(pygame.image.load(self.sprite[i]))
            self.transform.append(pygame.transform.scale(self.load[i], self.scale))
        
        return self.transform

    def animer(self, spritesheet):
        tick = int(72/len(spritesheet))
        WINDOW.blit(spritesheet[self.count//tick], self.pos)
    
"""
class Spillerbåt:
    def __init__(self, animasjon):
        self.ani = animasjon           
        self.idle_boat = [pygame.image.load(piratskip1_path), pygame.image.load(piratskip0_path), pygame.image.load(piratskipm1_path),pygame.image.load(piratskip0_path)]
        self.idle_boat = [pygame.transform.scale(self.idle_boat[0], (120,120)),pygame.transform.scale(self.idle_boat[1], (120,120)),pygame.transform.scale(self.idle_boat[2], (120,120)),pygame.transform.scale(self.idle_boat[3], (120,120))]
        
        
    
    def idle(self):

        window.blit(self.idle_boat[self.ani//18], (550,350))
"""

class Fiender:
    def __init__(self, runde):
        self.runde = runde

    def squid(self):
        if self.runde == 3:
            return prep_squid_dykk

        elif self.runde == 7:
            return prep_squid_opp   

        elif self.runde >= 4:
            return prep_squidu

        else:
            return prep_squido
    
    def shark(self):
       
        if self.runde >= 4:
            return prep_sharko
        
        else:
            return prep_sharku
                  
prep_båt = Animer(0,pirat_sprites, (120,120), 0).prep()

prep_squido = Animer(0,squido_sprites, (60,120), 0).prep()
prep_squid_dykk = Animer(0,squid_dykk_sprites, (60,120), 0).prep()
prep_squid_opp = Animer(0,squid_opp_sprites, (60,120), 0).prep()
prep_squidu = Animer(0,squidu_sprites, (60,120), 0).prep()

prep_sharku = Animer(0,sharku_sprites, (60,120), 0).prep()
prep_sharko = Animer(0,sharko_sprites, (60,120), 0).prep()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    WINDOW.fill(color_ocean)

    #window.blit(pygame.image.load(piratskip1_path),(100,200))


    CLOCK.tick(fps)

    #Spillerbåt(anicount).idle()
    Animer(count, 0, 0, (400, 350)).animer(Fiender(runde).shark())
    Animer(count, 0, 0, (400,500)).animer(prep_båt)
    Animer(count, 0, 0, (200,500)).animer(Fiender(runde).squid())

    count +=1
    if count >= 72:
        count=0
        runde += 1
        if runde == 8:
            runde = 0
    
    pygame.display.update()
