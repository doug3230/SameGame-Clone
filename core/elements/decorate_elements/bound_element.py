'''
Created on Dec 5, 2015

@author: Richard
'''
from elements import ElementCollection
from decorate_element import DecorateElement

class BoundElement(ElementCollection, DecorateElement):
    def __init__(self, element, bound_rect, **kwargs):
        self.element=element
        self.bound_rect=bound_rect
        ElementCollection.__init__(self, subelements=[self.element], **kwargs)
        self.rect=self.decorated_element().rect
        return
    
    def decorated_element(self):
        return DecorateElement.decorated_element(self)
    
    def update(self):
        ElementCollection.update(self)
        self.rect = self.decorated_element().rect
        self.rect.x = min(max(self.bound_rect.x, self.rect.x), 
                          self.bound_rect.x + self.bound_rect.w - self.rect.w)
        self.rect.y = min(max(self.bound_rect.y, self.rect.y),
                          self.bound_rect.y + self.bound_rect.h - self.rect.h)
        return
    
def screen_bound(element, **kwargs):
    from game import screen_rect
    return BoundElement(element, screen_rect(), **kwargs)