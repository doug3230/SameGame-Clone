'''
Created on Mar 1, 2016

@author: Richard
'''
from grid_element import GridElement
from grid_boundary_position import GridBoundaryPosition

class GridBoundaryElement(GridElement):
    def __init__(self, **kwargs):
        if not kwargs.has_key("grid_position"):
            kwargs['grid_position'] = GridBoundaryPosition()
        elif not isinstance(kwargs['grid_position'], GridBoundaryPosition):
            raise Exception("grid_position must be an instance of GridBoundaryPosition")
        GridElement.__init__(self, **kwargs)
        self.update_boundary()
        return
    
    def update_boundary(self):
        position = self.grid_position
        camera = self.grid_camera
        position.x = camera.x - 1
        position.y = camera.y - 1
        position.w = camera.w + 2
        position.h = camera.h + 2
        return
    
    def update(self):
        self.update_boundary()
        GridElement.update(self)
        return