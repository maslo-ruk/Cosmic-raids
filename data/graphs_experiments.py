import networkx

g = networkx.Graph()
g.add_nodes_from([1,2,3,4])
g.add_nodes_from([4,3,5,6])
print(g.nodes)