def ini4(a, b):
    s = 0
    for i in range(a, b):
        if i % 2 != 0:
            s += i
    return s

print(ini4(4351, 9062))
