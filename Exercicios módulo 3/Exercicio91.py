from random import randint
from time import sleep
from operator import itemgetter
jogo={'Jogador 1': randint(0,6),
      'Jogador 2': randint(0,6),
      'Jogador 3': randint(0,6),
      'Jogador 4': randint(0,6)
      }
ranking =[]
for k,v in jogo.items():
    print(f'- {k} tirou {v} !')
    sleep(0.5)
ranking = sorted(jogo.items(), key= itemgetter(1),reverse=True)
print('-='*30)
print(f'Ranking dos jogadores'.center(60))
print('-='*30)
for col,k in enumerate(ranking):
    print(f'{col+1}º Lugar ---> {k[0]} com {k[1]}')
    sleep(0.5)