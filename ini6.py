def ini6(s):
    list_w = s.split()
    dic = {}
    for w in list_w:
        if w not in dic:
            dic[w] = 1
        else:
            dic[w] += 1
    return dic


with open(r'rosalind_ini6.txt', 'r') as file, open('ini6_out.txt', 'w') as out:
    s = file.readline()
    dic = ini6(s)
    for key in dic:
        out.write(key + ' ' + str(dic[key]) + '\n')
