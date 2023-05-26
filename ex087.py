valores =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end='')
        if valores[l][c] % 2 == 0:
            soma_par += valores[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_par}')
for l in range(0, 3):
    soma_col += valores[l][2]
print(f'A soma doa valores da terceira coluna é {soma_col}.')
for c in range(0, 3):
    if c == 0:
        maior = valores[1][c]
    elif valores[1][c] > maior:
        maior = valores[1][c]
print(f'O maior valor da segunda linha é {maior}.')

