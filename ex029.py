velocidade = float(input('Informe a velocidade: '))
multa = (velocidade - 80) * 7.0

if velocidade > 80:
    print(f'Velocidade a cima do limite permitido.')
    print(f'Você deve pagar {multa} reais de multa')
else:
    print('Você está dentro da velocidade permitida.')