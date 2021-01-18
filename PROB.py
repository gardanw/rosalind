import math

with open(r'rosalind_prob.txt', 'r') as file:
    seq = file.readline()[:-1]
    array = file.readline()[:-1].split(' ')

for i in range(len(array)):
    array[i] = float(array[i])

# seq = 'ACGATACAA'
# array = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]
a = seq.count('A')
t = seq.count('T')
g = seq.count('G')
c = seq.count('C')
out_array = []
for x in array:
    at = (1 - x) ** (a + t)
    gc = x ** (g + c)
    out_array.append(round(math.log10(at * gc / 2 ** (len(seq))), 3))

for i in range(len(out_array)):
    out_array[i] = str(out_array[i])

out_array = ' '.join(out_array)
print(out_array)
