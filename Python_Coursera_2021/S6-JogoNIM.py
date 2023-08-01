#JOGO NIM#

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
  #      campeonato(x)
  else:
    print("partida()")



#FUNÇÕES ADICIONAIS#
     
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
            
        
def usuario_escolhe_jogada(n,m):
  x=int(input("Quantas peças você vai tirar? "))
  while x>n or x>m or x==0:
    print()
    print("Oops! Jogada inválida! Tente de novo.")
    print()
    x=int(input("Quantas peças você vai tirar? "))
  if x==1:
    print()
    print("Você tirou uma peça.")
  else:
    print()
    print("Você tirou ",x," peças.")
  n=n-x
  if n==1:
    print("Agora resta apenas uma peça no tabuleiro.")
  else:
    print("Agora restam ",n,"peças no tabuleiro.")
  return n

def computador_escolhe_jogada(n,m):
  if n<=m:
    if n==1:
      print("O computador tirou uma peça.")
    else:
      print("O computador tirou ",n," peças.")
    n=n-n
  else:
    x=n%(m+1)
    if x>0:
      if x==1:
        print("O computador tirou uma peça.")
      else:
        print("O computador tirou ",x," peças.")
      n=n-x
    else:
      if m==1:
        print("O computador tirou uma peça.")
      else:
        print("O computador tirou ",m," peças.")
      n=n-m
  if n==1:
    print("Agora resta uma peça no tabuleiro.")
  else:
    print("Agora restam ",n," peças no tabuleiro.")
  return n
