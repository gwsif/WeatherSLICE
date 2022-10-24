# This class is for drawing graphics
# 
#   The intent of this class is to draw objects to the screen.
#   After careful observation of existing Weather Star 4000 systems
#   I've determined that many of the original gradients and other objects
#   were drawn on-screen using the original graphics module rather than
#   pre-rendered. This class aims to reproduce this as best as possible by 
#   providing methods within to draw commonly used assets inside of the 
#   Weather Star 4000 simulation.
#
#   All comments beginning with #// can (and should be!) cleaned prior to release
import pygame

# INTERFACE ELEMENTS
#    Please refer to GFX-Diagram images for labels
#    Bar A  : bottom-most bar, blue, without the borders (used for ad crawls/scrolling text)
#    Bar B  : secondary bar, orange, rendered above the bottom most. Part of the twilight_bg gradient illusion.
#    Bar_C  : bottom-most bar border. Blueish-White. Gives Bar A a top border.
#    Bar_D  : Top Bar background. Indigo or Dark Blue. Typically invisible due to image mask for Bar E.
#    Bar_E  : Series of gradient bars at top. Shades of Orange. Typically overlayed with slide title, logo, and time.
#    MASK_E : Top overlay mask. Indigo. Sits on top of Bar E to give slanted appearance.
#//
#// userHeight * 0.849 gives the exact height of the message crawl bar without borders when screensize is set to 768x480

#// https://youtu.be/xfnRywBv5VM?t=154
class slicegraphics():
    def __init__(self):
        self.screen = pygame.display.get_surface() # get/set the surface object that currently exists
        self.userWidth = self.screen.get_width() # get/set width
        self.userHeight = self.screen.get_height() # get/set height
        
    # used to draw the twilight_bg gradient when we need it
    def drawGradient(self):
        # Twilight Background (purple -> orange gradient)
        # Colors:
        #    Purple : (34, 67, 137)
        #    Orange : (221, 117, 15)
        twilight_bg = pygame.image.load("assets/graphics/twilight_bg.bmp")
        twilight_bg_size = (self.userWidth, 274)
        twilight_bg = pygame.transform.scale(twilight_bg, twilight_bg_size)

        #// 91 for Y height is perfect match to screenshotfor twilight_bg size
        self.screen.blit(twilight_bg, (0,91))

    # BAR GENERATION DEFINITIONS
    # --------------------------
    def drawBar_A(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(0, (self.userHeight * 0.845), self.userWidth,200))

    def drawBar_B(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(0, (self.userHeight * 0.76249), self.userWidth,37))
    
    # used to draw bar C
    def drawBar_C(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(0, (self.userHeight * 0.843), self.userWidth,2))

    # used to draw bar D
    def drawBar_D(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(0, (self.userHeight * 0.0), self.userWidth,91))