from random import randint
num = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10) )
print(f'Os valores sorteados foram:')
for n in num:
    print(f'{n}', end=' ')