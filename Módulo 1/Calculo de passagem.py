print('=' * 20)
pessoa = float(input('\n Em km quantos quilometros foi a viagem: '))
preco = pessoa * 0.50 if pessoa <= 200 else pessoa * 0.45
print(f' Você vai pagar R${preco:.2f}\n')
print('=' * 20)