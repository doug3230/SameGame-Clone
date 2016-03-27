'''
Created on Mar 19, 2016

@author: Richard
'''
from algorithms import uf_node, uf_find, uf_union
from elements import GridRectCollisionDetector
from selements import BubbleCluster

class SameGameCollisionDetector(GridRectCollisionDetector):
    def __init__(self, **kwargs):
        GridRectCollisionDetector.__init__(self, **kwargs)
        self.recalculate_clusters()
        return
    
    def get_clusters(self):
        return self.clusters
    
    def recalculate_clusters(self):
        uf_nodes = {}
        for element in self.grid_elements:
            uf_nodes[(element.grid_position.x, element.grid_position.y)] \
            = uf_node(element=element)
        
        bubble = None
        x_neighbour = None
        y_neighbour = None
        for x in range(self.grid_rect.x, self.grid_rect.x + self.grid_rect.w):
            for y in range(self.grid_rect.y, self.grid_rect.y + self.grid_rect.h):
                if self.is_tile_occupied(x, y):
                    bubble = uf_nodes[(x, y)]
                    if self.is_tile_occupied(x - 1, y):
                        x_neighbour = uf_nodes[(x - 1, y)]
                        if bubble.element.colour == x_neighbour.element.colour:
                            uf_union(bubble, x_neighbour)
                    if self.is_tile_occupied(x, y - 1):
                        y_neighbour = uf_nodes[(x, y - 1)]
                        if bubble.element.colour == y_neighbour.element.colour:
                            uf_union(bubble, y_neighbour)
        
        cluster_positions = {}
        for element in self.grid_elements:
            uf_parent = uf_find(uf_nodes[(element.grid_position.x, element.grid_position.y)])
            if not cluster_positions.has_key(uf_parent):
                cluster_positions[uf_parent] = []
            cluster_positions[uf_parent].append(element)
            
        self.clusters = []
        for key in cluster_positions.keys():
            bubbles = cluster_positions[key]
            cluster = BubbleCluster(bubbles=bubbles, grid_camera=self.grid_rect)
            self.clusters.append(cluster)
        return
    
    def remove_cluster(self, cluster):
        points = []
        for ge in cluster.subelements:
            self.remove_element(ge)
            points.append((ge.grid_position.x, ge.grid_position.y))
        points = sorted(points, key=lambda point: point[1])
        for point in points:
            for ge in self.occupants_with_x(point[0], max_y=point[1] - 1):
                ge.grid_position.y += 1
        
        self.recalculate_occupied_tiles()
        empty_cols = []
        cols_cleared = set([e.grid_position.x for e in cluster.subelements])
        for x in cols_cleared:
            if self.is_col_empty(x):
                empty_cols.append(x)
        empty_cols = sorted(empty_cols, key=lambda x: -x)
        for x in empty_cols:
            for element in self.occupants_after_x(x):
                element.grid_position.x -= 1
        
        if empty_cols:
            self.recalculate_occupied_tiles()
        self.recalculate_clusters()
        return empty_cols
    
    def insert_element(self, element):
        x = element.grid_position.x
        y = element.grid_position.y
        if not self.is_tile_occupied(x, y):
            GridRectCollisionDetector.insert_element(self, element)
        else:
            for e in self.occupants_with_x(x, max_y=y):
                GridRectCollisionDetector.remove_element(self, e)
                e.grid_position.y -= 1
                GridRectCollisionDetector.insert_element(self, e)
            GridRectCollisionDetector.insert_element(self, element)
        return
    
    def insert_cluster(self, cluster, emptied_cols=[]):
        if emptied_cols:
            emptied_cols = sorted(emptied_cols, key=lambda x: x)
            for x in emptied_cols:
                for e in self.occupants_after_x(x - 1):
                    GridRectCollisionDetector.remove_element(self, e)
                    e.grid_position.x += 1
                    GridRectCollisionDetector.insert_element(self, e)
            self.recalculate_occupied_tiles()
        
        sorted_elements = sorted(cluster.subelements, key=lambda e: -e.grid_position.y)
        for e in sorted_elements:
            self.insert_element(e)
        self.recalculate_clusters()
        return