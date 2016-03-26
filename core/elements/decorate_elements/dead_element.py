'''
Created on Dec 5, 2015

@author: Richard
'''
from elements import ElementCollection
from decorate_element import DecorateElement

class DeadElement(ElementCollection, DecorateElement):
    def __init__(self, element, dead_rects=[], **kwargs):
        self.element=element
        self.dead_rects=dead_rects
        ElementCollection.__init__(self, subelements=[self.element], **kwargs)
        self.rect=self.decorated_element().rect
        self.is_dead = False
        return
    
    def decorated_element(self):
        return DecorateElement.decorated_element(self)
    
    def kill(self):
        self.is_dead = True
        self.decorated_element().suspend()
        return
    
    def update(self):
        self.rect = self.decorated_element().rect
        if self.decorated_element().active:
            self.is_dead = False
            for rect in self.dead_rects:
                if self.rect.colliderect(rect):
                    self.is_dead = True
                    self.kill()
                    break
        ElementCollection.update(self)
        return
    
def screen_is_dead(element, **kwargs):
    from game import screen_rect
    return DeadElement(element, dead_rects=[screen_rect()], **kwargs)