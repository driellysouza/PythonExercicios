'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu sexo [M]/[F]: ')).strip().upper()[0]
#while sexo != 'M' and sexo != 'F':
while sexo not in 'MmFf':
    print('[ERRO]')
    sexo = str(input('Digite seu sexo [M]/[F]: ')).upper()
print(f'O sexo informado foi {sexo}')