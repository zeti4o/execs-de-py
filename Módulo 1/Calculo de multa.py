#80 - 90 = 10 * 7
print('=' * 20)
multa = int(input('\n A quantos KM/H você estava?: '))
if multa >= 80:
	mula = (80 - multa) * 7
	print(f' Xi você está lascado vai ter que pagar R${mula:.2f}\n')
else:
	print(' Parabéns continue assim você está dentro dos trilhos ou melhor da pista :)\n')
print('=' * 20)