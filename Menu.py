"""Menú principal para acceder a las opciones solicitadas por el cliente, se reutilizo el menu del primer proyecto.

by: Lucia Cardenas Borunda
"""
from Routes import routes
from Transport import transport
from Total import total

def menu():
        ##Definición de las variables tipo texto que solo se utilizaran para el formato del menú imprimido despues de la creación.
    title = "Synergy Logistics"
    print ("\n", title.center (60), "\n")

    ##Variable input en cual se agregara la opción que accederas de los servicios
    menu = int(input("""
    1. Rutas de Importación y Exportación 
    2. Medio de transporte utilizado
    3. Total de importaciones y exportaciones
    0. Salir \n
        Ingresa una opción: """))

    #Se define un ciclo while que declara que mientras menu sea diferente a 0 se realizaria una acción ya que si es igual saldria del programa.
    while menu != 0:
        ##Aqui se mostrara los accesos a las funciones conforme los selecciones nos enviara a la función requerida
        if menu == 1:
            routes()
            break
        elif menu == 2:
            transport()
            break
        elif menu == 3:
            total()
            break
        #Si llegara a ingresar un numero de los que no estan admitidos, mostrara el mensaje de error.
        else:
            print("\n")
            print("¡Error!".center (60))
            print("Seleccione una opcion valida".center(60))
            break   

if __name__== "__main__":
    menu()#Muestra la información del menu
