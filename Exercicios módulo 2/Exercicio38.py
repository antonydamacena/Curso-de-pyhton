print('')
print('=-='*20)

print('')
print('\033[1;37;40m Digite dois números para determinar qual o maior entre eles!\033[m')
print('')

v1 = int(input('Digite o \033[4;37;40mprimeiro\033[m valor: '))
v2 = int(input('Digite o \033[4;37;40msegundo\033[m valor:'))
print('')

if v1>v2:
    print('O Primeiro valor é o \033[0;34;40mMaior\033[m!')
elif v1<v2:
    print('O Segundo valor é o \033[0;34;40mMaior\033[m! ')
else:
    print('Ambos os valores são \033[0;34;40mIguais\033[m!')

print('')
print('=-='*20)
print('')
