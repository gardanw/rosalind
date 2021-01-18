n = 97
k = 8
out = 1
for i in range(k):
    out *= n-i

print(out%1000000)
