def testa_primo(n):
    primo = True
    if n<1:
        d=2
    else:
        d=n-1
    while primo and d>1:
        if n%d==0:
            primo = False
        d=d-1
    return primo

def maior_primo(n):
    if testa_primo(n) ==True:
        return n
    else:
        while not testa_primo(n):
            n=n-1
            if testa_primo(n)==True:
                return n

