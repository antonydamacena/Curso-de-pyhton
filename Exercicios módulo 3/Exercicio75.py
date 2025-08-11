
pares = []
while True:
    try:
        numeros =( int(input('Digite um numero:')),int(input('Digite um numero:')),
                    int(input('Digite um numero:')),int(input('Digite um numero:')),)
        break
    except ValueError:
        print('Valor inválido! Por fvor Digite um número')


if 3 in numeros:
    posição =(f'aparece na posição {numeros.index(3)+1}')
else:
    posição = 'Não aparece'
print('')
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')
print(f' O numero 3 {posição}')
print(f'Os números pares foram',end=' ')
for n in numeros:

    if n %2 == 0:
        print(n, end=' ')