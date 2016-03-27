'''
Created on Mar 15, 2016

@author: Richard
'''
from elements import ElementCollection, Rectangle, rectangle_button, Text
from control_panel_settings import *

class ControlPanel(ElementCollection):
    def __init__(self):
        self.background_rect = Rectangle(rect=CONTROL_PANEL_RECT,
                                         colour=CONTROL_PANEL_COLOUR)
        self.new_game_button = CONTROL_PANEL_BUTTON(
                                       text_element=Text(text=CONTROL_PANEL_NEW_GAME_BUTTON_TEXT,
                                                         rect=CONTROL_PANEL_NEW_GAME_BUTTON_RECT,
                                                         font_size=CONTROL_PANEL_NEW_GAME_BUTTON_FONT_SIZE),
                                       border=CONTROL_PANEL_NEW_GAME_BUTTON_BORDER)
        self.resume_game_button = CONTROL_PANEL_BUTTON(
                                       text_element=Text(text=CONTROL_PANEL_RESUME_GAME_BUTTON_TEXT,
                                                         rect=CONTROL_PANEL_RESUME_GAME_BUTTON_RECT,
                                                         font_size=CONTROL_PANEL_RESUME_GAME_BUTTON_FONT_SIZE),
                                       border=CONTROL_PANEL_RESUME_GAME_BUTTON_BORDER)
        self.intro_button = CONTROL_PANEL_BUTTON(
                                       text_element=Text(text=CONTROL_PANEL_INSTRUCTIONS_BUTTON_TEXT,
                                                         rect=CONTROL_PANEL_INSTRUCTIONS_BUTTON_RECT,
                                                         font_size=CONTROL_PANEL_INSTRUCTIONS_BUTTON_FONT_SIZE),
                                       border=CONTROL_PANEL_INSTRUCTIONS_BUTTON_BORDER)
        self.undo_button = CONTROL_PANEL_BUTTON(
                                       text_element=Text(text=CONTROL_PANEL_UNDO_MOVE_BUTTON_TEXT,
                                                         rect=CONTROL_PANEL_UNDO_MOVE_BUTTON_RECT,
                                                         font_size=CONTROL_PANEL_UNDO_MOVE_BUTTON_FONT_SIZE),
                                       border=CONTROL_PANEL_UNDO_MOVE_BUTTON_BORDER)
        self.reset_button = CONTROL_PANEL_BUTTON(
                                       text_element=Text(text=CONTROL_PANEL_RESET_GAME_BUTTON_TEXT,
                                                         rect=CONTROL_PANEL_RESET_GAME_BUTTON_RECT,
                                                         font_size=CONTROL_PANEL_RESET_GAME_BUTTON_FONT_SIZE),
                                       border=CONTROL_PANEL_RESET_GAME_BUTTON_BORDER)
        subelements = [self.background_rect, self.intro_button,
                       self.new_game_button, self.resume_game_button,
                       self.undo_button, self.reset_button]
        ElementCollection.__init__(self, rect=CONTROL_PANEL_RECT,
                                   subelements=subelements)
        return