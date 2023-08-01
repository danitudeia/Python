def remove_repetidos(lista):
  remove_repetidos=[]
  for x in lista:
    if x not in remove_repetidos:
      remove_repetidos.append(x)
  return sorted(remove_repetidos)
