from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print(f'Pensei no número {computador}')

if computador == jogador:
    print('PARABÉNS VOCÊ VENCEU!!')
else:
    print('VOCÊ PERDEU, TENTE NOVAMENTE!')
