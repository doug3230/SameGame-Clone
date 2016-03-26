'''
Created on May 31, 2015

@author: Richard
'''
from elements import AnimatedSequence
from text import Text

class AnimatedText(AnimatedSequence):
    def __init__(self, text="", speed=1, **kwargs):
        AnimatedSequence.__init__(self, speed=speed)
        self.element = Text(text=text, **kwargs)
        self.text = text
        self.max_index = len(self.text)
        self.rect = self.element.rect
        return
    
    def reset_font(self):
        if not self.element:
            self.element = Text(text=self.text)
        if self.font_type:
            self.element.font_type = self.font_type
        if self.font_size:
            self.element.font_size = self.font_size
        if self.bold:
            self.element.bold = self.bold
        if self.italic:
            self.element.italic = self.italic
        self.element.reset_font()
        return
    
    def element_at_index(self, index):
        if self.element:
            self.element.text = self.text[:int(index)]
        return self.element
    
    def update(self):
        self.max_index = len(self.text)
        AnimatedSequence.update(self)
        return