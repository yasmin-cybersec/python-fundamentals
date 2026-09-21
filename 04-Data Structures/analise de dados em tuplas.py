núm = (int(input('Digite um número:')),
int(input('Digite outro número:')),
 int(input('Digite mais um número:')),
int(input('Digite o último número:')))

print(f'Você digitou os valores: {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
print(f'O número 3 foi digitado na posição {núm.index(3)+1}')