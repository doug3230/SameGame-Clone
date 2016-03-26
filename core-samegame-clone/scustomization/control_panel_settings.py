'''
Created on Mar 15, 2016

@author: Richard
'''
from pygame import Rect
from constants import WHITE
from customization import INIT_SCREEN_SIZE
CONTROL_PANEL_RECT = Rect((0, 430), (INIT_SCREEN_SIZE[0], 100))
CONTROL_PANEL_COLOUR = WHITE
NEW_GAME_BUTTON_RECT = Rect((10, 455), (100, 20))
RESUME_GAME_BUTTON_RECT = Rect((125, 455), (125, 20))
INTRO_BUTTON_RECT = Rect((265, 455), (125, 20))
UNDO_BUTTON_RECT = Rect((65, 490), (110, 20))
RESET_BUTTON_RECT = Rect((200, 490), (125, 20))