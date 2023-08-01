primo = True
n=int(input("Digite um número inteiro:"))
d=2

while primo and d<n:
    if n%d==0:
        primo = False
    d=d+1

if primo:
    print("primo")
else:
    print("não primo")

