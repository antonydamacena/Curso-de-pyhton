#Exercicio 16 Mostrar a parte decimal de um numero:
from math import trunc
n=float(input('Digite um numero: '))
print(f'O numero digitado foi {n} mas a sua porção inteira é {trunc(n)} Ou {int(n)}')