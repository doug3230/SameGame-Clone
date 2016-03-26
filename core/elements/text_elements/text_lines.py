'''
Created on Mar 12, 2016

@author: Richard
'''
from constants import BLACK
from elements import ElementCollection
from text import Text

class TextLines(ElementCollection):
    def __init__(self, text=[], number_of_lines=None, font_type="Monospace",
                 font_colour=BLACK, font_size=20, bold=False, italic=False, **kwargs):
        if number_of_lines is None:
            number_of_lines = len(text)
        self.text = text
        self.number_of_lines = number_of_lines
        self.font_type = font_type
        self.font_colour = font_colour
        self.font_size = font_size
        self.bold = bold
        self.italic = italic
        ElementCollection.__init__(self, **kwargs)
        self.redisplay_lines()
        return
    
    def redisplay_lines(self):
        lines = []
        current_y = self.rect.y
        text_height = self.rect.h // self.number_of_lines
        for i in range(self.number_of_lines):
            new_line = Text(font_type=self.font_type, font_colour=self.font_colour,
                            font_size=self.font_size, bold=self.bold, italic=self.italic)
            if i < len(self.text):
                new_line.text = self.text[i]
            new_line.rect.x = self.rect.x
            new_line.rect.y = current_y
            new_line.rect.w = self.rect.w
            new_line.rect.h = text_height
            lines.append(new_line)
            current_y += text_height
        self.subelements = lines
        self.refresh()
        return
    
    def get_line(self, index):
        return self.subelements[index]