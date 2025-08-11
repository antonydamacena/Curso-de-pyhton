jogador= {}
temp=0
gollist = []
tot=0

jogador['nome']=input('Nome: ')
part= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range (1,part+1):
    temp = int(input(f'Quantos gols {jogador['nome']} fez na {i}º partida? '))
    tot+=temp
    gollist.append(temp)

jogador['gols'] = [gollist[:]]
jogador['total']= tot
print(jogador)
print(jogador['gols'][0][0] )
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {jogador["nome"]} jogou {part} partidas')

for c in range(len(jogador['gols'][0])):
    print(f'=> Na {c+1}º partida, {jogador["nome"]} fez {jogador['gols'][0][c]} gols')
print(f'Foi um total de {jogador["total"]}')
   