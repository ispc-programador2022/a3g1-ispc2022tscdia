from enteros import ing2i

def cociente(n1, n2):
    """divide dos enteros n1 y n2 y retorna el resultado

    Args:
        n1 (int): primer valor ingresado
        n2 (int): segundo valor ingresado
    
    Returns:
        float: división de los enteros
    """
    div = n1 / n2
    return div

# n1, n2 = ing2i()
# print(f'La división es: {round(cociente(n1, n2), 2)}')