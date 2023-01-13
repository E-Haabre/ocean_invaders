import pygame
from pygame.locals import *
import sys
from pathlib import Path

grafikk_path = Path(__file__).resolve().parent

ball_path = str(grafikk_path) + '\Grafikk\png_ball.png'
piratskip1_path = str(grafikk_path) + '\Grafikk\Piratskip1.png'
piratskip0_path = str(grafikk_path) + '\Grafikk\Piratskip0.png'
piratskipm1_path = str(grafikk_path) + '\Grafikk\Piratskip-1.png'

black = (0,0,0)
window_width = 1000
window_height = 600
fps = 30

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

print(ball_path)

ball_bilde = pygame.image.load(ball_path)
idle_boat = [pygame.image.load(piratskip1_path), pygame.image.load(piratskip0_path), pygame.image.load(piratskipm1_path)]
idle_boat = pygame.transform.scale(idle_boat, (80,80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.fill(black)

    window.blit(idle_boat,(100,200))

    pygame.display.update()

    clock.tick(fps)
