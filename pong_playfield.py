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

# in-game palette
Palette_width = 100
Palette_height = 20
BLUE = (0, 0, 255)
Palette_1_position = (350, 360) # palette primary position written in tuple
# creating the palette and filling it in with color
Palette1 = pygame.Surface((Palette_width, Palette_height))
Palette1.fill(BLUE)
# setting the square with the palette in a primary position
Palette1_rectangle = Palette1.get_rect()
Palette1_rectangle.x = Palette_1_position[0]
Palette1_rectangle.y = Palette_1_position[1]
# main loop
while True:    # handling player-generated events
    for event in pygame.event.get():  # capture window close
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # drawing objects
    game_window.fill(LT_BLUE) # window color

    # draw the palette inside the game window
    game_window.blit(Palette1, Palette1_rectangle)

    # update game window and display it
    pygame.display.update()
