#tem que ver se o numero é divisivel apenas por 1 e por ele mesmo
numero = int(input("Digite um número: "))
total_divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0 :
        total_divisores += 1
if total_divisores == 2:
    print('É um numero primo')
else:
    print('Não é um numero primo')
    