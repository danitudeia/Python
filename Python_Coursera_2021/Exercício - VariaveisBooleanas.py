
decrescente = True
anterior = int(input("digite o primeiro numero da sequencia: "))

valor = 1

while valor !=0 and decrescente:
    valor =(int(input("digite o próximo numero da sequencia:"))
    if valor>anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("Sequencia é decrescente")
else:
    print("Sequencia é crescente")
