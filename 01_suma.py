from enteros import ing2i

def suma():
  n1, n2 = ing2i()
  sumar = n1 + n2
  return sumar
  
print(f'La suma es: {suma()}')