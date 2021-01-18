import math


with open(r'rosalind_PMCH.txt', 'r') as file:
    seq = ''
    for line in file:
        if len(line) != 0 and line[0] != '>':
            seq += line[:-1]

# seq = 'AGCUAGUCAU'

au = seq.count('A')
gc = seq.count('G')

print(math.factorial(au) * math.factorial(gc))
