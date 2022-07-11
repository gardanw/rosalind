def heap(a):
    if 2 * a + 2 <= n - 1 and data[2 * a + 2] > data[a]:
        data[2 * a + 2], data[a] = data[a], data[2 * a + 2]
        heap(2 * a + 2)
    if 2 * a + 1 <= n - 1 and data[2 * a + 1] > data[a]:
        data[2 * a + 1], data[a] = data[a], data[2 * a + 1]
        heap(2 * a + 1)


with open("rosalind_hea.txt", "r") as file:
    n = int(file.readline())
    data = list(map(int, file.readline().split()))


for i in range(n, 0, -1):
    heap(i - 1)

print(" ".join(map(str, data)))
