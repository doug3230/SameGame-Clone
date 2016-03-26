'''
Created on Jun 11, 2015

@author: Richard
'''
from elements import ElementCollection

class MenuElement(ElementCollection):
    def __init__(self, cursorElement, x_index=0, y_index=0, max_x_index=0, max_y_index=0,
                 base_x=None, base_y=None, x_gap=0, y_gap=0, page_index=0, max_page_index=0, **kwargs):
        self.cursorElement = cursorElement
        self.x_index = x_index
        self.y_index = y_index
        self.page_index = page_index
        self.max_x_index = max_x_index
        self.max_y_index = max_y_index
        self.max_page_index = max_page_index
        if base_x is None:
            base_x = self.cursorElement.rect.x
        self.base_x = base_x
        if base_y is None:
            base_y = self.cursorElement.rect.y
        self.base_y = base_y
        self.x_gap = x_gap
        self.y_gap = y_gap
        ElementCollection.__init__(self, subelements=[cursorElement], **kwargs)
        return
    
    def page_size(self):
        return (self.max_x_index + 1) * (self.max_y_index + 1)
    
    def move_left(self):
        if self.x_index > 0:
            self.x_index -= 1
        return
    
    def move_right(self):
        if self.x_index < self.max_x_index:
            self.x_index += 1
        return
    
    def move_up(self):
        if self.y_index > 0:
            self.y_index -= 1
        else:
            self.page_up()
        return
    
    def move_down(self):
        if self.y_index < self.max_y_index:
            self.y_index += 1
        else:
            self.page_down()
        return
    
    def page_up(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.x_index = 0
            self.y_index = 0
        return
    
    def page_down(self):
        if self.page_index < self.max_page_index:
            self.page_index += 1
            self.x_index = 0
            self.y_index = 0
        return
    
    def update(self):
        self.rect.x = self.base_x + self.x_gap * self.x_index
        self.rect.y = self.base_y + self.y_gap * self.y_index
        self.cursorElement.rect.x = self.rect.x
        self.cursorElement.rect.y = self.rect.y
        ElementCollection.update(self)
        return
