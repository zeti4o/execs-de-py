from random import randint
from time import sleep
pc = str(randint(0,5))
print('=' * 20)
print('\n Analisando números...\n')
sleep(3)
print(' Números analisados, com sucesso\n')
pessoa = str(input(' Digite um número de 0 a 5: ')).strip()
if pessoa == pc:
	print('\n Você tem um Q.i de gênio \n')
else:
	print('\n Você errou :( \n')
print('=' * 20)