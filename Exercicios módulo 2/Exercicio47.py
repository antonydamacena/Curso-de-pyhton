n = int(input('Digite um numero e eu direi todos os numeros impares ou pares de 1 até chegar ao números escolhido!  '))
v = int (input('''
               Você quer saber
               [1]Os números ímpares
               ou
               [2]Os números pares
                '''))

if v==2:
    for numeros_pares in range(2,n+1,2):
        print(numeros_pares)
else:
    for numeros_impares in range (1,n+1,2):
        print(numeros_impares)


        '''or'''


'''for par in range(1,10+1):
    
        if par%2 == 0 :
            
            print(par)

'''