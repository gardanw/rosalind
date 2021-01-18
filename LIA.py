import math

k = 5
N = 9
all_org = 2 ** k
P = sum([((3 / 4) ** (all_org - i)) * ((1 / 4) ** i) * math.factorial(all_org) / (
            math.factorial(i) * math.factorial(all_org - i)) for i in range(N, all_org + 1)])
print(P)
