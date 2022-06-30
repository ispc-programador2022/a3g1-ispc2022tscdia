from genrnd import genrnd

from media_genrnd import media
from mediana_genrnd import mediana
from rango_genrnd import rango
from varianza_genrnd import varianza
from min_genrnd import minimo
from max_genrnd import maximo

import time

start = time.perf_counter()

rnd = genrnd()
# print(rnd)

media(rnd)
mediana(rnd)
rango(rnd)
varianza(rnd)
minimo(rnd)
maximo(rnd)

end = time.perf_counter()

print(f'Tiempo de ejecución: {end - start} segundos.')