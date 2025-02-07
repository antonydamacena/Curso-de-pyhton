from random import randint
from time import sleep

n= randint (0,5)
a1=(input('Iremos jogar um jogo de sorte ou azar você topa, sim ou não? ')).lower()

if a1 == 'sim' or a1=='s' or a1== 'sin' or a1=='si':
    a2= int(input(('Escolha um número entre 0 e 5 ')))
    print('Carregando...')
    sleep(1.5)
       
    if a2 == n:
        print(' Você ganhou!')
    else:
         print(f'Você morreu! o número certo era o {n}')
else: 
    print('Você é chato!')