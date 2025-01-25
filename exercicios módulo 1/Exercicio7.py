 # Exercicio 7 Média aritimétrica:

print('Para este Exercicios eu precisarei dos nomes de 3 alunos e suas notas na materia de matemática!')
print(' ')
aluno1= str(input('Qual é o nome do primeiro aluno? '))
aluno2= str(input('Qual o nome do segundo aluno? '))
aluno3= str(input('Qual o nome do terceiro aluno? '))
nota1= float(input(f'Qual foi a nota de {aluno1}? '))
nota2= float(input(f'Qual foi a nota de {aluno2}? '))
nota3= float(input(f'Qual foi a nota de {aluno3}? '))
print(' ')
print(f' A nota de {aluno1} é {nota1}\nA nota de {aluno2} é {nota2}\n e a nota de {aluno3} é {nota3}\n e a média das 3 notas é {(nota1+nota2+nota3)/3:.3f}')