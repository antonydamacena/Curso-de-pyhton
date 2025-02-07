s= int(input('Qual o seu salário atual? R$'))
if s>= 1250:
    print(f'PARABÉNS. Você acaba de recerber um aumento de 10% e passará a receber {s*10 /100}')
else:
    print(f'PARABÉNS. Você acaba de receber um aumento de 15%  e passará a receber {s*15 /100}')