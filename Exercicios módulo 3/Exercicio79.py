num =[]

while True:
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except ValueError:
            print('Valor invalido! Digte apenas número inteiros!')

    if numero not in num:
        print('Valor adicionado com sucesso!')
        num.append(numero)
    else:
        print(f'O numero {numero} já está na lista, Não irei adicionar')
        

    while True:
        opc= input('Quer continuar [S|N]? ').upper().strip() 
        if opc in ['S', 'N']:
            break
      
        else:
            print('Por favor digite apenas [S]Sim ou [N]Não')
            continue

    if opc == 'N':
        break   
num.sort()
print(num)