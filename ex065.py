
cont = soma = maior = menor = media = 0
res = 'S'
while res == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    res = str(input('Quer continuar? [S/N]')).upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')

