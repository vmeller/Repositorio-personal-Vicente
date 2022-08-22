from re import S
import parametros
import tablero
import random

def contador_de_bestias(tablero, ancho, largo, ancho_total, largo_total):
    b = 0
    if tablero[ancho][largo] == "-":
        if ancho >= 1:
            if tablero[ancho-1][largo] == "N":
                b += 1
        elif ancho < ancho_total:
            if tablero[ancho+1][largo] == "N":
                b += 1
        elif largo >= 1:
            if tablero[ancho][largo-1] == "N":
                b += 1
        elif largo < largo_total:
            if tablero[ancho][largo+1] == "N":
                b += 1
        elif ancho >= 1 and largo >= 1:
            if tablero[ancho-1][largo-1] == "N":
                 b += 1
        elif ancho >= 1 and largo < largo_total:
            if tablero[ancho-1][largo+1] == "N":
                b += 1
        elif ancho < ancho_total and largo >= 1:
            if tablero[ancho+1][largo-1] == "N":
                b += 1
        elif ancho < ancho_total and largo < largo_total:
            if tablero[ancho+1][largo+1] == "N":
                b += 1
        else:
            b += 0
    else:
        tablero = tablero
    tablero[ancho][largo] = b
    return tablero

#puntaje_jugador = cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT

#Tarea_0
print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")

tablero = []
eleccion_inicio = int(input("Indique su opcion (0, 1, 2 o 3): "))
if eleccion_inicio == 1:
    print("""Antes de comenzar el juego, debemos armar el tablero,
dime las medidas con las que deseas jugar: """)
    largo_tablero = int(input("largo: "))
    ancho_tablero = int(input("ancho: "))
    while largo_tablero > 15 or largo_tablero < 3 or ancho_tablero > 15 or ancho_tablero < 3:
        print("valores no validos, por favor ingrese otros valores:")
        largo_tablero = int(input("largo (debe ser un numero entre 3 y 15): "))
        ancho_tablero = int(input("ancho (debe ser un numero entre 3 y 15): "))

    for a in range(ancho_tablero):
        tablero.append([])
    for tabla in tablero:
        for l in range(largo_tablero):
            tabla.append("-")
    
    cantidad_de_bestias = int((float(largo_tablero) * float(ancho_tablero) * parametros.PROB_BESTIA)//1)
    for n in range(cantidad_de_bestias):
        tablero[random.randint(0,ancho_tablero-1)][random.randint(0,largo_tablero-1)] = "N"
    for anchos in range(len(tablero)):
        for largos in range(len(tablero[anchos])):
            if tablero[anchos][largos] == "N":
                tablero[anchos][largos] == "N"
            elif tablero[anchos][largos] == "-":
                tablero_final = contador_de_bestias(tablero, anchos, largos, ancho_tablero, largo_tablero)
                



elif eleccion_inicio == 2:
    print("Cargando partidas...")
    with open("partidas.txt", "r") as file:
        lista_partidas = file.readlines()
        file.close()
        partidas = []
        for linea in lista_partidas:
            partidas.append(linea.strip())
        x = 1
        for juego in partidas:
            print(x,")",juego)
            x+=1
        eleccion_partida = int(input("Indique el numero de partida que sea jugar: "))
        print(eleccion_partida)
        print("usted selecciono: ",partidas[(eleccion_partida - 1)])

elif eleccion_inicio == 3:
    print("Cargando ranking...")
    with open("puntajes.txt", "r") as file:
        lista_puntajes = file.readlines()
        file.close()
        puntajes = []
    for linea in lista_puntajes:
        puntajes.append(linea.strip())
    x = 1
    for juego in puntajes:
        print(x,")",juego)
        x += 1

elif eleccion_inicio == 0:
    print("Hasta la proxima...")


for l in tablero:
    print(l)
