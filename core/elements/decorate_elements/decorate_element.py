'''
Created on Dec 6, 2015

@author: Richard
'''
from elements import Element

class DecorateElement(Element):
    def __init__(self, element=None, **kwargs):
        Element.__init__(self, **kwargs)
        self.element = element
        self.old_element = None
        return
    
    def decorated_element(self):
        if not self.element:
            d_e = None
        else:
            d_e = self.element.decorated_element()
        return d_e
    
    def refresh(self):
        Element.refresh(self)
        if self.element:
            self.element.refresh()
            for dirty_rect in self.element.dirty_list:
                self.dirty_list.append(dirty_rect)
            self.element.dirty_list = []
        return
    
    def draw(self, screen):
        Element.draw(self, screen)
        if self.element:
            self.element.draw(screen)
        return
    
    def update(self):
        if self.element or self.old_element:
            if (not self.old_element) or (not self.element) or \
            (self.element != self.old_element):
                self.refresh()
            if self.element:
                self.element.update()
                self.rect = self.element.rect
                for dirty_rect in self.element.dirty_list:
                    self.dirty_list.append(dirty_rect)
                self.element.dirty_list = []
            self.old_element = self.element
        Element.update(self)
        return