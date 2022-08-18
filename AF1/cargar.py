# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    with open(ruta_archivo, "r") as file:
        lista = file.readlines()
        file.close()
        platos = []
        for linea in lista:
            platos.append(linea.strip())
        

        print(platos)
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass

cargar_platos("AF1/platos.csv")
