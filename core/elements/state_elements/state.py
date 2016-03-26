'''
Created on Nov 1, 2014

@author: Richard
'''
import game, pygame
from elements import ElementCollection

class State(ElementCollection):
    def __init__(self, music_file=None, **kwargs):
        ElementCollection.__init__(self, **kwargs)
        self.music_file = music_file
        self.refresh_screen = True
        return
    
    def draw(self, screen):
        background = game.components.background()
        screen.fill(background)
        ElementCollection.draw(self, screen)
        return
    
    def handle_event(self, event):
        if event.type == pygame.locals.QUIT:
            game.finalization.finalize()
        return
    
    def play_music(self):
        if self.music_file:
            game.file_processing.load_music(self.music_file)
            game.file_processing.play_music()
        return