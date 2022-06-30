from enteros import ing2i
from suma import suma

def p1(n1, n2, n3):
    """reutiliza la función suma() y suma el resultado de la función con n3.

    Args:
        n3 (int): valor ingresado por el usuario

    Returns:
        int: suma entre 2 parámetros anteriores con n3
    """
    sumar = suma(n1, n2) + n3
    return sumar

# n1, n2 = ing2i()
# print(p1(n1, n2, int(input("Número 3: "))))