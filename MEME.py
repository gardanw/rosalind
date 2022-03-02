def chop(st, k):
    """ Chop string into k-mers of given length """
    for i in range(len(st) - (k - 1)):
        yield st[i:i + k], st[i:i + k - 1], st[i + 1:i + k]


with open('rosalind_meme.txt') as file:
    seqs = []
    for line in file:
        if line[0] == '>':
            seqs.append('')
        else:
            seqs[-1] += line[:-1]

kmers = {}
for seq in seqs:
    for i in range(20, len(seq)):
        if i not in kmers:
            kmers[i] = {}
        for c, p, l in chop(seq, i):
            if c not in kmers[i]:
                kmers[i][c] = 1
            else:
                kmers[i][c] += 1

newkmers = {}
for k in kmers:
    for kk in kmers[k]:
        if kmers[k][kk] > 1:
            # print(f'>{kk}\n{kk}')
            if k not in newkmers:
                newkmers[k] = []
            newkmers[k].append(kk)
for k in newkmers[max(list(newkmers.keys()))]:
    print(f'>{k}\n{k}')

