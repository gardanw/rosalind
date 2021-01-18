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
def FIBD(n, m):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        x = [FIBD(k, m) for k in range(n-m, n-1)]
        return sum(x)


print(FIBD(100, 19))
