cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    número = int(input('Qual número de 0 a 20,você quer que eu escreva por extenso? '))
    if 0 <= número <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[número]}')
    