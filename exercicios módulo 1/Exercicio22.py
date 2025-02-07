# Exercicio 22 Criar um programa que leia o nome de uma pessoa e mostre: ele todo em minusculo, maiusculo, quantas letras tem ao todo sem espaços e quantas letras tem o primeiro nome
n=(input('Digite seu nome: '))
s=n.split()

print(f''' Seu nome todo em maiúscuo:\n
       {n.upper()}\n\n

         Ele todo em minusculo:\n 
         {n.lower()}\n\n 

         Seu nome tem um total de {len(''.join(s))} letras\n\n 
         
         e o seu primeiro nome tem {len(s[0])} ''')