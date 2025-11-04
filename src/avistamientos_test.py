import avistamientos as av
from avistamientos import Avistamiento
from datetime import datetime, date
from coordenadas import *
from typing import Iterable, TypeVar

K = TypeVar('K')
V = TypeVar('V')


def mostrar_iterable_enumerado(iterable:Iterable)->None:
    for indx, elem in enumerate(iterable, 1):
        print(f"\t{indx}-{elem}")

def mostrar_diccionario(dicc:dict[K,V])->None:
    for clave, valor in dicc.items():
        print(f"{clave} ==>")
        mostrar_iterable_enumerado(valor)

def mostrar_diccionario2(dicc:dict[K,V])->None:
    for clave, valor in dicc.items():
        print(f"\t{clave}: {valor}")

def test_lee_avistamientos(avistamientos:list[Avistamiento])->None:
    print(f"Se han leido {len(avistamientos)} avistamientos.")
    print("Los cinco avistamientos primeros son: ")
    mostrar_iterable_enumerado(avistamientos [:5])
    print("Los cinco avistamientos últimos son: ")
    mostrar_iterable_enumerado(avistamientos [-5:])

def test_numero_avistamientos_fecha(avistamientos:list[Avistamiento], fecha:datetime)->None:
    res = av.numero_avistamientos_fecha(avistamientos, fecha)
    fechastr = fecha.strftime("%m/%d/%Y")
    print(f"El día {fechastr} se produjeron {res} avistamientos")

def test_formas_estados(avistamientos:list[Avistamiento], estados:set[str])->int:
    estados_str = ', '.join(estados)
    res = av.formas_estados(avistamientos, estados)
    print(f"Número de formas distintas observadas en los estados {estados_str}: {res}")
    
def test_duracion_total(avistamientos:list[Avistamiento], estado:str)->None:
    res = av.duracion_total(avistamientos, estado)
    print(f"Duración total de los avistamientos en {estado}: {res} segundos.")
 
def test_avistamientos_cercanos_ubicacion(avistamientos:list[Avistamiento], ubicacion:Coordenadas, radio:float)->None:
    res = av.avistamientos_cercanos_ubicacion(avistamientos, ubicacion,radio)
    print(f"Avistamientos cercanos a ({ubicacion.latitud}, {ubicacion.longitud}):" )
    mostrar_iterable_enumerado(res)

def test_avistamiento_mayor_duracion(avistamientos: list[Avistamiento], forma:str)->None:
    res = av.avistamiento_mayor_duracion(avistamientos, forma)
    print(f"Avistamiento de forma \'{forma}\' de mayor duración: {res}")

def test_avistamiento_cercano_mayor_duracion(avistamientos:list[Avistamiento], coordenadas:Coordenadas, radio:float=0.5)->None:
    res = av.avistamiento_cercano_mayor_duracion(avistamientos, coordenadas, radio)
    comentario, duracion=None, None
    if res!= None:
        comentario,duracion=res
    print(f"Duración del avistamiento más largo en un entorno de radio {radio} sobre\
             las coordenadas {coordenadas.latitud}, {coordenadas.longitud}: {duracion}")
    print(f"Comentario: {comentario}")

def test_avistamientos_fechas(avistamientos:list[Avistamiento], fecha_inicial:date|None=None, fecha_final:date|None=None)->None:
    avistamientos_fec = av.avistamientos_fechas(avistamientos, \
                                         fecha_inicial, fecha_final)
    print(msg_avistamientos_fecha(fecha_inicial, fecha_final))     
    #mostrar_iterable_enumerado(avistamientos_fec)
    print(f"Total avistamientos {len(avistamientos_fec)}")                                
  
### Función auxliar para generar un mensaje personalizado                
def msg_avistamientos_fecha(fecha_inicial:date|None=None, fecha_final:date|None=None)->str:    
    if fecha_inicial == None and fecha_final == None:
        msg = "Mostrando todos los avistamientos"
    elif fecha_inicial== None:
        mes_final = fecha_final.strftime("%B")
        msg = f"Mostrando los avistamientos anteriores al {fecha_final.day} de {mes_final} de {fecha_final.year}: "
    elif fecha_final== None:
        mes_inicial = fecha_inicial.strftime("%B")
        msg = f"Mostrando los avistamientos posteriores al {fecha_inicial.day} de {mes_inicial} de {fecha_inicial.year}: "
    else:
        mes_inicial = fecha_inicial.strftime("%B")
        mes_final = fecha_final.strftime("%B")
        msg= f"Mostrando los avistamientos entre el {fecha_inicial.day} de {mes_inicial} de {fecha_inicial.year} y "+ \
        f"el {fecha_final.day} de {mes_final} de {fecha_final.year}: "
    return msg

def test_comentario_mas_largo(avistamientos:list[Avistamiento], anyo:int, palabra:str)->None:
    print(f'El avistamiento con el comentario más largo de {anyo} incluyendo la palabra "{palabra}" es:')     
    print(av.comentario_mas_largo(avistamientos, anyo, palabra))

def test_media_dias_entre_avistamientos(avistamientos:list[Avistamiento], anyo:int|None=None)->None:
    msg = "La media entre dos avistamientos consecutivos"
    if anyo != None:
        msg+= f" del año {anyo}"
    msg+= " es"
    media = av.media_dias_entre_avistamientos(avistamientos, anyo)
    print(f"{msg}: {media}")

def test_avistamientos_por_fecha(avistamientos:list[Avistamiento])->None:
    indice = av.avistamientos_por_fecha(avistamientos)
    print("Avistamientos por fecha (mostrando fechas específicas):")
    fechas_a_mostrar = [date(1986, 9, 18), date(1986, 7, 20)]
    mini_dict = {fecha: indice[fecha] for fecha in fechas_a_mostrar if fecha in indice}
    mostrar_diccionario(mini_dict)

def test_formas_por_mes(avistamientos:list[Avistamiento])->None:
    indice = av.formas_por_mes(avistamientos)
    for mes in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]:
        formas = indice.get(mes, set())
        print(f"{mes} ({len(formas)} formas) ==> {sorted(formas)}")

def test_numero_avistamientos_por_año(avistamientos:list[Avistamiento])->None:  
    d = av.numero_avistamientos_por_año(avistamientos)
    print("Número de avistamientos por año:")
    mostrar_diccionario2(d)

def test_num_avistamientos_por_mes(avistamientos:list[Avistamiento])->None:  
    d = av.num_avistamientos_por_mes(avistamientos)
    print("Número de avistamientos por mes")
    mostrar_diccionario2(d)

def test_coordenadas_mas_avistamientos(avistamientos:list[Avistamiento])->None:
    res = av.coordenadas_mas_avistamientos(avistamientos)
    print(f"Coordenadas redondeadas de la región en la que se observaron más avistamientos: ({res.latitud}, {res.longitud})") 

def test_hora_mas_avistamientos(avistamientos:list[Avistamiento])->None:
    res = av.hora_mas_avistamientos(avistamientos)
    print(f"Hora en la que se han observado más avistamientos: {res}")

def test_longitud_media_comentarios_por_estado(avistamientos:list[Avistamiento])->None:
    res = av.longitud_media_comentarios_por_estado(avistamientos)
    print("Mostrando la media de la longitud de los comentarios de los avistamientos de los estados:")
    mostrar_diccionario2(res)

def test_porc_avistamientos_por_forma(avistamientos:list[Avistamiento])->None:
    res = av.porc_avistamientos_por_forma(avistamientos)
    print("Porcentajes de avistamientos de las distintas formas")
    mostrar_diccionario2(res)

def test_avistamientos_mayor_duracion_por_estado(avistamientos:list[Avistamiento], n:int=3)->None:
    res = av.avistamientos_mayor_duracion_por_estado(avistamientos, n)
    print(f"Mostrando los {n} avistamientos de mayor duración por estado")
    mostrar_diccionario(res)

def test_año_mas_avistamientos_forma(avistamientos:list[Avistamiento], forma:str)->None:
    año = av.año_mas_avistamientos_forma(avistamientos, forma)
    print(f"Año con más avistamientos de tipo '{forma}': {año}")

def test_estados_mas_avistamientos(avistamientos:list[Avistamiento], n:int=5)->None:
    estados = av.estados_mas_avistamientos(avistamientos, n)
    print(f"Estados con más avistamientos, de mayor a menor nº de avistamientos: {estados}")

def test_duracion_total_avistamientos_año(avistamientos:list[Avistamiento], estado:str)->None:
    indice = av.duracion_total_avistamientos_año(avistamientos, estado)
    print(f"Mostrando la duración total de los avistamientos por año en el estado {estado}")
    mostrar_diccionario2(indice)

def test_avistamiento_mas_reciente_por_estado(avistamientos:list[Avistamiento])->None:
    indice = av.avistamiento_mas_reciente_por_estado(avistamientos)
    print("Mostrando la fecha del último avistamiento por estado")
    mostrar_diccionario2(indice)

def test_ej2_1(avistamientos:list[Avistamiento])->None:
    print("2.1" , "#"*70)
    fecha = datetime(2005, 5, 1).date()
    test_numero_avistamientos_fecha(avistamientos, fecha)

def test_ej2_2(avistamientos:list[Avistamiento])->None:
    print("2.2" , "#"*70)
    conjunto_estados = {'in', 'nm', 'pa', 'wa'}
    test_formas_estados(avistamientos, conjunto_estados)

def test_ej2_3(avistamientos:list[Avistamiento])->None:
    print("2.3" , "#"*70)
    conjunto_estados = {'in', 'nm', 'pa', 'wa'}
    for estado in conjunto_estados:
        test_duracion_total(avistamientos, estado)

def test_ej2_4(avistamientos:list[Avistamiento])->None:
    print("2.4" , "#"*70)
    coordenadas = Coordenadas(40.1933333,-85.3863889)
    radio = 0.1        
    test_avistamientos_cercanos_ubicacion(avistamientos,coordenadas, radio)

def test_ej3_1(avistamientos:list[Avistamiento])->None:
    print("3.1" , "#"*70)
    forma = 'circle'
    test_avistamiento_mayor_duracion(avistamientos, forma)

def test_ej3_2(avistamientos:list[Avistamiento])->None:
    print("3.2" , "#"*70)
    coordenadas = Coordenadas(40.1933333,-85.3863889)
    test_avistamiento_cercano_mayor_duracion(avistamientos, coordenadas)

def test_ej3_3(avistamientos:list[Avistamiento])->None:
    print("3.3" , "#"*70)
    f1 =  datetime(2005,5,1).date()
    f2 = datetime(2005,5,1).date()
    test_avistamientos_fechas(avistamientos, f1, f2)
    test_avistamientos_fechas(avistamientos,  fecha_final=f1)
    test_avistamientos_fechas(avistamientos,  fecha_inicial=f1)

def test_ej3_4(avistamientos:list[Avistamiento])->None:
    print("3.4" , "#"*70)
    test_comentario_mas_largo(avistamientos, 2005, "ufo")

def test_ej3_5(avistamientos:list[Avistamiento])->None:
    print("3.5" , "#"*70)
    test_media_dias_entre_avistamientos(avistamientos)
    test_media_dias_entre_avistamientos(avistamientos, 1979)

def test_ej4_1(avistamientos:list[Avistamiento])->None:
    print("4.1" , "#"*70)
    test_avistamientos_por_fecha(avistamientos)

def test_ej4_2(avistamientos:list[Avistamiento])->None:
    print("4.2" , "#"*70)
    test_formas_por_mes(avistamientos)

def test_ej4_3(avistamientos:list[Avistamiento])->None:
    print("4.3" , "#"*70)
    test_numero_avistamientos_por_año(avistamientos)

def test_ej4_4(avistamientos:list[Avistamiento])->None:
    print("4.4" , "#"*70)
    test_num_avistamientos_por_mes(avistamientos)

def test_ej4_5(avistamientos:list[Avistamiento])->None:
    print("4.5" , "#"*70)
    test_coordenadas_mas_avistamientos(avistamientos)

def test_ej4_6(avistamientos:list[Avistamiento])->None:
    print("4.6" , "#"*70)
    test_hora_mas_avistamientos(avistamientos)

def test_ej4_7(avistamientos:list[Avistamiento])->None:
    print("4.7" , "#"*70)
    test_longitud_media_comentarios_por_estado(avistamientos)

def test_ej4_8(avistamientos:list[Avistamiento])->None:
    print("4.8" , "#"*70)
    test_porc_avistamientos_por_forma(avistamientos)

def test_ej4_9(avistamientos:list[Avistamiento])->None:
    print("4.9" , "#"*70)
    test_avistamientos_mayor_duracion_por_estado(avistamientos)

def test_ej4_10(avistamientos:list[Avistamiento])->None:
    print("4.10" , "#"*70)
    test_año_mas_avistamientos_forma(avistamientos, 'circle')

def test_ej4_11(avistamientos:list[Avistamiento])->None:
    print("4.11" , "#"*70)
    test_estados_mas_avistamientos(avistamientos)

def test_ej4_12(avistamientos:list[Avistamiento])->None:
    print("4.12" , "#"*70)
    test_duracion_total_avistamientos_año(avistamientos, 'ca')

def test_ej4_13(avistamientos:list[Avistamiento])->None:
    print("4.13" , "#"*70)
    test_avistamiento_mas_reciente_por_estado(avistamientos)

def main():
    avistamientos = av.lee_avistamientos("data/ovnis.csv")
    test_lee_avistamientos(avistamientos)

    test_ej2_1(avistamientos)
    test_ej2_2(avistamientos)
    test_ej2_3(avistamientos)
    test_ej2_4(avistamientos)
    test_ej3_1(avistamientos)
    test_ej3_2(avistamientos)
    test_ej3_3(avistamientos)
    test_ej3_4(avistamientos)
    test_ej3_5(avistamientos)
    test_ej4_1(avistamientos)
    test_ej4_2(avistamientos)
    test_ej4_3(avistamientos)
    test_ej4_4(avistamientos)
    test_ej4_5(avistamientos)
    test_ej4_6(avistamientos)
    test_ej4_7(avistamientos)
    test_ej4_8(avistamientos)
    test_ej4_9(avistamientos)
    test_ej4_10(avistamientos)
    test_ej4_11(avistamientos)
    test_ej4_12(avistamientos)
    test_ej4_13(avistamientos)

if __name__=="__main__":
    main()
