from enteros import ing2i
from resta import resta

def p1(n1, n2, n3):
    """reutiliza la función resta() y resta el resultado de la función con n3.

    Args:
        n3 (int): valor ingresado por el usuario

    Returns:
        int: resta entre 2 parámetros anteriores con n3
    """
    restar = resta(n1, n2) - n3
    return restar

# n1, n2 = ing2i()
# print(p1(n1, n2, int(input("Número 3: "))))