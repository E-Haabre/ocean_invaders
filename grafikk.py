import pygame
from pygame.locals import *
import sys
from sprites import *

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
    def __init__(self, count, sprite, scale, rotation, pos=0, rect = False):
        self.count = count
        self.sprite = sprite
        self.pos = pos
        self.rotation = rotation
        self.load = []
        self.transform = []
        self.rotate = []
        self.scale = scale
        self.rect = rect

    def prep(self):
        for i in range(0,len(self.sprite)):
            self.load.append(pygame.image.load(self.sprite[i]))
            self.rotate.append(pygame.transform.rotate(self.load[i], self.rotation))
            self.transform.append(pygame.transform.scale(self.rotate[i], self.scale))
            
        if self.rect == True:
            self.ent_rect = self.transform[0].get_rect()
            return self.ent_rect

        return self.transform
    
        

    def animer(self, spritesheet):
        tick = int(72/len(spritesheet))
        WINDOW.blit(spritesheet[self.count//tick], self.pos)


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
                  
prep_båt = Animer(0,pirat_sprites, (120,120), 90).prep()

prep_squido = Animer(0,squido_sprites, (60,120), 0).prep()
prep_squid_dykk = Animer(0,squid_dykk_sprites, (60,120), 0).prep()
prep_squid_opp = Animer(0,squid_opp_sprites, (60,120), 0).prep()
prep_squidu = Animer(0,squidu_sprites, (60,120), 0).prep()

prep_sharku = Animer(0,sharku_sprites, (60,120), 0).prep()
prep_sharko = Animer(0,sharko_sprites, (60,120), 0).prep()


"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    WINDOW.fill(color_ocean)

    CLOCK.tick(fps)

    Animer(count, 0, 0, 0, (400, 350)).animer(Fiender(runde).shark())
    Animer(count, 0, 0, 0, (400,500)).animer(prep_båt)
    Animer(count, 0, 0, 0, (200,500)).animer(Fiender(runde).squid())

    count +=1
    if count >= 72:
        count=0
        runde += 1
        if runde == 8:
            runde = 0
    
    pygame.display.update()
"""