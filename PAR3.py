with open("rosalind_par3.txt", "r") as file:
    n = int(file.readline())
    data = list(map(int, file.readline().split()))

out = [i for i in data[1:] if i < data[0]] + [i for i in data if i == data[0]] + [i for i in data[1:] if i > data[0]]

print(*out)
