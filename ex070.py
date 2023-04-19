'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

tot = totmil =  menor = cont = 0
while True:
    print('-' * 30)
    print('SUPER ATACADO')
    print('-' * 30)
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor: '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi {tot:.2f}')
print(f'Quantidade de produtos que custam mais de 1.000: {totmil}')
print(f'O produto mais barato foi: {barato} custando {menor}')


