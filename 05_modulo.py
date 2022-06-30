from enteros import ing2i

n1, n2 = ing2i()
def modulo(n1, n2):
    """divide dos enteros n1 y n2 y retorna el resto

    Returns:
        int: resto de la división de los enteros
    """
    mod = n1 % n2
    return mod

print(f'El módulo es: {modulo(n1, n2)}')