número = int(input('Digite um número: '))
total = 0
for c in range (1, número + 1 ):
    if número % c == 0:
        print('\033[33m')
        total += 1
    else:
        print('\033[31m')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível por {} vezes...'.format(número, total))
if total == 2:
    print('O número {} é um número PRIMO!'.format(número))
else:
    print('Ele NÃO é primo!')
