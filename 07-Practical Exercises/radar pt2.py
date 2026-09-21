from time import sleep
v = int(input('Qual a velocidade atual de um carro?'))
print('PROCESSANDO...')
sleep(3)
multa= (v - 80) * 7
if v >=80:
    print('Você foi multado! A multa vai custar R${}...'.format(multa))
else:
    print('Você está no limite de velocidade!')