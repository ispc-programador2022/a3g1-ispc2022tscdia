from enteros import ing2i

n1, n2 = ing2i()
def cociente(n1, n2):
    """divide dos enteros n1 y n2 y retorna el resultado

    Returns:
        float: división de los enteros
    """
    div = n1 / n2
    return div

print(f'La división es: {round(cociente(n1, n2), 2)}')