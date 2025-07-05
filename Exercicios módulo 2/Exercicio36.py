from time import sleep 
print('=-='*10,'\033[1mBanco do Brasil\033[m','=-='*10)
print(' ')

valor_casa = int(input('Bom dia senhor(a)!\nPara darmos inicio a avaliação do seu empréstimo, diga-nos o valor do imóvel do que o(a) senhor(a) deseja\nR$ '))
salario= int(input('Ta certo!\nE qual o seu salario atual, senhor(a)?\nR$ '))
anos_totais= int(input('E para finalizarmos...\nem quantos anos o(a) senhor(a) deseja parcelar o pagamento do imóvel?\n'))
prestacao_mensal= (valor_casa / (anos_totais*12))

print('')
print('ANALIZANDO DADOS...')
sleep(2)
print('')

if (salario*0.3)>= prestacao_mensal:
    print(f'Seu empréstimo foi\033[1;32m ACEITO\033[m, meus parabéns\n A sua prestação mensal é de R${prestacao_mensal:.2f} ')
else:
    print('Infelizmente seu empréstimo foi \033[1;31mNEGADO\033[m')
