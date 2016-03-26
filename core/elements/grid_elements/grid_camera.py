'''
Created on Feb 28, 2016

@author: Richard
'''
from grid_rect_position import GridRectPosition

class GridCamera(GridRectPosition):
    def __init__(self, rect=None, **kwargs):
        self.rect = rect
        GridRectPosition.__init__(self, **kwargs)
        return
    
    def tile_width(self):
        return self.rect.w // self.w
    
    def tile_height(self):
        return self.rect.h // self.h