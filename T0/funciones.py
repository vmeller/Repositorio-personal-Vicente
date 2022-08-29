import random
import tablero
def posicion(tablero1, tablero2, fila, columna):
    #intercambia el numero espacio vacio del tablero 1 por el numero respectivo del tablero 2
    x = str(tablero2[fila][columna])
    tablero1[fila][columna] = x
    return tablero1

def bestias_en_tablero(cantidad_bestias, tablero1, ancho, largo):
    c = 0
    for i in range(cantidad_bestias):
        #introduce de manera aleatoria las bestias en el tablero
        if tablero1[random.randint(0,ancho-1)][random.randint(0,largo-1)] == 0:
            tablero1[random.randint(0,ancho-1)][random.randint(0,largo-1)] = "N"
            c += 1
        else:
            c += 0
    if c < cantidad_bestias:
        #revisa que la cantidad de bestias en el tablero sea la correcta
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
    #asiga un numero en la posicion [x][y] dependiendo de cuantas bestias tiene en las casillas adyacentes
    return [tablero_admin[r][c] for r in range(y-1 if y > 0 else y, y + 2 if y < int(len(tablero_admin))-1 else y + 1)\
     for c in range(x-1 if x > 0 else x, x + 2 if x < int(len(tablero_admin[0]))-1 else x + 1)].count('N')

def cargar_partida(lista):
    c = 1
    for i in lista:
        nombre = i[0]
        puntaje = i[1]
        tablero_jugador = (i[3])    #debo hacerlo una lista
        # me entrega la lista de partidas guardadas de manera ordenada
        print(c,")",nombre,"=",puntaje,"puntos")
        tablero.print_tablero(tablero_jugador)
        c += 1
    return

def cargar_ranking(lista):
    c = 1
    
    print(lista)
    for i in lista:
        nombre = i[0]
        puntaje = i[1]
        # me entrega la lista de puntajes guardadas de manera ordenada
        print(c,")",nombre,"=",puntaje,"puntos")
        c += 1
    return


