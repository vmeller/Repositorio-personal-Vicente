from re import S
from typing import Counter
import parametros
import tablero
import random
from math import ceil
import funciones

simbolos = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM,.-<{ +}'¿|"
#puntaje_jugador = cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT


#Tarea_0
###########################################################################   Menu de inicio
print(""" STAR ADVANCED! 
Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")

tablero_juego_jugador = []
tablero_juego_admin = []
eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
x = eleccion_inicio.isdigit()
while x == False or  int(eleccion_inicio) > 3:
    print("Opcion no valida, por favor ingresar un numero valido")
    print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
    eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
    y = eleccion_inicio.isdigit()
    if y == True:
        if int(eleccion_inicio) == 0 or int(eleccion_inicio) == 1 or \
            int(eleccion_inicio) == 2 or int(eleccion_inicio) == 3:
            break

if int(eleccion_inicio) == 1:
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
    tablero_juego_admin = funciones.bestias_en_tablero(cantidad_de_bestias, tablero_juego_admin, ancho_tablero, largo_tablero)
    tablero_juego_admin = funciones.contador_de_bestias(tablero_juego_admin, ancho_tablero, largo_tablero)
    print(tablero_juego_admin)

    tablero.print_tablero(tablero_juego_jugador)
    print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
    menu_juego = input("Indique su opcion (1, 2 o 3): ")
    letras = menu_juego.isdigit()

elif int(eleccion_inicio) == 2:
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

elif int(eleccion_inicio) == 3:
    print("Cargando ranking...")
    with open("puntajes.txt", "r") as file:
        lista_puntajes = file.readlines()
        file.close()
        puntajes = []
    for linea in lista_puntajes[:10]:
        puntajes.append(linea.strip().split("="))
    x = 1
    for juego in puntajes:
        print(x,")",juego[0],"=",juego[1])
        x += 1

elif int(eleccion_inicio) == 0:                             
    print("Hasta la proxima...")
    termino_de_juego = 1               

#######################################################################   Menu del juego
termino_de_juego = 0
while termino_de_juego == 0 and int(eleccion_inicio) == 1:
    tablero.print_tablero(tablero_juego_jugador)
    while int(menu_juego) <= 3:

        if int(menu_juego) == 1:
            sector_fila = input("seleccione una fila (numeros): ")
            if sector_fila in simbolos or int(sector_fila) > ancho_tablero-1:
                print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
                sector_fila = input("seleccione una fila (numeros): ")
                while sector_fila in simbolos or int(sector_fila) > ancho_tablero-1:
                    print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
                    sector_fila = input("seleccione una fila (numeros): ")
                    if sector_fila <= ancho_tablero:
                        break
            
            sector_columna = input("seleccione una columna (letras): ")
            letra = funciones.convertidor_columna_en_numero(sector_columna)
            if letra > largo_tablero-1:
                print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
                sector_columna = input("seleccione una columna (letras): ")
                letra = funciones.convertidor_columna_en_numero(sector_columna)
                while letra > largo_tablero-1:
                    print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
                    sector_columna = input("seleccione una columna (letras): ")
                    if letra <= largo_tablero-1:
                        break

            tablero_juego_jugador = funciones.posicion(tablero_juego_jugador, tablero_juego_admin, int(sector_fila), letra)
            
            if tablero_juego_jugador[int(sector_fila)][letra] == "N":
                tablero.print_tablero(tablero_juego_jugador)
                print("Perdiste...")
                termino_de_juego = 1
                break
        
        tablero.print_tablero(tablero_juego_jugador)
        print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
        menu_juego = input("Indique su opcion (1, 2 o 3): ")
            
    while letras == False or  int(menu_juego) > 3:
        print("Opcion no valida, por favor ingresar un numero valido")
        print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
        menu_juego = input("Indique su opcion (1, 2 o 3): ")
        k = menu_juego.isdigit()
        if k == True:
            if int(menu_juego) <= 3:
                break           

