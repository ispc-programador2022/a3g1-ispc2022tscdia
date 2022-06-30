import random

def genrnd():
    """genera una lista de 50 números enteros aleatorios comprendidos entre 0 y 500.

    Returns:
        list: lista de 50 números enteros aleatorios
    """
    rnd = [random.randint(0, 100) for _ in range(50)]
    return rnd

# print(genrnd())