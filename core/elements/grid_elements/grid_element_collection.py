'''
Created on Mar 19, 2016

@author: Richard
'''
from grid_element import GridElement
from elements import ElementCollection

class GridElementCollection(ElementCollection, GridElement):
    def __init__(self, subelements=[], **kwargs):
        GridElement.__init__(self, **kwargs)
        ElementCollection.__init__(self, subelements=subelements)
        return
    
    def resize(self, width_scale=1, height_scale=1):
        for ge in self.subelements:
            ge.resize(width_scale=width_scale, height_scale=height_scale)
        return
    
    def place(self):
        for ge in self.subelements:
            ge.place()
        return
    
    def draw(self, screen):
        ElementCollection.draw(self, screen)
        return
    
    def update(self):
        GridElement.update(self)
        ElementCollection.update(self)
        return
    
    def is_mouse_over(self):
        mouse_over = False
        for ge in self.subelements:
            if ge.is_mouse_over():
                mouse_over = True
                break
        return mouse_over