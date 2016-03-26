'''
Created on May 27, 2015

@author: Richard
'''
from state import State

class StateSystem(State):
    def __init__(self, child_state=None, **kwargs):
        State.__init__(self, **kwargs)
        self.child_state = child_state
        self.old_child_state = None
        return
    
    def draw(self, screen):
        State.draw(self, screen)
        if self.child_state:
            self.child_state.draw(screen)
        return
    
    def update(self):
        State.update(self)
        if self.child_state:
            self.child_state.update()
            self.dirty_list += self.child_state.dirty_list
            self.child_state.dirty_list = []
            if not self.refresh_screen:
                self.refresh_screen = self.child_state.refresh_screen
            self.child_state.refresh_screen = False
            if self.old_child_state is None or self.old_child_state != self.child_state:
                self.refresh_screen = True
                self.old_child_state = self.child_state
        return
    
    def handle_event(self, event):
        State.handle_event(self, event)
        if self.child_state:
            self.child_state.handle_event(event)
        return
    
    def play_music(self):
        State.play_music(self)
        if self.child_state:
            self.child_state.play_music()
        return
    
    def refresh(self):
        State.refresh(self)
        if self.child_state:
            self.child_state.refresh()
        return