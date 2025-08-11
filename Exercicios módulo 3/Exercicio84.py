pessoas = []
dados= []
maiorp =menorp =0
maior_name =[]
menor_name =[]
total =0
while True:
    dados.append(str(input('Nome: ')).capitalize().strip())
    while True:
        try:
            dados.append(float(input('Peso: ')))
            break
        except ValueError:
            print('Digite apenas números:')
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    opc = input('Quer continuar? [S|N]').upper().strip()
    if opc == 'N':
        break
cont=0
for gnt in pessoas:
    cont += 1
    if cont == 1:
        maiorp =(gnt[1])
        maior_name.append(gnt[0])
        menorp=(gnt[1])
        menor_name.append(gnt[0])
    else:
        if gnt[1] > maiorp:
            
            maior_name.clear()
            maiorp= (gnt[1])
            maior_name.append(gnt[0])
        elif gnt[1] < menorp:
            
            menor_name.clear()
            menorp=(gnt[1])
            menor_name.append(gnt[0])
        elif gnt[1] == maiorp:
            maior_name.append(gnt[0])
        elif gnt [1] == menorp:
            menor_name.append(gnt[0])

print('')
print('-='*30) 
print(f'No total foram registrados {len(pessoas)} pessoas ')
print(f'O maior peso foi de {maiorp} kg, esse peso foi de {maior_name}')
print(f'O menor peso foi de {menorp} kg, esse peso foi de {menor_name}')
