# pygame demo 1 - draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

class Player():
    def __init__(self, window, windowWidth, windowHeight):
        pass

class Enemy():
    def __init__(self, window, windowWidth, windowHeight, speed) -> None:
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        pathToShip = BASE_PATH / 'Grafikk/Shark/shark0(over).png'
        self.enemyImage = pygame.image.load(pathToShip)
        self.enemyImage = pygame.transform.rotate(self.enemyImage,180)
        self.enemyImage = pygame.transform.scale(self.enemyImage, (SHIP_WIDTH_HEIGHT, SHIP_WIDTH_HEIGHT))
        self.enemyRect = self.enemyImage.get_rect()
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
    
    def draw(self):
        window.blit(self.enemyImage, self.enemyRect)

    #def __del__(self):
    #    print("deleted")

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

    #def __del__(self):
    #    print("deleted")

class bullet_Gen():

    def __init__(self, window, windowWidth, windowHeight, ship, speed):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.ship = ship
        self.speed = speed
        self.radius = 1
        
        self.x = self.ship[0] + (self.ship[2]/32*(32-12))
        self.y = self.ship[1] + (self.ship[3]/32*9)

        self.circle = pygame.draw.circle(self.window, BLACK, (self.x, self.y), self.radius)

    def update(self):
        self.y = self.y - self.speed
        if self.y < 0 - self.radius:
            bullets.remove(self)
        elif any([bullet.circle.colliderect(enemy.enemyRect) for enemy in enemies]):
            anExplosion = Explosion(window, WINDOW_WIDTH, WINDOW_HEIGHT, bullet.x, bullet.y, 20)
            explosions.append(anExplosion)
            bullets.remove(self)

    def draw(self):
        self.circle = pygame.draw.circle(self.window, BLACK, (self.x, self.y), self.radius)

    #def __del__(self):
    #    print("deleted")


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
FRAMES_PER_SECOND = 30
SHIP_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - SHIP_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - SHIP_WIDTH_HEIGHT
TARGET_WIDHT_HEIGHT = 120
N_PIXELS_TO_MOVE = WINDOW_WIDTH / 200

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
pathToShip = BASE_PATH / 'Grafikk/Pirat_spiller/Piratskip0.png'
shipImage = pygame.image.load(pathToShip)
shipImage = pygame.transform.rotate(shipImage,90)
shipImage = pygame.transform.scale(shipImage, (SHIP_WIDTH_HEIGHT, SHIP_WIDTH_HEIGHT))

# 5 - Initialize variables
shipRect = shipImage.get_rect()
shipRect.left = WINDOW_WIDTH/2
shipRect.top = WINDOW_HEIGHT - (WINDOW_HEIGHT/20) - SHIP_WIDTH_HEIGHT
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
        shipRect.left = shipRect.left - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:
        shipRect.left = shipRect.left + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_SPACE]:
        aBullet = bullet_Gen(window, WINDOW_WIDTH, WINDOW_HEIGHT, shipRect, 5)
        bullets.append(aBullet)
    if keyPressedTuple[pygame.K_UP]:
        aEnemy = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT, 2)
        aEnemy.spawn(random.randint(SHIP_WIDTH_HEIGHT/2, WINDOW_WIDTH-SHIP_WIDTH_HEIGHT), 200)
        enemies.append(aEnemy)

    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()
    
    # 9 - Clear the window
    window.fill(OCEAN_COLOR)
    
    # 10 - Draw all window elements
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    for explosion in explosions:
        explosion.update()
    
    window.blit(shipImage, shipRect)    
    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait