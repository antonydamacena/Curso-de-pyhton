num=[]
posiçãomax= []
posiçãomin= []
maior =menor =0
for i in range (0,5):
    while True:
        try:
            num.append(int(input(f"Digite o número inteiro da posição {i}: ")))
            break
        except ValueError:
            print('Digite apenas números inteiros (123...)')
for pos, c in enumerate(num):

    if pos == 0:
        maior=menor= c
        posiçãomax.append(pos)
        posiçãomin.append(pos)
        
    if pos != 0:
        if c > maior:
            maior =c
            posiçãomax = [pos]
        elif c < menor:
            menor =c
            posiçãomin =[pos]
        elif c == maior:
            posiçãomax.append(pos)
        elif c == menor:
            posiçãomin.append(pos)

print(f'O maior valor é {maior} na posição',end=' ')
for max in posiçãomax:
    print(max,end=', ')
print(f'O menor valor {menor} na posição')   
for min in posiçãomin:
    print(min, end= ', ')
