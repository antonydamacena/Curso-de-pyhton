import pygame
import random
import sys

# Configurações
TAM_CELULA = 40
LINHAS, COLUNAS = 9, 9
BOMBAS = 10
VIDAS = 3

# Cores
CINZA = (189, 189, 189)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

pygame.init()
fonte = pygame.font.SysFont(None, 24)
fonte_emoji = pygame.font.SysFont("Segoe UI Emoji", 28)
tela = pygame.display.set_mode((COLUNAS * TAM_CELULA, LINHAS * TAM_CELULA + 50))
pygame.display.set_caption("Campo Minado 💣")

# Inicialização
tabuleiro = [['0' for _ in range(COLUNAS)] for _ in range(LINHAS)]
visivel = [[' ' for _ in range(COLUNAS)] for _ in range(LINHAS)]
flags = set()
vidas = VIDAS
inicio = pygame.time.get_ticks()

def posicionar_bombas():
    bombas = 0
    while bombas < BOMBAS:
        l = random.randint(0, LINHAS - 1)
        c = random.randint(0, COLUNAS - 1)
        if tabuleiro[l][c] != 'B':
            tabuleiro[l][c] = 'B'
            bombas += 1

def contar_bombas(l, c):
    total = 0
    for i in range(l - 1, l + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < LINHAS and 0 <= j < COLUNAS and tabuleiro[i][j] == 'B':
                total += 1
    return total

def preencher_numeros():
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i][j] != 'B':
                tabuleiro[i][j] = str(contar_bombas(i, j))

def revelar(l, c):
    if visivel[l][c] != ' ' or (l, c) in flags:
        return
    visivel[l][c] = tabuleiro[l][c]
    if tabuleiro[l][c] == '0':
        for i in range(l - 1, l + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < LINHAS and 0 <= j < COLUNAS:
                    revelar(i, j)

def desenhar():
    tela.fill(BRANCO)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            x, y = j * TAM_CELULA, i * TAM_CELULA
            pygame.draw.rect(tela, CINZA, (x, y, TAM_CELULA, TAM_CELULA))
            pygame.draw.rect(tela, PRETO, (x, y, TAM_CELULA, TAM_CELULA), 1)
            if visivel[i][j] == '💣':
                texto = fonte_emoji.render('💣', True, PRETO)
                tela.blit(texto, (x + 8, y + 5))
            elif visivel[i][j] != ' ':
                texto = fonte.render(visivel[i][j], True, AZUL)
                tela.blit(texto, (x + 15, y + 10))
            elif (i, j) in flags:
                pygame.draw.circle(tela, VERMELHO, (x + 20, y + 20), 8)

    tempo = (pygame.time.get_ticks() - inicio) // 1000
    score = sum(row.count(' ') for row in visivel)
    hud = fonte.render(f"⏱️ Tempo: {tempo}s   ❤️ Vidas: {vidas}   🏆 Score: {score}", True, PRETO)
    tela.blit(hud, (20, LINHAS * TAM_CELULA + 10))
    pygame.display.flip()

# Início do jogo
posicionar_bombas()
preencher_numeros()

# Loop principal
rodando = True
while rodando:
    desenhar()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            linha = y // TAM_CELULA
            coluna = x // TAM_CELULA
            if linha >= LINHAS:
                continue
            if evento.button == 1:  # Clique esquerdo
                if tabuleiro[linha][coluna] == 'B':
                    visivel[linha][coluna] = '💣'
                    vidas -= 1
                    if vidas == 0:
                        print("💥 Game Over!")
                        rodando = False
                else:
                    revelar(linha, coluna)
            elif evento.button == 3:  # Clique direito
                if (linha, coluna) in flags:
                    flags.remove((linha, coluna))
                else:
                    flags.add((linha, coluna))

pygame.quit()
sys.exit()
