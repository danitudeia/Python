#FUNÇÃO COMPUTADOR ESCOLHE#

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

 

  
