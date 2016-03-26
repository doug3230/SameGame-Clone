'''
Created on May 27, 2015

@author: Richard
'''
from state import State
from elements import ElementCollection

class SubState(State):
    def __init__(self, parent=None, **kwargs):
        State.__init__(self, **kwargs)
        self.parent = parent
        return
    
    def draw(self, screen):
        ElementCollection.draw(self, screen)
        return