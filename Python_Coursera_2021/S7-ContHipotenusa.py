
import math

def soma_hipotenusas(n):
  soma=0
  while n>0:
    if é_hipotenusa(n)==True:
      soma=soma+n
    n=n-1
  return soma

def é_hipotenusa(n):
  co=1
  ca=1
  hipotenusa=False
  while ca<n:
    while co<n:
      if n==math.sqrt((co**2)+(ca**2)):
        hipotenusa==True
        return True
      co=co+1
    ca=ca+1
    co=1

  
