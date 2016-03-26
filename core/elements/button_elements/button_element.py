'''
Created on Mar 16, 2016

@author: Richard
'''
from elements import Element
from game import mouse_position, current_time_in_ms

DEFAULT_BUTTON_CLICK_DURATION = 0.25

class ButtonElement(Element):
    def __init__(self, click_rect=None, is_clicked=False,
                 click_duration=DEFAULT_BUTTON_CLICK_DURATION,
                 **kwargs):
        Element.__init__(self, **kwargs)
        self.click_rect = click_rect
        self.is_clicked = is_clicked
        self.old_is_clicked = None
        if not self.click_rect:
            self.click_rect = self.rect
        self.click_duration = click_duration
        self.click_time_end = None
        return
    
    def click(self):
        self.is_clicked = True
        self.click_time_end = current_time_in_ms() + self.click_duration*1000
        return
    
    def unclick(self):
        self.is_clicked = False
        self.click_time_end = None
        return
    
    def is_mouse_over(self):
        return self.visible and self.click_rect.collidepoint(mouse_position())
    
    def update(self):
        Element.update(self)
        if not self.click_rect:
            self.click_rect = self.rect
        if self.is_mouse_clicking():
            self.click()
        if self.is_clicked and self.click_time_end and \
        current_time_in_ms() > self.click_time_end:
            self.unclick()
        if self.old_is_clicked is None or self.is_clicked != self.old_is_clicked:
            self.old_is_clicked = self.is_clicked
            self.refresh()
        return