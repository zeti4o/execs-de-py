from math import hypot
print('=' * 20)
print('')
cat_op = float(input (' Digite o cateto oposto: '))
cat_ad = float(input(' Digite o cateto adjacente: '))
hipor = hypot(cat_op, cat_ad)
print('')
print(f' A hipotenusa deu: {hipor:.2f}')
print('')
print('=' * 20)
