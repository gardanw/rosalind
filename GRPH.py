with open(r'rosalind_grph.txt', 'r') as file:
    dic = {}
    for line in file:
        if line[0] == '>':
            name = line[1:-1]
            dic[name] = ''
        else:
            dic[name] += line[:-1]

list_edge = []

keys = list(dic.keys())
for i in range(len(keys)):
    for j in range(len(keys)):
        if i != j and dic[keys[i]][-3:] == dic[keys[j]][:3]:
            list_edge.append((keys[i], keys[j]))

for edge in list_edge:
    print(edge[0], edge[1])
