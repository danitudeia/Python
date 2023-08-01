import math

def equacao():
    a_digitado=float(input("Digite o valor de a:"))
    b_digitado=float(input("Digite o valor de b:"))
    c_digitado=float(input("Digite o valor de c:"))
    imprime_raizes(a_digitado,b_digitado,c_digitado)

def imprime_raizes(a,b,c):
    delta =(b**2)-(4*a*c)
    if delta <0:
        print("esta equação não possui raízes reais")
    else:
        if delta==0:
            print("a raiz desta equação é",(-b+delta)/(2*a))
        else:
            if (-b+math.sqrt(delta))/(2*a)<=(-b-math.sqrt(delta))/(2*a):
                print("as raízes da equação são",(-b+math.sqrt(delta))/(2*a),"e",(-b-math.sqrt(delta))/(2*a))
            else:
                print("as raízes da equação são",(-b-math.sqrt(delta))/(2*a),"e",(-b+math.sqrt(delta))/(2*a))

            

