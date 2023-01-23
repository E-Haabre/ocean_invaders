# pygame demo 1 - draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random
from grafikk import *

class Player():
    def __init__(self, window, windowWidth, windowHeight, ship_width_height):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.ship_width_height = ship_width_height
        self.playerEntity = Animer(pirat_sprites, (ship_width_height, ship_width_height), 90, 0)
        self.playerEntity.prep()
        self.playerRect = self.playerEntity.ent_rect
        self.playerRect.left = self.windowWidth/2
        self.playerRect.top = self.windowHeigth - (self.windowHeigth/20) - ship_width_height
        self.cannons = [(self.playerRect[2]/32*16.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*19.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*22.5, self.playerRect[3]/32*10)]

    def shoot(self, cannon:int):
        shootingPoint = (self.cannons[cannon][0] + self.playerRect.left, self.cannons[cannon][1] + self.playerRect.top)
        aBullet = bullet_Gen(self.window, self.windowWidth, self.windowHeigth, shootingPoint, 5)
        bullets.append(aBullet)

    def update(self, count):
        self.playerEntity.animer(count)
        if (self.playerRect[2], self.playerRect[3]) != (self.ship_width_height, self.ship_width_height):
            width_height = self.playerRect[2] + 1
            self.playerEntity.scale = (width_height, width_height)
            self.playerEntity.prep()
            self.playerEntity.ent_rect = self.playerRect
            self.playerRect[2] += 1
            self.playerRect[3] += 1
            self.playerRect.top = self.windowHeigth - (self.windowHeigth/20) - self.playerRect[2]
            self.cannons = [(self.playerRect[2]/32*16.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*19.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*22.5, self.playerRect[3]/32*10)]

    def evolve(self, size):
        self.ship_width_height = size

class Enemy():
    def __init__(self, window, windowWidth, windowHeight, enemyWidth, enemyHeight, speed) -> None:
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.enemyEntity = Animer(sharko_sprites,(enemyWidth,enemyHeight),0,0)
        self.enemyEntity.prep()
        self.enemyRect = self.enemyEntity.ent_rect
        self.x = 0
        self.y = - SHIP_WIDTH_HEIGHT
        self.enemyRect.top = self.y
        self.speed = speed

    def spawn(self, x, y):
        self.x = x
        self.y = y
        self.enemyRect.left = self.x

    def update(self):
        ind = enemies.index(self)
        other = enemies.copy()
        other.pop(ind)
        if any([self.enemyRect.colliderect(enemy.enemyRect) for enemy in other]):
            return
        if self.enemyRect.top != self.y:
            fortegn = (self.enemyRect.top - self.y) / abs(self.enemyRect.top - self.y)
            self.enemyRect.top = self.enemyRect.top - (self.speed * fortegn)
        if self.enemyRect.left != self.x:
            fortegn = (self.enemyRect.left - self.x) / abs(self.enemyRect.left - self.x)
            self.enemyRect.left = self.enemyRect.left + (self.speed * fortegn)

    def draw(self, count, runde):
        self.enemyEntity.shark(runde)
        self.enemyEntity.animer(count)

class Explosion():
    def __init__(self, window, windowWidth, windowHeight, x, y, radius):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = x
        self.y = y
        self.radius = radius
        self.curRadius = 1
        self.minus = radius/5

    def update(self):
        if self.radius != self.curRadius:
            self.circle = pygame.draw.circle(self.window, EXPLOSION1, (self.x, self.y), self.radius-self.curRadius)
            self.circle = pygame.draw.circle(self.window, EXPLOSION2, (self.x, self.y), self.radius-self.curRadius-self.minus)
            self.circle = pygame.draw.circle(self.window, EXPLOSION3, (self.x, self.y), self.radius-self.curRadius-(self.minus*2))
            self.circle = pygame.draw.circle(self.window, EXPLOSION4, (self.x, self.y), self.radius-self.curRadius-(self.minus*3))
            self.circle = pygame.draw.circle(self.window, EXPLOSION5, (self.x, self.y), self.radius-self.curRadius-(self.minus*4))
            self.curRadius = self.curRadius + 1
        else:
            explosions.remove(self)

class bullet_Gen():

    def __init__(self, window, windowWidth, windowHeight, pos, speed):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.pos = pos
        self.speed = speed
        self.radius = 1

        self.x = pos[0]
        self.y = pos[1]

        self.circle = pygame.draw.circle(self.window, BLACK, (self.x, self.y), self.radius)

    def update(self):
        self.y = self.y - self.speed
        print(self.y)
        if self.y < 0 - self.radius:
            bullets.remove(self)
        elif any([bullet.circle.colliderect(enemy.enemyRect) for enemy in enemies]):
            anExplosion = Explosion(window, WINDOW_WIDTH, WINDOW_HEIGHT, bullet.x, bullet.y, 40)
            explosions.append(anExplosion)
            bullets.remove(self)

    def draw(self):
        self.circle = pygame.draw.circle(self.window, BLACK, (self.x, self.y), self.radius)


# 2 - Define constants
BASE_PATH = Path(__file__).resolve().parent
EXPLOSION1 = (254,255,181)
EXPLOSION2 = (255,192,113)
EXPLOSION3 = (255,162,85)
EXPLOSION4 = (255,91,20)
EXPLOSION5 = (255,35,35)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
OCEAN_COLOR = (212, 241, 249)
OCEAN_COLOR = (118, 200, 213)
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768
FRAMES_PER_SECOND = 28
SHIP_WIDTH_HEIGHT = 96
ENEMY_WIDTH = 64
ENEMY_HEIGHT = 96
MAX_WIDTH = WINDOW_WIDTH - SHIP_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - SHIP_WIDTH_HEIGHT
N_PIXELS_TO_MOVE = WINDOW_WIDTH / 200

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.


# 5 - Initialize variables
player = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_WIDTH_HEIGHT)
#shipRect = shipImage.get_rect()
#shipRect.left = WINDOW_WIDTH/2
#shipRect.top = WINDOW_HEIGHT - (WINDOW_HEIGHT/20) - SHIP_WIDTH_HEIGHT
bullets = []
enemies = []
explosions = []
bulletSpeed = WINDOW_HEIGHT/100
 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program 
        if event.type == pygame.QUIT:    
            pygame.quit()  
            sys.exit()

    # 8  Do any "per frame" actions
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:
        player.playerRect.left = player.playerRect.left - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:
        player.playerRect.left = player.playerRect.left + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_SPACE]:
        player.shoot(2)
    if keyPressedTuple[pygame.K_UP]:
        aEnemy = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, 2)
        aEnemy.spawn(random.randint(ENEMY_WIDTH/2, WINDOW_WIDTH-ENEMY_WIDTH), 200)
        enemies.append(aEnemy)
    if keyPressedTuple[pygame.K_c]:
        player.evolve(200)

    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()
    
    # 9 - Clear the window
    window.fill(OCEAN_COLOR)
    
    # 10 - Draw all window elements
    player.update(count)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw(count, runde)
    for explosion in explosions:
        explosion.update()

    count +=1
    if count >= 72:
        count=0
        runde += 1
        if runde == 8:
            runde = 0
    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait