'''
Created on Mar 26, 2016

@author: Richard
'''
from pygame import Rect
from constants import BLUE, RED, GREEN, YELLOW
GAME_COLOURS = (BLUE, RED, GREEN, YELLOW)
GAME_GRID_CAMERA_RECT = Rect((0, 0), (400, 400))
GAME_GRID_CAMERA_W = 15
GAME_GRID_CAMERA_H = 15
GAME_OVER_TEXT_RECT = Rect((150, 190), (100, 20))
SCORE_TEXT_RECT = Rect((10, 410), (390, 20))