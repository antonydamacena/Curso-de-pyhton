'''matriz = []
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
print(f'[| {matriz[6]} |] [| {matriz[7]} |] [| {matriz[8]} |]')''' 


matriz=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for c in range(0,3):
        matriz[i][c]=(int(input(f'Digite um valor para a posição [{i}, {c}]')))
print('-='*30)
for i in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]',end='')
    print()
    