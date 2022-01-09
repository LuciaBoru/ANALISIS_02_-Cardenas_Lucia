"""Con este se evaluan el top de paises que son mejores para realizar el comercio, tanto como en exportaciones e importaciones, viendo desde su pais de origen y destino.
by: Lucia Cardenas Borunda
"""
import pandas as x #importacion de pandas y renombre para ser usado

def routes():
    #Se crea la función para leer el archivo desde un CSV, agregando el delimitador que divide la información y que el index qus se autogenere se iguale al existente del archivo.
    csv = x.read_csv("synergy_logistics_database.csv", delimiter=",", index_col = 0) 

    #Se agrega una variable donde se llamaran las columnas para validar las rutas, tanto como el destino y origen, siendo depositada en una lista, siendo size el que valida los mayores viajes
    route = csv.groupby(["origin","destination"]).size()
    #Al momento de llamar la ruta, esta se le agrega un ordenar pero el que ejecuta pandas y para limitarlo usamos head
    title = "Rutas de importación y exportación"
    print ("\n \n \n", title.center (60), "\n")
    print(route.sort_values(ascending=False).head(10))

    
