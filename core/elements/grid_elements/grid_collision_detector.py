'''
Created on Mar 1, 2016

@author: Richard
'''

class GridCollisionDetector:
    def __init__(self, grid_elements=[]):
        self.grid_elements = grid_elements
        self.recalculate_occupied_tiles()
        return
    
    def recalculate_occupied_tiles(self):
        self.occupied_tiles = {}
        for element in self.grid_elements:
            for position in element.grid_position.occupied_tiles():
                if not self.occupied_tiles.has_key(position):
                    self.occupied_tiles[position] = []
                self.occupied_tiles[position].append(element)
        return
    
    def is_tile_occupied(self, x, y):
        return self.occupied_tiles.has_key((x, y))
    
    def tile_occupants(self, x, y):
        occupants = []
        if self.is_tile_occupied(x, y):
            occupants = self.occupied_tiles[(x, y)]
        return occupants
    
    def tile_occupant(self, x, y):
        return self.tile_occupants(x, y)[0]
    
    def occupants_in_rect(self, x, y, w, h):
        elements = []
        for i in range(x, x + w):
            for j in range(y, y + h):
                for element in self.tile_occupants(i, j):
                    elements.append(element)
        return elements
    
    def insert_element(self, element):
        self.grid_elements.append(element)
        for position in element.grid_position.occupied_tiles():
            if not self.occupied_tiles.has_key(position):
                self.occupied_tiles[position] = []
            self.occupied_tiles[position].append(element)
        return
    
    def remove_element(self, element):
        self.grid_elements.remove(element)
        for position in element.grid_position.occupied_tiles():
            self.occupied_tiles[position].remove(element)
        return