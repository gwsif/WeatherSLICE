#@@ Notes to myself
#@@ Notes that should be purged before github start with #@@
#@@ we swapped to pygame to support the Weather Star 4000's infamous 768x480 images.
#@@    Please note that the other resolutions and their associated command bits are
#@@    0 384x120
#@@    1 384x240
#@@    2 768x240
#@@    3 768x480 (ours)
#@@
#@@ NTSC RESOLUTION IS NTSC 486x440.

####################################################################################
# THE     # A fully functional replica of the Weather Star 4000 and the infamous   #
# WEATHER #   station on which it appeared in the 90s complete with commercial     #
# SLICE   #   control, soundtrack choice, custom announcers, and more!             #
####################################################################################
####################################################################################
# The Weather SLICE                                                                #
# Licensed Under the MIT License                                                   #
# (c) 2022 Kevan M. Pledger                                                        #
#                                                                                  #
####################################################################################
#   IF YOU ARE WONDERING WHERE TO BEGIN PLEASE READ THE README FILE IN ENTIRETY!   #
####################################################################################



# -- BEGIN CODE BLOCK --
import pygame
from pygame.locals import *
import sys

# Initialize pygame
pygame.init()

# Set screen Title and Icon
pygame.display.set_caption("The Weather SLICE")
icon = pygame.image.load('assets/graphics/weatherSLICE_icon.png')
pygame.display.set_icon(icon)

# Desired Screen resolutions (here for now) (width x height)
userWidth = 768
userHeight = 480

# Set this display surface (aka window)
displaysurface = pygame.display.set_mode((userWidth, userHeight))
displaysurface.fill((72,72,72))

# INTERFACE ELEMENTS
#    Please refer to GFX-Diagram images for labels
#    bar_a : bottom-most bar without the borders
#    bar_b : secondary bar rendered above the bottom most (typically orange)
#    bar_c : bottom-most bar border dark
#@@
#@@ userHeight * 0.849 gives the exact height of the message crawl bar without borders when screensize is set to 768x480
#

# Twilight Background (purple -> orange gradient)
# Colors:
#    Purple : (34, 67, 137)
#    Orange : (221, 117, 15)
twilight_bg = pygame.image.load("assets/graphics/twilight_bg.bmp")
TWILIGHT_BG_SIZE = (userWidth, 272)
twilight_bg = pygame.transform.scale(twilight_bg, TWILIGHT_BG_SIZE)

displaysurface.blit(twilight_bg, (0,95))

# Obj a
color_a = ((47, 64, 131))
pygame.draw.rect(displaysurface, color_a, pygame.Rect(0, (userHeight * 0.849), userWidth,200))
#@@                                                      ( x   y    w   h )
# Obj b
color_b = ((221,117,15))
pygame.draw.rect(displaysurface, color_b, pygame.Rect(0, (userHeight * 0.765), userWidth,35)) #<---ME
#barborderis pygame.draw.rect(displaysurface, color_b, pygame.Rect(0, (userHeight * 0.849), userWidth,1))
# Obj c
#color_c = (())
#pygame.draw.rect(displaysurface, color_c, pygame.Rect(0, (userHeight * 0.849), userWidth,10))




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #displaysurface.blit(bottomBar_0, (50,50))
    #displaysurface.blit(bottomBar_1, (50,150))

    pygame.display.update()