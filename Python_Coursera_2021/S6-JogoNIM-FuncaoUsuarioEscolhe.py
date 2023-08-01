#FUNÇÃO USUARIO ESCOLHE#

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
