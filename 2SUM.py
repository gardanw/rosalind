with open("rosalind_2sum.txt", "r") as file:
    file.readline()
    out = []
    for line in file:
        line = list(map(int, line.split()))
        if line.count(0) > 1:
            ind1 = line.index(0)
            ind2 = ind1 + line[ind1 + 1 :].index(0) + 1
            out.append(f"{ind1+1} {ind2+1}\n")
            continue
        for l in line:
            if -l in line:
                out.append(f"{line.index(l)+1} {line.index(-l)+1}\n")
                break
        else:
            out.append("-1\n")
print("".join(out))
