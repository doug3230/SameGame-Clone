'''
Created on May 31, 2015

@author: Richard
'''
from copy import deepcopy
from elements import ElementCollection
from decorate_element import DecorateElement

class MarginElement(ElementCollection, DecorateElement):
    def __init__(self, element, margin=0, **kwargs):
        self.margin=margin
        self.element=element
        if not 'rect' in kwargs.keys():
            kwargs['rect'] = deepcopy(element.rect)
        if not 'layer' in kwargs.keys():
            kwargs['layer'] = element.layer
        ElementCollection.__init__(self, subelements=[self.element], **kwargs)
        return
    
    def decorated_element(self):
        return DecorateElement.decorated_element(self)
    
    def margin_left(self):
        if isinstance(self.margin, (list, tuple)):
            if len(self.margin) == 2:
                margin_left = self.margin[0]
            else:
                margin_left = self.margin[0]
        else:
            margin_left = self.margin
        return margin_left
    
    def margin_right(self):
        if isinstance(self.margin, (list, tuple)):
            if len(self.margin) == 2:
                margin_right = self.margin[0]
            else:
                margin_right = self.margin[1]
        else:
            margin_right = self.margin
        return margin_right
    
    def margin_top(self):
        if isinstance(self.margin, (list, tuple)):
            if len(self.margin) == 2:
                margin_top = self.margin[1]
            else:
                margin_top = self.margin[2]
        else:
            margin_top = self.margin
        return margin_top
    
    def margin_bottom(self):
        if isinstance(self.margin, (list, tuple)):
            if len(self.margin) == 2:
                margin_bottom = self.margin[1]
            else:
                margin_bottom = self.margin[3]
        else:
            margin_bottom = self.margin
        return margin_bottom
    
    def update(self):
        self.element.rect.x = self.rect.x + self.margin_left()
        self.element.rect.y = self.rect.y + self.margin_top()
        self.element.rect.width = self.rect.width - (self.margin_left() + self.margin_right())
        self.element.rect.height = self.rect.height - (self.margin_top() + self.margin_bottom())
        ElementCollection.update(self)
        return
    
def margin(element, margin_size, **kwargs):
    return MarginElement(element, margin=margin_size, **kwargs)
