soma = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        soma += n
print(f'O valor total da soma dos valores pares é {soma}.')

