num = int(input('Digite um número para ver sua PA (Progreção aritimétrica):'))
raz = int(input('Digite a razão: '))
qnt =0
print(num)
while qnt != 10:
    qnt +=1
    num += raz
    print(num)
opc = 0
while opc != 2:
    opc = int(input('''O que você deseja?
                    [1]Mais termos
                    [2]Finalizar por aqui
                    Digite o sua escolha: '''))
    if opc == 1:
        qnt = int(input('Digite quantos Mais termos você deseja ver: '))
        qnt1= 0
        while qnt1 != qnt:
            qnt1 += 1
            num += raz
            print(num)
print('OK')