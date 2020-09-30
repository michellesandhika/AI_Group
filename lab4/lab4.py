import networkx as nx
import matplotlib.pylab as plt

""" 
Answers to the question is in answer.txt
"""

# create empty digraph
G = nx.DiGraph()

# Add nodes
G.add_node(7)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_node(12)
G.add_node(1)
G.add_node(2)

# Add edge
G.add_edge(7, 9, length = 30)
G.add_edge(7, 11, length = 50)
G.add_edge(7, 10, length = 40)

G.add_edge(9, 1, length = 50)
G.add_edge(9, 11, length = 30)
G.add_edge(9, 12, length = 40)

G.add_edge(10, 12, length = 30)
G.add_edge(10, 1, length = 40)

G.add_edge(11, 1, length = 30)
G.add_edge(11, 2, length = 40)

G.add_edge(12, 2, length = 30)

G.add_edge(1, 2, length = 30)

path =nx.shortest_path (G, 7, 2, weight = 'length')
path_length=nx.shortest_path_length(G,7,2,weight='length')
print(path)
print(path_length)

# draw the graph
edge_labels = nx.get_edge_attributes(G,'length')
pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
nx.draw_networkx(G, pos)
plt.show()



