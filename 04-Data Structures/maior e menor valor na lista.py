valores = list()
for cont in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-='*15)
print(f'Você digitou os valores {valores}')
for pos, v in enumerate(valores):
    if v == max(valores):
      print(f'O maior valor digitado foi {max(valores)} na posição {pos}')

    if v == min(valores):
      print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))+1}')