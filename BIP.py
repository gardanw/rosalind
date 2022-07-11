class Graph:
    def __init__(self, n):
        self.n_nodes = n
        self.edges = [[0 for _ in range(n)] for _ in range(n)]
        self.colors = [-1 for _ in range(self.n_nodes)]

    def is_bipartite_util(self, n):
        q = [n]
        while q:
            u = q.pop()
            if self.edges[u][u] == 1:
                return False
            for v in range(self.n_nodes):
                if self.edges[u][v] == 1 and self.colors[v] == -1:
                    self.colors[v] = 1 - self.colors[u]
                    q.append(v)
                elif self.edges[u][v] == 1 and self.colors[v] == self.colors[u]:
                    return False
        return True

    def is_bipartite(self):
        self.colors = [-1 for _ in range(self.n_nodes)]
        for i in range(self.n_nodes):
            if self.colors[i] == -1:
                if not self.is_bipartite_util(i):
                    return False
        return True


with open("rosalind_bip.txt", "r") as file:
    file.readline()
    file.readline()
    graphs = []
    for line in file:
        n, e = list(map(int, line.split()))
        g = Graph(n)
        for _ in range(e):
            line = file.readline()
            n1, n2 = list(map(int, line.split()))
            g.edges[n1 - 1][n2 - 1] = 1
            g.edges[n2 - 1][n1 - 1] = 1

        graphs.append(g)
        file.readline()


out = []

for g in graphs:
    print(g.n_nodes)
    print(sum([sum(e) for e in g.edges]) / 2)
    out.append(1 if g.is_bipartite() else -1)

print(*out)
