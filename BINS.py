def binary_serch(lista, number):
    mini = 0
    maxi = len(lista)
    while mini <= maxi:
        half = mini + (maxi - mini) // 2
        if lista[half] == number:
            return half + 1
        elif number < lista[half]:
            maxi = half - 1
        else:
            mini = half + 1
    return -1


with open('rosalind_bins.txt', 'r') as file:
    lines = file.readlines()
array = list(map(int, lines[2].strip('\n').split(' ')))
number_list = list(map(int, lines[3].strip('\n').split(' ')))

out = [str(binary_serch(array, n)) for n in number_list]

print(' '.join(out))
