d = float(input('Qual a distância da sua viagem em km?     '))
if d <= 200:
    p1 = d * 0.5
    print('Você está prestes a começar uma viagem de {} km... \n E o preço da sua passagem será de R${:.2f}'.format(d, p1))

else:
    p2 = d * 0.45
    print('Você está prestes a começar uma viagem de {} km... \n E o preço da sua passagem será de R${:.2f}'.format(d, p2))
    
