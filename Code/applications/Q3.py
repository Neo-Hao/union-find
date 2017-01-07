# Approach 1: Union Find
def validTree(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    if len(edges) != n-1: return False
    
    union = Union()
    # step 1: makeSet
    for u, v in edges:
        union.makeSet(u)
        union.makeSet(v)
    # step 2: traverse the edges
    for u, v in edges:
        if union.findSet(u) == union.findSet(v):
            return False
        else:
            union.union(u, v)
    return True

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



# Approach 2: BFS
def validTree(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    if len(edges) != n-1: return False
    
    table = {i:[] for i in range(n)}
    for i, j in edges:
        table[i].append(j)
        table[j].append(i)
    
    bfs(table, 0)
    return not table

def bfs(self, table, node):
    nbs = table.pop(node, [])
    for n in nbs:
        bfs(table, n)

