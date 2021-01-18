def PERM(k, A, a_perm):
    if k == 1:
        a_perm.append(A[:])
    else:
        PERM(k-1, A, a_perm)
        for i in range(k-1):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            PERM(k-1, A, a_perm)
    return a_perm


n = 5
all_perm = PERM(n, [i for i in range(1, n+1)], [])

with open('perm_out.txt', 'w') as file:
    file.write(str(len(all_perm)) + '\n')
    for perm in all_perm:
        for n in perm:
            if n != perm[-1]:
                file.write(str(n) + ' ')
            else:
                file.write(str(n) + '\n')
