valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionnar...')
    res = str(input(f'Quer continuar? [S/N] ')).upper().strip()
    if res == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Os valores digitados foram: {valores}')