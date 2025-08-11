num_exts =( 'Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        print('-'*20,'Número Em Extenso','-'*20)
        try:
            num = int(input('Digte um número entre 0-20 para vê-lo em extenso: '))
            
            print('')
            if num < 0 or num  > 20:
                print('\033[0;33mPor favor,  Insira um valor entre 0-20\033[m')
                continue
            else:
                break

            
        except ValueError:
            print('\033[0;31mValor inválido! Por favor dite um número entre 0-20\033[m')

    print(f'O numero {num} em extenso é: {num_exts[num]}')
    opc = input('você quer continuar [S|N]? ').strip().upper()
    if opc not in ['S','N']:
        while True:
            opc = input('você quer continuar [S|N]? ')
            if opc in ['S','N']:
                break
            else:
                continue
    if opc == 'N':
        break
    
print('Programa finalizado!')