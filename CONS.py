with open(r'rosalind_cons.txt', 'r') as file:
    seq_list = []
    for line in file:
        if line[0] == '>':
            seq_list.append('')
        else:
            seq_list[-1] += line[:-1]

matrix = {'A': [0 for _ in range(len(seq_list[0]))], 'C': [0 for _ in range(len(seq_list[0]))],
          'G': [0 for _ in range(len(seq_list[0]))], 'T': [0 for _ in range(len(seq_list[0]))]}

for seq in seq_list:
    for i in range(len(seq)):
        matrix[seq[i]][i] += 1

fin_seq = ''
for i in range(len(matrix['A'])):
    max_count = 0
    base = str()
    for key in matrix:
        if matrix[key][i] > max_count:
            max_count = matrix[key][i]
            base = key
    fin_seq += base

print(fin_seq)
for key in matrix:
    mtr = str(matrix[key]).strip('[]').split(', ')
    print(f'{key}: ' + ' '.join(mtr))
