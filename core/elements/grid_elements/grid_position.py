'''
Created on Feb 28, 2016

@author: Richard
'''
class GridPosition:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        return
    
    def occupied_tiles(self):
        return ((self.x, self.y),)
    
    def occupied_tiles_relative(self, rel_x=0, rel_y=0):
        return ((tile[0] + rel_x, tile[1] + rel_y) for tile in self.occupied_tiles())
    
    def max_x(self):
        return max(tile[0] for tile in self.occupied_tiles())
    
    def min_x(self):
        return min(tile[0] for tile in self.occupied_tiles())
    
    def max_y(self):
        return max((tile[1] for tile in self.occupied_tiles()))
    
    def min_y(self):
        return min((tile[1] for tile in self.occupied_tiles()))
    
    def get_width(self):
        return self.max_x() - self.min_x() + 1
    
    def get_height(self):
        return self.max_y() - self.min_y() + 1