'''
Created on Oct 27, 2014

@author: Richard
'''
import pygame, game
from sgame import MainState

def main():
    game.initialize()
    main_loop(MainState())
    return

def main_loop(initial_state):
    game.set_state(initial_state)
    state = game.state()
    while True:
        for event in pygame.event.get():
            state.handle_event(event)
        state.update()
        if state.refresh_screen:
            state.draw(game.screen())
            game.refresh_screen()
            state.refresh_screen = False
        elif state.dirty_list:
            state.draw(game.screen())
            game.refresh_subscreen(state.dirty_list)
        state.dirty_list = []
        state = game.state()
        game.tick()
    return

if __name__ == "__main__":
    main()