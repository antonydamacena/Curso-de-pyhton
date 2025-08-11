expressão =[]
expressão2 =[]
simb =[]
print('Digite sua expressão:')
expressão.append(input('-> '))
expressão2 = expressão[0]
for i in expressão2:
    if i == '(':
        simb.append('(')
    elif i == ')':
        if len(simb) > 0:
            simb.pop()
        else:
            simb.append(')')

if len(simb) != 0:
    print('Expressão INVÁLIDA!')
else:
    print('Expresão VÁLIDA!')
    