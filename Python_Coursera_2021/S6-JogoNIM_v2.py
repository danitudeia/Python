#FUNÇÃO PRINCIPAL JOGO NIM#

def main():
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
    campeonato(x)
  else:
    partida()



#FUNÇÕES ADICIONAIS#
    
def campeonato(x):
  rodada=1
  while rodada<=3:
    print()
    print("**** Rodada ",rodada," ****")
    print()
    partida()
    rodada = rodada+1
  print()
  print("**** Final do campeonato! ****")
  print()
  print("Placar: Você 0 X 3 Computador")
  
def partida():
  n=1
  m=2
  while n<m or n==0 or m==0:
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    print()
  if n%(m+1)==0:
    computador = False
    print("Você começa!")
    print()   
  else:
    computador = True
    print("Computador começa!")
    print()
  while n>0:
    if computador:
      n=n-computador_escolhe_jogada(n,m)
      if n==1:
        print("Agora resta apenas uma peça no tabuleiro.")
        print()
      else:
        print("Agora restam ",n,"peças no tabuleiro.")
        print()
      computador = False
    else:
      n=n-usuario_escolhe_jogada(n,m)
      if n==1:
        print("Agora resta apenas uma peça no tabuleiro.")
        print()
      else:
        print("Agora restam ",n,"peças no tabuleiro.")
        print()
      computador = True
  print("Fim do jogo! O computador ganhou!")
            
        
def usuario_escolhe_jogada(n,m):
  x=int(input("Quantas peças você vai tirar? "))
  while x>n or x>m or x<=0:
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
  return x

def computador_escolhe_jogada(n,m):
  if n<=m:
    x=n
    if x==1:
      print("O computador tirou uma peça.")
    else:
      print("O computador tirou ",x," peças.")
    return x
  else:
    x=n%(m+1)
    if x>0:
      if x==1:
        print("O computador tirou uma peça.")
      else:
        print("O computador tirou ",x," peças.")
      return x
    else:
      if m==1:
        print("O computador tirou uma peça.")
      else:
        print("O computador tirou ",m," peças.")
      return m

#EXECUTA JOGO#
main()
