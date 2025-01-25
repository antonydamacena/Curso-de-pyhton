from random import choice, sample
# Exercicio 19 e 20  Sorteio de aluno e ordem de apresentação:
a1= (input('Qual o nome do primeiro aluno a participar do sorteio? '))
a2=(input('Qual o nome do segundo?'))
a3=(input('Qual o nome do terceiro? '))
a4=(input('Qual o nome do quarto? '))
a5=(input('Qual o nome do quinto? '))
t=(a1, a2, a3, a4, a5)
print(f'O aluno(a) sorteado foi {choice(seq= t)}\n')
print (f'E a ordem de apresentação será:\n\n {sample(t, k= len(t))}')
