with open(r'rosalind_tran.txt', 'r') as file:
    seq_list = []
    for line in file:
        if len(line) != 0 and line[0] == '>':
            seq_list.append('')
        else:
            seq_list[-1] += line[:-1]

s1 = seq_list[0]
s2 = seq_list[1]
print(s1)
print(s2)

transition = 0
transversion = 0
for n1, n2 in zip(s1, s2):
    if n1 == 'A' and n2 == 'G' or n1 == 'G' and n2 == 'A' or n1 == 'C' and n2 == 'T' or n1 == 'T' and n2 == 'C':
        transition += 1
    elif n1 != n2:
        transversion += 1
print(transition/transversion)
