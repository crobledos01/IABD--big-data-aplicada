from pyspark.sql import SparkSession
import shutil
import os

spark = SparkSession.builder.appName('Basics').master("local[*]").getOrCreate()

sc = spark.sparkContext

# EJERCICIO 1: cargar ambos archivos como RDD y unirlos
rdd_1 = sc.textFile('/content/drive/MyDrive/Big_Data_IA/Big Data Aplicado/Spark-1/laliga.txt')
rdd_2 = sc.textFile('/content/drive/MyDrive/Big_Data_IA/Big Data Aplicado/Spark-1/laliga2.txt')

partidos = rdd_1.union(rdd_2)

# EJERCICIO 2: obtener todos los equipos que han participado

equipos = partidos.flatMap(
    lambda linea: [linea.split(",")[0], linea.split(",")[1]]
)

print(f"2. Los equipos participantes. Son: ")
print(equipos.distinct().collect())

# EJERCICIO 3: contar cuántos partidos hay
print(f"3. Hay un total de {equipos.distinct().count()} equipos")

# EJERCICIO 4: obtener los partidos en los que el local haya marcado más de un gol
local_mas_1 = partidos.filter(
    lambda linea: int(linea.split(",")[2]) > 1
)

print("4. Los partidos en los que el local ha marcado más de un gol son: ")
print(local_mas_1.collect())

# EJERCICIO 5: calcula el total de goles en todos los partidos
goles = partidos.map(
    lambda linea: int(linea.split(",")[2]) + int(linea.split(",")[3])
)

total_goles = goles.reduce(lambda a, b: a + b)

print(f"5. Se han marcado {total_goles} goles entre todos los partidos")

# EJERCICIO 6: obtener los 3 primeros partidos del rdd combinado
primeros_3 = partidos.take(3)
print("6. Los tres primeros partidos del rdd son: ")
print(primeros_3)

# EJERCICIO 7: recoge todos los equipos distintos en el driver
equipos_driver = equipos.distinct().collect()

print("7. Equipos distintos recogidos en el driver:")
print(equipos_driver)

# EJERCICIO 8: guarda en disco los equipos distintos
# (El if del principio es para eliminar el archivo si ya existe)
if os.path.exists("equipos_futbol"):
    shutil.rmtree("equipos_futbol")

equipos.distinct().saveAsTextFile("equipos_futbol")

# EXTRA 1: obtener los goles totales por equipo

goles_por_equipo = partidos.flatMap(
    lambda linea: [
        (linea.split(",")[0], int(linea.split(",")[2])),
        (linea.split(",")[1], int(linea.split(",")[3]))
    ]
)

goles_totales_equipo = goles_por_equipo.reduceByKey(lambda a, b: a + b)

print("Goles totales por equipo:")
print(goles_totales_equipo.collect())

# EXTRA 2: obtener equipo más goleador

equipo_mas_goleador = goles_totales_equipo.reduce(
    lambda a, b: a if a[1] > b[1] else b
)

print(f"Equipo más goleador es el {equipo_mas_goleador[0]} con {equipo_mas_goleador[1]} goles")