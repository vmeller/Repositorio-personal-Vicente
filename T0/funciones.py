from ast import AsyncWith
from contextlib import AbstractAsyncContextManager
import random
from re import A
import tablero
def menu_inicio(x):
    simbolos = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM,.-<{ +}'¿|456789"
    if x in simbolos:
        print("Opcion no valida, por favor ingresar un numero valido")
        print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
    if x not in simbolos:
        if x == "1":
            nueva_partida = input("Indiqueme su nombre: ")
            print("""Antes de comenzar el juego, debemos armar el tablero,
dime las medidas con las que deseas jugar: """)
            largo_tablero = input("largo: ")
            ancho_tablero = input("ancho: ")
            while largo_tablero in simbolos or ancho_tablero in simbolos or int(largo_tablero) > 15 \
                or int(largo_tablero) < 3 or int(ancho_tablero) > 15 or int(ancho_tablero) < 3:
                print("valores no validos, por favor ingrese otros valores:")
                largo_tablero = input("largo (debe ser un numero entre 3 y 15): ")
                ancho_tablero = input("ancho (debe ser un numero entre 3 y 15): ")
#        if x == "2:
#        if x == "3":
#        if x == "4":


def posicion(tablero1, tablero2, fila, columna):
    x = str(tablero2[fila][columna])
    tablero1[fila][columna] = x
    return tablero1

def bestias_en_tablero(cantidad_bestias, tablero1, ancho, largo):
    c = 0

    for i in range(cantidad_bestias):
        if tablero1[random.randint(0,ancho-1)][random.randint(0,largo-1)] == 0:
            tablero1[random.randint(0,ancho-1)][random.randint(0,largo-1)] = "N"
            c += 1
        else:
            c += 0
    if c < cantidad_bestias:
        return bestias_en_tablero
    else:
        return tablero1

def convertidor_columna_en_numero(letra):
    numero = 0
    if letra == "a" or letra == "A":
        numero = 0
        return numero
    elif letra == "b" or letra == "B":
        numero = 1
        return numero
    elif letra == "c" or letra == "C":
        numero = 2
        return numero
    elif letra == "d" or letra == "D":
        numero = 3
        return numero
    elif letra == "e" or letra == "E":
        numero = 4
        return numero 
    elif letra == "f" or letra == "F":
        numero = 5
        return numero
    elif letra == "g" or letra == "G":
        numero = 6
        return numero
    elif letra == "h" or letra == "H":
        numero = 7
        return numero
    elif letra == "i" or letra == "I":
        numero = 8
        return numero
    elif letra == "j" or letra == "J":
        numero = 9
        return numero
    elif letra == "k" or letra == "K":
        numero = 10
        return numero
    elif letra == "l" or letra == "L":
        numero = 11
        return numero
    elif letra == "m" or letra == "M":
        numero = 12
        return numero
    elif letra == "n" or letra == "N":
        numero = 13
        return numero
    elif letra == "o" or letra == "O":
        numero = 14
        return numero
    else:
        numero = "valor no valido"
        return numero

def surrounding(tablero_admin, x, y):
   return [tablero_admin[r][c] for r in range(y-1 if y > 0 else y, y + 2 if y < int(len(tablero_admin))-1 else y + 1)\
     for c in range(x-1 if x > 0 else x, x + 2 if x < int(len(tablero_admin[0]))-1 else x + 1)].count('N')

def cargar_partida(lista):
    c = 1
    for i in lista:
        nombre = i[0]
        puntaje = i[1]
        tablero_jugador = eval(i[3])
        print(c,")",nombre,"=",puntaje,"puntos")
        tablero.print_tablero(tablero_jugador)
        c += 1
    return

