def HAMM(s, t):
    out = 0
    for i, j in zip(s, t):
        if i != j:
            out += 1
    return out


with open(r'rosalind_hamm.txt', 'r') as file:
    lines = file.readlines()
print(HAMM(lines[0], lines[1]))
