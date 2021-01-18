import requests

list_id = []
with open(r'rosalind_mprt.txt', 'r') as file:
    for line in file:
        if line != '' and line != '\n':
            list_id.append(line[:-1])

list_prot = {}
for p in list_id:
    page = requests.get(f'https://www.uniprot.org/uniprot/{p}.fasta')
    seq = ''.join([part for part in page.text.split('\n') if part != '' and part[0] != '>'])
    list_prot[p] = {'seq': seq, 'N-g': []}

for s in list_prot:
    for i in range(0, len(list_prot[s]['seq'])-2):
        if list_prot[s]['seq'][i] == 'N' and 'P' not in list_prot[s]['seq'][i + 1] + list_prot[s]['seq'][i + 3] and \
                list_prot[s]['seq'][i + 2] in 'ST':
            list_prot[s]['N-g'].append(i + 1)

with open('mprt_out.txt', 'w') as file:
    for s in list_prot:
        if len(list_prot[s]['N-g']) != 0:
            file.write(s + '\n')
            for i in list_prot[s]['N-g']:
                if i != list_prot[s]['N-g'][-1]:
                    file.write(str(i) + ' ')
                else:
                    file.write(str(i))
            file.write('\n')
