primeiro_termo = int (input('Diga o primeiro termo de uma PA: '))
razao= int(input('Agora fale a razão: '))

for pa in range(primeiro_termo, 11,razao):
    
    print(pa,end=' ')
    