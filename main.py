# pygame demo 1 - draw one image

# 1 - Import packages
import sys
import random
from sprites import *
from grafikk import *


class Player():
    def __init__(self, window, windowWidth, windowHeight, ship_width_height):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.ship_width_height = ship_width_height
        #self.hitbox = (self.x, self.y, self.width, self.height)
        self.playerEntity = Animer(pirat_sprites, (ship_width_height, ship_width_height), 90)
        self.playerEntity.prep()
        self.playerRect = self.playerEntity.ent_rect
        self.playerRect.left = self.windowWidth/2
        self.playerRect.top = self.windowHeigth - (self.windowHeigth/20) - ship_width_height
        self.playerHitbox = self.playerRect.copy()
        self.playerHitbox.inflate_ip(-2, -46)
        self.lives = 3
        self.cannons = [(self.playerRect[2]/32*16.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*19.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*22.5, self.playerRect[3]/32*10)]
        self.cannonIndex = 0
        self.charge = 0

    def shoot(self, cannon:int = None):
        if self.charge <= 0:
            if cannon != None:
                self.cannonIndex = cannon
            shootingPoint = (self.cannons[self.cannonIndex][0] + self.playerRect.left, self.cannons[self.cannonIndex][1] + self.playerRect.top)
            aBullet = bullet_Gen(self.window, self.windowWidth, self.windowHeigth, shootingPoint, 5, CANNONBALL, self.playerRect[2]/96)
            bullets.append(aBullet)
            self.cannonIndex += 1
            if self.cannonIndex >= 3:
                self.cannonIndex = 0
            self.charge = 14

    def update(self, count):
        self.charge -=1
        self.playerHitbox.clamp_ip(self.playerRect)
        self.playerEntity.animer(count)
        pygame.draw.rect(window, (255,0,0), self.playerHitbox, 2)
        """
        if (self.playerRect[2], self.playerRect[3]) != (self.ship_width_height, self.ship_width_height):
            width_height = self.playerRect[2] + 1
            self.playerEntity.scale = (width_height, width_height)
            self.playerEntity.prep()
            self.playerEntity.ent_rect = self.playerRect
            if (self.playerRect[2], self.playerRect[3]) < (self.ship_width_height, self.ship_width_height):
                self.playerRect[2], self.playerRect[3] = self.playerRect[2] + 1, self.playerRect[3] + 1
                self.playerRect.left -= 0
            elif (self.playerRect[2], self.playerRect[3]) > (self.ship_width_height, self.ship_width_height):
                self.playerRect[2], self.playerRect[3] = self.playerRect[2] - 1, self.playerRect[3] - 1
                self.playerRect.left += 0
            self.playerRect.top = self.windowHeigth - (self.windowHeigth/20) - self.playerRect[2]
            self.cannons = [(self.playerRect[2]/32*16.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*19.5, self.playerRect[3]/32*10), (self.playerRect[2]/32*22.5, self.playerRect[3]/32*10)]
        """
        if self.lives <= 0:
            pygame.quit()  
            sys.exit()

    def evolve(self, size):
        self.ship_width_height = size

class Enemy():
    def __init__(self, window, windowWidth, windowHeight, enemyWidth, enemyHeight, speed, sprites, y, shark = False, squid = False) -> None:
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.enemyEntity = Animer(sprites,(enemyWidth,enemyHeight),0,0)
        self.enemyEntity.prep()
        self.enemyRect = self.enemyEntity.ent_rect
        #self.enemyHitbox = self.enemyRect.copy()
        #self.enemyHitbox.inflate_ip(-1,-20)
        #self.enemyHitbox = self.enemyRect.copy()
        #self.enemyHitbox.inflate_ip(-1,-40)
        self.speed = speed
        self.shark = shark
        self.squid = squid
        self.x = 0
        self.y = y
        self.enemyRect.top = self.y
        self.speed = speed
        self.lives = 1
        self.charge = 0
        if self.shark == True:
            self.enemyHitbox = self.enemyRect.copy()
            self.enemyHitbox.inflate_ip(-1,-20)
            self.cannon = (self.enemyRect[2]/16*8, self.enemyRect[3]/32*22)
            self.color = (99, 142, 149)
        else:
            self.enemyHitbox = self.enemyRect.copy()
            self.enemyHitbox.inflate_ip(-1,-40)
            self.cannon = (self.enemyRect[2]/16*8, self.enemyRect[3]/32*17)
            self.color = (129, 142, 177)

    def spawn(self, x, y):
        self.x = x
        self.y = y
        self.enemyRect.left = self.x

    def shoot(self):
        if self.charge <= 0:
            shootingPoint = (self.enemyRect.left + self.cannon[0], self.enemyRect.top + self.cannon[1])
            aBullet = bullet_Gen(self.window, self.windowWidth, self.windowHeigth, shootingPoint, -5, self.color, 8, enemyFire = True)
            bullets.append(aBullet)
            self.charge = 28*3

    def update(self):
        if self.lives == 0:
            enemies.remove(self)
            return
        self.charge -= 1
        ind = enemies.index(self)
        other = enemies.copy()
        other.pop(ind)
        if any([(self.enemyHitbox.colliderect(bullet.circle) and bullet.enemyFire == False) for bullet in bullets]):
            self.lives -= 1
        if self.enemyEntity.shooting == True:
            self.shoot()
        if any([self.enemyHitbox.colliderect(enemy.enemyHitbox) for enemy in other]):
            return
        if self.enemyRect.top != self.y:
            fortegn = (self.enemyRect.top - self.y) / abs(self.enemyRect.top - self.y)
            self.enemyRect.top = self.enemyRect.top - (self.speed * fortegn)
        if self.enemyRect.left != self.x:
            fortegn = (self.enemyRect.left - self.x) / abs(self.enemyRect.left - self.x)
            self.enemyRect.left = self.enemyRect.left + (self.speed * fortegn)

    def draw(self, count, runde):
        if self.shark == True:
            self.enemyEntity.shark(runde)
        elif self.squid == True:
            self.enemyEntity.squid(runde)
        self.enemyEntity.animer(count)
        self.enemyHitbox.clamp_ip(self.enemyRect)
        pygame.draw.rect(window, (255,0,0), self.enemyHitbox, 2)


class Explosion():
    def __init__(self, window, windowWidth, windowHeight, x, y, radius):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = x
        self.y = y
        self.radius = radius
        self.curRadius = 0
        self.minus = radius/5

    def update(self):
        if self.radius != self.curRadius:
            pygame.draw.circle(self.window, EXPLOSION1, (self.x, self.y), self.radius-self.curRadius)
            pygame.draw.circle(self.window, EXPLOSION2, (self.x, self.y), self.radius-self.curRadius-self.minus)
            pygame.draw.circle(self.window, EXPLOSION3, (self.x, self.y), self.radius-self.curRadius-self.minus*2)
            pygame.draw.circle(self.window, EXPLOSION4, (self.x, self.y), self.radius-self.curRadius-self.minus*3)
            pygame.draw.circle(self.window, EXPLOSION5, (self.x, self.y), self.radius-self.curRadius-self.minus*4)
            self.curRadius = self.curRadius + 1
        else:
            explosions.remove(self)

class bullet_Gen():

    def __init__(self, window, windowWidth, windowHeight, pos, speed, color, radius = 1, enemyFire = False):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeigth = windowHeight
        self.pos = pos
        self.speed = speed
        self.radius = radius
        self.enemyFire = enemyFire
        self.color = color

        self.x = pos[0]
        self.y = pos[1]

        self.circle = pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.y = self.y - self.speed
        if self.y < 0 - self.radius or self.y > self.windowHeigth + self.radius:
            bullets.remove(self)
            return
        if self.enemyFire == True:
            #anExplosion = Explosion(window, self.windowWidth, self.windowHeigth, bullet.x, bullet.y, self.radius)
            #explosions.append(anExplosion)
            if bullet.circle.colliderect(player.playerHitbox):
                anExplosion = Explosion(window, self.windowWidth, self.windowHeigth, bullet.x, bullet.y, self.radius*10)
                explosions.append(anExplosion)
                bullets.remove(self)
                player.lives -= 1
        else:
            if any([bullet.circle.colliderect(enemy.enemyHitbox) for enemy in enemies]):
                anExplosion = Explosion(window, self.windowWidth, self.windowHeigth, bullet.x, bullet.y, self.radius*10)
                explosions.append(anExplosion)
                bullets.remove(self)

    def draw(self):
        self.circle = pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

class SpawnBox():
    def __init__(self, window, pos, width, height):
        self.window = window
        self.pos = pos
        self.width = width
        self.height = height
        self.occupied = False
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
    
    def update(self):
        if any([self.rect.colliderect(enemy.enemyRect) for enemy in enemies]):
            self.occupied = True
        else: 
            self.occupied = False

def makeSpawn(min_boxes:int = 28):
    space_x = 16
    space_y = 4
    height = ENEMY_HEIGHT
    width = ENEMY_WIDTH
    spawns_per_y = int(WINDOW_WIDTH/(width + space_x/2))
    leftover = WINDOW_WIDTH - (width + space_x/2) * spawns_per_y
    rows = 1
    boxes = rows * spawns_per_y
    while boxes < min_boxes:
        rows += 1
        boxes = rows * spawns_per_y
    for row in range(rows):
        for box in range(spawns_per_y):
            x = int(leftover/2 + space_x/2 + (width + space_x/2)*box)
            y = int((-space_y-height)*(row+1))
            box = SpawnBox(window, (x, y), width, height)
            spawnLocations.append(box)

class Water():
    def __init__(self, window, windowWidth, windowHeight, pos = 0):
        self.WHITE = (183, 226, 233)
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.timer = 28
        self.width_height = 3
        if pos == 0:
            self.pos = (random.randrange(0, self.windowWidth,self.width_height),random.randrange(0,self.windowHeight, self.width_height))
        else:
            self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width_height, self.width_height)

    def spawn(self, pos):
        if 0 < pos[0] < window_width and 0 < pos[1] < window_height:
            water_thing = Water(self.window, self.windowWidth, self.windowHeight, pos)
            whites.append(water_thing)

    def update(self):
        perc = 0.004
        self.timer -= 1
        if self.timer <= 0:
            whites.remove(self)
        pygame.draw.rect(self.window, self.WHITE, self.rect)
        if random.random() < perc:
            new_pos = (self.pos[0] + self.width_height, self.pos[1])
            self.spawn(new_pos)
        if random.random() < perc:
            new_pos = (self.pos[0] - self.width_height, self.pos[1])
            self.spawn(new_pos)
        if random.random() < perc:
            new_pos = (self.pos[0], self.pos[1] + self.width_height)
            self.spawn(new_pos)
        if random.random() < perc:
            new_pos = (self.pos[0] - self.width_height, self.pos[1] - self.width_height)
            self.spawn(new_pos)
        if random.random() < perc:
            new_pos = (self.pos[0] - self.width_height, self.pos[1] + self.width_height)
            self.spawn(new_pos) 
        if random.random() < perc:
            new_pos = (self.pos[0] + self.width_height, self.pos[1] - self.width_height)
            self.spawn(new_pos)
        if random.random() < perc:
            new_pos = (self.pos[0] + self.width_height, self.pos[1] + self.width_height)
            self.spawn(new_pos)       

# 2 - Define constants
BASE_PATH = Path(__file__).resolve().parent
EXPLOSION1 = (254,255,181)
EXPLOSION2 = (255,192,113)
EXPLOSION3 = (255,162,85)
EXPLOSION4 = (255,91,20)
EXPLOSION5 = (255,35,35)
BLACK = (0, 0, 0)
CANNONBALL = (80, 83, 84)
RED = (255, 0, 0)
OCEAN_COLOR = (212, 241, 249)
OCEAN_COLOR = (118, 200, 213)
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768
FRAMES_PER_SECOND = 28
SHIP_WIDTH_HEIGHT = 96
ENEMY_WIDTH = 48
ENEMY_HEIGHT = 96
MAX_WIDTH = WINDOW_WIDTH - SHIP_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - SHIP_WIDTH_HEIGHT
N_PIXELS_TO_MOVE = int(WINDOW_WIDTH / 200)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.


# 5 - Initialize variables
player = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_WIDTH_HEIGHT)
bullets = []
enemies = []
explosions = []
spawnLocations = []
whites = []
bulletSpeed = WINDOW_HEIGHT/100
makeSpawn()

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
        player.shoot()
    if keyPressedTuple[pygame.K_UP]:
        index = random.randint(0, len(spawnLocations)-1)
        shark_or_squid = random.randint(0,1)
        box = spawnLocations[index]
        if box.occupied == False and len(enemies) <= len(spawnLocations):
            spawnLocation = box.pos
            if shark_or_squid == 1:
                aEnemy = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, 2, squido_sprites, spawnLocation[1], shark = True)
            else:
                aEnemy = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, 2, squido_sprites, spawnLocation[1], squid = True)
            aEnemy.spawn(spawnLocation[0], 200)
            enemies.append(aEnemy)
    if keyPressedTuple[pygame.K_c]:
        player.evolve(200)
    if keyPressedTuple[pygame.K_x]:
        player.evolve(100)

    for enemy in enemies:
        enemy.update()
    for bullet in bullets:
        bullet.update()
    for spawnBox in spawnLocations:
        spawnBox.update()
    
    # 9 - Clear the window
    window.fill(OCEAN_COLOR)
    
    # 10 - Draw all window elements
    if any([count%6 == 0]):
        noe = Water(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        whites.append(noe)
    for white in whites:
        white.update()
    player.update(count)
    for bullet in bullets:
        bullet.draw()
    for enemy in reversed(enemies):
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