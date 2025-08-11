alunos = []
dado=[[],[[],[]]]
media =0
print('-='*10,' CADASTRO DE ALUNO ','-='*10)
while True:
    
    dado[0].append(input('Nome: ').capitalize())
    while True:
        try:
            dado[1][0].append(float(input('1º Nota: ')))
            dado[1][1].append(float(input('2º Nota: ')))
            break
        except ValueError:
            print('Valor inválido, Digite apenas números .')
    alunos.append(dado[:])
    dado.clear()
    dado=[[],[[],[]]]
    while True: 

        opc = input('Quer continuar [S|N]? ').upper().strip()
        if opc in ['S','N']:
            break
    if opc == 'N':
        break
    print('-'*30)

print('-='*30)
print('No.      Nome      Média')
print('-'*30)
for num, forn in enumerate(alunos):
    
    media = (forn[1][0][0] + forn[1][1][0]) / 2  # Acessa as notas do aluno atual
    print(f'{num + 1:<9} {forn[0][0]:<20} {media:.2f}')                                                                                  
notas =0
while notas != 999:   
    notas = int(input('Mostrar as notas de qual alunos [999 para interromper]: '))
    print(f'Notas de {alunos[notas-1][0][0]}:')
    print(f'Primeira nota --> {alunos[notas-1][1][0][0]}')
    print(f'Segunda nota --> {alunos[notas-1][1][1][0]}')

print('PROGRAMA FINALIZADO!')