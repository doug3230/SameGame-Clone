'''
Created on Dec 6, 2015

@author: Richard
'''
from game import screen_rect
from velocity_element import VelocityElement

class VelocityBounceElement(VelocityElement):
    def __init__(self, element, bound_rect=None, **kwargs):
        if not bound_rect:
            bound_rect = screen_rect()
        VelocityElement.__init__(self, element, **kwargs)
        self.bound_rect = bound_rect
        self.rect = self.decorated_element().rect
        return
    
    def update(self):
        self.rect = self.decorated_element().rect
        if self.rect.x <= self.bound_rect.x \
        or self.rect.x + self.rect.w >= self.bound_rect.x + self.bound_rect.w:
            self.vel_x = -self.vel_x
        if self.rect.y <= self.bound_rect.y \
        or self.rect.y + self.rect.h >= self.bound_rect.y + self.bound_rect.h:
            self.vel_y = -self.vel_y
        VelocityElement.update(self)
        return
    
    def bounce_x(self):
        self.vel_x = -self.vel_x
        return
    
    def bounce_y(self):
        self.vel_y = -self.vel_y
        return 
    
    def bounce(self):
        self.bounce_x()
        self.bounce_y()
        return
