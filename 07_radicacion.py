from enteros import ing2i

n1, n2 = ing2i()
def radicacion(n1, n2):
    """calcula la raíz n2 del entero n1 y retorna el resultado

    Returns:
        int: raiz n2 del entero n1
    """
    raiz = n1 ** (1/n2)
    return raiz

print(f'La raíz es: {round(radicacion(n1, n2), 2)}')