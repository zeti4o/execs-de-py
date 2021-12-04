print('=' * 30)
vl1 = int(input('\n Digite o primeiro valor: '))
vl2 = int(input('\n Digite o segundo valor: '))
vl3 = int(input('\n Digite o terceiro valor: '))
menor = vl1
#\/ para definir o menor \/
if vl2 < vl3 and vl2 < vl1:
	menor = vl2
if vl3 < vl2 and vl3 < vl1:
	menor = vl3
maior = vl3
#\/ para definir o maior \/
if vl2 > vl3 and vl2 > vl1:
	maior = vl2
if vl3 > vl2 and vl3 > vl1:
	maior = vl3
print(f'\n O menor valor digitado é: {menor}\n O maior valor digitado é: {maior}\n')
print('=' * 30)