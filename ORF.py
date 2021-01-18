def ORF(s, c):
    prot_list = []
    for f in range(3):
        prot = ''
        for i in range(f, len(s) - 2, 3):
            if len(prot) == 0 and c[s[i:i + 3]] == 'M':
                prot += c[s[i:i + 3]]
            elif len(prot) != 0 and c[s[i:i + 3]] != '\n':
                prot += c[s[i:i + 3]]
            elif len(prot) != 0 and c[s[i:i + 3]] == '\n':
                prot += c[s[i:i + 3]]
                if prot not in prot_list:
                    prot_list.append(prot)
                prot = ''
    return prot_list


codons = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', 'TTA': 'L',
          'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P',
          'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'TCA': 'S', 'CCA': 'P', 'ACA': 'T',
          'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
          'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'TAA': '\n', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'TAG': '\n',
          'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R',
          'AGC': 'S', 'GGC': 'G', 'TGA': '\n', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'TGG': 'W', 'CGG': 'R', 'AGG': 'R',
          'GGG': 'G'}

with open(r'rosalind_orf.txt', 'r') as file:
    dna = ''
    for line in file:
        if len(line) != 0 and line[0] != '>' and line[0] != '\n':
            dna += line[:-1]

comp_dna = ''
for n in dna:
    if n == 'A':
        comp_dna += 'T'
    if n == 'T':
        comp_dna += 'A'
    if n == 'G':
        comp_dna += 'C'
    if n == 'C':
        comp_dna += 'G'

print(dna)
print(comp_dna[::-1])
prot_l = ORF(dna, codons)
for p in ORF(comp_dna[::-1], codons):
    if p not in prot_l:
        prot_l.append(p)

for p in prot_l:
    if p.count('M') > 1:
        for i in range(1, len(p)):
            if p[i] == 'M' and p[i:] not in prot_l:
                prot_l.append(p[i:])

with open('orf_out.txt', 'w') as file:
    for p in prot_l:
        file.write(p)
