#FUNÇÃO PARTIDA#

def partida():
    n=1
    m=2
    while n<m or n==0 or m==0:
        n=int(input("Quantas peças? "))
        m=int(input("Limite de peças por jogada? "))
        print()
    if n%(m+1)==0:
        print("Você começa!")
        print()
        while n!=0:
            usuario_escolhe_jogada(n,m)
            computador_escolhe_jogada(n,m)
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Computador começa!")
        print()
        while n!=0:
            computador_escolhe_jogada(n,m)
            usuario_escolhe_jogada(n,m)
        print("Fim do jogo! O computador ganhou!")
            
