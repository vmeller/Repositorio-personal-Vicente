from re import S
from typing import Counter
import parametros
import tablero
import random
from math import ceil
import eleccion_posicion

#puntaje_jugador = cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT

#Tarea_0
print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")

tablero_juego_jugador = []
tablero_juego_admin = []
eleccion_inicio = int(input("Indique su opcion (0, 1, 2 o 3): "))

while eleccion_inicio > 3:
    print("Opcion no valida, por favor ingresar un numero valido")
    print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
    eleccion_inicio = int(input("Indique su opcion (0, 1, 2 o 3): "))
    if eleccion_inicio == 0 or eleccion_inicio == 1 or eleccion_inicio == 2 or eleccion_inicio == 3:
        break

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
        tablero_juego_jugador.append([])
        tablero_juego_admin.append([])
    for tabla in tablero_juego_jugador:
        for l in range(largo_tablero):
            tabla.append(" ")
    for tabla in tablero_juego_admin:
        for l in range(largo_tablero):
            tabla.append(0)

    cantidad_de_bestias = ceil(largo_tablero * ancho_tablero * float(parametros.PROB_BESTIA))
    for n in range(cantidad_de_bestias):
        tablero_juego_admin[random.randint(0,ancho_tablero-1)][random.randint(0,largo_tablero-1)] = "N"



    tablero_juego_admin = eleccion_posicion.contador_de_bestias(tablero_juego_admin, ancho_tablero, largo_tablero)

    tablero.print_tablero(tablero_juego_jugador)
    print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
    menu_juego = int(input("Indique su opcion (1, 2 o 3): "))
    while menu_juego > 3:
        print("Opcion no valida, por favor ingresar un numero valido")
        print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
        menu_juego = int(input("Indique su opcion (1, 2 o 3): "))
        if menu_juego <= 3:
            break    
    while menu_juego <= 3:
        tablero.print_tablero(tablero_juego_jugador)
#        print("""Seleccione una opcion:
#[1] Descubrir un sector
#[2] Guardar partida
#[3] Salir de la partida""")
        if menu_juego == 1:
            sector_fila = int(input("seleccione una fila: "))
            sector_columna = input("seleccione una columna: ")
            letra = eleccion_posicion.convertidor_columna_en_numero(sector_columna)
            tablero_juego_jugador = eleccion_posicion.posicion(tablero_juego_jugador, tablero_juego_admin, sector_fila, letra)
            if tablero_juego_jugador[sector_fila][letra] == "N":
                tablero.print_tablero(tablero_juego_jugador)
                print("Perdiste...")
                break
                

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


#for l in tablero_juego:
#    print(l)
