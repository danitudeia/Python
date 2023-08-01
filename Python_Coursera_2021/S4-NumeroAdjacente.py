naoadjacente = True

n=int(input("Digite um número inteiro:"))

r=1

comp=1

while naoadjacente and n!=0:
    r=n%10
    comp=(n//10)%10
    if r==comp:
        naoadjacente = False
    n=n//10
        
if naoadjacente:
    print("não")
else:
    print("sim")
