tamanho=int(input("digite quantos numeros serão multiplicados: "))

produto = 1

i=0
        
while i<tamanho:
    valor = int(input("digite um valor a ser multiplicado:"))
    produto = produto * valor
    i=i+1
    
print("o produto dos valores digitados é",produto)
