from enteros import ing2i
from producto import producto

def p1(n1, n2, n3):
    """reutiliza la función producto() y multiplica el resultado de la función por n3.

    Args:
        n3 (int): valor ingresado por el usuario

    Returns:
        int: producto entre 2 parámetros anteriores con n3
    """
    prod = producto(n1, n2) * n3
    return prod

# n1, n2 = ing2i()
# print(p1(n1, n2, int(input("Número 3: "))))