from time import sleep
p = int(input('Primeiro valor:   '))
s = int(input('Segundo valor:    '))
t = int(input('Terceiro valor:   '))
print('PROCESSANDO...')
sleep(3)
#VERIFICANDO QUEM É MENOR=

if p<s and p<t:
    menor = p
if s<p and s<t:
    menor = s
if t<p and t<s:
    menor = t
print('O menor valor digitado foi {}'.format(menor))

if p>s and p>t:
    maior = p
if s>p and s>t:
    maior = s 
if t>p and t>s:
    maior = t

print('O maior valor que foi digitado foi {}'.format(maior))


