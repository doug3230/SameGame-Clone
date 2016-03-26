'''
Created on Dec 11, 2015

@author: Richard
'''
from constants import BLACK
from elements import ElementCollection
from animated_text import AnimatedText

class AnimatedLines(ElementCollection):
    def __init__(self, text=[], number_of_lines=2, speed=1, font_type="Monospace",
                 font_colour=BLACK, font_size=20, bold=False, italic=False, **kwargs):
        self.text = text
        self.number_of_lines = number_of_lines
        self.speed = speed
        self.font_type = font_type
        self.font_colour = font_colour
        self.font_size = font_size
        self.bold = bold
        self.italic = italic
        self.current_index = -1
        self.lines = []
        self.redisplay_lines()
        ElementCollection.__init__(self, subelements=self.lines, **kwargs)
        return
    
    def start(self):
        self.current_index = -1
        self.page_lines()
        return
    
    def is_started(self):
        return self.current_index >= 0
    
    def reset(self):
        self.current_index = -1
        for line in self.lines:
            line.text = ""
            line.reset()
        return
    
    def finish_page(self):
        for line in self.lines:
            line.finish()
        return
    
    def page_lines(self):
        self.current_index += 1
        for i in range(self.number_of_lines):
            self.lines[i].text = self.text[self.current_index][i]
            self.lines[i].reset()
        return
    
    def redisplay_lines(self):
        lines = []
        for i in range(self.number_of_lines):
            new_line = AnimatedText(speed=self.speed, font_type=self.font_type,
                                    font_colour=self.font_colour, font_size=self.font_size,
                                    bold=self.bold, italic=self.italic)
            if i < len(self.lines):
                new_line.rect = self.lines[i].rect
            lines.append(new_line) 
        self.lines = lines
        self.subelements = self.lines
        return
    
    def place_lines(self, x=0, y=0, w=0, h=0):
        current_y = y
        for line in self.lines:
            line.rect.x = x
            line.rect.y = current_y
            line.rect.w = w
            line.rect.h = h
            current_y += h + 1
        return
    
    def is_finished(self):
        return self.are_lines_finished() and self.current_index + 1 == len(self.text)
    
    def are_lines_finished(self):
        lines_finished = True
        for i in range(self.number_of_lines):
            line = self.lines[i]
            if not line.finished:
                lines_finished = False
                if not line.started:
                    line.start()
                break
        return lines_finished
    
    def update(self):
        for line in self.lines:
            if not line.is_finished():
                if not line.is_started():
                    line.start()
                break
        ElementCollection.update(self)
        return