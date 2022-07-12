with open("rosalind_dij.txt", "r") as file:
    n, e = list(map(int, file.readline().split()))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(e):
        n1, n2, w = list(map(int, file.readline().split()))
        graph[n1 - 1][n2 - 1] = w

dist = [float("inf")] * n
dist[0] = 0
use = [False] * n
for node1 in range(n):
    min_d = float("inf")
    for node2 in range(n):
        if dist[node2] < min_d and use[node2] is False:
            min_d = dist[node2]
            min_index = node2
    use[min_index] = True
    for node2 in range(n):
        if (
            graph[min_index][node2] > 0
            and use[node2] is False
            and dist[node2] > dist[min_index] + graph[min_index][node2]
        ):
            dist[node2] = dist[min_index] + graph[min_index][node2]

dist = [-1 if d == float("inf") else d for d in dist]
print(*dist)
