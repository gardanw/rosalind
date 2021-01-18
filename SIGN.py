import itertools

n = 6
all_number = [str(i) for i in range(-n, n+1) if i != 0]
print(all_number)

list_perm = list(itertools.permutations(all_number, n))
out_perm = []
for p in list_perm:
    for n in p:
        if str(-int(n)) in p:
            break
    else:
        out_perm.append(p)


with open('sign_out.txt', 'w') as file:
    file.write(str(len(out_perm)) + '\n')
    for p in out_perm:
        file.write(' '.join(p) + '\n')
