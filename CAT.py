def memoize(function):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val

    return decorated_function


@memoize
def catnum(n):
    mapping = {"A": "U", "U": "A", "G": "C", "C": "G"}
    if len(n) == 0:
        return 1
    c = 0
    for i in range(1, len(n), 2):
        if n[0] == mapping[n[i]]:
            c += catnum(n[1:i]) * catnum(n[i+1:])
    return c

with open('rosalind_cat.txt', 'r') as file:
    rna = ''
    for line in file:
        if line[0] != '>':
            rna += line[:-1]

print(catnum(rna) % 1000000)
