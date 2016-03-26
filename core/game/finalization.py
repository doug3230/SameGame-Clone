'''
Created on Oct 27, 2014

@author: Richard
'''
import pygame, game

def finalize():
    import sys
    game.file_processing.stop_music()
    pygame.quit()
    sys.exit()
    return
