larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parde tem a dimensão de {}x{} e sua area é de {}m2'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede, vc precisara de {} litros de tinta.'.format(tinta))