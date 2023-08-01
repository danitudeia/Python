largura=int(input("digite a largura: "))
while largura<=0:
  largura=int(input("digite a largura: "))
  
altura=int(input("digite a altura: "))
while altura<=0:
  altura=int(input("digite a altura: "))

y=altura
x=largura
while y>0:
  while x>0:
    if x==1 or x==largura:
      print("#"*largura)
    else:
      print("#"," "*(largura-3),end = "#\n")
    x=x-1
  y=y-1
  print()
