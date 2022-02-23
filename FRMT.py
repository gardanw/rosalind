from Bio import Entrez

with open('rosalind_frmt.txt', 'r') as file:
    ids = file.readline()[:-1].split()

records = {}
min_len = 10 ** 100
text = ''
for i in ids:
    handle = Entrez.efetch(db="nuccore", id=i, rettype="fasta")
    title = handle.readline()
    seq = handle.read()
    if len(seq) < min_len:
        min_len = len(seq)
        text = title + seq
print(text)
