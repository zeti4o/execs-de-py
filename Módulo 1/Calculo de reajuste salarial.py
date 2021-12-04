print('=' * 20)
salario = float(input(' Digite o valor do seu salário: '))
if salario <= 1250.00:
	aumento = salario + (salario * 15 / 100 )
else:
	aumento = salario + (salario * 10 / 100)
print(' O seu novo salário será de: R${:.2f}\n'.format(aumento))
print('=' * 20)