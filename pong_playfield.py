import pygame
import sys
from pygame.locals import *

# starting pygame
pygame.init()

# width and height of the playfield
Playfield_width = 800
Playfield_height = 400

# color of the game window, rgb witten into a tupla(?)
LT_BLUE = (230, 255, 255)

# drawing surface, initiation of the playing field
game_window = pygame.display.set_mode((Playfield_width, Playfield_height), 0, 32)

# game_window title
pygame.display.set_caption('Simple Pong')

# main loop
while True:    # handling player-generated events
    for event in pygame.event.get():  # capture window close
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # drawing objects
    game_window.fill(LT_BLUE) # window color

    # update game window and display it
    pygame.display.update()
