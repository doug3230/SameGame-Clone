'''
Created on Dec 6, 2015

@author: Richard
'''
from elements import ElementCollection
from decorate_element import DecorateElement

class VelocityElement(ElementCollection, DecorateElement):
    def __init__(self, element, vel_x=0, vel_y=0, **kwargs):
        self.element=element
        self.vel_x = vel_x
        self.vel_y = vel_y
        ElementCollection.__init__(self, subelements=[self.element], **kwargs)
        return
    
    def decorated_element(self):
        return DecorateElement.decorated_element(self)
    
    def update(self):
        if self.decorated_element().active:
            displacement_rect = self.decorated_element().rect
            displacement_rect.x += self.vel_x
            displacement_rect.y += self.vel_y
        ElementCollection.update(self)
        return