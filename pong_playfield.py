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

# AI Palette
RED = (255, 0,  0)
Palatte_AI_position = (350, 20) # AI Palette primary position

# setting up th palette, filling it with color
PaletteAI = pygame.Surface((Palette_width, Palette_height))
PaletteAI.fill(RED)

# setting up the rectangle with the palette in a primary position
PaletteAI_rectangle = PaletteAI.get_rect()
PaletteAI_rectangle.x = Palatte_AI_position[0]
PaletteAI_rectangle.y = Palatte_AI_position[1]

# AI palette speed
Speed_AI = 5

# Text, variables holding points and text-information
Points_p1 = "0"
Points_AI = "0"
fontObj = pygame.font.Font('freesansbold.ttf', 64) # in-game text font

def display_points1():
    text1 = fontObj.render(Points_p1, True, (0, 0, 0))
    text_rectangle1 = text1.get_rect()
    text_rectangle1.bottomleft = (50, Playfield_height - 10)
    game_window.blit(text1, text_rectangle1)

def display_pointsAI():
    textAI = fontObj.render(Points_AI, True, (0, 0, 0))
    text_rectangleAI = textAI.get_rect()
    text_rectangleAI.topright = (Playfield_width - 50, 10)
    game_window.blit(textAI, text_rectangleAI)

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

    # ball movement
    # move the ball after the events unfold
    Ball_rectangle.move_ip(Ball_speed_x, Ball_speed_y)

    # if the ball leaves the playfield  on the left/right - change the direction of the horizontal ball movement
    if Ball_rectangle.right >= Playfield_width or Ball_rectangle.left <= 0:
        Ball_speed_x *= -1

    if Ball_rectangle.top <= 0: # ball ran through the top
        Ball_speed_y *= -1 # change the movement direction from the top
        Ball_rectangle.x = Playfield_width / 2
        Ball_rectangle.y = Playfield_height / 2
        Points_p1 = str(int(Points_AI) + 1)

    if Ball_rectangle.bottom >= Playfield_height: # ball ran down
        Ball_rectangle.x = Playfield_width / 2 # starting from the middle
        Ball_rectangle.y = Playfield_height / 2
        Points_AI = str(int(Points_p1) + 1)

    # AI
    # when the ball runs to the right, shift the palette in the same direction, elif to the left
    if Ball_rectangle.centerx > PaletteAI_rectangle.centerx:
        PaletteAI_rectangle.x += Speed_AI
    elif Ball_rectangle.centerx < PaletteAI_rectangle.centerx:
        PaletteAI_rectangle.x -= Speed_AI

    # if the ball touches the palette AI, change the balls direction
    if Ball_rectangle.colliderect(PaletteAI_rectangle):
        Ball_speed_y *= -1
        Ball_rectangle.top = PaletteAI_rectangle.bottom

    # if the ball touches the players palette, shift it to another direction
    if Ball_rectangle.colliderect(Palette1_rectangle):
        Ball_speed_y *= -1 # deny the ball form penetrating the palette
        Ball_rectangle.bottom = Palette1_rectangle.top

    # drawing objects
    game_window.fill(LT_BLUE) # window color

    display_points1() # display players points
    display_pointsAI() # display AI points

    # draw the palette inside the game window
    game_window.blit(Palette1, Palette1_rectangle)
    game_window.blit(PaletteAI, PaletteAI_rectangle)

    # draw the ball
    game_window.blit(Ball, Ball_rectangle)

    # update game window and display it
    pygame.display.update()

    # update the gamer clock
    fps_clock.tick(FPS)
