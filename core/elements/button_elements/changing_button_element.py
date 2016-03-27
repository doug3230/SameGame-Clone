'''
Created on Mar 16, 2016

@author: Richard
'''
from constants.colours import LIGHTER_GRAY
from elements import DecorateElement, border
from button_element import ButtonElement

class ChangingButtonElement(ButtonElement, DecorateElement):
    def __init__(self, default_element=None, clicked_element=None, hover_element=None, **kwargs):
        DecorateElement.__init__(self, element=default_element)
        ButtonElement.__init__(self, **kwargs)
        if clicked_element is None:
            clicked_element = default_element
        if hover_element is None:
            hover_element = default_element
        self.default_element = default_element
        self.clicked_element = clicked_element
        self.hover_element = hover_element
        
        return
    
    def draw(self, screen):
        DecorateElement.draw(self, screen)
        return
    
    def refresh(self):
        DecorateElement.refresh(self)
        return
    
    def update(self):
        ButtonElement.update(self)
        if self.is_clicked:
            self.element = self.clicked_element
        elif self.is_mouse_over():
            self.element = self.hover_element
        else:
            self.element = self.default_element
        DecorateElement.update(self)
        return
    
def rectangle_button(text_element=None, border_size=0,
                     default_colour=LIGHTER_GRAY, clicked_colour=None, hover_colour=None):
    if not clicked_colour:
        clicked_colour = default_colour
    if not hover_colour:
        hover_colour = default_colour
    default_element = border(text_element, border_size, default_colour)
    clicked_element = border(text_element, border_size, clicked_colour)
    hover_element = border(text_element, border_size, hover_colour)
    return ChangingButtonElement(default_element=default_element,
                                 clicked_element=clicked_element,
                                 hover_element=hover_element)