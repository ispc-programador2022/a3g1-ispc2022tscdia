import random

def genrnd():
    """genera una lista de 500.000.000.000.000.000 números enteros aleatorios.

    Returns:
        list: lista de 50 números enteros aleatorios
    """
    rnd = [random.randint(0, 500000000000000000000000) for _ in range(500000000000000000)]
    return rnd

# print(genrnd())