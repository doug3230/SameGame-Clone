'''
Created on Nov 30, 2014

@author: Richard
'''
from polygon import Polygon
from game import screen_rect

class Rectangle(Polygon):
    def __init__(self, **kwargs):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        Polygon.__init__(self, points=points, **kwargs)
        return
    
def fullscreen_rect(colour):
    return Rectangle(rect=screen_rect(), colour=colour, layer=-1)