from random import randint
from time import sleep
computador = randint(0 , 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi? ')
sleep(2)
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        acertou = True
print('VOCÊ ACERTOU!')
