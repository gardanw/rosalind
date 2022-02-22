def rev_perm(p):
    for i in range(len(p)):
        for j in range(i + 2, len(p) + 1):
            yield p[:i] + p[i:j][::-1] + p[j:]


def drev(p1, p2):
    d = 0
    mind = 9
    if p1 == p2:
        return d
    rp1 = {p1: d}
    while d < 4:
        d += 1
        rpitem = list(rp1.items())
        for k, v in rpitem:
            if v == d - 1:
                for rp in rev_perm(k):
                    if rp == p2:
                        return d
                    if rp not in rp1:
                        rp1[rp] = d
    d = 0
    rp2 = {p2: d}
    while d < 4:
        d += 1
        rpitem = list(rp2.items())
        for k, v in rpitem:
            if v == d - 1:
                for rp in rev_perm(k):
                    if rp == p1:
                        return d
                    if rp not in rp2:
                        rp2[rp] = d
                    if rp in rp1:
                        mind = min(mind, rp1[rp] + rp2[rp])
    return mind


if __name__ == "__main__":
    distances = []

    with open('rosalind_rear.txt', 'r') as file:
        permutations = []
        for line in file:
            if line != '\n':
                permutations.append(
                    [tuple(map(int, line.strip().split())), tuple(map(int, file.readline().strip().split()))])

    for p in permutations:
        distances.append(drev(p[0], p[1]))
        print(p)

    print(' '.join(map(str, distances)))
