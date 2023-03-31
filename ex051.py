print('=' * 25)
print('   10 TERMOS DE UMA PA')
print('=' * 25)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r

for i in range(n, decimo + r, r):
    print(i, ' -= ', end=' ')
print('ACABOU')
