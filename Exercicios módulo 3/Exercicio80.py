numeros = []
for i in range(5):

    num= int(input('Digite um número: '))
    
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
    else:

        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                break
            pos +=1

print(numeros)