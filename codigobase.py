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
    if not 0<=coluna<colunas or coluna_cheia(tabuleiro, coluna):
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
def tabuleiro_cheio(tabuleiro):                                  
    return all(coluna_cheia(tabuleiro, c) for c in range(colunas)) 
#interface grafica
def desenhar_tabuleiro(canvas, tabuleiro, destaque=None):
    canvas.delete("all")
    destaque = destaque or []
    for linha in range(linhas):
        for coluna in range(colunas):
            x0=coluna*tamanho_celula+margem+6
            y0=linha*tamanho_celula+margem+6
            x1=x0+tamanho_celula-12
            y1=y0+tamanho_celula-12
            vencedora=(linha,coluna) in destaque
            canvas.create_oval(
                x0,y0,x1,y1,fill=cores[tabuleiro[linha][coluna]],outline=cordestaque if vencedora else "#123a91",
                width=5 if vencedora else 2)
def main():
    root=tk.Tk()
    root.title("Connect Four/Conecta 4")
    root.resizable(False,False)
    estado={"tabuleiro":criar_tabuleiro(),"jogador":jogador1,"fim":False}
    label_turno=tk.Label(root,font=("Helvetica",16, "bold"),pady=8,width=30)
    label_turno.pack(fill="x")
    label_aviso=tk.Label(root, text="",fg="#b71c1c",font=("Helvetica",11))
    label_aviso.pack()
    frame_botoes=tk.Frame(root)
    frame_botoes.pack(fill="x",padx=margem)
    largura=colunas*tamanho_celula+margem*2
    altura=linhas*tamanho_celula+margem*2
    canvas=tk.Canvas(root,width=largura,height=altura,bg=cortabuleiro,highlightthickness=0)
    canvas.pack()
    def atualizar_turno():
        jogador=estado["jogador"]
        label_turno.config(text=f"Vez do {nomes[jogador]}",bg=cores[jogador],fg=cortexto[jogador])
    def jogar(coluna):
        if estado["fim"]:
            return
        tabuleiro=estado["tabuleiro"]
        jogador=estado["jogador"]
        linha=inserir_ficha(tabuleiro,coluna,jogador)
        if linha is None:
            label_aviso.config(text="Coluna cheia! Escolha outra coluna.")
            return
        label_aviso.config(text="")
        celulas_vencedoras=verificar_vitoria(tabuleiro,jogador)
        if celulas_vencedoras:
            estado["fim"]=True
            desenhar_tabuleiro(canvas,tabuleiro,celulas_vencedoras)
            label_turno.config(text=f"{nomes[jogador]} venceu!",bg=cores[jogador],fg=cortexto[jogador])
        elif tabuleiro_cheio(tabuleiro):
            estado["fim"]=True
            desenhar_tabuleiro(canvas,tabuleiro)
            label_turno.config(text="Empate! Tabuleiro cheio.", bg="#cfd8dc", fg="black")
        else:
            estado["jogador"]=jogador2 if jogador==jogador1 else jogador1
            desenhar_tabuleiro(canvas,tabuleiro)
            atualizar_turno()
    def reiniciar():
        estado["tabuleiro"]=criar_tabuleiro()
        estado["jogador"]=jogador1
        estado["fim"]=False
        label_aviso.config(text="")
        desenhar_tabuleiro(canvas,estado["tabuleiro"])
        atualizar_turno()
    for c in range(colunas):
        frame_botoes.columnconfigure(c,weight=1,uniform="col")
        tk.Button(frame_botoes,text=str(c+1),command=lambda col=c:jogar(col)).grid(row=0,column=c,sticky="ew",padx=2,pady=2)
    def aoclicar(evento):
        coluna=(evento.x-margem)//tamanho_celula
        if 0<=coluna<colunas:
            jogar(coluna)
    canvas.bind("<Button-1>",aoclicar)
    tk.Button(root,text="Reiniciar",command=reiniciar,font=("Helvetica",12),pady=4).pack(pady=8)
    desenhar_tabuleiro(canvas,estado["tabuleiro"])
    atualizar_turno()
    root.mainloop()
    
if __name__=="__main__":
    main()