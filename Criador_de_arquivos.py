import os

# Diretório onde os arquivos serão criados (diretório atual)
diretorio = 'C:/Users/anton/OneDrive/Área de Trabalho/Curso-de-pyhton/Exercicios módulo 2'

# Loop para criar arquivos com nomes 'Exercicio36.py' a 'Exercicio45.py'
for i in range(46, 56):
    nome_arquivo = f'Exercicio{i}.py'
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_completo, 'w') as arquivo:
        pass  # Cria o arquivo vazio

print('Arquivos criados com sucesso!')
