'''
Created on Dec 14, 2015

@author: Richard
'''
from elements import ElementCollection

class NarrationBox(ElementCollection):
    def __init__(self, rectangle=None, animated_lines=None, **kwargs):
        self.rectangle = rectangle
        self.animated_lines = animated_lines
        subelements = [self.rectangle, self.animated_lines]
        ElementCollection.__init__(self, subelements=subelements, **kwargs)
        return
    
    def update(self):
        self.rectangle.layer = self.layer
        self.animated_lines.layer = self.layer + 1
        ElementCollection.update(self)
        return