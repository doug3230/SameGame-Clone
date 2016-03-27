'''
Created on Mar 15, 2016

@author: Richard
'''
from pygame import Rect
from constants.colours import WHITE, YELLOW, GREEN, LIGHTER_GRAY
from game import INITIALIZATION_SCREEN_SIZE

CONTROL_PANEL_RECT = Rect((0, 430), (INITIALIZATION_SCREEN_SIZE[0], 100))
CONTROL_PANEL_COLOUR = WHITE

CONTROL_PANEL_NEW_GAME_BUTTON_TEXT = "New Game"
CONTROL_PANEL_NEW_GAME_BUTTON_RECT = Rect((10, 455), (100, 20))
CONTROL_PANEL_NEW_GAME_BUTTON_FONT_SIZE = 16
CONTROL_PANEL_NEW_GAME_BUTTON_BORDER = (10, 5, 5, 0)

CONTROL_PANEL_RESUME_GAME_BUTTON_TEXT = "Resume Game"
CONTROL_PANEL_RESUME_GAME_BUTTON_RECT = Rect((125, 455), (125, 20))
CONTROL_PANEL_RESUME_GAME_BUTTON_FONT_SIZE = 16
CONTROL_PANEL_RESUME_GAME_BUTTON_BORDER = (10, 5, 5, 0)

CONTROL_PANEL_INSTRUCTIONS_BUTTON_TEXT = "Instructions"
CONTROL_PANEL_INSTRUCTIONS_BUTTON_RECT = Rect((265, 455), (125, 20))
CONTROL_PANEL_INSTRUCTIONS_BUTTON_FONT_SIZE = 15
CONTROL_PANEL_INSTRUCTIONS_BUTTON_BORDER = (10, 0, 3, 7)

CONTROL_PANEL_UNDO_MOVE_BUTTON_TEXT = "Undo Move"
CONTROL_PANEL_UNDO_MOVE_BUTTON_RECT = Rect((65, 490), (110, 20))
CONTROL_PANEL_UNDO_MOVE_BUTTON_FONT_SIZE = 16
CONTROL_PANEL_UNDO_MOVE_BUTTON_BORDER = (10, 5, 5, 0)

CONTROL_PANEL_RESET_GAME_BUTTON_TEXT = "Reset Game"
CONTROL_PANEL_RESET_GAME_BUTTON_RECT = Rect((200, 490), (125, 20))
CONTROL_PANEL_RESET_GAME_BUTTON_FONT_SIZE = 16
CONTROL_PANEL_RESET_GAME_BUTTON_BORDER = (10, 5, 5, 0)

CONTROL_PANEL_BUTTON_DEFAULT_COLOUR = LIGHTER_GRAY
CONTROL_PANEL_BUTTON_HOVER_COLOUR = YELLOW
CONTROL_PANEL_BUTTON_CLICKED_COLOUR = GREEN
def CONTROL_PANEL_BUTTON(text_element=None, border=0):
    from elements import rectangle_button
    return rectangle_button(text_element=text_element,
                            border_size=border,
                            default_colour=CONTROL_PANEL_BUTTON_DEFAULT_COLOUR,
                            clicked_colour=CONTROL_PANEL_BUTTON_CLICKED_COLOUR,
                            hover_colour=CONTROL_PANEL_BUTTON_HOVER_COLOUR)