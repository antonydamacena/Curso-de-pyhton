num = int(input('Digite um número para converte-lo '))
print('''Deseja converter este numero para:
              [1]Hexadecimal
              [2]Octodecimal
              [3]Binario
              ''')
value = int(input (''))
if value == 1:
    print(f'{num} em Hexadecimal fica {hex(num)[2:]}')
elif value == 2:
    print(f'{num} em Octodecimal fica {oct(num)[2:]}')
elif value == 3:
    print(f'{num} em Binario fica {bin(num)[2:]}')
else:
    print('Opção invalida, Tente novamente!')