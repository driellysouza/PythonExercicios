numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quize', 'dezeseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {(numeros [n])}')

# resposta do professor:
# while True:
#     núm = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= núm <= 20:
#         break
#       print('Tente novamente. ', end='')
# print(f'Você digitou o número {(numeros [n])}')