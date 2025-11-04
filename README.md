# Ejercicio: Avistamientos
**Autores**: Daniel Mateos, Mariano González, Toñi Reina   **Revisores**: Fermín Cruz, Toñi Reina, José C. Riquelme.     **Última modificación:** 04/11/2025

En este ejercicio vamos a trabajar con un conjunto de datos con información sobre avistamientos de objetos voladores no identificados (OVNIs) en los Estados Unidos. El objetivo del ejercicio es leer estos datos y realizar distintas operaciones con ellos. Cada operación se implementará en una función distinta.


## 1. Carga de datos
Los datos se encuentran almacenados en un fichero en formato CSV codificado en UTF-8. Cada registro del fichero ocupa una línea y contiene los datos correspondientes a un avistamiento: fecha y hora en la que se produjo del avistamiento, ciudad y acrónimo del estado donde se produjo, forma observada del avistamiento, duración en segundos, una descripción textual del avistamiento y la latitud y longitud del lugar donde se produjo.

Estas son las primeras líneas del fichero (acortando la descripción del avistamiento). La primera línea es una cabecera que contiene los nombres de los campos del registro:

    datetime,city,state,shape,duration,comments,latitude,longitude
    07/04/2011 22:00,muncie,in,light,240, ((HOAX??)) 4th  of July ufo...,40.1933333,-85.3863889
    04/07/2005 17:01,deming (somewhere near),nm,changing,1200, ((NUFORC...,32.2686111,-107.7580556
    03/12/2010 19:56,erie,pa,changing,300, 3/12/10Viewed a comet like...,42.1291667,-80.0852778
    07/04/2013 22:25,seattle,wa,unknown,600, A RED Light was seen over...,47.6063889,-122.3308333


El tipo `Avistamiento` está implementado en el módulo `avistamientos.py`:

```python
Avistamiento = NamedTuple('Avistamiento', [
    ('fechahora', datetime),
    ('ciudad', str),
    ('estado', str),
    ('forma', str),
    ('duracion', int),
    ('comentarios', str),
    ('ubicacion', Coordenadas)
])
```

El tipo `Coordenadas` está implementado en el módulo `coordenadas.py`:

```python
Coordenadas = NamedTuple('Coordenadas', [
    ('latitud', float), ('longitud', float)
])
```


Implementa todas las funciones en el módulo `avistamientos.py`, salvo que se te diga lo contrario.

### 1.1 Función de lectura de datos

Implementa una función `lee_avistamientos` que reciba la ruta del archivo CSV y devuelva una `list[Avistamiento]`. 

El resultado de ejecutar las pruebas de este ejercicio debe ser el siguiente:

```
Se han leido 31682 avistamientos.
Los cinco avistamientos primeros son: 
        1-Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=240, comentarios='((HOAX??))  4th  of July ufo and a image of a ghostly alien face very disturbing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
        2-Avistamiento(fechahora=datetime.datetime(2005, 4, 7, 17, 1), ciudad='deming (somewhere near)', estado='nm', forma='changing', duracion=1200, comentarios='((NUFORC Note:  Helium-filled heliostat.  PD)) The shape-shifting object danced around at various speed  height and direction.', ubicacion=Coordenadas(latitud=32.2686111, longitud=-107.7580556))
        3-Avistamiento(fechahora=datetime.datetime(2010, 3, 12, 19, 56), ciudad='erie', estado='pa', forma='changing', duracion=300, comentarios='3/12/10Viewed a comet like object very bright fall out of the sky about 1 mile.', ubicacion=Coordenadas(latitud=42.1291667, longitud=-80.0852778))
        4-Avistamiento(fechahora=datetime.datetime(2013, 7, 4, 22, 25), ciudad='seattle', estado='wa', forma='unknown', duracion=600, comentarios='A RED Light was seen over the Highland Park area of Seattle (((Drone?))).', ubicacion=Coordenadas(latitud=47.6063889, longitud=-122.3308333))
        5-Avistamiento(fechahora=datetime.datetime(2003, 9, 9, 0, 40), ciudad='clearwater', estado='fl', forma='triangle', duracion=120, comentarios='bright light to east split to 3 triangle 1 hovered and 2 dropped.  ((NUFORC Note:  Titan 4 launch from Cape Canaveral.  PD))', ubicacion=Coordenadas(latitud=27.9655556, longitud=-82.8002778))
Los cinco avistamientos últimos son:
        1-Avistamiento(fechahora=datetime.datetime(2010, 7, 23, 21, 30), ciudad='huntington beach', estado='ca', forma='light', duracion=300, comentarios='Zig-zagging point of light.', ubicacion=Coordenadas(latitud=33.6602778, longitud=-117.9983333))
        2-Avistamiento(fechahora=datetime.datetime(2004, 7, 20, 0, 45), ciudad='federal way', estado='wa', forma='unknown', duracion=30, comentarios='Zig-zagging star(?) over Seattle.', ubicacion=Coordenadas(latitud=47.3225, longitud=-122.3113889))
        3-Avistamiento(fechahora=datetime.datetime(2004, 12, 2, 20, 0), ciudad='carrollton', estado='va', forma='light', duracion=3600, comentarios='ZIG-ZAGGING STARLIKE OBJECT', ubicacion=Coordenadas(latitud=36.9466667, longitud=-76.5608333))
        4-Avistamiento(fechahora=datetime.datetime(2008, 3, 31, 0, 0), ciudad='eagle river', estado='ak', forma='light', duracion=1200, comentarios='Zig-zaging light moves over north horizon of Alaska town.', ubicacion=Coordenadas(latitud=61.3213889, longitud=-149.5677778))
        5-Avistamiento(fechahora=datetime.datetime(2003, 12, 5, 11, 0), ciudad='stafford', estado='va', forma='light', duracion=300, comentarios='Zipping White Light.', ubicacion=Coordenadas(latitud=38.4219444, longitud=-77.4086111))
 ```   

## 2. Operaciones de filtrado, conteo y suma

### 2.1 Número de avistamientos producidos en una fecha

Función que obtiene el número total de avistamientos que se han producido en una fecha determinada, dada por su día, mes y año. Se contarán, por tanto, los avistamientos que hayan tenido lugar a cualquier hora del día.

El resultado de ejecutar las pruebas de este ejercicio debe ser el siguiente:
```
    El día 01/05/2005 se produjeron 5 avistamientos
```    

### 2.2 Número de formas observadas en un conjunto de estados

Función que obtiene el número de formas distintas que presentaron los avistamientos observados en uno o varios estados. 


El resultado del test debe ser:
```
    Número de formas distintas observadas en los estados nm, in, pa, wa: 23
```    

### 2.3 Duración total de los avistamientos en un estado

Función que devuelve la duración total en segundos de los avistamientos que se han observado en un estado. 

El resultado del test debe ser:
```
    Duración total de los avistamientos en in: 3318305 segundos.
    Duración total de los avistamientos en nm: 3211887 segundos.
    Duración total de los avistamientos en pa: 1241235 segundos.
    Duración total de los avistamientos en wa: 1822712 segundos.
```    

### 2.4 Avistamientos cercanos a una ubicación

Función que calcula un conjunto con los avistamientos cercanos a una ubicacion dada. Concretamente, vamos a obtener los avistamientos que se encuentren dentro de un determinado radio de distancia de la ubicación.

Para calcular distancias terrestres, utiliza la distancia euclidea (debes implementar la función `distancia` en el módulo `coordenadas.py`). 

El resultado del test debería ser:
```
 Avistamientos cercanos a (40.1933333, -85.3863889):
	1-Avistamiento(fechahora=datetime.datetime(2007, 6, 20, 22, 30), ciudad='muncie', estado='in', forma='triangle', duracion=120, comentarios='Black triangle with 2 bright white lights on back 2 points floated by  no sound.  paused lights turned to orange  craft disappeared', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	2-Avistamiento(fechahora=datetime.datetime(2002, 5, 21, 22, 0), ciudad='muncie', estado='in', forma='changing', duracion=360, comentarios='It was the shape of a brihgte star than it Kinda turned recktangular shape and started flying. The center was rad and the ends yellow.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	3-Avistamiento(fechahora=datetime.datetime(2011, 12, 2, 23, 0), ciudad='muncie', estado='in', forma='fireball', duracion=3600, comentarios='1 orb hovering in sky and exploding in a ball of blue light before disappearing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	4-Avistamiento(fechahora=datetime.datetime(2010, 11, 8, 23, 30), ciudad='muncie', estado='in', forma='light', duracion=2700, comentarios='Strobing Star like objects in the sky being observed by aircraft', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	5-Avistamiento(fechahora=datetime.datetime(1958, 7, 1, 21, 0), ciudad='muncie', estado='in', forma='unknown', duracion=300, comentarios='A star sized object circled the sky and then shot straight out of sight at very great speed.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	6-Avistamiento(fechahora=datetime.datetime(2012, 9, 26, 20, 40), ciudad='muncie', estado='in', forma='circle', duracion=300, comentarios='Glowing Fire Colored Orb in the Sky', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	7-Avistamiento(fechahora=datetime.datetime(2009, 9, 1, 22, 0), ciudad='muncie', estado='in', forma='sphere', duracion=300, comentarios='Bright orange light in the northwest sky near the Muncie airport.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	8-Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=180, comentarios='saw glowing orange ball of light and ghostly face', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	9-Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=240, comentarios='((HOAX??))  4th  of July ufo and a image of a ghostly alien face very disturbing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	10-Avistamiento(fechahora=datetime.datetime(2007, 2, 24, 16, 0), ciudad='muncie', estado='in', forma='rectangle', duracion=120, comentarios='((HOAX??))  Red  Rectangle object at constant speed that could not be described as a known thing in the air.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
```    

## 3 Operaciones con máximos, mínimos y ordenación

### 3.1 Avistamiento de una forma con mayor duración

Función que obtiene el avistamiento de mayor duración de entre todos los avistamientos que tienen una forma determinada. 

El resultado del test debe ser:
```
    Avistamiento de forma 'circle' de mayor duración: Avistamiento(fechahora=datetime.datetime(1984, 3, 15, 20, 0), ciudad='griffin', estado='ga', forma='circle', duracion=7894800, comentarios='7 large yellow lights with red center  estimated by distance to be at least 400 feet across  seen form top of hill just above tree line', ubicacion=Coordenadas(latitud=33.2466667, longitud=-84.2641667))
```    

### 3.2 Avistamiento cercano a un punto con mayor duración

Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada; es decir, la distancia entre la ubicación del avistamiento y las coordenadas que se pasan como parámetro de entrada debe ser menor al radio que también aparece como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios).

El resultado del test debe ser:
```
    Duración del avistamiento más largo en un entorno de radio 0.5 sobre las coordenadas (40.1933333, -85.3863889): 3600
    Comentario: 1 orb hovering in sky and exploding in a ball of blue light before disappearing.
```    

### 3.3 Avistamientos producidos entre dos fechas

Función que devuelve una lista con los avistamientos observados entre una fecha inicial y una fecha final, ambas inclusive. La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. Si la fecha inicial es None, se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es None, se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son None, se devolverá la lista de avistamientos completa. 


El resultado del test debe ser:
```
Mostrando los avistamientos entre el 1 de May de 2005 y el 1 de May de 2005:
Total avistamientos 5
Mostrando los avistamientos anteriores al 1 de May de 2005: 
Total avistamientos 12639
Mostrando los avistamientos posteriores al 1 de May de 2005:
Total avistamientos 19048
```    

### 3.4 Avistamiento de un año con el comentario más largo

Función que devuelve el avistamiento con el comentario más largo, de entre todos los avistamientos observados en un año dado y cuyo comentario incluye una palabra concreta.

El resultado del test debe ser:
```
    El avistamiento con el comentario más largo de 2005 incluyendo la palabra "ufo" es:
    Avistamiento(fechahora=datetime.datetime(2005, 6, 15, 12, 0), ciudad='fort myers', estado='fl', forma='disk', duracion=1200, comentarios="hey all you ufo peeps i am only writing this to verify another guys sighting here in swf there here alot ufo's and there disturbing the", ubicacion=Coordenadas(latitud=26.6402778, longitud=-81.8725))
```    

### 3.5 Media de días entre avistamientos consecutivos

Función que devuelve la media de días transcurridos entre dos avistamientos consecutivos en el tiempo. La función permite hacer el cálculo para todos los avistamientos, o solo para los de un año concreto.

El resultado del test debe ser:
```
    La media de días entre dos avistamientos consecutivos es: 1.1982576307566049
    La media de días entre dos avistamientos consecutivos del año 1979 es: 4.089887640449438
```    

## 4 Operaciones con diccionarios

### 4.1 Avistamientos por fecha

Función que crea un diccionario que relaciona las fechas con los avistamientos observados en dichas fechas. Es decir, un diccionario cuyas claves son las fechas y cuyos valores son los conjuntos de avistamientos observados en cada fecha. 

El resultado del test debe ser:
```
Avistamientos por fecha (mostrando fechas específicas):
1986-09-18 ==>
        1-Avistamiento(fechahora=datetime.datetime(1986, 9, 18, 16, 0), ciudad='owensboro', estado='ky', forma='cylinder', duracion=180, comentarios='Baton-shaped object moving end-over-end in clear afternoon sky.', ubicacion=Coordenadas(latitud=37.7741667, longitud=-87.1133333))
1986-07-20 ==>
        1-Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 23, 30), ciudad='new haven', estado='ct', forma='triangle', duracion=600, comentarios='Black Triangle spotted in CT back in mid-eighties', ubicacion=Coordenadas(latitud=41.3080556, longitud=-72.9286111))
        2-Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 1, 0), ciudad='tucson', estado='az', forma='light', duracion=900, comentarios='Lights and beems over AZ desert', ubicacion=Coordenadas(latitud=32.2216667, longitud=-110.9258333))
        3-Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 3, 30), ciudad='san marcos', estado='tx', forma='rectangle', duracion=600, comentarios='Was looking at all kinds of sites that came up on the Yahoo web site.  It talked about how people are looking at UFO sites.  It reminde', ubicacion=Coordenadas(latitud=29.8830556, longitud=-97.9411111))
```    

### 4.2 Formas de avistamientos por mes

Función que devuelve un diccionario que indexa las distintas formas de avistamientos por los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las formas distintas observadas en dicho mes. 

El resultado del test debe ser:
```
Enero (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Febrero (22 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'delta', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Marzo (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Abril (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Mayo (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Junio (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Julio (22 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'delta', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Agosto (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Septiembre (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Octubre (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
Noviembre (23 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'delta', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'round', 'sphere', 'teardrop', 'triangle', 'unknown']
Diciembre (21 formas) ==> ['changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle', 'sphere', 'teardrop', 'triangle', 'unknown']
```    

### 4.3 Número de avistamientos por año

Función que crea un diccionario que relaciona cada año con el número de avistamientos observados en dicho año. Es decir, un diccionario cuyas claves son los años y cuyos valores son el número de avistamientos observados en cada año. 

El resultado del test debe ser:
```
    Número de avistamientos por año:
    	2011: 2200
    	2005: 1582
    	2010: 1731
    	2013: 2940
    	2003: 1505
    	2007: 1685
    	1964: 35
    	2004: 1591
    	2014: 978
    	2008: 1978
    	2000: 1072
    	1986: 69
    	1997: 513
    	1983: 48
    	2006: 1450
    	1991: 84
    	1985: 82
    	1999: 1122
    	1990: 98
    	2001: 1214
    	2012: 3139
    	1981: 71
    	2002: 1169
    	1993: 98
    	1994: 167
    	2009: 1790
    	1996: 206
    	1989: 97
    	1984: 70
    	1965: 70
    	1978: 123
    	1971: 38
    	1969: 49
    	1976: 117
    	1998: 704
    	1987: 85
    	1920: 1
    	1966: 76
    	1951: 9
    	1967: 79
    	1961: 18
    	1959: 26
    	1995: 210
    	1992: 94
    	1974: 103
    	1975: 108
    	1979: 90
    	1954: 20
    	1973: 83
    	1945: 4
    	1947: 13
    	1952: 19
    	1955: 7
    	1963: 33
    	1968: 85
    	1970: 40
    	1972: 58
    	1980: 97
    	1957: 30
    	1953: 15
    	1950: 5
    	1958: 21
    	1988: 100
    	1982: 74
    	1960: 24
    	1956: 18
    	1977: 102
    	1937: 2
    	1948: 4
    	1962: 28
    	1946: 4
    	1949: 6
    	1910: 1
    	1939: 1
    	1944: 1
    	1934: 1
    	1936: 1
    	1925: 1
```     

### 4.4 Número de avistamientos por mes del año

Función que devuelve el número de avistamientos observados en cada mes del año. 

El resultado del test debe ser:
```
Número de avistamientos por mes
        Enero: 2185
        Febrero: 1825
        Marzo: 2132
        Abril: 2126
        Mayo: 2082
        Junio: 3129
        Julio: 3782
        Agosto: 3336
        Septiembre: 2989
        Octubre: 3089
        Noviembre: 2756
        Diciembre: 2251
```    

### 4.5 Coordenadas con mayor número de avistamientos

Función que devuelve las coordenadas redondeadas que se corresponden con la zona donde más avistamientos se han observado. Por ejemplo, si hay avistamientos en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), la zona con más avistamientos corresponde a las coordenadas (40, -8) con 2 avistamientos. 

Implementa antes la función `redondear` en el módulo `coordenadas.py` que recibe unas coordenadas y devuelve las coordenadas redondeadas. Usa la función `round` para redondear.

El resultado del test debe ser:
```
Coordenadas redondeadas de la región en la que se observaron más avistamientos: (34.0, -118.0)
```    

### 4.6 Hora del día con mayor número de avistamientos

Función que devuelve la hora del día (de 0 a 23) en la que se han observado un mayor número de avistamientos. 

El resultado del test debe ser:
```
Hora en la que se han observado más avistamientos: 21
```    

### 4.7 Longitud media de los comentarios por estado

Función que devuelve un diccionario en el que las claves son los estados donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos observados en cada estado. 

El resultado del test debe ser:
```
    Mostrando la media del tamaño de los comentarios de los avistamientos de los estados 'in','nm', 'pa' y 'wa':
    	in: 82.87873754152824
    	nm: 79.51461988304094
    	pa: 78.50746268656717
    	wa: 82.73590021691975
		...
```    

### 4.8 Porcentaje de avistamientos por forma

Función que devuelve un diccionario en el que las claves son las formas de los avistamientos, y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos. 

El resultado del test debe ser:
```
Porcentajes de avistamientos de las distintas formas
    	changing: 2.47%
    	chevron: 1.29%
    	cigar: 2.59%
    	circle: 9.54%
		...
```    

### 4.9 Avistamientos de mayor duración por estado

Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor duración observados en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos de mayor duración. 

Puedes llamar a la función `agrupa_avistamientos_por_estado` definida anteriormente como uno de los pasos de la resolución de este ejercicio.

El resultado del test debe ser:
```
    Mostrando los 3 avistamientos de mayor duración de los estados 'in' y 'nm':
    	 in
    		 Avistamiento(fechahora=datetime.datetime(2012, 4, 22, 21, 0), ciudad='cedar lake', estado='in', forma='light', duracion=2631600, comentarios='I have seen the same object in the sky for the past month. It always appears around 21:00pm and usually stays there until 23:00. It mov', ubicacion=Coordenadas(latitud=41.3647222, longitud=-87.4411111))
    		 Avistamiento(fechahora=datetime.datetime(1968, 5, 12, 9, 0), ciudad='valparaiso', estado='in', forma='unknown', duracion=109800, comentarios="1968  Grey Squares in Sky  I'll take you with me cuz you're my friend  9 o'clock past bozo circus noon  scary man  doll burning", ubicacion=Coordenadas(latitud=41.4730556, longitud=-87.0611111))
    		 Avistamiento(fechahora=datetime.datetime(2001, 2, 19, 19, 0), ciudad='carmel', estado='in', forma='light', duracion=37800, comentarios='Carmel  Indiana on US 31.  On several occasions have noticed a bright light to the south west.  Thought it was venus  however  this eve', ubicacion=Coordenadas(latitud=39.9783333, longitud=-86.1180556))
    	 nm
    		 Avistamiento(fechahora=datetime.datetime(2011, 5, 4, 9, 0), ciudad='albuquerque', estado='nm', forma='other', duracion=2102400, comentarios='((HOAX??))  Get the metal out of my body', ubicacion=Coordenadas(latitud=35.0844444, longitud=-106.6505556))
    		 Avistamiento(fechahora=datetime.datetime(1945, 8, 16, 11, 30), ciudad='san antonio', estado='nm', forma='oval', duracion=777600, comentarios="THE CRAFT APPEARED TO HAVE DECENDED AT AN ANGL  SKIDDED OVER A HUNDRED YARDS PUSHING THE DIRT IN FRONT OF IT AND BURIED IT'S SELF", ubicacion=Coordenadas(latitud=33.9177778, longitud=-106.8652778))
    		 Avistamiento(fechahora=datetime.datetime(1997, 3, 20, 13, 0), ciudad='santa fe', estado='nm', forma='triangle', duracion=28800, comentarios='Was MACHINED by ME ((name deleted)) at LOS ALAMOS NATIONAL labs.  Triangle of BERYLIUM METAL.', ubicacion=Coordenadas(latitud=35.6869444, longitud=-105.9372222))
```    

### 4.10 Año con más avistamientos de una forma

Función que devuelve el año en el que se han observado más avistamientos de una forma dada. 

El resultado del test debe ser:
```
    Año con más avistamientos de tipo 'circle': 2013
```    

### 4.11 Estados con mayor número de avistamientos

Función que devuelve una lista con el nombre y el número de avistamientos de los estados con mayor número de avistamientos, ordenados de mayor a menor número de avistamientos. Si no se indica nada, se obtendrán los cinco estados con más avistamientos.

El resultado del test debe ser:

```
Estados con más avistamientos, de mayor a menor nº de avistamientos: [('ca', 4286), ('fl', 1867), ('wa', 1844), ('tx', 1693), ('ny', 1459)]
``` 

### 4.12 Duración total de los avistamientos de cada año en un estado dado

Función que devuelve un diccionario que relaciona cada año con la suma de las duraciones de todos los avistamientos observados durante ese año en un estado dado. 

El resultado del test debe ser:
```
Mostrando la duración total de los avistamientos por año en el estado ca
        2004: 336497
        2005: 197987
        1997: 41973
        2008: 163570
        2007: 470490
        1994: 10533943
		...
```    

### 4.13 Fecha del avistamiento más reciente de cada estado

Función que devuelve un diccionario que relaciona cada estado con la fecha del último avistamiento observado en el estado.

Puedes llamar a la función `agrupa_avistamientos_por_estado` definida anteriormente como uno de los pasos para resolver este ejercicio.

El resultado del test debe ser:

```
Mostrando la fecha del último avistamiento por estado
        in: 2014-04-12 22:23:00
        nm: 2014-04-24 08:45:00
        pa: 2014-05-01 22:50:00
        wa: 2014-05-06 21:00:00
        fl: 2014-05-07 20:30:00
		...
```    
