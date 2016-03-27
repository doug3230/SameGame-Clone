'''
Created on Oct 25, 2014

@author: Richard
'''
import pygame
from pygame.freetype import Font, SysFont
from file_processing_settings import *

def path_to_file(dir_name, file_name):
    if dir_name:
        return "{0}/{1}".format(dir_name, file_name)
    else:
        return file_name

def path_to_image(file_name):
    return path_to_file(FILE_PROCESSING_IMAGE_DIRECTORY, file_name)

def path_to_music(file_name):
    return path_to_file(FILE_PROCESSING_MUSIC_DIRECTORY, file_name)

def path_to_level(file_name):
    return path_to_file(FILE_PROCESSING_LEVEL_DIRECTORY, file_name)

def path_to_font(file_name):
    return path_to_file(FILE_PROCESSING_FONT_DIRECTORY, file_name)

def path_to_sound(file_name):
    return path_to_file(FILE_PROCESSING_SOUND_DIRECTORY, file_name)

def load_music(file_name, path_included = False):
    if not path_included:
        pygame.mixer.music.load(path_to_music(file_name))
    else:
        pygame.mixer.music.load(file_name)
    return

def play_music(loop = True):
    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()
    return
    
def stop_music():
    pygame.mixer.music.stop()
    return

def load_sound(file_name, path_included = False):
    if not path_included:
        return pygame.mixer.Sound(path_to_sound(file_name))
    else:
        return pygame.mixer.Sound(file_name)

def load_image(file_name, path_included = False, size=None):
    from game import System
    if not path_included:
        file_name = path_to_image(file_name)
    image = pygame.image.load(file_name)
    if size != None:
        image = resize_image(image, size[0], size[1])
    if System.INITIALIZED:
        return image.convert()
    else:
        return image

def resize_image(image, new_width, new_height):
    from game import System
    image = pygame.transform.scale(image, (int(new_width), int(new_height)))
    if System.INITIALIZED:
        return image.convert()
    else:
        return image

def load_font(file_name, size, bold = False, italic = False, path_included = False):
    if not path_included:
        font = Font(path_to_font(file_name), size, bold, italic)
    else:
        font = Font(file_name, size, bold, italic)
    return font

def load_system_font(file_name, size, bold = False, italic = False):
    font = SysFont(file_name, size, bold, italic)
    return font

