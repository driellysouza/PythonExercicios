print('=' * 25)
print('   10 TERMOS DE UMA PA')
print('=' * 25)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{n} <<< ', end='')
        n += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')