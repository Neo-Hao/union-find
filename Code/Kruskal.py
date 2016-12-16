# class Union is already defined

# input: weighted edges
# weightedEdges: 	[(1, 'A', 'B'),
#     (5, 'A', 'C'),
#     (3, 'A', 'D'),
#     (4, 'B', 'C'),
#     (2, 'B', 'D'),
#     (1, 'C', 'D')]
# output: a list of edges
#	sample: [('A', 'B') ('B', 'C'), ('C', 'D'), ('D', 'E')]

def kruskal(weightedEdges):
	union = Union()
	result = []
	# step 1
	for u, v in weightedEdges:
		union.makeSet(v)
	# step 2
	weightedEdges.sort()
	# step 3
	for w, u, v in weightedEdges:
		if union.findSet(u) != union.findSet(v):
			result.append((u, v))
			union.union(u, v)

	return result