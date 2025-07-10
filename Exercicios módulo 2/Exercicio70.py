nome=nome_pb= opc =''
valor=total_gasto = produto_caro = tot_produtos =0
while True:
    print('-' * 50)
    print(f'{'DAMACENA STORE':^50}') 
    print('-' * 50)

    #adquirindo os dados 

    nome = input('Digite o nome do produto: ').capitalize().strip()
    while True:
        try:
            valor = float(input('Digite o valor do produto: R$'))
            break
        except ValueError:
            
            print('ERRO! Por favor, insira um valor válido (Apenas números). Exemplo: 99.99')
            print('')

    #Analize de dados:
    total_gasto += valor
    tot_produtos+=1
    if valor > 1000:
        produto_caro +=1
    if tot_produtos <=1 or valor <= produto_barato:

        produto_barato = valor
        nome_pb =nome
    #Continuar ou Não:
    print('-'*50)
    opc = input('Deseja continuar? [S|N]: ').upper().strip()
    while opc not in ['S','N']:
        print('Digite uma opção válida [S]Sim [N]Não')
        opc = input('Deseja continuar? [S|N]: ').upper().strip()
    if opc == 'N':
        break
print('-'*50) 
print('-'*15,'Fim do programa','-'*15) 
print('')
print(f'Ao total, foi gasto R${total_gasto} na compra de {tot_produtos} produtos.\n Dentre esses produtos...\n {produto_caro} Custam mais de R$1000\n E o mais barato foi o {nome_pb} custando {produto_barato:.2f}')