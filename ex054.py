'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date


atual = date.today().year
cont = 0
cont2 = 0

for i in range (1, 8):
    ano = int(input(f'Digite o {i}º ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        cont += 1
    else:
        cont2 += 1
print(f'O número de pessoas MAIORES de idade é {cont}')
print(f'O número de pessoas MENORES de idade é {cont2}')
