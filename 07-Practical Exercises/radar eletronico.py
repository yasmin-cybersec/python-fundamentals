from time import sleep
v = int(input('Qual é a velocidade atual do carro?'))
print('PROCESSANDO...')
sleep(3)
if v >= 80:
    multa = (v - 80) *7
    print('MULTADO por excesso de velocidade!!! \n Você excedeu o limite permitido de 80km/h! \n Você deve pagar uma multa de R${}'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
print('Tenha um bom dia! Dirija com segurança!')