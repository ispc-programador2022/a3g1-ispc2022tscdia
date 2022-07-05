from genrnd_high import genrnd

def rango(rnd):
    """calcula el rango de la lista rnd de números aleatorios.

    Args:
        rnd (list): lista de números aleatorios

    Returns:
        int: rango de la lista
    """
    rango = max(rnd) - min(rnd)
    return rango

# rnd = genrnd()
# print(rango(rnd))