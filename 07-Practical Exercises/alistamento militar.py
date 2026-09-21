ano = int(input('Digite sua data de nascimento: '))
idade = 2026 - ano
print('Quem nasceu no ano de {}, tem {} anos em 2026...'.format(ano, idade))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    anos2 = 18 - idade
    anos3 = (18 - idade) + ano
    print('Ainda faltam {} anos para o seu alistamento...'.format(anos2))
    print('Seu alistamento será em {}.'.format(anos3))
elif idade > 18:
    anos4 = idade - 18
    print('Voce já deveria ter se alistado há {} anos!'.format(anos4))