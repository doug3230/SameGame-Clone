'''
Created on Mar 16, 2016

@author: Richard
'''
from elements import SubState, Text, TextLines
from intro_state_settings import *

class IntroState(SubState):
    def __init__(self):
        self.title_text = Text(text=INTRO_STATE_TITLE_TEXT, bold=True,
                               rect=INTRO_STATE_TITLE_RECT,
                               font_size=INTRO_STATE_TITLE_FONT_SIZE)
        self.instruction_heading = Text(text=INTRO_STATE_INSTRUCTIONS_HEADING_TEXT,
                               rect=INTRO_STATE_INSTRUCTIONS_HEADING_RECT,
                               font_size=INTRO_STATE_INSTRUCTIONS_HEADING_FONT_SIZE)
        self.instruction_lines = TextLines(text=INTRO_STATE_INSTRUCTIONS_TEXT,
                                           rect=INTRO_STATE_INSTRUCTIONS_RECT,
                                           font_size=INTRO_STATE_INSTRUCTIONS_FONT_SIZE)
        subelements = [self.title_text, self.instruction_heading, self.instruction_lines]
        SubState.__init__(self, subelements=subelements)
        return