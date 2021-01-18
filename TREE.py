import networkx as nx
import matplotlib.pyplot as plt

with open(r'rosalind_tree.txt', 'r') as file:
    n = int(file.readline()[:-1])
    edges = []
    for line in file:
        edges.append(tuple([int(i) for i in list(line[:-1].split())]))

print(n)
graph = [(edges[0][0], edges[0][1])]
print(edges)

G = nx.Graph()
G.add_nodes_from([i for i in range(1, n+1)])
G.add_edges_from(edges)

print(len(list(nx.connected_components(G)))-1)
