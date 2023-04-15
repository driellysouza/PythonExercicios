'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor: '))
op = 0
while op != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    op = int(input('>>>>>Qual é a sua opção? '))
    if op == 1:
        resultado = n1 + n2
        print(f'A soma de {n1} + {n2} é {resultado}')

    elif op == 2:
        resultado = n1 * n2
        print(f'A multiplicação de {n1} + {n2} é {resultado}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n1}')
    elif op == 4:
        n1 = float(input('Informe o 1º valor: '))
        n2 = float(input('Informe o 2º valor: '))
    elif op == 5:
        print('Finalizando>>>>>')
    else:
        print('Opção Inválida. Tente novamente!')
    print('=-='*10)
print('Fim do programa. Volte sempre!')
