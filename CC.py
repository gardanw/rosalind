import networkx as nx


with open("rosalind_cc.txt", "r") as file:
    G = nx.Graph()
    n = int(file.readline().split()[0])
    for i in range(1, n + 1):
        G.add_node(i)

    for line in file:
        line = line.split()
        G.add_edge(int(line[0]), int(line[1]))

print(len([c for c in nx.connected_components(G)]))
