def n_primos(n):
  conta=0
  while n>=2:
    if testa_primo(n)==True:
      conta=conta+1
    n=n-1
  return conta

def testa_primo(n):
    primo = True
    d=n-1
    while primo and d>1:
        if n%d==0:
            primo = False
        d=d-1
    return primo
