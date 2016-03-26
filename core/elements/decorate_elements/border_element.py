'''
Created on May 31, 2015

@author: Richard
'''
from copy import deepcopy
from constants import BLACK
from elements import ElementCollection
from decorate_element import DecorateElement

class BorderElement(ElementCollection, DecorateElement):
    def __init__(self, element, border=0, border_colour=BLACK, **kwargs):
        from elements import Rectangle
        self.border=border
        self.element=element
        if not 'rect' in kwargs.keys():
            kwargs['rect'] = deepcopy(element.rect)
        if not 'layer' in kwargs.keys():
            kwargs['layer'] = element.layer
        self.border_rectangle = Rectangle(colour=border_colour, **kwargs)
        ElementCollection.__init__(self, subelements=[self.border_rectangle, self.element], **kwargs)
        return
    
    def decorated_element(self):
        return DecorateElement.decorated_element(self)
    
    def border_left(self):
        if isinstance(self.border, (list, tuple)):
            if len(self.border) == 2:
                border_left = self.border[0]
            else:
                border_left = self.border[0]
        else:
            border_left = self.border
        return border_left
    
    def border_right(self):
        if isinstance(self.border, (list, tuple)):
            if len(self.border) == 2:
                border_right = self.border[0]
            else:
                border_right = self.border[1]
        else:
            border_right = self.border
        return border_right
    
    def border_top(self):
        if isinstance(self.border, (list, tuple)):
            if len(self.border) == 2:
                border_top = self.border[1]
            else:
                border_top = self.border[2]
        else:
            border_top = self.border
        return border_top
    
    def border_bottom(self):
        if isinstance(self.border, (list, tuple)):
            if len(self.border) == 2:
                border_bottom = self.border[1]
            else:
                border_bottom = self.border[3]
        else:
            border_bottom = self.border
        return border_bottom
    
    def update(self):
        self.border_rectangle.x = self.rect.x
        self.border_rectangle.y = self.rect.y
        self.border_rectangle.width = self.rect.width
        self.border_rectangle.height = self.rect.height
        self.border_rectangle.layer = self.layer
        self.element.layer = self.border_rectangle.layer + 1
        self.element.rect.x = self.rect.x + self.border_left()
        self.element.rect.y = self.rect.y + self.border_top()
        self.element.rect.width = self.rect.width - (self.border_left() + self.border_right())
        self.element.rect.height = self.rect.height - (self.border_top() + self.border_bottom())
        ElementCollection.update(self)
        return
    
def border(element, border_size, border_colour=BLACK, **kwargs):
    return BorderElement(element, border=border_size, border_colour=border_colour, **kwargs)
