from Bio.SeqUtils import GC



def GC_c(s):
    return 100 * (s.count('G') + s.count('C')) / len(s)


with open(r'rosalind_gc.txt', 'r') as file:
    dic = {}
    for line in file:
        if line[0] == '>':
            name = line[1:-1]
            dic[name] = ''
        else:
            dic[name] += line[:-1]

best = 0
for key in dic:
    gc_content = GC_c(dic[key])
    if gc_content > best:
        best = gc_content
        best_name = key
print(best_name)
print(best)
print(GC(dic[best_name]))
