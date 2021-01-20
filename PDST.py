import numpy as np

with open('rosalind_pdst.txt', 'r') as file:
    seq_list = []
    for line in file:
        if line[0] == '>':
            seq_list.append('')
        else:
            seq_list[-1] += line[:-1]

len_list = len(seq_list)
len_seq = len(seq_list[0])
matrix = np.zeros([len_list, len_list])

for i in range(len_list):
    for j in range(len_list):
        r = 0
        for k in range(len_seq):
            if seq_list[i][k] != seq_list[j][k]:
                r += 1
        matrix[i, j] = r / len_seq
print(matrix)
