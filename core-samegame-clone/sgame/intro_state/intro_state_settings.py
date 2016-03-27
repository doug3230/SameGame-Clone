'''
Created on Mar 16, 2016

@author: Richard
'''
from pygame import Rect

INTRO_STATE_TITLE_TEXT = "SameGame Clone"
INTRO_STATE_TITLE_RECT = Rect((50, 20), (300, 60))
INTRO_STATE_TITLE_FONT_SIZE = 37

INTRO_STATE_INSTRUCTIONS_HEADING_TEXT = "Instructions"
INTRO_STATE_INSTRUCTIONS_HEADING_RECT = Rect((20, 80), (360, 20))
INTRO_STATE_INSTRUCTIONS_HEADING_FONT_SIZE = 18

INTRO_STATE_INSTRUCTIONS_TEXT = \
        ["This game is played using the mouse.",
        "",
        "Click adjacent bubbles with the same colour",
        "to destroy them.",
        "",
        "Destroy more bubbles at once to ",
        "score more points.",
        "",
        "The game is over when there are no more ",
        "bubbles that can be popped.",
        "",
        "Use the buttons in the control panel",
        "to administer your game."]
INTRO_STATE_INSTRUCTIONS_RECT = Rect((20, 100), (360, 280))
INTRO_STATE_INSTRUCTIONS_FONT_SIZE = 14

