lista = []
lista_pares = []
lista_impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    res = str(input('Quer contniuar? [S/N]')).strip()
    if res in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de ímpares é: {lista_impares}')
