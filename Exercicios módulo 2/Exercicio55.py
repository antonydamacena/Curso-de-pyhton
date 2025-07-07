maior= 0 
menor = 0

for p in range (1,6):
    peso = float(input(f'Qual o peso da {p}º pessoa: '))        
    if p == 1:
        maior = peso 
        menor = peso 
    if peso >= maior:
        maior= peso
        
    else:
        menor= peso
        
print(f' o menor peso foi {menor}')
print(f' e o maior foi {maior}')
