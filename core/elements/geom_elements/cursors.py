'''
Created on Nov 30, 2014

@author: Richard
'''
from polygon import Polygon

class RightCursor(Polygon):
    def __init__(self, **kwargs):
        points = [(0, 0), (0, 1), (1, 0.5)]
        Polygon.__init__(self, points=points, **kwargs)
        return
    
class LeftCursor(Polygon):
    def __init__(self, **kwargs):
        points = [(0, 0.5), (1, 0), (1, 1)]
        Polygon.__init__(self, points=points, **kwargs)
        return
    
class UpCursor(Polygon):
    def __init__(self, **kwargs):
        points = [(0, 1), (1, 1), (0.5, 0)]
        Polygon.__init__(self, points=points, **kwargs)
        return
    
class DownCursor(Polygon):
    def __init__(self, **kwargs):
        points = [(0, 0), (1, 0), (0.5, 1)]
        Polygon.__init__(self, points=points, **kwargs)
        return