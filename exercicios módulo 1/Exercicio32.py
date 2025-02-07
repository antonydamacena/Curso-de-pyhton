from datetime import date
ano= int(input('Digite um ano para saber se ele é ou não bissexto?.Digite 0 para saber o ano atual!  '))
if ano == 0:
    ano= date.today().year
if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    print(f'O ano de {ano} é um ano bissexto!')
else:
    print(f' O ano de {ano} não é bissexto!')