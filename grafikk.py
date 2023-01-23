import pygame
from pygame.locals import *
from sprites import *

count = 0
runde = 0

window_width = 1500
window_height = 850

WINDOW = pygame.display.set_mode((window_width, window_height))

class Animer:
    def __init__(self, sprites, scale, rotation, pos=0):
        self.sprites = sprites
        self.pos = pos
        self.rotation = rotation
        self.scale = scale

    def prep(self, spriteList:list = None, new_rect = True):
        self.transformed = []
        if spriteList == None:
            spriteList = self.sprites
        for sprite in spriteList:
            sprite = (pygame.image.load(sprite))
            sprite = (pygame.transform.rotate(sprite, self.rotation))
            sprite = (pygame.transform.scale(sprite, self.scale))
            self.transformed.append(sprite)

        if new_rect == True:
            self.ent_rect = self.transformed[0].get_rect()

    def squid(self):
        if runde == 3:
            self.prep(squid_dykk_sprites, False)
        elif runde == 7:
            self.prep(squid_opp_sprites, False)
        elif runde >= 4:
            self.prep(squidu_sprites, False)
        else:
            self.prep(squido_sprites, False)

    def shark(self, runde):
        if runde >= 4:
            self.prep(sharko_sprites, False)
        else:
            self.prep(sharku_sprites, False)

    def animer(self,count):
        tick = int(72/len(self.transformed))
        WINDOW.blit(self.transformed[count//tick], self.ent_rect)