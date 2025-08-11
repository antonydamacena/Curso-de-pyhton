from datetime import date
dados ={}
hoje = date.today().year

dados['nome']=input('Nome: ')
ano = int(input('Ano de nascimento: '))
dados['idade']= hoje-ano
dados['ct']=int(input('Carteira de trabalho (0 Não tem): '))
if dados['ct'] != 0:
    dados['ano_cont']= int(input('Ano de contratação: '))
    dados['salario']= int(input('Salário: R$'))
    #ATENTION
    dados['aposentadoria']= dados['idade']+((dados['ano_cont']+35)-hoje)
for k,v in dados.items():
    print(f'{k} tem valor de {v}')