from enteros import ing2i

n1, n2 = ing2i()
def potencia(n1, n2):
    """eleva el entero n1 a la potencia n2 y retorna el resultado

    Returns:
        int: potencia de los enteros
    """
    pot = n1 ** n2
    return pot

print(f'La potencia es: {potencia(n1, n2)}')