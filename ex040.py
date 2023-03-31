n1 = float(input('Digite a  primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média foi {media} \nREPROVADO!')
elif media <= 6.9:
    print(f'Sua média foi {media} \nRECUPERAÇÃO!')
else:
    print(f'Sua média foi {media} \n APROVADO!')

