num = int(input('Digite um numero para saber seu fatorial: '))
fatorial_while = 1
fatorial_for = 1
num1 =num
#Usando while:
while num != 1:
   fatorial_while *= num
   num -= 1
print(f'O fatorial de {num1} é {fatorial_while}')

num= num1
#Usando for:
for i in range (num,0,-1):
   fatorial_for *= i
print(fatorial_for)
