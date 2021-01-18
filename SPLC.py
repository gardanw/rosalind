def translate(s, c):
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



with open(r'rosalind_splc.txt', 'r') as file:
    dna = ''
    introns = []
    first_seq = True
    file.readline()
    for line in file:
        if first_seq and len(line) != 0 and line[0] != '>':
            dna += line[:-1]
        elif len(line) != 0 and line[0] != '>':
            introns[-1] += line[:-1]
        if len(line) != 0 and line[0] == '>':
            first_seq = False
            introns.append('')

print(dna)
for intron in introns:
    dna = dna.replace(intron, '')
print(dna)

codons = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', 'TTA': 'L',
          'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P',
          'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'TCA': 'S', 'CCA': 'P', 'ACA': 'T',
          'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
          'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'TAA': '\n', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'TAG': '\n',
          'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R',
          'AGC': 'S', 'GGC': 'G', 'TGA': '\n', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'TGG': 'W', 'CGG': 'R', 'AGG': 'R',
          'GGG': 'G'}

print(translate(dna, codons))
