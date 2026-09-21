primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo= primeiro + (10 -1) * razão #Décimo termo
for c in range (primeiro, décimo, razão):
    print('{} '.format(c), end=' -> ')
print('FIM!')