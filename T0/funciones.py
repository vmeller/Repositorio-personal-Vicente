import random
import tablero
import funciones_2
def posicion(tablero1, tablero2, fila, columna):
    #intercambia el numero espacio vacio del tablero 1 por el numero respectivo del tablero 2
    x = str(tablero2[fila][columna])
    tablero1[fila][columna] = x
    return tablero1

def valor_fila(ancho_tablero):
    x = input("seleccione una fila (numeros): ")
    if x in "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM,.-<{ +}'¿|" \
        or int(x) > int(ancho_tablero)-1:
        print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
        return valor_fila(ancho_tablero)
    if int(x) <= int(ancho_tablero):
        return x

def valor_columna(largo_tablero):
    sector_columna = input("seleccione una columna (letras): ")
    x = funciones_2.convertidor_columna_en_numero(sector_columna)
    if x == "valor no valido" \
        or int(x) > int(largo_tablero)-1:
        print("El valor ingresado no se encuentra dentro del tablero, ingrese un valor que se encuentre en la tabla")
        return valor_columna(largo_tablero)
    if int(x) <= int(largo_tablero)-1:
        return x


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
    return [tablero_admin[r][c] for r in range(y-1 if y > 0 else y, y + 2 if y < len(tablero_admin)-1 else y + 1)\
     for c in range(x-1 if x > 0 else x, x + 2 if x < len(tablero_admin[0])-1 else x + 1)].count('N')

def cargar_partida(lista):
    g = 1
    for i in lista:
        nombre = i[0]
        puntaje = i[1]
        ancho_tablero = i[2]
        largo_tablero = i[3]
        numeros = i[4]
        tablero_jugador = []
        # me entrega la lista de partidas guardadas de manera ordenada
        for j in range(int(ancho_tablero)):
            listas = []
            for k in range(int(largo_tablero)):
                listas.append(" ")
            tablero_jugador.append(listas)
        a = 0
        b = 1
        c = 2
        for s in range(int(len(numeros)/3)):
            num = int(numeros[a])
            linea = int(numeros[b])
            columna = int(numeros[c])
            a += 3
            b += 3
            c += 3
            tablero_jugador[linea][columna] = num
        print(g,")",nombre,"=",puntaje,"puntos")
        tablero.print_tablero(tablero_jugador)
        g += 1
    return

def cargar_ranking(lista):
    c = 1
    top = 0
    ordenada = sorted(lista, key=lambda ordenada:int(ordenada[1]), reverse=True)
    for i in ordenada:
        nombre = i[0]
        puntaje = i[1]
        # me entrega la lista de puntajes guardadas de manera ordenada
        print(c,")",nombre,"=",puntaje,"puntos")
        c += 1
        top += 1
        if top == 10:
            break
    return

def creador_tablero_admin(lista):
    for i in lista:
        ancho_tablero = i[2]
        largo_tablero = i[3]
        bestias = i[5]
        tablero_admin = []
        # me va a crear el tablero con las ubicaciones de las bestias
        for j in range(int(ancho_tablero)):
            listas = []
            for k in range(int(largo_tablero)):
                listas.append(" ")
            tablero_admin.append(listas)
        d = 0
        e = 1
        f = 2
        for r in range(int(len(bestias)/3)):
            bes = bestias[d]
            linea_b = int(bestias[e])
            columna_b = int(bestias[f])
            d += 3
            e += 3
            f += 3
            tablero_admin[linea_b][columna_b] = bes
    return tablero_admin

def creador_tablero_jugador(lista):
    for i in lista:
        ancho_tablero = i[2]
        largo_tablero = i[3]
        numeros = i[4]
        tablero_jugador = []
        # me entrega la lista de partidas guardadas de manera ordenada
        for j in range(int(ancho_tablero)):
            listas = []
            for k in range(int(largo_tablero)):
                listas.append(" ")
            tablero_jugador.append(listas)
        a = 0
        b = 1
        c = 2
        for s in range(int(len(numeros)/3)):
            num = int(numeros[a])
            linea = int(numeros[b])
            columna = int(numeros[c])
            a += 3
            b += 3
            c += 3
            tablero_jugador[linea][columna] = num
    return tablero_jugador
        