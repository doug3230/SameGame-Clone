'''
Created on Dec 14, 2015

@author: Richard
'''
from elements import ElementCollection

class DialogBox(ElementCollection):
    PAIR_TITLE_AND_ICON_INDEX = 0
    PAIR_TEXT_INDEX = 1
    TITLE_INDEX = 0
    ICON_INDEX = 1
    
    def __init__(self, rectangle=None, animated_lines=None,
                 title=None, icon=None, **kwargs):
        self.rectangle = rectangle
        self.animated_lines = animated_lines
        self.title = title
        self.icon = icon
        self.dialog = None
        subelements = [self.rectangle, self.title, self.icon, self.animated_lines]
        ElementCollection.__init__(self, subelements=subelements, **kwargs)
        return
    
    def load_dialog(self, dialog):
        self.dialog = dialog
        self.animated_lines.text = [pair[DialogBox.PAIR_TEXT_INDEX] for pair in self.dialog]
        return
    
    def update(self):
        self.rectangle.layer = self.layer
        self.title.layer = self.layer + 1
        self.icon.layer = self.layer + 1
        self.animated_lines.layer = self.layer + 1
        if self.dialog:
            current_line = self.dialog[self.animated_lines.current_index]
            title_and_icon = current_line[DialogBox.PAIR_TITLE_AND_ICON_INDEX]
            self.title.text = title_and_icon[DialogBox.TITLE_INDEX]
            self.icon.image_name = title_and_icon[DialogBox.ICON_INDEX]
        ElementCollection.update(self)
        return