'''
Created on Jun 13, 2015

@author: Richard
'''
from elements import Element
from game import load_image

class ImageElement(Element):
    def __init__(self, image_name="", **kwargs):
        Element.__init__(self, **kwargs)
        self.image_name = image_name
        self.old_image_name = None
        self.image = None
        return
    
    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect.topleft)
        return
    
    def update(self):
        def names_are_synchronized():
            return self.image_name == self.old_image_name
        def sizes_are_synchronize():
            return self.old_rect is not None and self.rect.size == self.old_rect.size
        if not (names_are_synchronized() and sizes_are_synchronize()) and self.image_name != "":
            self.image = load_image(self.image_name, size=self.rect.size)
            self.refresh()
        self.old_image_name = self.image_name
        Element.update(self)
        return