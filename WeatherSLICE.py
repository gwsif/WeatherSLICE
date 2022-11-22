#// Notes to myself
#// Notes that should be purged before github start with #//
#// We swapped to pygame to support the Weather Star 4000's infamous 768x480 images.
#//    Please note that the other resolutions and their associated command bits are
#//    0 384x120
#//    1 384x240
#//    2 768x240
#//    3 768x480 (ours)
#//
#// NTSC RESOLUTION IS NTSC 486x440.

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
#      Graphical object definitions are found in the slicegraphics.py class        #
####################################################################################



# -- BEGIN CODE BLOCK --
import pygame
from pygame.locals import *
import sys

from slicegraphics import slicegraphics

# Initialize pygame
pygame.init()

# Set screen Title and Icon
pygame.display.set_caption("WeatherSLICE")
icon = pygame.image.load('assets/graphics/weatherSLICE_icon.png')
pygame.display.set_icon(icon)

# Desired viewport size (here for now)
#   Classic viewport size is 768 width x 480 height
userWidth = 768
userHeight = 480

# Initialize display surface (aka window)
displaysurface = pygame.display.set_mode((userWidth, userHeight))
displaysurface.fill((72,72,72))

# Initialize slicegraphics object as sliceWindow
sliceWindow = slicegraphics()
sliceWindow.drawGradient()

#// NOTES TO SELF:
#// Using out slicegraphics object of sliceWindows, we will now
#//   set our colors here (so we can change them later if desired)
#//   and then call the individual functions to draw the bars
#//   LATER: we will want to define these colors in a class or something
#//   and then and call these draw functions in individual slide definitions
#//   so we can create custom WS4000 slide routines (like changing order or adding more etc.)

# Draw Bar A
#    colors may be changed using RGB values
#    suggested colors are commented beside.
#    Definitions may be found in slicegraphics.py
color_a = ((47, 64, 131)) # suggested: 47, 64, 131
sliceWindow.drawBar_A(color_a)

# bar b
# orange bar above blue bar (part of twilight_bg)
color_b = ((221,117,15)) # suggested: 221,117,15
sliceWindow.drawBar_B(color_b)

# bar c
# bluish-white border bar at bottom
color_c = ((93,125,189)) # suggested: 93,125,189
sliceWindow.drawBar_C(color_c)

# bar d
# top indigo/dark blue bar -> not always shown
color_d = ((39,17,97)) # suggested: 39,17,97 
sliceWindow.drawBar_D(color_d)

# bar e
# top gradient bar. Masked my Mask_A to give it a slanted appearance.
color_e1 = ((221,116,15))
color_e2 = ((200,109,21))
color_e3 = ((183,98,34))
color_e4 = ((165,90,42))
color_e5 = ((149,80,51))
color_e6 = ((134,71,63))
color_e7 = ((115,62,74))
color_e8 = ((94,56,80))
sliceWindow.drawBar_E1(color_e1)
sliceWindow.drawBar_E2(color_e2)
sliceWindow.drawBar_E3(color_e3)
sliceWindow.drawBar_E4(color_e4)
sliceWindow.drawBar_E5(color_e5)
sliceWindow.drawBar_E6(color_e6)
sliceWindow.drawBar_E7(color_e7)
sliceWindow.drawBar_E8(color_e8)

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()