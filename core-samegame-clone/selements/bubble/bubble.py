'''
Created on Mar 19, 2016

@author: Richard
'''
from constants.colours import BLACK
from elements import GridElement, Ellipse, margin
from bubble_settings import *

class Bubble(GridElement):
    def __init__(self, grid_camera=None, colour=BLACK):
        GridElement.__init__(self, element=margin(Ellipse(colour=colour), BUBBLE_MARGIN),
                             grid_camera=grid_camera, auto_place=True, auto_resize=False,)
        self.colour = colour
        return
    
    def update(self):
        self.decorated_element().colour = self.colour
        GridElement.update(self)
        return