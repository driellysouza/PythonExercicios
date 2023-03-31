n = int(input('Digite um número: '))
c = 1
print('-=' * 12)

for i in range(1, 11):
    print(f'{n} x {c} = {n * c}')
    c += 1
print('-=' * 12)