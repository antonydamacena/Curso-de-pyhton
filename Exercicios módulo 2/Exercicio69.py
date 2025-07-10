sexo = opc ='' 
idade= p18 = homens =mulher20= tot =0
while True:

    print('-'*20,'Cadastrar uma pessoa','-'*20)

    #Verificação de sexo:
    sexo = (input('Digite o sexo (M|F): ')).upper().strip()
    if sexo  not in [ 'M', 'F']:
        while sexo not in [ 'M', 'F']:
            print( 'Por favor, insira um sexo válido [M] para masculino [F] para feminino')
            sexo = (input('Digite o sexo (M|F): ')).upper().strip()

    #verificação de idade:
    while True:
        try:
            idade = int(input('Digite a idade: '))
            if idade < 0 or idade > 150: 
                print('Por favor, insira uma idade válida:')
                continue
            break
        except ValueError:
            print('Por favor, insira uma idade válida(Apenas números):')
             

    #Analize de dados:
    tot +=1
    if idade > 18:
        p18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and  idade < 20:
        mulher20 += 1

    #Continuar ou não
    opc = input('Deseja continuar (S|N)? ').upper().strip()
    while opc not in ['S', 'N']:
        print('Por favor, insira uma opção válida [S]Sim [N]Não')
        opc = input('Deseja continuar (S|N)? ').upper().strip()

    if opc == 'N':
        break

    #Finalização
print(f'Ao total temos {tot} pessoa(s) cadastradas.\n Dentre ela(s) temos {mulher20} mulher(es) abaixo de 20 anos\n {p18} pessoa(s) acima de 18 anos \n E {homens} homen(s).')
    