from enteros import ing2i

n1, n2 = ing2i()
def resta(n1, n2):
    """resta dos enteros n1 y n2, en ese orden, y retorna el resultado

    Returns:
        int: resta de los enteros
    """
    restar = n1 - n2
    return restar

print(f'La resta es: {resta(n1, n2)}')