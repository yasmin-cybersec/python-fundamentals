#COM 15% DE  DESCONTO 
# #salário = float(input('Qual é o salário do funcionário?'))
#resposta = salário + (salário*15 / 100)
#print('Um funcionário que ganhava R${} \n Com 15% de aumento, passará a receber R${:.2f}'.format(salário, resposta))


#DESCONTO VARIÁVEL
salário = float(input('Qual o salário do colaborador?'))
porcentagem = (int(input('Qual a porcentagem de aumento?')))
resposta = salário + (salário*porcentagem / 100)
print('Um fincionário que ganhava R${} \n Com {}% de aumento passará a ganhar R${:.2f}'.format(salário, porcentagem, resposta))