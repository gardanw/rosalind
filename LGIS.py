with open(r'rosalind_lgis.txt', 'r') as file:
    n = file.readline()
    pi = []
    for p in file.readline()[:-1].split(' '):
        pi.append(int(p))

# pi = [8, 2, 1, 6, 5, 7, 4, 3, 9]

l = [1]
for i in range(1, len(pi)):
    l.append(1 + max([l[j] if pi[i] >= pi[j] else 0 for j in range(len(l))]))

print(l)

pi_i = pi[::-1]
l_i = l[::-1]
lis = [pi_i[l_i.index(max(l_i))]]
for i in range(l_i.index(max(l_i)) + 1, len(l_i)):
    if l_i[i] == max(l_i) - len(lis) and lis[-1] >= pi_i[i]:
        lis.append(pi_i[i])

lis = lis[::-1]

l = [1]
for i in range(1, len(pi)):
    l.append(1 + max([l[j] if pi[i] <= pi[j] else 0 for j in range(len(l))]))

print(l)

pi_d = pi[::-1]
l_d = l[::-1]
lds = [pi_d[l_d.index(max(l_d))]]
for i in range(l_d.index(max(l_d)) + 1, len(l_d)):
    if l_d[i] == max(l_d) - len(lds) and lds[-1] <= pi_d[i]:
        lds.append(pi_d[i])

lds = lds[::-1]

for i in range(len(lis)):
    lis[i] = str(lis[i])

for i in range(len(lds)):
    lds[i] = str(lds[i])

with open('lgis_out.txt', 'w') as file:
    file.write(' '.join(lis) + '\n')
    file.write(' '.join(lds) + '\n')
