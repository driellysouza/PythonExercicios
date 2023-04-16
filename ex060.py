'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input('Digite um número: '))
cont = n
fat = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else f' =  {fat}', end='')
    fat *= cont
    cont -= 1
print(f'\nO fatorial de {n} é {fat}')
