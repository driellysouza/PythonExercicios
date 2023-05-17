'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''
c50 = c20 = c10 = c1 = 0
while True:
    print('=' * 20)
    print(f'{:^20 'BANCO ITAÚ'}')
    print('=' * 20)
    valor = float(input('Que valor você quer sacar? R$'))


    '''print(f'Total de {} cédulas de R$50')
    print(f'Total de {} cédulas de R$20')
    print(f'Total de {} cédulas de R$10')
    print(f'Total de {} cédulas de R$1')
    print('=' * 20)
    print('Volte sempre ao BANCO ITAÚ! Tenha um Bom Dia!')'''