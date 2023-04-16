print('=' * 25)
print('   10 TERMOS DE UMA PA')
print('=' * 25)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{n} <<< ', end='')
    n += r
    cont += 1
print('FIM')