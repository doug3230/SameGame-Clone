'''
Created on Mar 16, 2016

@author: Richard
'''
from pygame import MOUSEBUTTONDOWN
from elements import StateSystem
from selements import ControlPanel
from intro_state import IntroState
from game_state import GameState

class MainState(StateSystem):
    def __init__(self):
        self.control_panel = ControlPanel()
        self.intro_state = IntroState()
        self.game_state = GameState()
        subelements = [self.control_panel]
        StateSystem.__init__(self, child_state=self.intro_state,
                             subelements=subelements)
        self.set_game_buttons_visible(visible=False)
        return
    
    def handle_event(self, event):
        StateSystem.handle_event(self, event)
        if event.type == MOUSEBUTTONDOWN:
            if self.control_panel.intro_button.is_mouse_clicking():
                self.child_state = self.intro_state
                self.set_game_buttons_visible(visible=False)
            elif self.control_panel.new_game_button.is_mouse_clicking():
                self.child_state = self.game_state
                self.game_state.new_game()
                self.set_game_buttons_visible(visible=True)
            elif self.control_panel.resume_game_button.is_mouse_clicking():
                self.child_state = self.game_state
                self.set_game_buttons_visible(visible=True)
            elif self.control_panel.reset_button.is_mouse_clicking():
                self.game_state.reset_game()
                self.child_state = self.game_state
                self.set_game_buttons_visible(visible=True)
            elif self.control_panel.undo_button.is_mouse_clicking():
                self.game_state.undo_move()
                self.child_state = self.game_state
                self.set_game_buttons_visible(visible=True)
        return
    
    def set_game_buttons_visible(self, visible=True):
        self.control_panel.undo_button.visible = visible
        self.control_panel.reset_button.visible = visible
        return