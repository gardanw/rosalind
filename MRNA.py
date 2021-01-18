with open(r'rosalind_mrna.txt', 'r') as file:
    prot = file.readline()[:-1]

aa_codon_count = {'M': 1, 'T': 4, 'N': 2, 'K': 2, 'S': 6, 'R': 6, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4, 'F': 2,
                  'L': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'I': 3}

t_number = 3
for aa in prot:
    t_number *= aa_codon_count[aa]

print(t_number % 1000000)
