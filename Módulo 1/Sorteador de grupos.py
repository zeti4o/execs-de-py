from random import choice
print('=' * 20)
print('\n Primeiro grupo:\n')
vl1 = str(input(' Digite o nome do primeiro aluno: '))
vl2 = str(input(' Digite o nome do segundo aluno: '))
vl3 = str(input(' Digite o nome do terceiro aluno: '))
print('\n Segundo grupo:\n')
vl4 = str(input(' Digite o nome primeiro aluno: '))
vl5 = str(input(' Digite o nome segundo aluno: '))
vl6 = str(input(' Digite o nome terceiro aluno: '))
print('\n Terceiro grupo:\n')
vl7 = str(input(' Digite o nome do primeiro aluno: '))
vl8 = str(input(' Digite o  nome do segundo aluno: '))
vl9 = str(input(' Digite o nome do terceiro aluno: '))
print('\n Quarto grupo:\n')
vl10 = str(input(' Digite o nome do primeiro aluno: '))
vl11 = str(input(' Digite o nome do segundo aluno: '))
vl12 = str(input(' Digite o nome do terceiro aluno: '))
lista1 = [vl1,vl2,vl3]
lista2 = [vl4,vl5,vl6]
lista3 = [vl7,vl8,vl9]
lista4 = [vl10,vl11,vl12]
print(f'z\n O grupo escolhido foi: {choice([lista1,lista2,lista3,lista4])}\n')
print('=' * 20)