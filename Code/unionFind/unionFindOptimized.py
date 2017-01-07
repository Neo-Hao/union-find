### Fully Optimized Approach
class Node(object):
    def __init__(self, v):
        self.v = v
        self.parent = None
        self.rank = 0

class Union(object):
    def __init__(self):
        self.table = {}
    
    # makeSet method
    def makeSet(self, val):
        node = Node(val)
        node.parent = node
        self.table[val] = node
    
    # union method
    def union(self, v1, v2):
        i, j = self.findSet(v1), self.findSet(v2)
        
        # if they belong to the same set, do nothing
        if i == j: return
        
        if i.rank > j.rank:
            j.parent = i
        elif i.rank < j.rank:
            i.parent = j
        else:
            # if they have the same rank, increase the rank of the new representative
            j.parent = i
            i.rank += 1
    
    # findSet method
    def findSet(self, v):
        node = self.table[v]
        return self.findSetHelper(node)

    def findSetHelper(self, n):
        # representative itself
        if n == n.parent:
            return n
        n.parent = self.findSetHelper(n.parent)
        return n.parent