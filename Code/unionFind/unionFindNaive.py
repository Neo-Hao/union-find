### Naive Approach
class Node(object):
    def __init__(self, v):
        self.v = v
        self.parent = None

class Union(object):
    def __init__(self):
        # use table to associate a vertex and a node
        self.table = {}

    # makeSet method
    def makeSet(self, v):
        # input: vertex
        node = Node(v)
        node.parent = node
        self.table[v] = node

    # union method
    def union(self, v1, v2):
        # input: vertex1, vertex2
        i, j = self.findSet(v1), self.findSet(v2)
        if i == j:
            return
        j.parent = i

    # findSet method
    def findSet(self, v):
        # input vertex
        n = self.table[v]
        return self.findSetHelper(n)

    def findSetHelper(self, n):
        # input node
        if n.parent == n:
            return n
        return self.findSetHelper(n.parent)