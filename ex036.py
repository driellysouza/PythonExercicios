casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa} em {anos} anos')
print(f'a prestação será de R${prestação}')

if prestação > minimo:
    print('Empréstimo negado.')
else:
    print('Emprestimo  concedido!')