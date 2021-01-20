with open('rosalind_ddeg.txt', 'r') as file:
    n, e = tuple(map(int, file.readline().strip().split(' ')))
    node = {i: set() for i in range(1, n + 1)}
    for line in file:
        line = list(map(int, line.strip().split(' ')))
        if len(line) == 2:
            node[line[0]].add(line[1])
            node[line[1]].add(line[0])

out = [sum([len(node[k]) for k in node[i]]) for i in range(1, n + 1)]
print(' '.join(list(map(str, out))))
