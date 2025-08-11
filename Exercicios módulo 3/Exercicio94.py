grupo= []
mulheres=[]
pessoas={}
media=0
while True:
    pessoas['nome']= input('Nome: ').capitalize().strip()

    while True:
        try:
            pessoas['idade']= int(input('Idade: '))
            break
        except ValueError:
                print('Digite um valor válido!')
    while True:
        pessoas['sexo']= input('Sexo (M|F): ').upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO KRITIKO ALERTA GAY ⚠ ⚠ ☢ Apenas [M|F]')
            print('')
    if pessoas['sexo']== 'F':
        mulheres.append(pessoas['nome'])
    while True:
        opc = input('Deseja continuar?').upper().strip()[0]
        if opc in 'SN':
            break
        else:
            print('ERRO || Apenas [S]Sim ou [N]Não')
    grupo.append(pessoas.copy())
    media += pessoas['idade']
    pessoas.clear()
    if opc == 'N':
        break

print('-='*30)
media = media/ len(grupo)
print(f'- Foram cadastradas {len(grupo)} pessoas')
print(f'- A média de idade é {media}')

print('- As mulheres cadastradas foram:')
for c in range(0,(len(mulheres))):
  
    print(mulheres[c],end=', ')
 
print('')
print('- A lista de pessoas que estão acima da média são:')
for i,p in enumerate(grupo):
    if p['idade'] > media:
        print(f'=> {p}')
