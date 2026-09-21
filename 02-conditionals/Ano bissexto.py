
ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))