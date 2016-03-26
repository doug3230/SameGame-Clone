'''
Created on Mar 1, 2016

@author: Richard
'''
from grid_rect_position import GridRectPosition

class GridBoundaryPosition(GridRectPosition):
    def occupied_tiles(self):
        return tuple((i, j)
                     for i in range(self.x, self.x + self.w)
                     for j in range(self.y, self.y + self.h)
                     if ((i == self.x or i == self.x + self.w - 1) or
                         (j == self.y or j == self.y + self.h - 1)))