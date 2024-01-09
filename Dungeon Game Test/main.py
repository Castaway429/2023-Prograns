import pygame, sys
from maps import *
from room import Room, current_room_index

#start Pygame
pygame.init()
#Screen Resolution

clock = pygame.time.Clock()

#Our screen variable
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

current_room_data = rooms[current_room_index]
room = Room(current_room_data, screen)  # Initialize the first room

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click click~!")

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.fill('black')
    room.run()

    pygame.display.update()
    clock.tick(60)
