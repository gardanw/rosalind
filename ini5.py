with open(r'rosalind_ini5.txt', 'r') as file, open('ini5_out.txt', 'w') as out:
    i = 1
    for line in file:
        if i % 2 == 0:
            out.write(line)
        i += 1
