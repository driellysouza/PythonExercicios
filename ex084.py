pessoas = []
dados = []
totmaior = totmenor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        totmenor = totmaior = dados[1]
    else:
        if dados[1] > totmaior:
            totmaior = dados[1]
        if dados[1] < totmenor:
            totmenor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N]')).strip()
    if res in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {totmaior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == totmaior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {totmenor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == totmenor:
        print(f'{p[0]} ', end='')