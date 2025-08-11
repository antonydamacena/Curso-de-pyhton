numeros= [[],[]]
for i in range (7):
    while True:
        try:
            dado= int(input('Digite um numero inteiro: '))
            break
        except ValueError:
            print('Valor inválido! Digite um número')
    if dado % 2 ==0:
        numeros[0].append(dado)
    else:
        numeros[1].append(dado)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares fora {numeros[0]}')
print(f'Os números ímpares foram {numeros[1]}')