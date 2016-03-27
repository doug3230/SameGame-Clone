'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame
from initialization_settings import *

def initialize_pygame():
    from os import environ
    if INITIALIZATION_CENTERED:
        environ['SDL_VIDEO_CENTERED'] = '1'
    else:
        screen_position = INITIALIZATION_SCREEN_POSITION
        environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % screen_position
    pygame.init()
    pygame.mixer.init()
    return

def initialize_caption():
    from game import COMPONENTS_CAPTION
    caption = COMPONENTS_CAPTION
    if caption:
        pygame.display.set_caption(caption)
    return

def initialize_icon():
    from game import COMPONENTS_ICON, COMPONENTS_EMPTY_ICON, load_image
    icon = COMPONENTS_ICON
    if icon:
        icon_image = load_image(icon)
    else:
        icon_image = COMPONENTS_EMPTY_ICON
    pygame.display.set_icon(icon_image)
    return

def initialize_background():
    from game import INITIALIZATION_BACKGROUND, System
    System.BACKGROUND = INITIALIZATION_BACKGROUND
    return

def initialize_clock():
    from game import System
    clock = pygame.time.Clock()
    System.CLOCK = clock
    return

def initialize_screen():
    from pygame.locals import DOUBLEBUF, RESIZABLE
    from game import COMPONENTS_DOUBLE_BUFFERED, COMPONENTS_RESIZABLE, INITIALIZATION_SCREEN_SIZE
    flags = 0
    if COMPONENTS_DOUBLE_BUFFERED:
        flags |= DOUBLEBUF
    if COMPONENTS_RESIZABLE:
        flags |= RESIZABLE
    screen_size = INITIALIZATION_SCREEN_SIZE
    pygame.display.set_mode(screen_size, flags)
    return

def initialize():
    initialize_pygame()
    initialize_caption()
    initialize_clock()
    initialize_background()
    initialize_icon()
    initialize_screen()
    return
