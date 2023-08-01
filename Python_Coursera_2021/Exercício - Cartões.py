meucartao = input("Digite o número do seu cartão de credito ")

cartaolido = 1

encontreicartaonalista = False

while cartaolido !=0 and not encontreicartaonalista:
    cartaolido = int(input("Digite o número do próximo cartão de credito "))
    if cartaolido == meucartao:
        encontreicartaonalista = True
if encontreicartaonalista:
    print("Eba meu cartão está lá")
else:
    print("Xi, meu cartão não está lá")
    
