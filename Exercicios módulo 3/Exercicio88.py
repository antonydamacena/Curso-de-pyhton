from random import randint
from time import sleep
numeros =[]
dado=[]
sort=0
qnt= int(input('Digite quantos números quer que eu sorteie: '))


for y in range(0,qnt):

    while len(dado) < 6:
        sort= randint(0,60)
        
        if sort not in (dado):
            dado.append(sort)


    numeros.append(dado[:])
    dado.clear()
        
for c in range(0,len(numeros)):
    print(f'Jogo{c+1}: {numeros[c]}')
    sleep(0.5)