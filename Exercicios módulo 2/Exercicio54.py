from datetime import date
maior = 0
menor = 0
data = date.today()

for i in range (1,8):
    ano = int(input(f'Digite o ano de nascimento da {i}º pessoa: '))
    if ano > (data.year) or ano < 1900:
        print('insira uma data valida')
    else:
        if ((data.year)-ano) >= 21:
            maior += 1
        else:
            menor += 1
print(f'No total foram {maior} maior(es) de idade e {menor} menor(es) de idade!')
