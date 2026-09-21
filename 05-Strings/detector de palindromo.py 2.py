frase = str(input('Digite uma palavra:  ')).upper().strip()
palavras = frase.split() #Separa as palavras
junto = ''.join(palavras) #junta as palavras '' -> isso significa sem espaço
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('A frase, {}, é um PALÍNDROMO!'.format(frase))
else:
    print('A frase, {}, NÃO é um palíndromo!'.format(frase))