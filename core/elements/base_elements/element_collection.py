'''
Created on Nov 29, 2014

@author: Richard
'''
from element import Element

class ElementCollection(Element):
    def __init__(self, subelements=[], **kwargs):
        Element.__init__(self, **kwargs)
        self.subelements = sorted(subelements, key=lambda e: e.layer)
        return
    
    def draw(self, screen):
        for se in self.subelements:
            if se.visible:
                se.draw(screen)
        return
    
    def update(self):
        for se in self.subelements:
            se.update_active_and_visible()
            if se.active:
                se.update()
            for dirty_rect in se.dirty_list:
                self.dirty_list.append(dirty_rect)
            se.dirty_list = []
        return
    
    def add_element(self, element):
        self.subelements.append(element)
        element.refresh()
        self.resort()
        return
    
    def remove_element(self, element):
        self.subelements.remove(element)
        element.refresh()
        for dirty_rect in element.dirty_list:
            self.dirty_list.append(dirty_rect)
        element.dirty_list = []
        return
    
    def remove_all_elements(self):
        while self.subelements:
            self.remove_element(self.subelements[0])
        return
    
    def resort(self):
        nonduplicates = list(set(self.subelements))
        if None in nonduplicates:
            nonduplicates.pop(nonduplicates.index(None))
        self.subelements = sorted(nonduplicates, key=lambda e: e.layer)
        return
    
    def refresh(self):
        for element in self.subelements:
            element.refresh()
            for dirty_rect in element.dirty_list:
                self.dirty_list.append(dirty_rect)
            element.dirty_list = []
        return