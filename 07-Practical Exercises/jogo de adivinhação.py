from random import randint
from time import sleep
computador = randint (0, 5) #Faz o computador pensar! 
print('=--=' *10)
print('Vou pensar em um número entre 0 a 5.Tente adivinhar!')
print('=--=' *10)
jogador = int(input('Em que número pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Pensei no número {}! Tente outra vez...'.format(computador))