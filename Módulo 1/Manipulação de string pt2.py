print('=' * 20)
print('')
nome = str(input(' Qual o seu nome: ')).strip()
separa = nome.split()
'''print('\n O seu primeiro nome tem {} letras'.format(nome.find(' ')))'''
print(f' O seu primeiro nome é: {separa[0]} e ele tem {len(separa[0])} letras')
print(' O seu nome tem: {} letras'.format((len(nome)) - nome.count(' ')))
print(f' Seu nome em maiúscula : {nome.upper():^20}')
print(f' Seu nome em minúsculas: {nome.lower():^20}\n')
print('=' *20)
