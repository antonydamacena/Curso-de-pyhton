numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(2)]
print(numeros)
opcao = 0
while opcao != 5:
    opcao = int(input ('''O que você deseja fazer com estes números?
                       [1]Somar
                       [2]Multiplicar
                       [3]Novos números
                       [4]Maior
                       [5]Fechar programa
                       Digite sua resposta: '''))
    if opcao == 1 :
        soma= numeros[0]+ numeros[1]
        print(f'A soma de {numeros[0]} + {numeros[1]} = {soma}\n')
    elif opcao == 2:
        multiplicar = numeros [0] * numeros [1]
        print(f'A multiplicação de {numeros[0]} x {numeros[1]}= {multiplicar}\n')
    elif opcao == 3:
        numeros = [int(input(f'Digite o {i+1} novo número:'))for i in range(2)]
        print(numeros,'\n')
    elif opcao == 4:
        if numeros[0] > numeros[1]:
            print(f'O número {numeros[0]} é maior!')
        elif numeros[0]< numeros[1]:
            print(f'O número {numeros[1]} é maior!')
        else:
            print('Os números são iguais')
    elif opcao == 5:
            print()
    else:
        print('Opção inválida, tente novamente!')
    print('=-='*30)
print('Programa fechado!')



                       
