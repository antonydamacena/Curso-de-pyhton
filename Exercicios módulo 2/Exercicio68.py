from random import randint
cont=jogador=0
opc=result= ''
print('-'*10, 'VAMOS JOGAR PAR OU ÍMPAR')
while True:
    maquina = randint(0,10)
    jogador = int(input('Digite seu palpite:'))
    opc = str(input('Par ou Ímpar [P|I]: ')).upper().strip()[0]
    tot = (maquina +jogador)%2
    if tot == 0:
        result = 'Par' 
    else:
        result = 'ìmpar'
    if opc in ['P', 'I' 'Í']:

        if tot and opc == 'P' or result == 'Ímpar' and opc in ['I', 'Í']:
            cont+=1 
            print (f'Você jogou {jogador} e a maquina {maquina}. O total deu { jogador+maquina} entao deu {result}')
            print('PARABÉNS! Você acertou!')
            print('Jogar novamente...')
        else: 
            break
    else:
        print('Opção invalida! Por favor digite [I] para ímpar e [P] para par')

print(f'Você jogou {jogador} e a maquina {maquina}. O total deu { jogador+maquina} entao deu {result}')
print(f'Você perdeu! Você venceu {cont} vezes')
        