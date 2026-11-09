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
                celulas=[(linha + i*d_linha, coluna + i*d_coluna) for i in range(4)]
                if all(0<=l<linhas and 0<=c<colunas and tabuleiro[l][c]==jogador for l,c in celulas):
                    return celulas 
    return None
#interface grafica
def desenhar_tabuleiro(canvas, tabuleiro, destaque=None):
    canvas.delete("all")
    for linha in range(linhas):
        for coluna in range(colunas):
            x0=coluna*tamanho_celula+margem+6
            y0=linha*tamanho_celula+margem+6
            x1=x0+tamanho_celula-margem-12
            y1=y0+tamanho_celula-margem-12
            vencedora=(linha,coluna) in destaque
            canvas.create_oval(
                x0,y0,x1,y1,fill=cores[tabuleiro[linha][coluna]],outline=cordestaque if vencedora else "#123a91",
                width=5 if vencedora else 2)