'''
Created on Mar 6, 2016

@author: Richard
'''
from grid_collision_detector import GridCollisionDetector

class GridRectCollisionDetector(GridCollisionDetector):
    def __init__(self, grid_rect=None, **kwargs):
        GridCollisionDetector.__init__(self, **kwargs)
        self.grid_rect = grid_rect
        return
    
    def occupants_with_x(self, x, min_y=None, max_y=None):
        grid_rect = self.grid_rect
        if min_y is None:
            min_y = grid_rect.y
        if max_y is None:
            max_y = grid_rect.y + grid_rect.h - 1
        return self.occupants_in_rect(x, min_y, 1, max_y - min_y + 1)
    
    def occupants_with_y(self, y, min_x=None, max_x=None):
        grid_rect = self.grid_rect
        if min_x is None:
            min_x = grid_rect.x
        if max_x is None:
            max_x = grid_rect.x + grid_rect.w - 1
        return self.occupants_in_rect(grid_rect.x, y, max_x - min_x + 1, 1)
    
    def occupants_before_x(self, x):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, grid_rect.y, x - grid_rect.x, grid_rect.h)
    
    def occupants_after_x(self, x):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(x + 1, grid_rect.y,
                                      grid_rect.w - (x + 1), grid_rect.h)
        
    def occupants_before_y(self, y):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, grid_rect.y, grid_rect.w, y - grid_rect.y)
    
    def occupants_after_y(self, y):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, y + 1,
                                      grid_rect.w, grid_rect.h - (y + 1))
        
    def is_row_all_occupied(self, y):
        occupied = True
        grid_rect = self.grid_rect
        for x in range(grid_rect.x, grid_rect.x + grid_rect.w):
            if not self.is_tile_occupied(x, y):
                occupied = False
                break
        return occupied
    
    def is_col_all_occupied(self, x):
        occupied = True
        grid_rect = self.grid_rect
        for y in range(grid_rect.y, grid_rect.y + grid_rect.h):
            if not self.is_tile_occupied(x, y):
                occupied = False
                break
        return occupied
    
    def is_row_empty(self, y):
        empty = True
        grid_rect = self.grid_rect
        for x in range(grid_rect.x, grid_rect.x + grid_rect.w):
            if self.is_tile_occupied(x, y):
                empty = False
                break
        return empty
    
    def is_col_empty(self, x):
        empty = True
        grid_rect = self.grid_rect
        for y in range(grid_rect.y, grid_rect.y + grid_rect.h):
            if self.is_tile_occupied(x, y):
                empty = False
                break
        return empty