'''
Created on Dec 19, 2015

@author: Richard
'''
from animated_sequence import AnimatedSequence

class AnimatedSeries(AnimatedSequence):
    def __init__(self, animated_elements=[], **kwargs):
        AnimatedSequence.__init__(self, **kwargs)
        self.animated_elements = animated_elements
        self.max_index = len(animated_elements)
        return
    
    def element_at_index(self, index):
        element = None
        if 0 <= index < self.max_index:
            element = self.animated_elements[index]
        return element