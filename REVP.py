with open(r'rosalind_revp.txt', 'r') as file:
    dna = ''
    for line in file:
        if len(line) != 0 and line[0] != '>':
            dna += line[:-1]

# dna = 'TCAATGCATGCGGGTCTATATGCAT'

rev_dna = ''
for n in dna[::-1]:
    if n == 'A':
        rev_dna += 'T'
    if n == 'T':
        rev_dna += 'A'
    if n == 'C':
        rev_dna += 'G'
    if n == 'G':
        rev_dna += 'C'

out = []
for i in range(4, 13):
    for j in range(1, len(dna)-i+2):
        if j == 1:
            if dna[j-1:j+i-1] == rev_dna[-(j+i-1):]:
                out.append((j, i))
        else:
            if dna[j-1:j+i-1] == rev_dna[-(j+i-1):-(j-1)]:
                out.append((j, i))

print(len(dna))
print(dna)
print(rev_dna)
print(dna[507-1-2:507+14-1])
print(rev_dna[-(507+14-1):-(507-1-2)])

with open('revp_out.txt', 'w') as file:
    for o in out:
        x, y = o
        file.write(f'{x} {y}\n')
