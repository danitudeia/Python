n=int(input("Digite um número inteiro:"))
soma=0
r=0
while n!=0:
    soma=n%10
    n=n//10
    r=soma+r
print(r)
