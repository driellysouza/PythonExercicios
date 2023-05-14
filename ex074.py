from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
menor = numeros[0]
maior = numeros[0]
print('Os valores sorteados foram: ')
for n in numeros:
    print(f'{n} ', end='')
    # if n > maior:
    #     maior = n
    # if n < menor:
    #     menor = n
# print(f'\nO menor valor da lista é {menor}')
# print(f'O maior valor da lista é {maior}')

#resposta alternativa usando métodos
print(f'\nO menor valor da lista é {min(numeros)}')
print(f'O maior valor da lista é {max(numeros)}')
