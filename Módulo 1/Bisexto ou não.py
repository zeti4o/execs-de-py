from datetime import date
print('=' * 20)
ano = int(input('\n Digite um ano para analisar, digite 0 para analisar o ano atual: '))
if ano == 0:
	ano = date.today().year
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print(f' O ano {ano} é BISSEXTO\n')
else:
	print(f' O ano {ano} não é BISSEXTO\n')
print('=' * 20)
