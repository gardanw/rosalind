with open("rosalind_inv.txt", "r") as file:
    print(file.readline())
    data = list(map(int, file.readline().split()))

inv = 0
while data:
    dmax = max(data)
    ind_max = data.index(dmax)
    inv += len(data[ind_max + 1 :])
    inv -= data[ind_max + 1 :].count(dmax)
    data.pop(ind_max)

print(inv)
