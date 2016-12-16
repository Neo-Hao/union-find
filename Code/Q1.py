# Approach 1: Union Find
## class Union is already defined
def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    union = Union()
    
    for i in range(n):
        union.makeSet(i)
    for i, j in edges:
        union.union(i, j)
    
    return union.count

class Node(object):
    def __init__(self, v):
        self.v = v
        self.parent = None

class Union(object):
    def __init__(self):
        # use table to associate a vertex and a node
        self.table = {}
        self.count = 0

    # makeSet method
    def makeSet(self, v):
        # input: vertex
        node = Node(v)
        node.parent = node
        self.table[v] = node
        self.count += 1

    # union method
    def union(self, v1, v2):
        # input: vertex1, vertex2
        i, j = self.findSet(v1), self.findSet(v2)
        if i == j:
            return
        j.parent = i
        self.count -= 1

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



# Approach 2: DFS
def countComponents(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    table = {i:[] for i in range(n)}
    for a,b in edges:
        table[a].append(b)
        table[b].append(a)

    visited, count = [0]*n, 0
    for i in range(n):
        if not visited[i]:
            self.dfs(i, table, visited)
            count += 1
    return count

def dfs(self, node, table, visited):
    if visited[node]:
        return
    visited[node] = 1
    nbs = table.pop(node, [])
    for n in nbs:
        self.dfs(n, table, visited)