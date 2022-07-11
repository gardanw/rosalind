from itertools import combinations
from collections import defaultdict


with open("rosalind_3sum.txt", "r") as file:
    file.readline()
    out = []
    for line in file:
        line = list(map(int, line.split()))
        positions = defaultdict(set)
        for i, l in enumerate(line):
            positions[l].add(i)
        for (i, l1), (j, l2) in combinations(enumerate(line), 2):
            n = 0 - l1 - l2
            if positions[n].difference((i, j)):
                o = [line.index(n) + 1, i + 1, j + 1]
                o.sort()
                out.append(" ".join(map(str, o)))
                break
        else:
            out.append("-1")


for o in out:
    print(o)
