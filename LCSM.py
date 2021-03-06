def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and all(data[0][i:i + j] in x for x in data):
                    substr = data[0][i:i + j]
    return substr


with open(r'rosalind_lcsm.txt', 'r') as file:
    seq_list = []
    for line in file:
        if line[0] == '>':
            seq_list.append('')
        else:
            seq_list[-1] += line[:-1]

print(long_substr(seq_list))
