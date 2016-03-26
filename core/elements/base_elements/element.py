'''
Created on Nov 29, 2014

@author: Richard
'''
from pygame import Rect
from game import mouse_position, is_left_mouse_clicked

class Element:
    def __init__(self, rect = None, layer=0, visible=True, active=True):
        if rect is not None:
            self.rect = rect
        else:
            self.rect = Rect((0, 0), (0, 0))
        self.old_active = None
        self.old_visible = None
        self.old_rect = None
        self.layer = layer
        self.visible = visible
        self.active = active
        self.dirty_list = []
        return
    
    def draw(self, screen):
        return
    
    def update(self):
        def rects_are_synchronized():
            r = self.rect
            o = self.old_rect
            return (r.x, r.y, r.size) == (o.x, o.y, o.size)
        if self.old_rect is None:
            self.dirty_list.append(self.rect.inflate(5, 5))
            self.old_rect = Rect((self.rect.x, self.rect.y), (self.rect.w, self.rect.h))
        elif not rects_are_synchronized():
            self.refresh()
            self.old_rect = Rect((self.rect.x, self.rect.y), (self.rect.w, self.rect.h))
        self.update_active_and_visible()
        self.remove_duplicate_dirty_rects()
        return
    
    def remove_duplicate_dirty_rects(self):
        unique_list = []
        for dirty_rect in self.dirty_list:
            if not dirty_rect in unique_list:
                unique_list.append(dirty_rect)
        self.dirty_list = unique_list
        return
    
    def update_active_and_visible(self):
        if self.old_visible is None or self.old_visible != self.visible \
        or self.old_active is None or self.old_active != self.active:
            self.refresh()
        self.old_active = self.active
        self.old_visible = self.visible
        return
    
    def refresh(self):
        if self.old_rect is not None:
            self.dirty_list.append(self.old_rect.inflate(5, 5))
        self.dirty_list.append(self.rect.inflate(5, 5))
        return
    
    def suspend(self):
        self.active = False
        self.visible = False
        return
    
    def restore(self):
        self.active = True
        self.visible = True
        return
    
    def decorated_element(self):
        return self
    
    def is_mouse_over(self):
        return self.visible and self.rect.collidepoint(mouse_position())
    
    def is_mouse_clicking(self):
        return self.visible and is_left_mouse_clicked() and self.is_mouse_over()