'''
Created on Feb 28, 2016

@author: Richard
'''
from pygame import Rect
from game import mouse_position
from elements import DecorateElement
from grid_position import GridPosition

class GridElement(DecorateElement):
    def __init__(self, grid_position=None, \
                 grid_camera=None, auto_resize=True,
                 auto_place=True, **kwargs):
        if not grid_position:
            grid_position = GridPosition()
        DecorateElement.__init__(self, **kwargs)
        self.grid_position = grid_position
        self.grid_camera = grid_camera
        self.auto_resize = auto_resize
        self.auto_place = auto_place
        return
    
    def draw(self, screen):
        if self.element is not None and \
        (self.grid_camera is None or \
         self.grid_camera.rect.contains(self.element.rect)):
            self.element.draw(screen)
        return
    
    def resize(self, width_scale=1, height_scale=1):
        self.element.rect.w = self.grid_camera.tile_width()*width_scale
        self.element.rect.h = self.grid_camera.tile_height()*height_scale
        return
    
    def place(self):
        top_left = self.grid_camera.top_left()
        relative_x = self.grid_position.x - top_left[0]
        relative_y = self.grid_position.y - top_left[1]
        self.element.rect.centerx = self.grid_camera.rect.x + \
        (relative_x + 0.5) * self.grid_camera.tile_width()
        self.element.rect.centery = self.grid_camera.rect.y + \
        (relative_y + 0.5) * self.grid_camera.tile_height()
        return
    
    def grid_rect(self):
        top_left = self.grid_camera.top_left()
        relative_x = self.grid_position.x - top_left[0]
        relative_y = self.grid_position.y - top_left[1]
        x = self.grid_camera.rect.x + (relative_x*self.grid_camera.tile_width())
        y = self.grid_camera.rect.y + (relative_y*self.grid_camera.tile_height())
        w = self.grid_camera.tile_width()
        h = self.grid_camera.tile_height()
        return Rect((x, y), (w, h))
    
    def is_mouse_over(self):
        return self.grid_rect().collidepoint(mouse_position())
    
    def update(self):
        if self.auto_resize:
            self.resize()
        if self.auto_place:
            self.place()
        DecorateElement.update(self)
        return
    
def init_grid_element_at(classname=GridElement, x=0, y=0, **kwargs):
    element = classname(**kwargs)
    element.grid_position.x = x
    element.grid_position.y = y
    return element