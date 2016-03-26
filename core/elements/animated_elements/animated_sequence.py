'''
Created on Dec 13, 2015

@author: Richard
'''
from animated_element import AnimatedElement

class AnimatedSequence(AnimatedElement):
    def __init__(self, speed=1, max_index=1, **kwargs):
        AnimatedElement.__init__(self, **kwargs)
        self.current_index = 0
        self.max_index = max_index
        self.speed = speed
        self.element = None
        return

    def is_finished(self):
        return self.finished or (self.is_started() and \
            (self.current_index >= self.max_index or \
             not self.element_at_index(self.current_index)))
    
    def start(self):
        self.current_index = 0
        AnimatedElement.start(self)
        self.update_element()
        return
    
    def finish(self):
        self.current_index = self.max_index
        AnimatedElement.finish(self)
        self.update_element()
        return
    
    def reset(self):
        self.current_index = 0
        AnimatedElement.reset(self)
        self.update_element()
        return
    
    def element_at_index(self, index):
        return None
    
    def draw(self, screen):
        if self.element:
            self.element.draw(screen)
        return
    
    def update(self):
        if self.is_started() and not self.is_finished():
            if self.current_index < self.max_index and \
            self.element_at_index(self.current_index + self.speed):
                self.current_index += self.speed
                self.update_element()
        if self.element:
            self.element.rect = self.rect
            for rect in self.element.dirty_list:
                self.dirty_list.append(rect)
            self.element.dirty_list = []
        if self.is_finished() and not self.finished:
            self.refresh()
        AnimatedElement.update(self)
        return
    
    def get_element(self):
        return self.element
    
    def update_element(self):
        self.element = self.element_at_index(self.current_index)
        if self.element:
            self.element.update()
        return