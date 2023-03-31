valor = float(input('Quanto dinheiro você tem na carteira? '))

dolar= valor / 5.02

print('Com R${} você pode comprar US$ {:.2f}'.format(valor, dolar))