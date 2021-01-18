import itertools

with open(r'rosalind_lexf.txt', 'r') as file:
    char_list = file.readline()[:-1].split(' ')
    n = int(file.readline()[:-1])

print(char_list, n)

all_comb = list(itertools.combinations_with_replacement(char_list, n))
for i in range(len(all_comb)):
    all_comb[i] = ''.join(all_comb[i])

for comb in all_comb:
    for perm in list(itertools.permutations(list(comb))):
        if ''.join(perm) not in all_comb:
            all_comb.append(''.join(perm))
print(all_comb)
with open('lexf_out.txt', 'w') as file:
    for word in sorted(all_comb):
        file.write(word + '\n')
