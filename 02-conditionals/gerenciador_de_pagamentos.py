from time import sleep
print('===== LOJA YASMIN ======')
preço = float(input('Preço da compra:  R$'))
sleep(1)
print('FORMAS DE PAGAMENTOS: \n [1] À vista dinheiro \n [2] À vista cartão \n [3] 2x no cartão \n [4] 3x no cartão')
sleep(1)
pagamento = int(input('Qual será a forma de pagamento?'))
sleep(2)
if pagamento == 1:
    total = preço - (preço * 10 / 100)
elif pagamento == 2:
    total = preço - (preço * 5 / 100)
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {} SEM JUROS!'.format(parcela))
elif pagamento == 4:
    total = preço + (preço * 20 / 100)
    totparce = int(input('Quantas parcelas?'))
    parcela = total / totparce
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(totparce, parcela))
print('Sua compra de R${} irá custar R${} no final.'.format(preço, total))

