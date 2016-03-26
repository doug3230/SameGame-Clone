'''
Created on Mar 16, 2016

@author: Richard
'''
from elements import SubState, Text, TextLines
from scustomization import \
INSTRUCTIONS_TITLE_RECT, INSTRUCTIONS_TITLE_FONT_SIZE, \
INSTRUCTIONS_HEADING_RECT, INSTRUCTIONS_HEADING_FONT_SIZE, \
INSTRUCTIONS_RECT, INSTRUCTIONS_FONT_SIZE

class IntroState(SubState):
    def __init__(self):
        self.title_text = Text(text="SameGame Clone", bold=True,
                               rect=INSTRUCTIONS_TITLE_RECT,
                               font_size=INSTRUCTIONS_TITLE_FONT_SIZE)
        self.instruction_heading = Text(text="Instructions",
                               rect=INSTRUCTIONS_HEADING_RECT,
                               font_size=INSTRUCTIONS_HEADING_FONT_SIZE)
        instruction_text = ["This game is played using the mouse.",
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
        self.instruction_lines = TextLines(text=instruction_text,
                                           rect=INSTRUCTIONS_RECT,
                                           font_size=INSTRUCTIONS_FONT_SIZE)
        subelements = [self.title_text, self.instruction_heading, self.instruction_lines]
        SubState.__init__(self, subelements=subelements)
        return