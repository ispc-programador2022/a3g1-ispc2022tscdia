from genrnd import genrnd

def mediana(rnd):
    """calcula la mediana de la lista rnd de números aleatorios.

    Args:
        rnd (list): lista de números aleatorios

    Returns:
        int: mediana de la lista rnd
    """
    sorted_rnd = sorted(rnd)
    mediana = sorted_rnd[len(rnd)//2]
    return mediana

# rnd = genrnd()
# print(mediana(rnd))