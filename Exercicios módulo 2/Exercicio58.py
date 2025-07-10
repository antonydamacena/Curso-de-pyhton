from random import randint
maquina = randint(0,10)
tentativas = 1
print('Estou pensando em  um numero, tente adivinha-lo! ')
jogador= int(input('Digite o número que você acha que estou pensando: '))
while jogador != maquina  :
        if jogador > maquina:
                jogador= int(input(f'você errou! É MENOR que {jogador} Digite outro número: '))
        else: 
                jogador= int(input(f'você errou! É MAIOR que {jogador} Digite outro número: '))

        tentativas += 1
print(f'PARABÉNS você acertou! O número certo era {maquina} e precisou de {tentativas} tentativas até acertar!')
    
