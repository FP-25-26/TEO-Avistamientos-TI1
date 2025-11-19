import csv
from datetime import datetime, date
from typing import NamedTuple
from coordenadas import Coordenadas, distancia, redondear

## Definición de constantes
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

## Definición de tipos
Avistamiento = NamedTuple('Avistamiento', [
    ('fechahora', datetime),
    ('ciudad', str),
    ('estado', str),
    ('forma', str),
    ('duracion', int),
    ('comentarios', str),
    ('ubicacion', Coordenadas)
])

## 1. Operaciones de carga de datos
### 1.1 Función de lectura de datos
# Función de lectura que crea una lista de avistamientos
def lee_avistamientos(fichero:str)->list[Avistamiento]:
    '''
    Lee un fichero de entrada y devuelve una lista de tuplas. 
    Para convertir la cadena con la fecha y la hora al tipo datetime, usar
        datetime.strptime(fecha_hora,'%m/%d/%Y %H:%M')    
    
    :param fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
    :return: lista de tuplas con la información de los avistamientos 
    '''
    with open(fichero, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for (fechahora,city,state,shape,duration,
             comments,latitude,longitude) in lector:
            fechahora = datetime.strptime(fechahora, "%m/%d/%Y %H:%M")
            duration = int(duration)
            latitude = float(latitude)
            longitude = float(longitude)
            ubicacion = Coordenadas(latitude, longitude)
            res.append(
                Avistamiento(fechahora,city,state,shape,duration,
             comments, ubicacion)
            )
        return res

### 2.1 Número de avistamientos producidos en una fecha
def numero_avistamientos_fecha(
        avistamientos: list[Avistamiento], 
        fecha: date) -> int:
    ''' Avistamientos que se han producido en una fecha
    
    Toma como entrada una lista de avistamientos y una fecha.
    Devuelve el número de avistamientos que se han producido en esa fecha.

    :param avistamientos: lista de avistamientos
    :param fecha: fecha del avistamiento 
    :return:  Número de avistamientos producidos en la fecha 
    '''
    contador = 0
    for av in avistamientos:
        if av.fechahora.date() == fecha:
            contador += 1
    return contador

### 2.2 Número de formas observadas en un conjunto de estados
def formas_estados(avistamientos:list[Avistamiento], estados:set[str])->int:
    ''' 
    Devuelve el número de formas distintas observadas en avistamientos 
    producidos en alguno de los estados especificados.
    :param avistamientos: lista de tuplas con la información de los avistamientos
    :param estados: conjunto de estados para los que se quiere hacer el cálculo 
    :return: Número de formas distintas observadas en los avistamientos producidos en alguno de los estados indicados por el parámetro "estados"
    '''
    formas = set()
    for av in avistamientos:
        if av.estado in estados:
            formas.add(av.forma)
    return len(formas)    

### 2.3 Duración total de los avistamientos en un estado
def duracion_total(avistamientos:list[Avistamiento], estado:str)->int:
    ''' 
    Devuelve la duración total de los avistamientos de un estado. 
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param estado: estado para el que se quiere hacer el cálculo
    :return: duración total en segundos de todos los avistamientos del estado 
    '''
    duracion_total = 0
    for av in avistamientos:
        if av.estado == estado:
            duracion_total += av.duracion
    return duracion_total


### 2.4 Avistamientos cercanos a una ubicación
def avistamientos_cercanos_ubicacion(avistamientos:list[Avistamiento], ubicacion:Coordenadas, radio:float)->set[Avistamiento]:
    ''' 
    Devuelve el conjunto de avistamientos cercanos a una ubicación.
    :param avistamientos: lista de tuplas con la información de los avistamientos
    :param ubicacion: coordenadas de la ubicación para la cual queremos encontrar avistamientos cercanos 
    :param radio: radio de distancia
    :return:Conjunto de avistamientos que se encuentran a una distancia
         inferior al valor "radio" de la ubicación dada por el parámetro "ubicacion" 
    '''
    res = set()
    for av in avistamientos:
        # Si está en el radio de búsqueda
        distancia_av = distancia(ubicacion, av.ubicacion)
        if distancia_av <= radio:
            res.add(av)
    return res


## Operaciones con máximos y mínimos
### 3.1 Avistamiento de una forma con mayor duración
def avistamiento_mayor_duracion(avistamientos: list[Avistamiento], forma:str)->Avistamiento:
    '''
    Devuelve el avistamiento de mayor duración de entre todos los
    avistamientos de una forma dada.
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param forma: forma del avistamiento 
    :return:  avistamiento más largo de la forma dada
    '''
    mas_largo = None
    for av in avistamientos:
        if av.forma == forma:
            if mas_largo == None or av.duracion > mas_largo.duracion:
                mas_largo = av
    return mas_largo

def avistamiento_mayor_duracion_2(avistamientos: list[Avistamiento], forma:str)->Avistamiento:
    '''
    Devuelve el avistamiento de mayor duración de entre todos los
    avistamientos de una forma dada.
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param forma: forma del avistamiento 
    :return:  avistamiento más largo de la forma dada
    '''
    filtrado = []
    for av in avistamientos:
        if av.forma == forma:
            filtrado.append(av)
    # Buscar funcion filter y sustituir lo anterior
    return max(filtrado, key=lambda av:av.duracion)

### 3.2 Avistamiento cercano a un punto con mayor duración
def avistamiento_cercano_mayor_duracion(avistamientos:list[Avistamiento], ubicacion:Coordenadas, radio:float=0.5)->tuple[str, int]:
    '''
    Devuelve el comentario y la duración del avistamiento que más 
    tiempo ha durado de aquellos situados en el entorno de las
    coordenadas que se pasan como parámetro de entrada.
    El resultado debe ser una tupla de la forma (duración, comentarios)
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param coordenadas: tupla con latitud y longitud
    :param radio: radio de búsqueda
    :return: comentario y duración del avistamiento más largo en el entorno de las coordenadas 
    '''
    # TODO: Para el próximo miércoles, resolver en casa
    filtrado = []
    for av in avistamientos:
        if distancia(ubicacion, av.ubicacion) <= radio:
            filtrado.append(av)
    
    res = max(filtrado, key=lambda av: av.duracion)
    return (res.comentarios, res.duracion) # Me piden que devuelva esta tupla


### 3.3 Avistamientos producidos entre dos fechas

def avistamientos_fechas(avistamientos:list[Avistamiento], fecha_inicial:date|None=None, fecha_final:date|None=None)->list[Avistamiento]:
    '''
    Devuelve una lista con los avistamientos que han tenido lugar
    entre fecha_inicial y fecha_final (ambas inclusive). La lista devuelta
    estará ordenada de los avistamientos más recientes a los más antiguos.
    
    Si fecha_inicial es None se devolverán todos los avistamientos
    hasta fecha_final.
    Si fecha_final es None se devolverán todos los avistamientos desde
    fecha_inicial.
    Si ambas fechas son None se devolverá la lista de 
    avistamientos completa. 
    
    Usar el método date() para obtener la fecha de un objeto datetime.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param fecha_inicial: fecha a partir de la cual se devuelven los avistamientos
    :param fecha_final: fecha hasta la cual se devuelven los avistamientos
    :return: lista de tuplas con la información de los avistamientos en el rango de fechas
    '''
    res = []
    for av in avistamientos:
        if (fecha_inicial == None or fecha_inicial <= av.fechahora.date()) and (fecha_final == None or av.fechahora.date() <= fecha_final):
            res.append(av)
    # Como el primer elemento de las tuplas es fechahora, se ordena por ese campo
    res.sort(reverse=True) # reverse=True para ordenar de mayor a menor
    return res

    # También:
    # return sorted(res, reverse=True)

### 3.4 Avistamiento de un año con el comentario más largo
def comentario_mas_largo(avistamientos:list[Avistamiento], anyo:int, palabra:str)->Avistamiento:
    ''' 
    Devuelve el avistamiento cuyo comentario es el más largo, de entre
    los avistamientos observados en el año dado por el parámetro "anyo"
    y cuyo comentario incluya la palabra recibida en el parámetro "palabra".
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param anyo: año para el que se hará la búsqueda 
    :param palabra: palabra que debe incluir el comentario del avistamiento buscado 
    :return: avistamiento con el comentario más largo
    '''    
    filtrado = []
    for av in avistamientos:
        if av.fechahora.year == anyo and palabra in av.comentarios:
            filtrado.append(av)
    return max(filtrado, key = lambda av: len(av.comentarios))
    

### 3.5 Media de días entre avistamientos consecutivos
def media_dias_entre_avistamientos(avistamientos:list[Avistamiento], anyo:int|None=None)->float|None:
    ''' 
    Devuelve la media de días transcurridos entre dos avistamientos consecutivos.
    Si año es distinto de None, solo se contemplarán los avistamientos del año
    especificado para hacer el cálculo.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param anyo: año para el que se hará la búsqueda 
    :return: media de días transcurridos entre avistamientos. Si no se puede realizar el cálculo, devuelve None 
    '''    
    #Filtramos por año
    filtrado = []
    for av in avistamientos:
        if anyo == None or av.fechahora.year == anyo:
            filtrado.append(av)

    # Debe haber al menos dos avistamientos para poder hacer el cálculo que me piden
    if len(filtrado) <= 1:
        return None

    # Creamos una copia ordenada. CUIDADO! No ordenamos directamente la recibida,
    # porque si no estaríamos cambiándole la lista a quien nos la ha pasado
    ordenados = sorted(filtrado) 

    # Alternativa usando un generador:
    ordenados = sorted(av for av in avistamientos if anyo==None or av.fechahora.year==anyo)

    # avistamientos[1:] devuelve el trozo de avistamientos
    # que comienza en el segundo elemento (índice 1) y
    # llega hasta el final
    suma_dias = 0
    for av1, av2 in zip(ordenados, ordenados[1:]):
        dias = (av2.fechahora.date() - av1.fechahora.date()).days
        suma_dias += dias

    return suma_dias / (len(ordenados)-1)




## 4 Operaciones con diccionarios

### 4.1 Avistamientos por fecha
def avistamientos_por_fecha(avistamientos:list[Avistamiento])->dict[date, list[Avistamiento]]:
    ''' 
    Devuelve un diccionario que indexa los avistamientos por fechas
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return diccionario en el que las claves son las fechas de los avistamientos 
         y los valores son conjuntos con los avistamientos observados en esa fecha
    '''
    res = {} # res = dict()
    for av in avistamientos:
        fecha = av.fechahora.date()
        # Si fecha aún no está en el diccionario (no existe la clave)
        if fecha not in res:
            res[fecha] = [av] # Crea una lista con av, y la guarda en el diccionario para la clave fecha
        else:
            res[fecha].append(av)

    # Otra forma de escribir lo mismo:
    res = {} # res = dict()
    for av in avistamientos:
        fecha = av.fechahora.date()
        # Si fecha aún no está en el diccionario (no existe la clave)
        if fecha not in res:
            res[fecha] = [] # Crea una lista con av, y la guarda en el diccionario para la clave fecha
        res[fecha].append(av)
    return res

### 4.1.2 Formas distintas por año
def formas_distintas_por_año(avistamientos: list[Avistamiento]) -> dict[int, set[str]]:
    '''
    Devuelve un diccionario en el que se agrupan para cada año las formas distintas de los
    avistamientos de ese año. Las claves del diccionario son años (int) y los valores asociados
    a cada año son conjuntos de formas (set[str]).
    '''
    res = {}
    for av in avistamientos:
        año = av.fechahora.year
        if año not in res:
            res[año] = set()
        res[año].add(av.forma)
    return res

### 4.2 Formas de avistamientos por mes
def formas_por_mes(avistamientos:list[Avistamiento])->dict[str, set[str]]:
    ''' 
    Devuelve un diccionario que indexa las distintas formas de avistamientos
    por los nombres de los meses en que se observan.
    Por ejemplo, para el mes "Enero" se asociará un conjunto con todas las
    formas distintas observadas en dicho mes.
        
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario en el que las claves son los nombres de los meses 
         y los valores son conjuntos con las formas observadas en cada mes
    '''
    
    res = {}
    for av in avistamientos:
        #mes = pasa_mes_a_nombre(av.fechahora.month)
        mes = MESES[av.fechahora.month - 1]
        if mes not in res:
            res[mes] = set()
        res[mes].add(av.forma)
    return res

'''
def pasa_mes_a_nombre(mes: int) -> str:
    if mes == 1:
            return "Enero"
        elif mes == 2:
            return "Febrero"
        ...
'''

### 4.3 Número de avistamientos por año
def numero_avistamientos_por_año(avistamientos:list[Avistamiento])->dict[int, int]:
    '''
    Devuelve el número de avistamientos observados en cada año.
             
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario en el que las claves son los años
         y los valores son el número de avistamientos observados en ese año
    '''
    res = {}
    for av in avistamientos:
        año = av.fechahora.year
        if año not in res:
            res[año] = 0
        res[año] += 1
    return res

### 4.4 Número de avistamientos por mes del año
def num_avistamientos_por_mes(avistamientos:list[Avistamiento])->dict[int, int]:
    '''
    Devuelve el número de avistamientos observados en cada mes del año.
    Usar la expresión .date().month para obtener el número del mes de un objeto datetime.
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:

    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:diccionario en el que las claves son los nombres de los meses y 
         los valores son el número de avistamientos observados en ese mes
    '''
    res = {}
    for av in avistamientos:
        mes = MESES[av.fechahora.month - 1]
        if mes not in res:
            res[mes] = 0
        res[mes] += 1
    return res

### 4.5 Coordenadas con mayor número de avistamientos
def coordenadas_mas_avistamientos(avistamientos:list[Avistamiento])->Coordenadas:
    '''
    Devuelve las coordenadas enteras que se corresponden con 
    la zona donde más avistamientos se han observado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: Coordenadas (sin decimales) que acumulan más avistamientos
    '''
    # Hay que seguir dos pasos:
    # 1. Construir un diccionario de recuentos: "Cuantos avistamientos por coordenadas enteras"
    conteo_por_coordenadas = {}
    for av in avistamientos:
        coordenadas = redondear(av.ubicacion)
        if coordenadas not in conteo_por_coordenadas:
            conteo_por_coordenadas[coordenadas] = 0
        conteo_por_coordenadas[coordenadas] += 1
    # 2.- Buscar la clave (coordenadas enteras) que tienen el mayor valor asociado (recuentos)
    # Si escribo esto: max(conteo_por_coordenadas.values())
    # ... me devolvería uno de los conteos (int), pero yo quiero devolver LA CLAVE (Coordenadas)
    coordenadas, _ = max(conteo_por_coordenadas.items(), key = lambda item:item[1])

    #return max(conteo_por_coordenadas.items(), key = lambda item:item[1])[0]
    #return max(conteo_por_coordenadas, key = lambda clave:conteo_por_coordenadas[clave])
    return coordenadas



### 4.6 Hora del día con mayor número de avistamientos
def hora_mas_avistamientos(avistamientos:list[Avistamiento])->int:
    ''' 
    Devuelve la hora del día (de 0 a 23) con mayor número de avistamientos
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: hora del día en la que se producen más avistamientos
      
    '''
    # Primer paso
    conteo_por_horas = {}
    for av in avistamientos:
        hora = av.fechahora.hour
        if hora not in conteo_por_horas:
            conteo_por_horas[hora] = 0
        conteo_por_horas += 1
    # Segundo paso
    #                      devuelve un item (clave, valor)
    #      =======================================================
    #                                                             accedo a la clave
    #                                                              =====
    return max(conteo_por_horas.items(), key = lambda item:item[1])[0]

    

### 4.7 Longitud media de los comentarios por estado
def longitud_media_comentarios_por_estado(avistamientos:list[Avistamiento])->dict[str,float]:
    '''
    Devuelve un diccionario en el que las claves son los estados donde se
    producen los avistamientos y los valores son la longitud media de los
    comentarios de los avistamientos en cada estado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario que almacena la longitud media de los comentarios (valores) por estado (claves)
    '''
    # 1. Hacer un dicc que agrupe en listas los tamaños de los comentarios por estados
    # (clave: estados, valores: lista de tamaños de comentarios)
    aux = {}
    for av in avistamientos:
        if av.estado not in aux:
            aux[av.estado] = []
        aux[av.estado].append(len(av.comentarios))
    
    # 2. Recorrer cada estado y lista anterior, y calcular la media de la lista
    res = {}
    for estado, lista_tams_comentarios in aux.items():
        media = sum(lista_tams_comentarios) / len(lista_tams_comentarios)
        res[estado] = media

    return res    

### 4.8 Porcentaje de avistamientos por forma
def porc_avistamientos_por_forma(avistamientos:list[Avistamiento])->dict[str,float]:  
    '''
    Devuelve un diccionario en el que las claves son las formas de los
    avistamientos, y los valores los porcentajes de avistamientos con cada forma.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:  diccionario que almacena los porcentajes de avistamientos (valores)
         por forma (claves)
    '''  
    # TODO: Para el miércoles 26 de noviembre
    pass

### 4.9 Avistamientos de mayor duración por estado
def avistamientos_mayor_duracion_por_estado(avistamientos:list[Avistamiento], n:int=3)->dict[str,Avistamiento]:
    '''
    Devuelve un diccionario que almacena los n avistamientos de mayor duración 
    en cada estado, ordenados de mayor a menor duración.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param n: número de avistamientos a almacenar por cada estado 
    :return: diccionario en el que las claves son los estados y los valores son listas con los "n" avistamientos de mayor duración de cada estado, ordenados de mayor a menor duración
    '''
    # TODO: Para el miércoles 26 de noviembre
    pass

### 4.10 Año con más avistamientos de una forma
def año_mas_avistamientos_forma(avistamientos:list[Avistamiento], forma:str)->int:
    '''
    Devuelve el año en el que se han observado más avistamientos
    de una forma dada.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param forma: forma del avistamiento 
    :return: año con mayor número de avistamientos de la forma dada
    '''
    pass


### 4.11 Estados con mayor número de avistamientos
def estados_mas_avistamientos(avistamientos:list[Avistamiento], n:int=5)->list[tuple[str,int]]:
    '''
    Devuelve una lista con los estados en los que se han observado
    más avistamientos, junto con el número de avistamientos,
    ordenados de mayor a menor número de avistamientos.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    :param n: número de estados a devolver 
    :return: lista con los estados donde se han observado más avistamientos,
         junto con el número de avistamientos, en orden decreciente
         del número de avistamientos y con un máximo de "limite" estados.
    '''
    pass  

### 4.12 Duración total de los avistamientos de cada año en un estado dado
def duracion_total_avistamientos_año(avistamientos:list[Avistamiento], estado:str)-> dict[int, int]:
    '''
    Devuelve un diccionario que almacena la duración total de los avistamientos 
    en cada año, para un estado dado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param estado: nombre del estado
    :return: diccionario en el que las claves son los años y los valores son números con la suma de las duraciones de los avistamientos observados ese año en el estado dado.
    '''
    pass

### 4.13 Fecha del avistamiento más reciente de cada estado
def avistamiento_mas_reciente_por_estado(avistamientos:list[Avistamiento])->dict[str, datetime]:
    '''
    Devuelve un diccionario que almacena la fecha del último avistamiento
    observado en cada estado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:  diccionario en el que las claves son los estados y los valores son 
         las fechas del último avistamientos observado en ese estado.
    '''
    pass