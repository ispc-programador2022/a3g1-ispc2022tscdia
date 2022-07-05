from genrnd import genrnd

# REVISAR: no entendí bien la consigna

def suma_genrnd():
    rnd = genrnd()
    for i in range(len(rnd)):
        n1 = rnd[i]
        for n in range(len(rnd)):
            n2 = rnd[n]
            sumar = n1 + n2
            print(sumar)

suma_genrnd()