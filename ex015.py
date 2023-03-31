km = float(input('Informe quantos quilometros rodados: '))
dias = int(input('Informe quantos dias alugados: '))
valorTotal = 0.15 * km + dias * 60
print('O valor total a ser pago é: R$ {:.2f}.'.format(valorTotal))