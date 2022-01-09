"""Sacando el porcentaje total para realizar la evaluacion de los mejores paises en los que se debe de invertir tomando todo en cuenta y logrando generar una evaluacion
de un porcentaje minimo del 80% para que cumpla esta caracteristica

by: Lucia Cardenas Borunda
"""
import pandas as x #importacion de pandas

def total():
    aux = 0 #dato auxiliar que se usara en el for
    sumT = 0.0 #una suma de iterasión que se usara en el for

     #Se crea la función para leer el archivo desde un CSV, agregando el delimitador que divide la información y que el index qus se autogenere se iguale al existente del archivo.
    csv = x.read_csv("synergy_logistics_database.csv", delimiter=",", index_col = 0)     
    del csv["year"] # cuenta con la misma problematica de transporte y se tiene que eliminar

    exports = csv.groupby(["origin"]).sum().reset_index()#Se envia los datos de Origen se agruparon, ademas de esto se realiza una suma de lo agrupado y para que los datos
    #con este se agrega un reseteo a los datos, por que los encabezados no se extraian de manera correcta.
    imports = csv.groupby(["destination"]).sum().reset_index() #Se repite el proceso de la agrupación de origen pero con destino.
    exports = exports.rename(columns={"total_value":"Total_exports","origin":"Country"}) #Se renombran las columnas para poder saber a cual pertenece cada una y uniendo 
    #con las dos ciudades tanto de origen y destino para combinarlo en la ciudad y que no queden campos vacios en las ciudades y se puedan obtener los totales.
    imports = imports.rename(columns={"total_value":"Total_imports","destination":"Country"})#Se repite la misma sentencia con las importaciones


    #df = x.merge(exports, imports, left_on="origin", right_on="destination", how="outer") era un merge inicial, pero se descarto al cambio al unir las ciudad
    union = x.merge(exports, imports, on="Country", how="outer")##EL merge que une las diferentes 
    union['Total'] = union[["Total_exports", "Total_imports"]].sum(axis=1)##Se realiza una suma de los totales de cada total de importación y exportación, para sacar
    #un total completo, agregando el axis se aplique en filas. Agregando una columna total.
    total = union["Total"].sum() #Sacar un total de toda la información del total para poder sacar el porcentaje
    union["porcent"] = round(100 * union["Total"]/ total) #Operación para sacar el porcentaje
    union = union.sort_values("porcent",ascending=False) #Ordenamiento en los datos del porcentaje de mayor a menor
    
    #Se realiza una iteracion, con un bucle en la filas, donde se realiza una suma menor del porcentaje menor el 80, con el total de todos los paises se obtenga este 
    #valor total del porcentaje
    for index, row in union.iterrows():
        if sumT < 80.0: #evaluaciones del valor total
            sumT += row["porcent"]##Suma de la columna porcentaje
            aux +=1 #contando los datos existentes
        else:
            break #romper el bluque
        
    title = "Valor total de importaciones y exportaciones"
    print ("\n \n \n", title.center (70), "\n")
    print(union.head(aux)) #impresion de los datos con forme los primeros datos conforme el conteo del auxiliar.
    


    