times = ('Flamengo', 'Cruzeiro', 'RB Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético Mineiro', 'Botafogo', 'Mirassol', 'Corinthians',
 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

print('')
print('='*20)
print('')

print('1) Os 5 primeiros são:')
print('')
for c in range (0,5):

    print(f'{c+1}º --> {times[c]}')

print('')
print('='*20)
print('')

print('2) Os 4 ultimos são:')
print('')

total_times = len(times)
for col, tim in enumerate(times[-1:-5:-1]):
    print(f'{total_times-col}º --> {tim}')

print('')
print('='*20)
print('')
print('3) Os times em ordem alfabética é:')
print('')
ordem = sorted(times)
print(ordem)

print('')
print('='*20)
print('')

print('4) O corinthians se encontra na:')
print('')
print(f'{times.index('Corinthians')+1}º Colocação')

print('')
print('='*20)
print('')
