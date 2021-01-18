def FIB(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return k * FIB(n - 2, k) + FIB(n - 1, k)


print(FIB(29, 3))
