'''
Created on Mar 19, 2016

@author: Richard
'''
from elements import GridElementCollection

class BubbleCluster(GridElementCollection):
    def __init__(self, bubbles=[], grid_camera=None):
        GridElementCollection.__init__(self, subelements=bubbles,
                                       auto_place=True,auto_resize=False)
        return
    
    def is_selectable_cluster(self):
        return len(self.subelements) > 1
    
    def update(self):
        if self.is_mouse_over() and self.is_selectable_cluster():
            self.resize(width_scale=0.5, height_scale=0.5)
        else:
            self.resize(width_scale=1, height_scale=1)
        GridElementCollection.update(self)
        return