from genrnd import genrnd

def media(rnd):
    """calcula la media de la lista rnd de números aleatorios.

    Args:
        rnd (list): lista de números aleatorios

    Returns:
        float: media (promedio) de la lista rnd
    """
    media = sum(rnd)/len(rnd)
    return media

# rnd = genrnd()
# print(media())