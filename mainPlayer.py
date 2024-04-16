import pygame
import sys
from player import Player

pygame.init()

FPS = 60
dima = Player()
rrr = (255, 255, 255)
Colors = (0, 255, 0)

clock = pygame.time.Clock()
displays = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    displays.fill(rrr)
    dima.draw_player(displays, Colors, 16)

    # displays.fill(rrr)
    
    pygame.display.flip()
    clock.tick(FPS)