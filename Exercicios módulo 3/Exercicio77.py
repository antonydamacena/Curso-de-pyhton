
palavras = ('banana', 'foguete', 'caderno', 'girafa', 'tigre', 'sorvete', 'nuvem', 'praia', 'cadeira', 'estrela')
for c in palavras:
    print(f'\npara a palavra {c.upper()} temos as vogais= ',end='')
    for letra in c:
        if letra in 'aeiou' :
                print(letra, end=' ')