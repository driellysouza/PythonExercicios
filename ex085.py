# valores = []
# for c in range(0, 7):
#     valores.append(int(input(f'Digite o {c + 1}º valor: ')))
# print(f'Os valores pares digitados foram: ', end='')
# for v in valores:
#     if v % 2 == 0:
#         print(f'{v}', end=' ')
# print()
# print(f'Os valores ímpares digitados foram: ', end='')
# for v in valores:
#     if v % 2 != 0:
#         print(f'{v}', end=' ')
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
