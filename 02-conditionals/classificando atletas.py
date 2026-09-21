from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos...'.format(idade))
if idade <= 9:
    print('E está na categoria: MIRIM!')
elif idade > 9 and idade <= 14:         
    print('E está na categoria: INFANTIL!')
elif idade > 14 and idade <= 19:
    print('E está na categoria: JUNIOR!')
elif idade > 19 and idade <= 25:
    print('E está na categoria: SÊNIOR!')
else:
    print('E está na categoria: MASTER!')