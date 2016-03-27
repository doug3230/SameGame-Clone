'''
Created on Mar 20, 2016

@author: Richard
'''
def uf_node(element=None):
    class UnionNode:
        def __init__(self, element=None):
            self.element = element
            self.parent = self
            return
    return UnionNode(element=element)

def uf_find(uf_node):
    if uf_node.parent != uf_node:
        uf_node.parent = uf_find(uf_node.parent)
    return uf_node.parent

def uf_union(uf_node1, uf_node2):
    root1 = uf_find(uf_node1)
    root2 = uf_find(uf_node2)
    root2.parent = root1
    return