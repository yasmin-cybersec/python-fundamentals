n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota?  '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua nota está ótima!')
else:
    print('Você está abaixo da média!')