salario = float(input('Informe seu salário: '))

if salario <= 1250:
    aumento = salario * 1.15

else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario} passa a ganhar RS{aumento} agora.')