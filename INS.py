with open('rosalind_ins.txt', 'r') as file:
    n = int(file.readline().strip())
    number_list = list(map(int, file.readline().strip().split(' ')))

swap = 0
print(number_list)
for i in range(1, n):
    k = i
    while k > 0 and number_list[k] < number_list[k - 1]:
        number_list[k], number_list[k - 1] = number_list[k - 1], number_list[k]
        swap += 1
        k -= 1

print(swap)
