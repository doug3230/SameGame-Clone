'''
Created on Dec 12, 2015

@author: Richard
'''
from elements import Element

class AnimatedElement(Element):
    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)
        self.started = False
        self.finished = False
        return
    
    def start(self):
        self.started = True
        self.finished = False
        self.refresh()
        return
    
    def is_started(self):
        return self.started
    
    def finish(self):
        self.finished = True
        self.refresh()
        return
    
    def is_finished(self):
        return self.finished
    
    def reset(self):
        self.started = False
        self.finished = False
        self.refresh()
        return
    
    def update(self):
        Element.update(self)
        self.started = self.is_started()
        self.finished = self.is_finished()
        return