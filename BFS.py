import networkx as nx


with open("rosalind_bfs.txt", "r") as file:
    G = nx.DiGraph()
    n = int(file.readline().split()[0])
    for i in range(1, n + 1):
        G.add_node(i)

    for line in file:
        line = line.split()
        G.add_edge(int(line[0]), int(line[1]))
p = dict(nx.shortest_path_length(G))
out = []
for i in range(1, n + 1):
    try:
        plen = p[1][i]
    except KeyError:
        plen = -1
    out.append(plen)

print(" ".join(map(str, out)))
