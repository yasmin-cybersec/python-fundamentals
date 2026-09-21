frase = str(input('Digite uma frase:  ')).upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))