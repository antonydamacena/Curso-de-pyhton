#Exercicio 18 Seno Cosseno E Tanjente
from math import cos, sin, tan, radians
a= int(input('Digite um angulo qualquer para obtermos o seu seno cosseno e a sua tanjente: '))
r= radians(a)
print(f'O angulo digitado foi {a} o seno deste angulo seria {sin(r):.3f} o cosseno seria {cos(r):.3f} e a sua tanjente seria {tan(r):.3f}')
