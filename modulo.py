from enteros import ing2i

def modulo(n1, n2):
    """divide dos enteros n1 y n2 y retorna el resto

    Args:
        n1 (int): primer valor ingresado
        n2 (int): segundo valor ingresado
    
    Returns:
        int: resto de la división de los enteros
    """
    mod = n1 % n2
    return mod

# n1, n2 = ing2i()
# print(f'El módulo es: {modulo(n1, n2)}')