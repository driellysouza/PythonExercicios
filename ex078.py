valores = []
# maior =[]
# menor = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {v}: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

#SOLUÇAÕ ALTERNATIVA
# for cont, v in enumerate(valores):
#     if v == max(valores):
#         maior.append(cont)
#     if v == min(valores):
#         menor.append(cont)

print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')