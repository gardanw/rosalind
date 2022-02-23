mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}


def rev_seq(seq):
    rseq = ''
    for b in seq[::-1]:
        rseq += mapping[b]
    return rseq


with open(r'rosalind_corr.txt', 'r') as file:
    seqs = []
    rseqs = []
    for line in file:
        if line != '' and line[0] != '>':
            seqs.append(line[:-1])
            rseqs.append(rev_seq(line[:-1]))

to_corr = []
corr = set()
for s, r in zip(seqs, rseqs):
    if seqs.count(s) + rseqs.count(s) == 1:
        to_corr.append(s)
    else:
        corr.add(s)
        corr.add(r)

set_seq = set(seqs + rseqs)
end_corr = {}
for tcorr in to_corr:
    for seq in corr:
        c = 0
        for b1, b2 in zip(tcorr, seq):
            if b1 != b2:
                c += 1
            if c > 1:
                break
        if c == 1:
            if tcorr in end_corr:
                del end_corr[tcorr]
                break
            end_corr[tcorr] = seq
print(len(to_corr))
print(len(set_seq))
print(len(end_corr))
with open(r'rosalind_corr_out.txt', 'w') as file:
    for k, v in end_corr.items():
        file.write(f'{k}->{v}\n')
