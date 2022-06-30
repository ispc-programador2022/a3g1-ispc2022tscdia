from genrnd import genrnd
from media_genrnd import media

def varianza(rnd):
    """calcula la varianza de la lista rnd de números aleatorios.

    Args:
        rnd (list): lista de números aleatorios

    Returns:
        float: varianza de la lista rnd
    """
    media_rnd = media(rnd)
    total = 0
    for n in rnd:
        var = (n - media_rnd) ** 2
        total += var
    return round(total / len(rnd), 2)

# rnd = genrnd()
# print(varianza(rnd))