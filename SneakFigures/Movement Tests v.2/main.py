import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)#,  LATER
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
