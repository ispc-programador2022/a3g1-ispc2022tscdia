from genrnd_high import genrnd

from media_high_genrnd import media
from mediana_high_genrnd import mediana
from rango_high_genrnd import rango
from varianza_high_genrnd import varianza
from min_high_genrnd import minimo
from max_high_genrnd import maximo

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

print(f'Tiempo de ejecución: {round(end - start, 2)} segundos.')