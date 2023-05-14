times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atlético-MG',
         'Flamengo', 'Athletico-PR','Cruzeiro', 'Fortaleza', 'São Paulo',
         'Santos', 'Grêmio', 'Internacional', 'Bragantino', 'Bahia',
         'Vasco da Gama', 'Corinthians', 'Cuiabá', 'Goiás', 'Coritiba', 'América-MG')

print(f'Times do Brasileirão: ',times)
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-='*20)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-='*20)
print(f'Lista dos times em ordem alfabética:\n{sorted(times)}')
print('-='*20)
print(f'O time do Flamengo está na {times.index("Flamengo")+1}º posição')

