k = 22
m = 27
n = 27

suma = k + m + n

p = (k / suma) * ((k - 1) / (suma - 1)) + (k / suma) * (n / (suma - 1)) + (k / suma) * (m / (suma - 1)) + (m / suma) * (
            (m - 1) / (suma - 1)) * (3 / 4) + (m / suma) * (k / (suma - 1)) + (m / suma) * (n / (suma - 1)) * (1 / 2) + (
            n / suma) * (m / (suma - 1)) * (1 / 2) + (n / suma) * (k / (suma - 1))
print(p)
