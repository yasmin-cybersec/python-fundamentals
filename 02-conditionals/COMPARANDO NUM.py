primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
if primeiro > segundo:
    print('O PRIMEIRO número é maior!')
elif primeiro < segundo:
    print('O SEGUNDO número é maior!')
elif primeiro == segundo or segundo == primeiro:
    print('Os dois valores são IGUAIS!')