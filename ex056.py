'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

contf = 0
contId = 0
soma = 0
hVelho = 0
nomeVelho = ' '

for i in range(1, 5):
    nome = str(input('Informe seu nome: '))
    sexo = str(input('Informe seu sexo: ')).upper()
    idade = int(input('Informe sua idade: '))

    soma += idade
    contId += 1
    if sexo in 'Mm' and i == 1:
        hVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > hVelho:
        hVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        contf += 1

media = soma / contId
print(f'A média de idade do grupo foi {media}')
print(f'O nome do homem mais velho foi {nomeVelho}')
print(f'A quantidade de mulheres menores de vinte anos foi {contf}')