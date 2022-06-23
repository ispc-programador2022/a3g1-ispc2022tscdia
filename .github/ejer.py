a = 1
b = 10
def fn():
print(fn)    # la variable local a no esta asignada, no esta incluida en la función, es una variable global
'''b = 20      # la variable local b está asignada en la tabla de símbolos locales para la función.
print(b)    # la variable local b esta referenciada.
fn()
1
20
>>> b               # la variable global b no se ha modificado por la llamada a la función.
10'''