time = []
jogador= {}
temp =0
golspar=[]
tot=0
while True:
    jogador['nome']= input('Nome do jogador: ').capitalize().strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador ["nome"]} jogou: '))
    
    for c in range(jogador['partidas']):
        temp= (int(input(f'Quantoa gols na {c+1}º partida: ')))
        golspar.append(int(temp))
        tot+=temp
        
    jogador['gols'] = golspar[:]
    jogador['total']= tot
    tot=0
    golspar.clear()
    time.append(jogador.copy())
    jogador.clear()
    opc = input('Quer continuar [S|N]? ').upper().strip()
    if opc == 'N':
    
        break

print('-=' * 30)
print(f'{"Cod":<5}{"Nome":<20}{"Gols":<25}{"Total":>5}')
print('-' * 60)
for i in range(len(time)):
    print(f'{i+1:<5}{time[i]["nome"]:<20}{str(time[i]["gols"]):<25}{time[i]["total"]:>5}')
        
most = int(input('Mostrar dados de qual jogador? '))
most1=most-1
time[0]['gols']
for num, dad in enumerate(time[most1]['gols']):
    print(f'Na {num+1} partida {time[most-1]['nome']} fez {dad} gols')
    