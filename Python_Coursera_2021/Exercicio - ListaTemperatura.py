def MinMax(temperaturas):
  temperaturas_ordenada=sorted(temperaturas)
  print ("A menor temperatura do mês foi: ",temperaturas_ordenada[0], "graus Celsius")
  print ("A maior temperatura do mês foi: ",temperaturas_ordenada[len(temperaturas_ordenada)-1], "graus Celsius")


def test_msg_Min(temp,valor_esperado):
  valor_calculado = temperaturas_ordenada[0]
  if valor_calculado != valor_esperado:
    print("Valor Errado",temp)
    print("Valor Esperado: ",valor_esperado," e Valor Calculado: ",valor_calculado)

def test_Min():
  print("Iniciando testes")
  test_msg_Min ([0],0)
  test_msg_Min ([0,10,20,30,20,10],0)
  test_msg_Min ([25,10,23,26,35,10],10)
  test_msg_Min ([5,25,31,32,24,28,30,21,15],5)
  print("Finalizando testes")
  
def test_msg_Min(temp,valor_esperado):
  valor_calculado = temperaturas_ordenada[len(temperaturas_ordenada)-1]
  if valor_calculado != valor_esperado:
    print("Valor Errado",temp)
    print("Valor Esperado: ",valor_esperado," e Valor Calculado: ",valor_calculado)

def test_Max():
  print("Iniciando testes")
  test_msg_Max ([0],0)
  test_msg_Max ([0,10,20,30,20,10],30)
  test_msg_Max ([25,10,23,26,35,10],35)
  test_msg_Max ([5,25,31,32,24,28,30,21,15],32)
  print("Finalizando testes")
