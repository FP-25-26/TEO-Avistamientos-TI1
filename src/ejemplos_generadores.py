'''
Ejemplos para explicar qué son y para qué sirve los generadores
'''
from avistamientos import lee_avistamientos

avistamientos = lee_avistamientos("data/ovnis.csv")

# ¿Cuál es la suma de las duraciones de los avistamientos en la ciudad "muncie"

filtrado = []
for av in avistamientos:
    if av.ciudad == "muncie":
        filtrado.append(av.duracion)
print(filtrado)
suma_duraciones = sum(filtrado)
print(f"La suma es {suma_duraciones}")

# Vamos a resolver lo mismo usando un generador.
# Un generador se expresa así:
# EXPRESIÓN_GENERADORA for VARIABLE in ITERABLE if CONDICION
suma_duraciones = sum(av.duracion for av in avistamientos if av.ciudad == "muncie") 

# ¿Y si quiero construir una lista con los avistamientos de la ciudad?
filtrado = [av for av in avistamientos if av.ciudad=="muncie"]

# ¿Y si quiero construir un conjunto con las formas distintas de la ciudad "muncie"?
formas = {av.forma for av in avistamientos if av.ciudad == "muncie"}
