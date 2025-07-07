
media_idade = 0
mulheres_menores = 0  #As variáveis
mulheres_velhas = 0
homem =  0
nome_homem = ''
#--------------------------------------------------------------------

for p in range (1,5):
    print('=-='*5, f'{p}º pessoa', '=-='*5)
    nome = str(input(f'Nome: ')).capitalize().strip()  #laços
    idade= int(input(f'Idade: '))
    sexo = str (input(f'Sexo [M|F]: ')).upper()

#--------------------------------------------------------------------

    media_idade += idade #Somar todas as idades para obter a média

#--------------------------------------------------------------------

    if sexo == 'F' and idade < 20:
        mulheres_menores += 1     #Descobrir quantas mulheres são maiores e menores de 20
    elif sexo == 'F' and idade >=20:
        mulheres_velhas += 1

#--------------------------------------------------------------------

    if sexo == 'M' and p==1:
        homem = idade      #idade do homem mais velho
        nome_homem = nome

#--------------------------------------------------------------------

    if sexo == 'M' and idade > homem:
        homem = idade          # nome do homem mais velho
        nome_homem = nome

#--------------------------------------------------------------------

print(f' A média das idade é {media_idade/4:.1f}')
print (f' Existem {mulheres_menores} Mulheres menores que 20 anos e {mulheres_velhas} Mulheres que possuem mais exatamente igual a 20 anos!  ')
print(f' O Homem mais velho se chama {nome_homem} e tem {homem} anos!')
