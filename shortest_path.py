import numpy as np

class node:
    def __init__(self):
        self.data = []
        self.edges = []

class tree:
    def __init__(self, source):
        self.sourse = []
        self.ancestor = []
        self.descendant = []
        pass

    def add_descendant(self, descendant):
        self.descendant.append(descendant)

    def set_ancestor(self, ancestor):
        self.ancestor = ancestor

    def set_source(self, source):
        self.source = source

    def get_source(self):
        return self.source

    def get_ancestor(self):
        return self.ancestor

    def get_descendant(self):
        return self.descendant

    def short_path(self):
        pass