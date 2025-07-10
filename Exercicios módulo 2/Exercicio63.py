num=  int(input('Digite quantos termos deseja ver da sequencia de fibonacci: '))
cont =2
t1 =0
t2= 1
t3 =0
print('0 -> 1 -> ',end='')
while cont != num:
    t3 = t1 +t2
    print(f'{t3} -> ',end='')
    t1= t2
    t2 =t3
    cont +=1
print('Fim')
