def FIBO(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FIBO(n-1)+FIBO(n-2)

print(FIBO(23))
