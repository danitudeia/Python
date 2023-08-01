i=int(input("Digite um número inteiro positivo: "))
while i>0:
  primo = True
  d=2
  conta=1
  while d<i:
    conta=i%d
    if i%d==0:
      primo=False
    d=d+1
  print(primo)
  i=int(input("Digite um número inteiro positivo: "))
