num = cont = soma =0

while True:
    num = int(input('Digite um valor (999 para parar):'))
    if num == 999:
        break 
    soma+= num
    cont+=1 
print(f' Foram digitados {cont} numeros e samoa entre eles é {soma}')
