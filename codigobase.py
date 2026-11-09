import tkinter as tk
#cosntantes
linhas=6
colunas=7
tamanho_celula=80
margem=10
vazio=0
jogador1=1
jogador2=2
cores={vazio:"#e8f0ff",
       jogador1:"#e53935", #vermelho
       jogador2:"#ffd54f" #amarelo
       }
cortabuleiro= "#1e53c9"
cordestaque="#00c853"
nomes={jogador1:"Jogador 1(Vermelho)",
       jogador2:"Jogador 2(Amarelo)"
       }
cortexto={jogador1:"#ffffff",
           jogador2:"#000000"}
#jogo
def criar_tabuleiro():
    return [[vazio for _ in range(colunas)] for _ in range(linhas)]
def coluna_cheia(tabuleiro, coluna):
    return all(tabuleiro[linha][coluna] != vazio for linha in range(linhas))
def inserir_ficha(tabuleiro, coluna, jogador):
    if not 0<=coluna<COLUNAS or coluna_cheia(tabuleiro, coluna):
        return None
    for linha in range(linhas-1, -1, -1):
        if tabuleiro[linha][coluna] == vazio:
            tabuleiro[linha][coluna] = jogador
            return linha
    return None
def verificar_vitoria(tabuleiro, jogador):
    direcoes=[(0,1),(1,0),(1,1),(1,-1)]
    for linha in range(linhas):
        for coluna in range(colunas):
            for d_linha,d_coluna in direcoes:
                (linha+i*d_linha, coluna+i*d_coluna) for i in range(4)