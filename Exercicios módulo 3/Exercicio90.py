dados={}
dados["Nome"]= input('Nome: ').capitalize()
dados["Média"] = float(input(f'Média de {dados["Nome"]}: '))

if dados["Média"] >= 6:
    dados['Situação']='Aprovado'
else:
    dados["Situação"]= 'Reprovado'

for k,v in dados.items():
    print(f'{k} é igual á {v}')

    