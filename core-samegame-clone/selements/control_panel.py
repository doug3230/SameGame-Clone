'''
Created on Mar 15, 2016

@author: Richard
'''
from constants import YELLOW, GREEN
from elements import ElementCollection, Rectangle, rectangle_button, Text
from scustomization import CONTROL_PANEL_RECT, CONTROL_PANEL_COLOUR, \
NEW_GAME_BUTTON_RECT, RESUME_GAME_BUTTON_RECT, INTRO_BUTTON_RECT, \
UNDO_BUTTON_RECT, RESET_BUTTON_RECT

class ControlPanel(ElementCollection):
    def __init__(self):
        self.background_rect = Rectangle(rect=CONTROL_PANEL_RECT,
                                         colour=CONTROL_PANEL_COLOUR)
        self.new_game_button = rectangle_button(text_element=Text(text="New Game",
                                                         rect=NEW_GAME_BUTTON_RECT,
                                                         font_size=16),
                                       border_size=(10, 5, 5, 0),
                                       clicked_colour=GREEN,
                                       hover_colour=YELLOW)
        self.resume_game_button = rectangle_button(text_element=Text(text="Resume Game",
                                                         rect=RESUME_GAME_BUTTON_RECT,
                                                         font_size=16),
                                       border_size=(10, 5, 5, 0),
                                       clicked_colour=GREEN,
                                       hover_colour=YELLOW)
        self.intro_button = rectangle_button(text_element=Text(text="Instructions",
                                                         rect=INTRO_BUTTON_RECT,
                                                         font_size=15),
                                       border_size=(10, 0, 3, 7),
                                       clicked_colour=GREEN,
                                       hover_colour=YELLOW)
        self.undo_button = rectangle_button(text_element=Text(text="Undo Move",
                                                         rect=UNDO_BUTTON_RECT,
                                                         font_size=16),
                                       border_size=(10, 5, 5, 0),
                                       clicked_colour=GREEN,
                                       hover_colour=YELLOW)
        self.reset_button = rectangle_button(text_element=Text(text="Reset Game",
                                                         rect=RESET_BUTTON_RECT,
                                                         font_size=16),
                                       border_size=(10, 5, 5, 0),
                                       clicked_colour=GREEN,
                                       hover_colour=YELLOW)
        subelements = [self.background_rect, self.intro_button,
                       self.new_game_button, self.resume_game_button,
                       self.undo_button, self.reset_button]
        ElementCollection.__init__(self, rect=CONTROL_PANEL_RECT,
                                   subelements=subelements)
        return