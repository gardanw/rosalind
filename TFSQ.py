with open('rosalind_tfsq.txt', 'r') as fastaq, open('rosalind_tfsq_out.txt', 'w') as fasta:
    for line in fastaq:
        if line[0] == '@':
            fasta.write(f'>{line[1:]}')
        else:
            fasta.write(line)
            fastaq.readline()
            fastaq.readline()