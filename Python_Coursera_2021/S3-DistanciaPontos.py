import math

xa=float(input("Digite a coordenada x do ponto A:"))
ya=float(input("Digite a coordenada y do ponto A:"))
xb=float(input("Digite a coordenada x do ponto B:"))
yb=float(input("Digite a coordenada y do ponto B:"))

distancia=math.sqrt((xa-xb)**2+(ya-yb)**2)

if distancia>=10:
    print("longe")
else:
    print("perto")
