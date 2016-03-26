'''
Created on Nov 15, 2014

@author: Richard
'''
from constants import BLACK
from game import load_system_font
from elements import Element

class Text(Element):
    def __init__(self, font_type="Monospace", font_colour=BLACK, text="", \
                 font_size = 20, bold=False, italic=False, **kwargs):
        Element.__init__(self, **kwargs)
        self.font_type = font_type
        self.old_font_type = font_type
        self.font_colour = font_colour
        self.old_font_colour = font_colour
        self.text = text
        self.old_text = None
        self.bold = bold
        self.old_bold = bold
        self.italic = italic
        self.old_italic = italic
        self.font_size = font_size
        self.old_font_size = font_size
        self.font = load_system_font(font_type, self.font_size, bold, italic)
        return
    
    def draw(self, screen):
        Element.draw(self, screen)
        location = (self.rect.x, self.rect.y)
        self.font.render_to(screen, location, self.text, self.font_colour)
        return
    
    def update(self):
        if self.old_bold != self.bold or self.old_italic != self.italic or \
           self.old_font_size != self.font_size or self.old_font_type != self.font_type:
            self.reset_font()
        elif self.old_text is None or self.old_text != self.text or \
             self.old_font_colour != self.font_colour:
            self.refresh()
        self.old_text = self.text
        self.old_bold = self.bold
        self.old_italic = self.italic
        self.old_font_colour = self.font_colour
        self.old_font_size = self.font_size
        self.old_font_type = self.font_type
        Element.update(self)
        return
    
    def reset_font(self):
        self.font = load_system_font(self.font_type, self.font_size, self.bold, self.italic)
        self.refresh()
        return
