from enteros import ing2i

n1, n2 = ing2i()
def suma(n1, n2):
    """suma dos enteros n1 y n2 y retorna el resultado

    Returns:
        int: suma de los enteros
    """
    sumar = n1 + n2
    return sumar

print(f'La suma es: {suma(n1, n2)}')