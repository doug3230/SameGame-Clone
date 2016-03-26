'''
Created on Mar 19, 2016

@author: Richard
'''
import pygame
from constants import BLACK
from elements import Element

class Ellipse(Element):
    def __init__(self, colour=BLACK, thickness=0, **kwargs):
        Element.__init__(self, **kwargs)
        self.colour = colour
        self.thickness = thickness
        return
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.colour, self.rect, self.thickness)
        return