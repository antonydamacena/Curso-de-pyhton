from time import sleep
from random import randint

print('''Vamos jogar Jokenpô, se tu perder, perde a vida, 
      todavia, se você ganhar levará um voucher no ifood de R$1, aceita jogar?
      [1]Sim 
      [2]Não''')
resposta= int(input(''))
maquina =  randint(1,3)
if resposta == 1:
    print('''Agora escolha:
    [1]Pedra
    [2]Papel
    [3]Tesoura''')
    escolha= int(input(''))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    if maquina == 1 and resposta == 1 or maquina == 2 and resposta == 2 or maquina == 3 and resposta == 3:
        print('Empate')
    elif maquina == 1 and resposta == 3 or maquina == 2 and resposta == 1 or maquina == 3 and resposta == 2:
        print('Você perdeu')
    elif maquina == 1 and resposta == 2 or maquina == 2 and resposta == 3 or maquina == 3 and resposta == 1:
        print('Você ganhou')
    print(f'A maquina escolheu {maquina}')

else:
    print('Tá né? Cara chato!')

