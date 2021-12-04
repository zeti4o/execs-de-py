print('=' * 20)
r1 = float(input(' Digite o primeiro segmento: '))
r2 = float(input(' Digite o segundo segmento: '))
r3 = float(input(' Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
	print('\n Os segmentos formam um triangulo!\n')
else:
	print('\n Os segmentos não forma um triangulo!\n')
print('=' * 20)