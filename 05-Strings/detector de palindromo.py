frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separar as palavras
junto = ''.join(palavras) #juntar as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]
    