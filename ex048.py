soma = 0
c = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma += n
        c += 1
print(f'A soma de todos os {c} valores solicitados é {soma}')
print('Fim')
