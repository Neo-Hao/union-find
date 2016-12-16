# class Union is already defined

# input: graph in the form of edges
# 		edges: [['A', 'B'] ['B', 'C'], ['C', 'D'], ['D', 'E']]
# output: boolean value
#		if there is a cycle, then True; else False
def cycleDetection(edges):
	union = Union()
	# step 1: makeSet
	for u, v in edges:
		union.makeSet(u)
		union.makeSet(v)
	# step 2: traverse the edges
	for u, v in edges:
		if union.findSet(u) == union.findSet(v):
			return True
		else:
			union.union(u, v)
	return False

