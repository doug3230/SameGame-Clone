'''
Created on Mar 19, 2016

@author: Richard
'''
from elements import GridElementCollection
from bubble_cluster_settings import *

class BubbleCluster(GridElementCollection):
    def __init__(self, bubbles=[], grid_camera=None):
        GridElementCollection.__init__(self, subelements=bubbles,
                                       auto_place=True,auto_resize=False)
        return
    
    def is_selectable_cluster(self):
        return len(self.subelements) > 1
    
    def update(self):
        if self.is_mouse_over() and self.is_selectable_cluster():
            self.resize(width_scale=BUBBLE_CLUSTER_RESIZE_SMALL_WIDTH_SCALE,
                        height_scale=BUBBLE_CLUSTER_RESIZE_SMALL_HEIGHT_SCALE)
        else:
            self.resize(width_scale=BUBBLE_CLUSTER_RESIZE_BIG_WIDTH_SCALE,
                        height_scale=BUBBLE_CLUSTER_RESIZE_BIG_HEIGHT_SCALE)
        GridElementCollection.update(self)
        return