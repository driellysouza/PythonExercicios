'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''

cont_h = mulher = maiores = 0
while True:
        print('-' * 30)
        print('CADASTRE UMA PESSOA')
        print('-' * 30)
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            cont_h += 1
        if sexo == 'F' and idade < 20:
            mulher += 1
        if idade > 18:
            maiores += 1
        op = ' '
        while op not in 'SN':
            op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if op == 'N':
            break

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {cont_h}')
print(f'Total de mulheres menores de 20 anos: {mulher}')
