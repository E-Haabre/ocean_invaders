import pygame
from pygame.locals import *
from sprites import *

pirat_sprites = [pygame.image.load(sprite) for sprite in pirat_sprites]
squido_sprites = [pygame.image.load(sprite) for sprite in squido_sprites]
squid_dykk_sprites = [pygame.image.load(sprite) for sprite in squid_dykk_sprites]
squid_opp_sprites = [pygame.image.load(sprite) for sprite in squid_opp_sprites]
squidu_sprites = [pygame.image.load(sprite) for sprite in squidu_sprites]
sharku_sprites = [pygame.image.load(sprite) for sprite in sharku_sprites]
sharko_sprites = [pygame.image.load(sprite) for sprite in sharko_sprites]

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
        self.shoot = False
        self.shootIndex = 0
        self.shooting = False

    def prep(self, spriteList:list = None, new_rect = True):
        self.transformed = []
        if spriteList == None:
            spriteList = self.sprites
        for sprite in spriteList:
            sprite = (pygame.transform.rotate(sprite, self.rotation))
            sprite = (pygame.transform.scale(sprite, self.scale))
            self.transformed.append(sprite)

        if new_rect == True:
            self.ent_rect = self.transformed[0].get_rect()

    def squid(self, runde):
        if runde == 3:
            self.prep(squid_dykk_sprites, False)
            self.shoot = False
        elif runde == 7:
            self.prep(squid_opp_sprites, False)
            self.shoot = False
        elif runde >= 4:
            self.prep(squidu_sprites, False)
            self.shoot = True
            self.shootIndex = 2
        else:
            self.prep(squido_sprites, False)
            self.shoot = False

    def shark(self, runde):
        if runde >= 4:
            self.prep(sharko_sprites, False)
            self.shoot = True
            self.shootIndex = 1
        else:
            self.prep(sharku_sprites, False)
            self.shoot = False

    def animer(self,count):
        tick = int(72/len(self.transformed))
        WINDOW.blit(self.transformed[count//tick], self.ent_rect)
        if self.shoot == True and self.transformed[count//tick] == self.transformed[self.shootIndex]:
            self.shooting = True
        else:
            self.shooting = False