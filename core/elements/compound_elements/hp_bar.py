'''
Created on May 31, 2015

@author: Richard
'''
from copy import deepcopy
from elements import ElementCollection, Rectangle
from constants import GREEN, YELLOW, RED

class HPBar(ElementCollection):
    def __init__(self, current_hp=1, max_hp=1, 
                 high_colour=GREEN, mid_colour=YELLOW, low_colour=RED, 
                 low_threshold=0.2, mid_threshold=0.5, **kwargs):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.hp_rectangle = Rectangle(**kwargs)
        self.high_colour = high_colour
        self.mid_colour = mid_colour
        self.low_colour = low_colour
        self.low_threshold = low_threshold
        self.mid_threshold = mid_threshold
        ElementCollection.__init__(self, subelements=[self.hp_rectangle], **kwargs)
        self.rect = deepcopy(self.rect)
        return
    
    def draw(self, screen):
        if self.current_hp > 0:
            ElementCollection.draw(self, screen)
        return
    
    def update(self):
        self.subelements = [self.hp_rectangle]
        self.hp_rectangle.rect.x = self.rect.x
        self.hp_rectangle.rect.y = self.rect.y
        self.hp_rectangle.rect.height = self.rect.height
        bar_width = int(self.rect.width * self.damage_ratio())
        self.hp_rectangle.rect.width = bar_width
        self.hp_rectangle.colour = self.current_colour()
        ElementCollection.update(self)
        return
    
    def damage_ratio(self):
        return float(self.current_hp) / float(self.max_hp)
    
    def current_colour(self):
        damage_ratio = self.damage_ratio()
        if damage_ratio <= self.low_threshold:
            bar_colour = self.low_colour
        elif damage_ratio <= self.mid_threshold:
            bar_colour = self.mid_colour
        else:
            bar_colour = self.high_colour 
        return bar_colour
