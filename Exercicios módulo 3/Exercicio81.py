numeros =[]

while True:
    while True:
        try:

            numeros.append(int(input('Digite um número:')))
            break

        except ValueError:
            print('Valor inválido! Digite apenas números (123...)')

            
    while True:
        opc = input('Quer continuar [S|N]').upper().strip()
        if opc in ['S','N']:
            break
        else: 
            print('Valor inválido! Digite apenas [S]Sim ou [N]Não:')
            continue
    if opc == 'N':
        break
print('')
numeros.sort(reverse=True)
print(f'No total foram digitados um total de {len(numeros)} numero(s)')
print(f'Os números de forma decrescente fica:')

print(numeros)
if 5 in numeros:
    print('O numero 5 foi digitado!')
else:
    print('O numero 5 não foi digitado!')