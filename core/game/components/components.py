'''
Created on Oct 26, 2014

@author: Richard
'''
import pygame
from time import time
from components_settings import *

class System:
    CLOCK = None
    BACKGROUND = None
    STATE = None
    INITIALIZED = False

def screen():
    return pygame.display.get_surface()

def clock():
    return System.CLOCK

def background():
    return System.BACKGROUND

def state():
    return System.STATE

def refresh_screen():
    pygame.display.flip()
    return

def refresh_subscreen(dirty_rects):
    print(dirty_rects)
    pygame.display.update(dirty_rects)
    return

def tick(fps = COMPONENTS_FPS):
    System.CLOCK.tick(fps)
    return

def current_time_in_ms():
    return int(round(time()*1000))

def set_background(new_background):
    System.BACKGROUND = new_background
    return

def set_state(new_state, play_music = False):
    System.STATE = new_state
    if play_music:
        new_state.play_music()
    return

def screen_rect():
    return screen().get_rect()

def screen_width():
    from game import INITIALIZATION_SCREEN_SIZE
    return INITIALIZATION_SCREEN_SIZE[0]

def screen_height():
    from game import INITIALIZATION_SCREEN_SIZE
    return INITIALIZATION_SCREEN_SIZE[1]

def mouse_position():
    return pygame.mouse.get_pos()

def is_left_mouse_clicked():
    presses = pygame.mouse.get_pressed()
    return presses[0]
