preco = float(input('Preço total das compras: '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque\n''[ 2 ] à vista cartâo\n''[ 3 ] 2x no cartão\n''[ 4 ] 3x ou mais no cartão')
op = int(input('Qual é a opção? '))

if op == 1:
    total = preco - (preco * 10 / 100)
elif op == 2:
    total = preco - (preco * 5 / 100)
elif op == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de {parcela} SEM JUROS.')
elif op == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de {parcela} COM JUROS.')
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE')


print(f'Sua compra de R${preco} vai custar R${total} no final.')