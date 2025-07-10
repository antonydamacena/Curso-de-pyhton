opc=''
maior= menor =med =tot =0
while opc != 'N':
    tot+=1
    num= int(input('Digite um número: '))
    opc=str(input('Quer continuar? [S|N] ')).upper()
    med +=num
    if num >= maior:
        maior=num
    else:
        menor = num


print(f'''Você digitou {tot} numeros e a média deles foi {med/tot:.2f}
O maior número foi {maior} e o menor foi {menor}''')
                  