from enteros import ing2i

n1, n2 = ing2i()
def producto(n1, n2):
    """multiplica dos enteros n1 y n2 y retorna el resultado

    Returns:
        int: multiplicación de los enteros
    """
    mult = n1 * n2
    return mult

print(f'El producto es: {producto(n1, n2)}')