'''
Created on Nov 30, 2014

@author: Richard
'''
import pygame
from elements import Element
from constants.colours import BLACK

class Polygon(Element):
    def __init__(self, points=[], colour=BLACK, **kwargs):
        Element.__init__(self, **kwargs)
        self.points = points
        self.colour = colour
        return
    
    def draw(self, screen):
        if self.points:
            ref_point = self.rect.topleft
            width = self.rect.width
            height = self.rect.height
            draw_points = []
            for p in self.points:
                dp = (ref_point[0] + p[0]*width, ref_point[1] + p[1]*height)
                draw_points.append(dp)
            pygame.draw.polygon(screen, self.colour, draw_points)
        return