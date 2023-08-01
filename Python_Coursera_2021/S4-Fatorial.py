n=int(input("Digite o valor de n: "))

f=1
r=1
while n>0:
    r=n*f
    n=n-1
    f=r
print(r)
