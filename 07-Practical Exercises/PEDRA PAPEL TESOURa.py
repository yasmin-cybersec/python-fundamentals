from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(1,3)
print('Suas opções: \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA')
sleep(1)
jogada = int(input('Qual sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-=' * 7)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-=-=' * 7)
if computador == 1:
   if jogada == 1:
      print('EMPATE!')
   elif jogada == 2:
      print('JOGADOR VENCEU!')
   elif jogada == 3:
      print('COMPUTADOR GANHA!')
elif computador == 2:
    if jogada == 1:
       print('COMPUTADOR VENCEU!')
    elif jogada == 2:
       print('EMPATE!')
    elif jogada == 3:
          print('JOGADOR VENCEU!')
elif computador == 3:
   if jogada == 1:
      print('JOGADOR VENCEU!')
   elif jogada == 2:
      print('COMPUTADOR VENCE!')
   elif jogada == 3:
      print('EMPATE!')
          

#elif computador == 2:


#elif computador == 3:

   