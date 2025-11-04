from datetime import datetime, date
from typing import NamedTuple
from coordenadas import Coordenadas

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
    pass

### 2.1 Número de avistamientos producidos en una fecha
def numero_avistamientos_fecha(avistamientos: list[Avistamiento], fecha: date)->int:
    ''' Avistamientos que se han producido en una fecha
    
    Toma como entrada una lista de avistamientos y una fecha.
    Devuelve el número de avistamientos que se han producido en esa fecha.

    :param avistamientos: lista de avistamientos
    :param fecha: fecha del avistamiento 
    :return:  Número de avistamientos producidos en la fecha 
    '''
    pass    

### 2.2 Número de formas observadas en un conjunto de estados
def formas_estados(avistamientos:list[Avistamiento], estados:set[str])->int:
    ''' 
    Devuelve el número de formas distintas observadas en avistamientos 
    producidos en alguno de los estados especificados.
    :param avistamientos: lista de tuplas con la información de los avistamientos
    :param estados: conjunto de estados para los que se quiere hacer el cálculo 
    :return: Número de formas distintas observadas en los avistamientos producidos en alguno de los estados indicados por el parámetro "estados"
    '''
    pass
    

### 2.3 Duración total de los avistamientos en un estado
def duracion_total(avistamientos:list[Avistamiento], estado:str)->int:
    ''' 
    Devuelve la duración total de los avistamientos de un estado. 
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param estado: estado para el que se quiere hacer el cálculo
    :return: duración total en segundos de todos los avistamientos del estado 
    '''
    pass


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
    pass


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
    pass


### 3.2 Avistamiento cercano a un punto con mayor duración
def avistamiento_cercano_mayor_duracion(avistamientos:list[Avistamiento], coordenadas:Coordenadas, radio:float=0.5)->tuple[int, str]:
    '''
    Devuelve la duración y los comentarios del avistamiento que más 
    tiempo ha durado de aquellos situados en el entorno de las
    coordenadas que se pasan como parámetro de entrada.
    El resultado debe ser una tupla de la forma (duración, comentarios)
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param coordenadas: tupla con latitud y longitud
    :param radio: radio de búsqueda
    :return: duración y comentarios del avistamiento más largo en el entorno de las coordenadas comentarios del avistamiento más largo
    '''
    pass


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
    pass


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
    pass
    

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
    pass


## 4 Operaciones con diccionarios

### 4.1 Avistamientos por fecha
def avistamientos_por_fecha(avistamientos:list[Avistamiento])->dict[date, list[Avistamiento]]:
    ''' 
    Devuelve un diccionario que indexa los avistamientos por fechas
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return diccionario en el que las claves son las fechas de los avistamientos 
         y los valores son conjuntos con los avistamientos observados en esa fecha
    '''
    pass


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
    pass

### 4.3 Número de avistamientos por año
def numero_avistamientos_por_año(avistamientos:list[Avistamiento])->dict[int, int]:
    '''
    Devuelve el número de avistamientos observados en cada año.
             
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario en el que las claves son los años
         y los valores son el número de avistamientos observados en ese año
    '''
    pass

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
    pass

### 4.5 Coordenadas con mayor número de avistamientos
def coordenadas_mas_avistamientos(avistamientos:list[Avistamiento])->Coordenadas:
    '''
    Devuelve las coordenadas enteras que se corresponden con 
    la zona donde más avistamientos se han observado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: Coordenadas (sin decimales) que acumulan más avistamientos
    '''
    pass

### 4.6 Hora del día con mayor número de avistamientos
def hora_mas_avistamientos(avistamientos:list[Avistamiento])->int:
    ''' 
    Devuelve la hora del día (de 0 a 23) con mayor número de avistamientos
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: hora del día en la que se producen más avistamientos
      
    '''
    pass

### 4.7 Longitud media de los comentarios por estado
def longitud_media_comentarios_por_estado(avistamientos:list[Avistamiento])->dict[str,float]:
    '''
    Devuelve un diccionario en el que las claves son los estados donde se
    producen los avistamientos y los valores son la longitud media de los
    comentarios de los avistamientos en cada estado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario que almacena la longitud media de los comentarios (valores) por estado (claves)
    '''
    pass 

### 4.8 Porcentaje de avistamientos por forma
def porc_avistamientos_por_forma(avistamientos:list[Avistamiento])->dict[str,float]:  
    '''
    Devuelve un diccionario en el que las claves son las formas de los
    avistamientos, y los valores los porcentajes de avistamientos con cada forma.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:  diccionario que almacena los porcentajes de avistamientos (valores)
         por forma (claves)
    '''  
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