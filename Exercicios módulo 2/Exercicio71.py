while True:
    try:
        valor =int(input('Digite um valor a ser sacado R$'))
        break
    except ValueError:
        print('Erro! Por favor, Digite um válido. Ex: R$99,99')
c50=c20=c10=c1=0
while True:

    if valor >= 50:
        valor -= 50
        c50+=1
    elif valor <= 49 and valor >= 20:
        valor -= 20
        c20+=1
    elif valor<=19 and valor >= 10:
        valor -= 10
        c10+=1
    elif valor<= 9 :
        valor -= 1
        c1+=1
    if valor == 0:
        break
if c50> 0:
    print(f'Total de {c50} cédulas de R$50')
if c20> 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 >0:
    print(f'Total de {c10} cédulas de R$10')
if c1 >0:
    print(f'Total de {c1} cédulas de R$1')
