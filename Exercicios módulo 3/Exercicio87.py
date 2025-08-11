'''matriz = []
pares=soma=maior=0
for i in range(0,3):
    matriz.append(int(input(f'Digite um numero [0:{i}]: ')))
for i in range(0,3):
    matriz.append(int(input(f'Digite um numero [1:{i}]: ')))
for i in range(0,3):
    matriz.append(int(input(f'Digite um numero [2:{i}]: ')))
print('')

print('-='*30)
print(f'[| {matriz[0]} |] [| {matriz[1]} |] [| {matriz[2]} |]')
print(f'[| {matriz[3]} |] [| {matriz[4]} |] [| {matriz[5]} |]')
print(f'[| {matriz[6]} |] [| {matriz[7]} |] [| {matriz[8]} |]') 
print('-='*30)

couluna3=[matriz[2],matriz[5],matriz[8]]
linha2 = [matriz[3],matriz[4],matriz[5]]
for c in matriz:
    if c %2 == 0:
        pares +=c

for i in couluna3:
    soma += i
   
for x in linha2:
    if x == 0:
        maior= x
    else:
        if x >= maior:
            maior=x

print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da linha 2 é: {maior}')'''

matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=coluna3 = linha2=0

for i in range (0,3):
    for c in range(0,3):
        matriz[i][c]=(int(input(f'Digite um valor para a posição [{i}, {c}]')))
print('-='*30)
for i in range (0,3):
    for c in range(0,3):

        if i == 1:
            linha2 = matriz[i][c]
            if matriz[i][c] >= linha2:
                linha2= matriz[i][c]

        if c == 2:
            coluna3 += matriz[i][c]

        if matriz[i][c] %2 == 0:
            pares += matriz[i][c]

        print(f'[{matriz[i][c]:^5}]',end='')
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {linha2}')

# Soma
    #pares
        #De uma linha especifica
        #coluna especifica
        #todos
    #impares
    #primos
    #todos
#multiplicar