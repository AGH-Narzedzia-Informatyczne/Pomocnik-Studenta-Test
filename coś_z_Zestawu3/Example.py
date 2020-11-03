from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

with open ('TSP.txt') as f:
	pre = f.readlines()
pre = [line.split() for line in pre]
cities = []
for element in pre:
	cities.append([int(element[0]), float(element[1]), float(element[2])]) #creating list of cities with coordinates 
pre.clear()

def MatrixMaker(list):
	m = len(list)
	arr = []*100

	for k in range(m):
		temp_arr = []
		for l in range(m):
			temp_ = 0
			temp_ = sqrt(((list[k][1]-list[l][1])**2)+((list[k][2]-list[l][2])**2))
			temp_arr.append(temp_)
		arr.append(temp_arr)
	return arr


def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix >0)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

C_labels = [element[0] for element in cities]
C_graph = MatrixMaker(cities)

A = np.matrix(C_graph)
G = nx.from_numpy_matrix(A)

pos = nx.spring_layout(G)  # positions for all nodes

 #nodes
#nx.draw_networkx_nodes(G, pos, node_size=700)

 #edges
#nx.draw_networkx_edges(G, pos)

plt.axis('off')



mst = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
T = nx.shortest_path_length(mst,0,weight='weight')
A = nx.dfs_preorder_nodes(mst, 0)
E = nx.dfs_edges(mst,0)

mst = nx.minimum_spanning_tree(G, weight='weight', algorithm='prim')
nx.draw_networkx_edges(mst, pos)
nx.draw_networkx_nodes(mst, pos, node_size=70)
nx.draw_networkx_edge_labels(mst, pos,font_size=4)
plt.show()



