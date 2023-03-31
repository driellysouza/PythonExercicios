km = float(input('Qual a distância da sua viagem: '))

print(f'Você está prestes a começar um viagem de {km}km.')
if km <= 200:
    preco = 0.50 * km
else:
    preco = 0.45 * km
print(f'E o preço da sua passagem será de R${preco}.')
