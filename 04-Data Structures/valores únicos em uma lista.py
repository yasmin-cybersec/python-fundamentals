while True:
    n = int(input('Digite um valor: '))

    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!')

    r = input('Quer continuar? [S/N] ').upper()

    if r == 'N':
        break
    elif r == 'S':
        continue
    else:
        print('Resposta inválida!')