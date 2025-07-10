num=0
while True:
    print('-'*75)
    print('')
    num= int(input('Digite um valor para ver sua tabuada (Valor Negativo para parar): '))
    print('')
    print('-'*75)
    print('')
    if num < 0:
        break
    print('-'*25,f' \033[1;33mTabuada do número {num}\033[m ', '-'*25)
    print('')
    for tab in range (0,11):
        print(f'\033[0;33m{num:2} x {tab:2}\033[m = \033[0;32m{num*tab}\033[m')
    print('-'*75)
    print('')
print( 'Tabuada \033[1;31mENCERRADA\033[m')