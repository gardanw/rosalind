def dag(g, n):
    if g[n]["finished"]:
        return False
    if g[n]["visited"]:
        return True
    g[n]["visited"] = True
    for w in g[n]["neighbour"]:
        if dag(g, w):
            return True
    g[n]["finished"] = True
    return False


with open("rosalind_dag.txt", "r") as file:
    file.readline()
    file.readline()
    graphs = []
    for line in file:
        n, e = list(map(int, line.split()))
        g = {
            i + 1: {"neighbour": [], "visited": False, "finished": False}
            for i in range(n)
        }
        for _ in range(e):
            n1, n2 = list(map(int, file.readline().split()))
            g[n1]["neighbour"].append(n2)
        graphs.append(g)
        file.readline()

out = []
for g in graphs:
    for n in g:
        if dag(g, n):
            out.append(-1)
            break
    else:
        out.append(1)

print(*out)
