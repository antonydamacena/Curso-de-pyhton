numeros= []
pares = []
impares = []
while True:
    while True:
        try:
            numeros.append(int(input('Digite um número:')))
            break
        except ValueError:
            print('Valor ínválido! Digite apenas números!')
    while True:
        opc = input('Deseja continuar [S|N]:').upper().strip()
        if opc not in ['S','N']:
            print('Por favor, Digite apenas [S]Sim ou [N]Não!')
        else:
            break
    if opc == 'N':
        break
for i in numeros:
    if i %2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Você digitou os números {numeros}')
print('')
print('Os núemros pares são:')
print(pares)
print('Os numeros ímpares são:')
print(impares)