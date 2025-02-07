print(' Para sabermos se é possivel formar um triangulo. Digite a seguir o comprimento das 3 retas! ')
r1= float(input('Qual comprimento da primeira reta'))
r2= float(input('Qual comprimento da segunda reta'))
r3= float(input('Qual comprimento da terceira reta'))

if r1+r2 >= r3 and r1+r3>r2 and r2+r3>r1:
    print('As retas a citadas podem SIM formar um triangulo!')
else:
    print('As retas citadas NÃO podem formar um triangulo! ')
