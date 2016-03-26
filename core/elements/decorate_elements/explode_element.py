'''
Created on Dec 10, 2015

@author: Richard
'''
from dead_element import DeadElement

class ExplodeElement(DeadElement):
    def __init__(self, element, explosion, explosion_ticks=1, dead_rects=[], **kwargs):
        self.explosion = explosion
        self.explosion.decorated_element().suspend()
        self.is_exploding = False
        self.current_tick = 0
        self.explosion_ticks = explosion_ticks
        DeadElement.__init__(self, element, dead_rects=dead_rects, **kwargs)
        return
    
    def kill(self):
        DeadElement.kill(self)
        self.explode()
        return
    
    def explode(self):
        element = self.element.decorated_element()
        explosion_element = self.explosion.decorated_element()
        explosion_element.restore()
        explosion_element.rect.centerx = element.rect.centerx
        explosion_element.rect.centery = element.rect.centery
        self.is_exploding = True
        self.current_tick = 0
        return
    
    def update(self):
        DeadElement.update(self)
        if self.is_exploding:
            if self.current_tick >= self.explosion_ticks:
                self.current_tick = 0
                self.is_exploding = False
                self.explosion.decorated_element().suspend()
            else:
                self.current_tick += 1
        return