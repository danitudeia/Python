largura=int(input("digite a largura: "))
while largura<=0:
  largura=int(input("digite a largura: "))
  
altura=int(input("digite a altura: "))
while altura<=0:
  altura=int(input("digite a altura: "))

y=altura
x=largura
print("#"*largura)
while y>2:
  print("#"," "*(largura-3),end = "#\n")
  y=y-1
print("#"*largura)
