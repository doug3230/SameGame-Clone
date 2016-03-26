'''
Created on Dec 19, 2015

@author: Richard
'''
from elements import AnimatedSequence
from image_element import ImageElement

class AnimatedImage(AnimatedSequence):
    def __init__(self, speed=1, image_names=[], **kwargs):
        AnimatedSequence.__init__(self, speed=speed)
        self.element = ImageElement(**kwargs)
        self.image_names = image_names
        self.max_index = len(image_names)
        self.rect = self.element.rect
        return
    
    def element_at_index(self, index):
        if 0 <= index < self.max_index and self.element:
            self.element.image_name = self.image_names[int(index)]
        return self.element
    
    def update(self):
        self.max_index = len(self.image_names)
        AnimatedSequence.update(self)
        return