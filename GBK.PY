from Bio import Entrez

with open('rosalind_gbk.txt', 'r') as file:
    org, dat1, dat2 = map(lambda x: x.strip('\n'), file.readlines())

handle = Entrez.esearch(db="nuccore",
                        term=f'((("{dat1}"[Publication Date] : "{dat2}"[Publication Date])) AND {org}[Organism])')
record = Entrez.read(handle)
print(record['Count'])
