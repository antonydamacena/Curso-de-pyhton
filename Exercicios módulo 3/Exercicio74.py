from random import randint

nuns = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
total = len (nuns)
'''maior = nuns[0]
menor =nuns[0]
'''
print(f'Os números sorteados foram:  {nuns[0]} --> {nuns[1]} --> {nuns[2]} --> {nuns[3]}')
print(total)

'''for c in range (4):
    
    if nuns[c] > maior:
        maior = nuns[c]
    if nuns[c] < menor:
        menor = nuns[c]
print(maior, menor)
'''
#or

print(f'O maior valor sorteado foi {max(nuns)}')
print(f'O menor valor sorteado foi {min(nuns)}')