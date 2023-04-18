from random import randint
cont = 0
while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 15)
    n = int(input('Digite um valor: '))

    print('-' * 30)
    computador = randint(0, 10)
    soma = n + computador
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if op == 'P' and soma % 2 == 0:
        cont += 1
        print('-' * 30)
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR')
        print('-' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif op == 'I' and soma % 2 != 0:
        cont += 1
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR')
            print('Você PERDEU!')
            break
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR')
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')



