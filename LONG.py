def common_part(s1, s2):
    out = []
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if s2 in s1:
        print('same')
        return s1
    for i in range(len(s1)):
        if s1[i:len(s2) + i] == s2[:len(s1[i:len(s2) + i])]:
            out.append(s1 + s2[len(s1[i:len(s2) + i]):])
            break
    else:
        out.append(s1 + s2)
    for i in range(len(s2)):
        if s1[:len(s2) - i] == s2[i:]:
            out.append(s2 + s1[len(s2[i:]):])
            break
    else:
        out.append(s2 + s1)
    return min(out, key=len)


with open(r'rosalind_long.txt', 'r') as file:
    list_seq = []
    seq = ''
    for line in file:
        if line[0] == '>':
            list_seq.append(seq)
        else:
            list_seq[-1] += line[:-1]

shorted = max(list_seq, key=len) * 2

for i in range(len(list_seq)):
    for j in range(i + 1, len(list_seq)):
        temp = common_part(list_seq[i], list_seq[j])
        if len(temp) < len(shorted):
            shorted = temp

while len(list_seq) != 0:
    new_comm_part = []
    for seq in list_seq:
        if seq in shorted:
            list_seq.remove(seq)
    for seq in list_seq:
        new_comm_part.append(common_part(shorted, seq))
    if len(list_seq) == 0:
        break
    shorted = min(new_comm_part, key=len)

print(shorted)
