from random import choice
print('=' * 20)
print('')
aluno_1 = str(input(' Digite o nome do primeiro aluno: '))
print('')
aluno_2 = str(input(' Digite o nome do segundo aluno: '))
print('')
aluno_3 = str(input(' Digite o nome do terceiro aluno: '))
print('')
aluno_4 = str(input(' Digite o nome do quarto aluno: '))
print('')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
print(f' O resultado foi: {choice(lista)}')
print('')
print('=' * 20)
