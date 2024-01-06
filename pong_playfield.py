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

# setting the rectangle with the palette in a primary position
Palette1_rectangle = Palette1.get_rect()
Palette1_rectangle.x = Palette_1_position[0]
Palette1_rectangle.y = Palette_1_position[1]

# creating the ball
Ball_width = 20
Ball_height = 20
Ball_speed_x = 6 # horizontal speed
Ball_speed_y = 6 # vertical speed
GREEN = (0, 255, 0)

# creating the ball surface, drawing the ball and filling it with color
Ball = pygame.Surface((Ball_width, Ball_height), pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(Ball, GREEN, (0, 0, Ball_width, Ball_height))

# setting up the rectangle holding the ball in a primary position
Ball_rectangle = Ball.get_rect()
Ball_rectangle.x = Playfield_width / 2
Ball_rectangle.y = Playfield_height / 2

# setting up the animation
FPS = 30 # frames per second for low quality graphics
fps_clock = pygame.time.Clock() # in-game clock

# main loop
while True:    # handling player-generated events
    for event in pygame.event.get():  # capture window close
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # intercept the mouse movement
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos # coordinates x, y of mouse cursor

            # calculate the movement of the players palette
            shift = mouseX - (Palette_width / 2)

            # if we resurface on the right of the playfield
            if shift > Playfield_width - Palette_width:
                shift = Playfield_width - Palette_width
            # if we resurface on the left of the playfield
            if shift < 0:
                shift = 0
            # update the position of the palette
            Palette1_rectangle.x = shift

    # drawing objects
    game_window.fill(LT_BLUE) # window color

    # draw the palette inside the game window
    game_window.blit(Palette1, Palette1_rectangle)

    # update game window and display it
    pygame.display.update()
