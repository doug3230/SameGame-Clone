'''
Created on Mar 15, 2016

@author: Richard
'''
from random import choice
from copy import deepcopy
from pygame import MOUSEBUTTONDOWN
from elements import SubState, GridCamera, init_grid_element_at, Text
from selements import Bubble, SameGameCollisionDetector
from game_state_settings import *

class GameState(SubState):
    def __init__(self):
        SubState.__init__(self)
        self.new_game()
        return
    
    def new_game(self):
        self.grid_camera = GridCamera(rect=GAME_STATE_GRID_CAMERA_RECT,
                                      w=GAME_STATE_GRID_CAMERA_W, h=GAME_STATE_GRID_CAMERA_H)
        
        min_y = self.grid_camera.y
        max_y = self.grid_camera.y + self.grid_camera.h
        min_x = self.grid_camera.x
        max_x = self.grid_camera.x + self.grid_camera.w
        
        self.collision_detector = SameGameCollisionDetector(grid_rect=self.grid_camera,
                                                            grid_elements=[])
        for y in range(max_y - 1, min_y - 1, -1):
            for x in range(min_x, max_x, 1):
                element = init_grid_element_at(Bubble, x=x, y=y,
                                               colour=choice(GAME_STATE_COLOURS),
                                               grid_camera=self.grid_camera)
                self.collision_detector.insert_element(element)
        
        self.collision_detector.recalculate_clusters()
        self.new_game_elements = deepcopy(self.collision_detector.grid_elements)
        self.game_over = False
        self.game_over_text = Text(rect=GAME_STATE_GAME_OVER_TEXT_RECT, bold=True,
                                   font_size=GAME_STATE_GAME_OVER_TEXT_FONT_SIZE)
        self.score = 0
        self.score_text = Text(rect=GAME_STATE_SCORE_TEXT_RECT,
                               font_size=GAME_STATE_SCORE_TEXT_FONT_SIZE)
        self.clusters_removed = []
        return
    
    def remove_cluster(self, cluster):
        empty_cols = self.collision_detector.remove_cluster(cluster)
        self.remove_element(cluster)
        self.clusters_removed.append((cluster, empty_cols))
        self.score += GAME_STATE_SCORE_FOR_CLUSTER(cluster)
        return
    
    def undo_move(self):
        if self.clusters_removed:
            last_removed = self.clusters_removed.pop()
            cluster = last_removed[0]
            emptied_cols = last_removed[1]
            self.collision_detector.insert_cluster(cluster, emptied_cols=emptied_cols)
            self.score -= GAME_STATE_SCORE_FOR_CLUSTER(cluster)
        return
    
    def reset_game(self):
        grid_elements = self.new_game_elements
        self.new_game_elements = deepcopy(grid_elements)
        self.collision_detector = SameGameCollisionDetector(grid_rect=self.grid_camera,
                                                            grid_elements=grid_elements)
        self.clusters_removed = []
        self.score = 0
        return
    
    def handle_event(self, event):
        SubState.handle_event(self, event)
        if event.type == MOUSEBUTTONDOWN:
            for cluster in self.collision_detector.get_clusters():
                if cluster.is_selectable_cluster() and cluster.is_mouse_clicking():
                    self.remove_cluster(cluster)
                    break
        return
    
    def update(self):
        clusters = self.collision_detector.get_clusters()
        self.game_over = len(filter(lambda c: c.is_selectable_cluster(), clusters)) == 0
        if self.game_over:
            if clusters:
                self.game_over_text.text = GAME_STATE_GAME_OVER_TEXT_LOSE_TEXT
            else:
                self.game_over_text.text = GAME_STATE_GAME_OVER_TEXT_WIN_TEXT
        self.game_over_text.visible = self.game_over
        self.score_text.text = GAME_STATE_SCORE_TEXT_FOR_SCORE(self.score)
        self.subelements = clusters + [self.game_over_text, self.score_text]
        SubState.update(self)
        return