while True:
    print('-' * 35)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        print('PROGRAMA TABUADA ENNCERRADO. Volte sempre!')
        break
    for i in range(1, 10):
        print(f'{n} x {i} = {n * i}')
