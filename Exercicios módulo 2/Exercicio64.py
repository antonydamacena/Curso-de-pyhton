num=0
v1 = 0
tot=0
while num != 999:
    num = int(input('Digite um numero: '))   
    if num != 999:
        v1 += num
        tot+=1
print(f'Foram digitados {tot} numero(s) e a soma de todos os numeros foram {v1}')
