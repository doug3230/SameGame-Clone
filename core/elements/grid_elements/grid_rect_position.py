'''
Created on Feb 28, 2016

@author: Richard
'''
from grid_position import GridPosition

class GridRectPosition(GridPosition):
    def __init__(self, w=1, h=1, **kwargs):
        self.w = w
        self.h = h
        GridPosition.__init__(self, **kwargs)
        return
    
    def occupied_tiles(self):
        return tuple((i, j) for i in range(self.x, self.x + self.w) \
                for j in range(self.y, self.y + self.h))
    
    def min_x(self):
        return self.x
    
    def max_x(self):
        return self.x + self.w - 1
    
    def min_y(self):
        return self.y
    
    def max_y(self):
        return self.y + self.h - 1
    
    def top_left(self):
        return (self.x, self.y)
    
    def top_middle(self):
        return (self.x + (self.w - 1) // 2, self.y)