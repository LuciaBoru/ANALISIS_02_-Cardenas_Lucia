"""Evaluación de las mejores rutas por las cuales se puede realizar las importaciones o exportaciones y las mas utilizadas.

by: Lucia Cardenas Borunda
"""
import pandas as x #importacion de pandas

def transport():
     #Se crea la función para leer el archivo desde un CSV, agregando el delimitador que divide la información y que el index qus se autogenere se iguale al existente del archivo.
    csv = x.read_csv("synergy_logistics_database.csv", delimiter=",", index_col = 0) 
    
    del csv["year"]# se elimina la columna de año ya que por ser numerico se contabiliza en el resultado final
    transport = csv.groupby(["transport_mode"]).sum()    ##se realiza una agrupacion de los medios de transporte que hay para hacer una suma total de los valores y sacar el resultado
    title = "Transportes más importantes"
    print ("\n \n \n", title.center (60), "\n")
    print(transport.sort_values("total_value", ascending=False).head(3))#se imprime la informacion, de manera ordenada, pidiendo que solo imprima 3 valores
    
    subtitle = "Transporte que se puede reducir"
    print ("\n \n", subtitle.center (60), "\n")
    print(transport.sort_values("total_value").head(1))#se imprime la informacion, pidiendo que solo imprima 1 valor, siendo el primero en la lista que es el menos usado.


