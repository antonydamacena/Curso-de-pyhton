v= int(input('Qual a velocidade do veículo? '))

if v <= 80:
    print('Tudo certo!')
else:
    print(f'VOCÊ FOI MULTADO! O limite de velocidade era 80km/h vc passou á {v:.2f} por isso será multado em R${(v-80)*7} ')