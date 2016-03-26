'''
Created on Mar 20, 2016

@author: Richard
'''
class UnionNode:
    def __init__(self, element=None):
        self.element = element
        self.parent = self
        return
    
def uf_find(union_node):
    if union_node.parent != union_node:
        union_node.parent = uf_find(union_node.parent)
    return union_node.parent

def uf_union(union_node1, union_node2):
    root1 = uf_find(union_node1)
    root2 = uf_find(union_node2)
    root2.parent = root1
    return