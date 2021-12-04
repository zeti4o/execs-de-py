from time import sleep
print('=' * 40)
numero = int(input('\n Digite um número inteiro (de 1 a 9999): '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('\n Analisando o valor...\n')
sleep(3)
print(f'\n Unidade: {unidade:^6}')
print(f'\n Dezena: {dezena:^5}')
print(f'\n Centena {centena:^5}')
print(f'\n Milhar: {milhar:^5}\n')
print('=' * 40)
