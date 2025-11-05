## Definición de tipos
# Creación de una tupla con nombre para las coordenadas
import math
from typing import NamedTuple

Coordenadas = NamedTuple('Coordenadas', [
    ('latitud', float), ('longitud', float)
])

def distancia(coordenadas1:Coordenadas, coordenadas2:Coordenadas)->float:
    '''Devuelve la distancia euclidea entre dos coordenadas

    :param coordenadas1: Coordenadas del primer punto
    :param coordenadas2: Coordenadas del segundo punto
    :return: La distancia entre las dos coordenadas dadas como parámetro
    '''
    return math.sqrt((coordenadas1.latitud - coordenadas2.latitud) ** 2 + 
            (coordenadas1.longitud - coordenadas2.longitud) ** 2)    
    

def redondear(coordenadas:Coordenadas)->Coordenadas:
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    :param coordenadas: Coordenadas que se quieren redondear
    :return: Las coordenadas redondeadas
    '''
    return Coordenadas(round(coordenadas.latitud, 0), round(coordenadas.longitud, 0))