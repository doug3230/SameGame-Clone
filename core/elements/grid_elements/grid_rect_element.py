'''
Created on Feb 28, 2016

@author: Richard
'''
from grid_rect_position import GridRectPosition
from grid_element import GridElement

class GridRectElement(GridElement):
    def __init__(self, **kwargs):
        if not isinstance(kwargs['grid_position'], GridRectPosition):
            raise Exception("grid_position must be an instance of GridRectPosition")
        GridElement.__init__(self, **kwargs)
        return
    
    def update(self):
        top_left = self.grid_camera.top_left()
        relative_x = self.grid_position.x - top_left[0]
        relative_y = self.grid_position.y - top_left[1]
        self.element.rect.x = self.grid_camera.rect.x + \
        relative_x*self.grid_camera.tile_width()
        self.element.rect.y = self.grid_camera.rect.y + \
        relative_y*self.grid_camera.tile_height()
        self.element.rect.w = self.grid_position.w*self.grid_camera.tile_width()
        self.element.rect.h = self.grid_position.h*self.grid_camera.tile_height()
        GridElement.update(self)
        return