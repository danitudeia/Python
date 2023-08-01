
i=int(input("Digite uma sequencia de numeros "))
while i>=0:
  fat=1
  while i>1:
    fat=fat*i
    i=i-1
  print(fat,end='\t')
  print()
  i=int(input("Digite uma sequencia de numeros "))
