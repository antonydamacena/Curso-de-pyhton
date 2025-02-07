# Exercicio 24 Sua cidade começa com santo?
c=str(input('Digite o nome de sua cidade: ')).strip().lower().split()
print(f'Começa com santo {'santo' in c[0]}') 
print(f'outra alternativa {c[0] == 'santo'}')