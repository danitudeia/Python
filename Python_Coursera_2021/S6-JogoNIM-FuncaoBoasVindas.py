#BOAS VINDAS#
def jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    x=int(input(""))
    while x!=1 and x!=2:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        x=int(input(""))
    if x==2:
        print("Voce escolheu um campeonato!")
    else:
        print("teste")
