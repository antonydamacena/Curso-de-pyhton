d= int(input('Qual será a distancia total de sua viagem? '))

'''if d <= 200:
   valor= {0.5*d}
else:
    valor= {0.45*d}
print(f'O valor da passagem será de {valor}')'''
preço = d*0.5 if d<=200 else d*0.45
print(f'O valor da passagem foi de {preço}')