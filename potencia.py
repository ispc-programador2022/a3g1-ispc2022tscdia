from enteros import ing2i

def potencia(n1, n2):
    """eleva el entero n1 a la potencia n2 y retorna el resultado

    Args:
        n1 (int): primer valor ingresado
        n2 (int): segundo valor ingresado
    
    Returns:
        int: potencia de los enteros
    """
    pot = n1 ** n2
    return pot

# n1, n2 = ing2i()
# print(f'La potencia es: {potencia(n1, n2)}')