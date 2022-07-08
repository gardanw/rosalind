with open("rosalind_maj.txt", "r") as file:
    len_data, n = map(int, file.readline().split())
    out = []
    for line in file:
        line = line.split()
        for l in line:
            if line.count(l) > n / 2:
                out.append(str(l))
                break
        else:
            out.append("-1")

print(" ".join(out))
