from enteros import ing2i

def radicacion(n1, n2):
    """calcula la raíz n2 del entero n1 y retorna el resultado

    Args:
        n1 (int): primer valor ingresado
        n2 (int): segundo valor ingresado

    Returns:
        int: raiz n2 del entero n1
    """
    raiz = n1 ** (1/n2)
    return raiz

# n1, n2 = ing2i()
# print(f'La raíz es: {round(radicacion(n1, n2), 2)}')