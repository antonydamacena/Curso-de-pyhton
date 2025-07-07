'''frase = input('Digite uma frase para verificar se ela é um palindromo: ').strip(). upper()
frase_i = frase [::-1].split()
frase_s = frase.split()
if ''.join(frase_i) == ''.join(frase_s):
    print(' É um palindromo ')
else:
    print('Não é  um palindromo')
    print(len(frase_s))''' #desse jeito funciona mas tem que usar o for ent...

frase =  input('Digite uma frase para verificar se ela é um palindromo: ').strip().upper()
palavras= frase.split()
junto = ''.join(palavras)
inverso= ''
for palindromo in range(len(junto)-1,-1,-1):
    inverso += junto[palindromo]
if inverso == junto:
    print('é um palindromo')
else:
    print('não é um palindromo')
 